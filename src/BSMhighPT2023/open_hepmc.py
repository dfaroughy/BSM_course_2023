import numpy as np

class open_hepmc(object):
    
    def __init__(self, path, coords: str='pt_eta_phi_m', max_num_events: int=None):   

        self.hepmc = open(path,'r')
        self.coords = coords
        self.max_num_events = max_num_events
        self.N = 0

    def __enter__(self):

        for line in self.hepmc:

            is_first_event = line.startswith("E 0") 
            is_next_event = line.startswith("E ")

            state = str.split(line)
            is_final_state = True if (line.startswith("P ") and int(state[8])==1) else False

            if is_first_event:
                particle_features = []

            elif is_final_state:
                pid, px, py, pz, e = int(state[2]), float(state[3]), float(state[4]), float(state[5]), float(state[6])
                particle_features.append([pid, e, px, py, pz])

            elif is_next_event:

                if (self.max_num_events is not None and self.N > self.max_num_events): # exit
                    break
                else: self.N += 1

                event = np.array(particle_features)
                event = sorted(event, key=lambda x: x[0], reverse=True)
                particle_features = []
                
                yield event
                
                #...go to next event

            else:
                pass
    
    def __exit__(self, exc_type, exc_value, traceback):
        self.hepmc.close()


class open_lhe(object):
    
    def __init__(self, path, coords: str='pt_eta_phi_m', max_num_events: int=None):   

        self.lhe= open(path,'r')
        self.coords = coords
        self.max_num_events = max_num_events
        self.N = 0

    def __enter__(self):

        for line in self.lhe:
            

            is_start_event = line.startswith("<event>") 
            is_end_event = line.startswith("</event>")

            state = str.split(line)
            is_final_state = True if (line.startswith("<")==False and  line.startswith("#")==False and len(state)==13 and state[1]==1) else False


            if is_start_event:
                print(line)
                particle_features = []

            elif is_final_state:
                pid, px, py, pz, e = int(state[0]), float(state[6]), float(state[7]), float(state[8]), float(state[9])
                particle_features.append([pid, e, px, py, pz])

            elif is_end_event:

                if (self.max_num_events is not None and self.N > self.max_num_events): # exit
                    break
                else: self.N += 1

                event = np.array(particle_features)
                event = sorted(event, key=lambda x: x[0], reverse=True)
                particle_features = []
                
                yield event
                
                #...go to next event

            else:
                pass
    
    def __exit__(self, exc_type, exc_value, traceback):
        self.lhe.close()