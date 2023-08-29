
import numpy as np
from BSMhighPT2023.fastjet import get_jets
from BSMhighPT2023.isolation import isolated_object

class LHCO:
    
    def __init__(self, event, jet_def, pt_min):

        #...standard cuts:

        pt_jet = [pt_min, np.inf] 
        eta_jet = [-5, 5]
        
        pt_lep = [pt_min, np.inf]
        eta_lep = [-5, 5]

        pt_photon = [pt_min, np.inf]
        eta_photon = [-5, 5]

        #...compute MET:

        self.MET = met(event)
        
        #...get isolated leptons:

        lepton_mask = (abs(event['pid'])==11 ) | (abs(event['pid'])==13)
        leptons = event[lepton_mask]
        hadrons = event[~lepton_mask]
        self.leptons, event = isolated_object(leptons, hadrons, R_iso=0.3, threshold=0.12)
        self.electron = self.leptons[abs(self.leptons['pid']) == 11]
        self.muons = self.leptons[abs(self.leptons['pid']) == 13]
        
        #...get isolated photons:

        photon_mask = np.abs(event['pid']) == 22
        photons = event[photon_mask]
        hadrons = event[~photon_mask]
        self.photons, event = isolated_object(photons, hadrons, R_iso=0.4, threshold=0.2)

        #...get jets:

        self.jets = get_jets(event, jet_def, pt_min=pt_jet[0])

        #... aply basic cuts:

        self.jets = self.jets[(self.jets['eta'] > eta_jet[0]) &
                              (self.jets['eta'] < eta_jet[1])]

        self.leptons = self.leptons[(self.leptons['pt'] > pt_lep[0]) & 
                                    (self.leptons['pt'] < pt_lep[1]) & 
                                    (self.leptons['eta'] > eta_lep[0]) & 
                                    (self.leptons['eta'] < eta_lep[1])]

        self.photons = self.photons[(self.photons['pt'] > pt_photon[0]) &
                            (self.photons['pt'] < pt_photon[1]) &
                            (self.photons['eta'] > eta_photon[0]) &
                            (self.photons['eta'] < eta_photon[1])]
        
        
        #...combine leptons, photons and jets into one array:

        self.lhco = np.append(self.photons, self.leptons)
        self.lhco = np.append(self.lhco, self.jets)
        self.lhco = np.append(self.lhco, self.MET)


def met(event):

    sum_px = np.sum(event['pt'] * np.cos(event['phi']), axis=0)
    sum_py = np.sum(event['pt'] * np.sin(event['phi']), axis=0)
    phi = np.arctan2(sum_py, sum_px)
    pt = np.sqrt(sum_px**2 + sum_py**2)
    MET = np.array((pt, 0.0, phi, 0.0, sum_px, sum_py, 0.0, 0.0, 6), dtype=[('pt', 'f8'), ('eta', 'f8'), ('phi', 'f8'), ('M', 'f8'), ('px', 'f8'), ('py', 'f8'), ('pz', 'f8'), ('E', 'f8'), ('pid', 'i8')])
    return MET