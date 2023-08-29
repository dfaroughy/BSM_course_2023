
import numpy as np
from pyjet import cluster, DTYPE_EP
from numpy.lib.recfunctions import append_fields
import torch
from torch import Tensor
import torch.nn as nn

class GetJets(object):
    
    def __init__(self, 
                 path,  
                 fastjet: dict={'R': None, 'p': None, 'ptmin': None}, 
                 ptRange: tuple=(0.0, np.inf),
                 etaRange: tuple=(-np.inf, np.inf),
                 phiRange: tuple=(-np.pi, np.pi),
                 num_events: int=None,
                 discretize: bool=False
                ):   
        
        self.f = open(path,'r')
        self.num_events = num_events
        self.N = 0

        # kinemtic range of particles

        self.ptMin, self.ptMax   = ptRange[0], ptRange[1]
        self.etaMin, self.etaMax = etaRange[0], etaRange[1]
        self.phiMin, self.phiMax = phiRange[0], phiRange[1]

        # detector pixelization

        self.discretize = discretize

        # clustering

        self.R = fastjet['R']
        self.p = fastjet['p']
        self.ptmin_jet = fastjet['ptmin']
        self.cluster = True if self.R is not None else False

        if self.cluster:
            algo = {'-1' : 'anti-kt', '0' : 'C/A', '1' : 'kt'}
            print('INFO: clustering jets with {} algorithm.'.format(algo[str(self.p)]))
            print('INFO: radius R={}, min pt_jet={}'.format(self.R, self.ptmin_jet))

    def detector_smear(self, particle, eMaxTrack=220.0, resFudgeFactor=1.0, eps=1e-10):
            pid, e, px, py, pz = particle
            pt = np.sqrt(px**2 + py**2)
            if is_charged_hadron(pid): energyResolution = np.sqrt( (0.00025*pt)**2 + 0.015**2) if e <= eMaxTrack else np.sqrt( (1.20 / np.sqrt(e/7.0))**2 + 0.05**2)
            elif is_neutral_hadron(pid): energyResolution = np.sqrt( (1.20 / np.sqrt(e/7.0))**2 + 0.05**2)
            elif is_photon(pid): energyResolution = np.sqrt( (0.027 / np.sqrt(e/1.6))**2 + (0.15 / e * 1.6)**2 + 0.005**2)
            elif is_lepton(pid): energyResolution = np.sqrt( (0.00025*pt)**2 + 0.015**2) 
            else: energyResolution = 0.0
            smearedPt = max(eps, np.random.normal(1, energyResolution * resFudgeFactor))
            return pid, e * smearedPt,  px * smearedPt,  py * smearedPt,  pz * smearedPt

    def __enter__(self):


            for line in self.f:

                start_event = True if "<event>" in line else False
                next_state = line[0].isdigit()
                end_event = True if "</event>" in line else False
                    
                if start_event:
                    self.pid, self.particles = [], []

                if next_state:

                    state = str.split(line)           
                    pid, e, px, py, pz = self.detector_smear((int(state[1]), float(state[2]), float(state[3]), float(state[4]), float(state[5])))
                    pt = np.sqrt(px**2 + py**2)
                    eta = np.arcsinh(pz / pt)
                    phi = np.arctan2(py, px)

                    if (is_visible(pid) and 
                       (eta >= self.etaMin and eta <= self.etaMax) and  
                       (phi >= self.phiMin and phi <= self.phiMax) and  
                       (pt >= self.ptMin and pt < self.ptMax)):

                        self.particles.append( (e, px, py, pz) )
                        self.pid.append(pid)

                elif end_event:

                    if (self.num_events is not None and self.N >= self.num_events): break
                    else: self.N += 1
                    
                    particles = np.array(self.particles, dtype=DTYPE_EP)
                    particles = append_fields(particles, 'pid', data=np.array(self.pid))
                    sequence = cluster(particles, R=self.R,  p=self.p, ep=True)
                    jets = sequence.inclusive_jets(ptmin=self.ptmin_jet)
                    
                    if len(jets) > 0:
                        yield jets 



    def __exit__(self, exc_type, exc_value, traceback):
        self.f.close()

def is_charged_hadron(pid):
    if pid in [211,-211,321,-321,2212,-2212,3112,-3112,3222,-3222,3312,-3312]: return True
    else: return False

def is_neutral_hadron(pid):
    if pid in [3122,-3122,130,310,2112,-2112,3322,-3322]: return True
    else: return False

def is_photon(pid):
    if pid in [22,111]: return True
    else: return False

def is_lepton(pid):
    if pid in [-11,11,-13,13,-15,15]: return True
    else: return False

def is_visible(pid):
    if pid in [-12,12,-14,14,-16,16]: return False
    else: return True

class JetFeatures:
    def __init__(self, jet, max_const=150, pid=False):
        
        self.get_pid = pid
        self.num_const = len(jet)
        pid = [int(x.pid) for x in jet] if self.get_pid else []

        # constituent features from constituents
        
        c = jet.constituents_array(ep=True)
        c_had = jet.constituents_array(ep=False)
        

        # jet features from constituents
        
        self.num_const = len(jet)
        jet_from_consts = np.sum(np.array([c['E'], c['px'], c['py'], c['pz']]), axis=-1)
        e , px, py, pz = jet_from_consts[0], jet_from_consts[1], jet_from_consts[2], jet_from_consts[3]
        jet_pt = np.sqrt(np.clip(px**2 + py**2, 0, None))
        jet_eta = np.arcsinh(pz / jet_pt)
        jet_phi = np.arctan2(py, px)
        jet_mass = np.sqrt(np.clip(e**2 - px**2 - py**2 - pz**2, 0, None))
        
        # relative features for constituents

        pt_rel = c_had['pT'] / jet_pt
        eta_rel = c_had['eta'] - jet_eta
        phi_rel = c_had['phi'] - jet_phi
        phi_rel = (phi_rel + np.pi) % (2 * np.pi) - np.pi
        
        self.particle_features = np.array([c['E'], c['px'], c['py'], c['pz'], 
                                   c_had['pT'], c_had['eta'], c_had['phi'], c_had['mass'],
                                   pt_rel, eta_rel, phi_rel, pid]).T        
        # pt sort

        indx = np.argsort(self.particle_features[:,4]) 
        self.particle_features = self.particle_features[indx[::-1]]

        # add zero-pad and masking 
        
        self.particle_features = np.pad(self.particle_features, ((0, 0), (0, 1)), mode='constant', constant_values=1.0)    
        if self.num_const <= max_const:
            self.particle_features = np.pad(self.particle_features, ((0, max_const - self.num_const), (0, 0)), mode='constant')
        else:
            self.particle_features =  self.particle_features[:max_const]
        self.features = np.array([jet_pt, jet_eta, jet_phi, jet_mass, np.sum(self.particle_features[...,-1])])

    @property
    def particles_4mom(self):
        if self.get_pid:
            return np.concatenate((self.particle_features[..., :4], self.particle_features[..., 11, None], self.particle_features[..., -1, None]), axis=-1) 
        else:
            return np.concatenate((self.particle_features[..., :4], self.particle_features[..., -1, None]), axis=-1) 
    
    @property
    def particles(self):
        if self.get_pid:
            return np.concatenate((self.particle_features[..., 4:8], self.particle_features[..., 11, None], self.particle_features[..., -1, None]), axis=-1)
        else:
            return np.concatenate((self.particle_features[..., 4:8], self.particle_features[..., -1, None]), axis=-1)
   
    @property
    def particles_rel(self):
        if self.get_pid:
            return np.concatenate((self.particle_features[..., 8:11], self.particle_features[..., 11, None], self.particle_features[..., -1, None]), axis=-1) 
        else:
            return np.concatenate((self.particle_features[..., 8:11], self.particle_features[..., -1, None]), axis=-1) 

    @property
    def pid(self):
        return self.particle_features[..., 11] 

    @property
    def mask(self):
        return self.particle_features[..., -1] 
        

calo = {
        'HCAL': {
                'eta': {
                        'range': (-3.0, 3.0),
                        'resolution': 0.022
                        },
                'phi': {
                        'range': (-np.pi, np.pi),
                        'resolution': 0.22
                        },
                'e': { 'eMaxTrack' : 220.0}
                },

        'ECAL': {
                'eta': {
                        'range': (-3.0, 3.0),
                        'resolution': 0.0175
                        },
                'phi': {
                        'range': (-np.pi, np.pi),
                        'resolution': 0.0175
                        },
                'e': { 'eMaxTrack' : 220.0}
                }
        }


class DetectorEffects:

    def __init__(self, particles, calorimeter: dict=calo): # particles = (id, e, px, py, pz)

        self.pid = particles[0]
        self.particles = particles[1:]
        self.output= []

        self.etaMin, self.etaMax = calorimeter['HCAL']['eta']['range']
        self.phiMin, self.phiMax = calorimeter['HCAL']['phi']['range']
        self.etaResHcal = calorimeter['HCAL']['eta']['resolution']
        self.etaResEcal = calorimeter['ECAL']['eta']['resolution']
        self.phiResHcal = calorimeter['HCAL']['phi']['resolution']
        self.phiResEcal = calorimeter['ECAL']['phi']['resolution']
        self.eMaxTrack = calorimeter['HCAL']['e']['eMaxTrack']

        self.etaBinsHcal = int((self.etaMax - self.etaMin) / self.etaResHcal)
        self.phiBinsHcal = int((self.phiMax - self.phiMin) / self.phiResHcal)
        self.etaBinsEcal = int((self.etaMax - self.etaMin) / self.etaResEcal)
        self.phiBinsEcal = int((self.phiMax - self.phiMin) / self.phiResEcal)

        self.HcalGrid = np.zeros((self.etaBinsHcal, self.phiBinsHcal))
        self.EcalGrid = np.zeros((self.etaBinsEcal, self.phiBinsEcal))

        self.addedPileupEnergy = 0.0

    def pileup(self, numberOfPileup: int=0):
        pileupEnergyInDetector = numberOfPileup * 0.3
        addedPileupEnergy = 0
        while addedPileupEnergy < pileupEnergyInDetector:
            phi = np.random.uniform(self.phiMin, self.phiMax)
            eta = np.random.uniform(self.etaMin, self.etaMax)
            e = np.random.exponential(1/6) + 0.5
            self.EcalGrid[int(eta), int(phi)] += randEnergy
            self.HcalGrid[int(eta), int(phi)] += randEnergy
            self.addedPileupEnergy += e

    def energy_smear(self, resFudgeFactor=1.0, eps=1e-10):

        smeared=[]

        for particle in self.particles:

            pid, e, px, py, pz = particle
            pt = np.sqrt(px**2 + py**2)

            if is_charged_hadron(pid): energyResolution = np.sqrt( (0.00025*pt)**2 + 0.015**2) if e <= self.eMaxTrack else np.sqrt( (1.20 / np.sqrt(e/7.0))**2 + 0.05**2)
            elif is_neutral_hadron(pid): energyResolution = np.sqrt( (1.20 / np.sqrt(e/7.0))**2 + 0.05**2)
            elif is_photon(pid): energyResolution = np.sqrt( (0.027 / np.sqrt(e/1.6))**2 + (0.15 / e * 1.6)**2 + 0.005**2)
            elif is_lepton(pid): energyResolution = np.sqrt( (0.00025*pt)**2 + 0.015**2) 
            else: energyResolution = 0.0
    
            smearedPt = max(eps, np.random.normal(1, energyResolution * resFudgeFactor))
            smeared4Vec = (pid,
                           e * smearedPt, 
                           px * smearedPt, 
                           py * smearedPt, 
                           pz * smearedPt)

            smeared.append(smeared4Vec)
        self.particles = smeared

    def discretize(self, 
                   discretizeEcal: bool=False, 
                   maxChargedPt: float=1e10,  
                   maxChargedDr: float=1e10, 
                   trackingEfficiency: float=0.9,
                   eps: float=1e-06):

        for i, particle_i in enumerate(self.particles):

            pid, e_i, px_i, py_i, pz_i = particle_i
            pt_i = np.sqrt(px_i**2 + py_i**2)
            eta_i = np.arcsinh(pz_i / (pt_i + eps))
            phi_i = np.arctan2(py_i, px_i)

            if (eta_i >= self.etaMin and eta_i <= self.etaMax) and  (phi_i >= self.phiMin and phi_i <= self.phiMax):
                
                if is_charged_hadron(pid): track = True
                else: track = False
                    
                if track and (trackingEfficiency != 1.0) and (np.random.randint(100) > trackingEfficiency * 100.0):
                    track = False

                if track and (maxChargedDr < 10):
                    cutDr = np.random.randint(100) / 50. * maxChargedDr
                    
                    for j, particle_j in enumerate(particles):
                        _, e_j, px_j, py_j, pz_j = particle_j
                        pt_j = np.sqrt(px_j**2 + py_j**2)
                        eta_j = np.arcsinh(pz_j / (pt_j + eps))
                        phi_j = np.arctan2(py_j, px_j)

                        if (i != j) and (self.deltaR(eta_i, phi_i, eta_j, phi_j) < cutDr):
                            track = False
                            break

                if track and (maxChargedPt < 10000) and (pt_i > maxChargedPt):
                    track = False

                if track or is_lepton(pid) or (is_photon(pid) and not discretizeEcal):
                    self.output.append(particle_i)
               
                elif is_photon(pid):
                    x = int((eta_i - self.etaMin) / self.etaResEcal)
                    y = int((phi_i - self.phiMin) / self.phiResEcal)
                    self.EcalGrid[x, y] += e_i

                elif is_neutral_hadron(pid) or (not track):
                    x = int((eta_i - self.etaMin) / self.etaResHcal)
                    y = int((phi_i - self.phiMin) / self.phiResHcal)
                    self.HcalGrid[x, y] += e_i

                else:
                    print("WARNING: Input particle has unlisted PDG ID!")

    def get_Hcal_cells(self):

        etaBinCentersHcal = np.linspace(self.etaMin + self.etaResHcal/2, self.etaMax - self.etaResHcal/2, self.etaBinsHcal)
        phiBinCentersHcal = np.linspace(self.phiMin + self.phiResHcal/2, self.phiMax - self.phiResHcal/2, self.phiBinsHcal)

        for i in range(self.etaBinsHcal):
            for j in range(self.phiBinsHcal):
                curbincontent = self.HcalGrid[i, j]
                if curbincontent > 0:

                    eta_cell = etaBinCentersHcal[i]
                    phi_cell = phiBinCentersHcal[j]
                    e_cell = self.HcalGrid[i, j]
                    pt_cell = e_cell * 2 / (np.exp(eta_cell) + np.exp(-eta_cell))

                    cell = np.zeros(4)
                    cell[0], cell[1], cell[2], cell[3] = pt_cell, e_cell, eta_cell, phi_cell
                    cell = cell[np.newaxis, :]  # Add a new axis to create a 2D array
                    cell = np.append(cell, np.zeros((1, 3)), axis=1)  # Append zeros for mass and user_index
                    cell[0, -1] = 130  # Set user_index to 130
                    self.output.append(cell)
 
    def get_Ecal_cells(self):

        etaBinCentersEcal = np.linspace(self.etaMin + self.etaResEcal/2, self.etaMax - self.etaResEcal/2, self.etaBinsEcal )
        phiBinCentersEcal = np.linspace(self.phiMin + self.phiResEcal/2, self.phiMax - self.phiResEcal/2, self.etaBinsEcal )

        for i in range(self.etaBinsEcal):
            for j in range(self.phiBinsEcal):
                curbincontent = self.EcalGrid[i, j]
                if curbincontent > 0:
                    
                    eta_cell = etaBinCentersEcal[i]
                    phi_cell = phiBinCentersEcal[j]
                    e_cell = self.EcalGrid[i, j]
                    pt_cell = e_cell * 2 / (np.exp(eta_cell) + np.exp(-eta_cell))

                    cell = np.zeros(4)
                    cell[0], cell[1], cell[2], cell[3] = pt_cell, e_cell, eta_cell, phi_cell
                    cell = cell[np.newaxis, :]  # Add a new axis to create a 2D array
                    cell = np.append(cell, np.zeros((1, 3)), axis=1)  # Append zeros for mass and user_index
                    cell[0, -1] = 111  # Set user_index to 111                    
                    self.output.append(cell)


   