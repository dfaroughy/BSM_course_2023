import torch
import numpy as np
import pandas as pd
import yaml
import os
from particle import PDGID, Particle
from BSMhighPT2023.detector import smear

class open_lhe(object):
    
    def __init__(self, path, max_num_events: int=None):   

        self.lhe= open(path,'r')
        self.max_num_events = max_num_events
        self.N = 0


    def __enter__(self):

        for line in self.lhe:


            if '#  Number of Events' in line: 
                print(line)      
                print(next(self.lhe))
                continue

            is_start_event = line.startswith("<event>") 
            is_end_event = line.startswith("</event>")
            state = str.split(line)

            # is_parton = True if (len(state)==13 and 
            #                     (state[0].startswith('-') or state[0].isdigit()) and 
            #                      state[1].isdigit() and 
            #                      int(state[1])==-1) else False

            is_final_state = True if (len(state)==13 and 
                                     (state[0].startswith('-') or state[0].isdigit()) and 
                                      state[1].isdigit() and 
                                      int(state[1])==1) else False

            if is_start_event:
                particle_features = []

            elif is_final_state:
                pid, px, py, pz, e = int(state[0]), float(state[6]), float(state[7]), float(state[8]), float(state[9])
                particle_features.append((px, py, pz, e, pid))

            elif is_end_event:

                if (self.max_num_events is not None and self.N > self.max_num_events): # exit
                    break
                else: self.N += 1

                event = np.array(particle_features)
                particle_features = []
                yield event
                   
    def __exit__(self, exc_type, exc_value, traceback):
        self.lhe.close()


class open_HepMC(object):
    
    def __init__(self, 
                 path: str, 
                 max_num_events: int=None,
                 distill: bool=False):   

        # check if a distilled file in folder exists:
        if distill and os.path.isfile(os.path.splitext(path)[0] + '.dstl.hepmc'): 
            print('INFO: using distilled hepmc file')
            self.path = os.path.splitext(path)[0] + '.dstl.hepmc'
        else:
            self.path = self.distill_hepmc_file(path) if distill else path 

        self.hepmc = open(self.path,'r')
        self.max_num_events = max_num_events
        self.N = 0

    def __enter__(self):

        print('INFO: reading hepmc file')

        for line in self.hepmc:

            if line.startswith("E 0") :
                particle_features = []

            elif line.startswith("P "):
                  
                line = str.split(line)

                if int(line[8])==1: # get final state particles only
                
                    px, py, pz, e, pid = float(line[3]), float(line[4]), float(line[5]), float(line[6]), int(line[2])   
                                        
                    if abs(pid) != 12 and abs(pid) != 14 and abs(pid) != 16 : # exclude neutrinos    
                                             
                        pt = np.sqrt(px**2 + py**2)
                        eta = np.arcsinh(pz / pt)
                        phi = np.arctan2(py, px)
                        m2 = e**2 - px**2 - py**2 - pz**2
                        m = 0.0 if m2 <= 0 else np.sqrt(m2)                
                        particle_features.append((pt, eta, phi, m, px, py, pz, e, pid))

            elif line.startswith("E "):

                if (self.max_num_events is not None and self.N > self.max_num_events - 1): # exit
                    break
                else: self.N += 1

                event = np.array(particle_features, dtype=[('pt', 'f8'), ('eta', 'f8'), ('phi', 'f8'), ('M', 'f8'), ('px', 'f8'), ('py', 'f8'), ('pz', 'f8'), ('E', 'f8'), ('pid', 'i8')])
                particle_features = [] 
                idx = np.argsort(-event['pt'])  # The negative sign is to pt-sort in descending order
                yield event[idx]

    def distill_hepmc_file(self, path):

        hepmc_dstl = open(os.path.splitext(path)[0] + '.dstl.hepmc', 'w')

        with open(path, 'r') as hepmc:

            hepmc_dstl.write('Distilled HepMC file\n')
            print('INFO: distilling hepmc: {path}')

            for line in hepmc:
                if line.startswith("E ") :
                    hepmc_dstl.write(line)
                elif line.startswith("P ") and int(str.split(line)[8])==1:
                    hepmc_dstl.write(line)
                else: pass

        return hepmc_dstl

    def __exit__(self, exc_type, exc_value, traceback):
        self.hepmc.close()


def get_LHE_events(path):
    events = []
    with open_lhe(path) as events:
        for states in events:
            events.append(event)
    return events


def get_HepMC_events(path):
    events = []
    with open_HepMC(path) as showered_events:
        for particles in showered_events:
            events.append(particles)
    return events


def PDG_Info(pid):
    pd.set_option('display.float_format', lambda x: '%.1e' % x)  
    state = Particle.from_pdgid(pid)
    info = [int(pid), state.name, state.mass, state.width, state.lifetime, int(state.charge), state.quarks]
    state = pd.DataFrame(info)
    state.index =['pid', 'name', 'mass (MeV)', 'width (MeV)', 'lifetime (s)', 'charge (e)', 'quarks']    
    state.columns = state.iloc[0]
    state = state.drop(state.index[0])
    return state


def open_HEPData(path):
    assert path.endswith(".yaml")
    with open(path) as f:
        CMS_data = yaml.load(f, Loader=yaml.FullLoader)
    bins_low = np.array([entry["low"] for entry in CMS_data["independent_variables"][0]["values"]])
    bins_high = np.array([entry["high"] for entry in CMS_data["independent_variables"][0]["values"]])
    size = bins_high - bins_low
    observed =  size * np.array([entry["value"] for entry in CMS_data["dependent_variables"][0]["values"]])
    background =  size * np.array([entry['value'] for entry in CMS_data["dependent_variables"][1]['values']])
    error =  size * np.array([entry["errors"][0]["symerror"] for entry in CMS_data["dependent_variables"][1]["values"] if "errors" in entry and entry["errors"][0]["label"] == "total background uncertainty"])
    data = np.stack((bins_low, bins_high, observed, background, error), axis=1)
    data = pd.DataFrame(data, columns=["bins_low", "bins_high", "Nobs", "Nbkg", "err"])
    return data