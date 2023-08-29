import numpy as np
import awkward as ak
import fastjet

def get_jets(event, jetdef, pt_min=20.0):
    
    event = ak.Array(event)
    
    cluster = fastjet.ClusterSequence(event, jetdef)    
    jets_ak = cluster.inclusive_jets(pt_min)
    jets = ak.to_numpy(jets_ak)

    #... get jet feature

    jet_pt = np.sqrt(jets['px']**2 + jets['py']**2)
    jet_rap = np.arctanh(jets['pz'] / jets['E'])
    jet_phi = np.arctan2(jets['py'], jets['px'])
    jet_M2 = jets['E']**2 - jets['px']**2 - jets['py']**2 - jets['pz']**2
    jet_M = np.sqrt(jet_M2[jet_M2 > 0])
    jet_pid = np.ones_like(jet_M) * 4

    jets = np.array(list(zip(jet_pt, jet_rap, jet_phi, jet_M, jets['px'], jets['py'], jets['pz'], jets['E'], jet_pid)), dtype=[('pt', 'f8'), ('eta', 'f8'), ('phi', 'f8'), ('M', 'f8'), ('px', 'f8'), ('py', 'f8'), ('pz', 'f8'), ('E', 'f8'), ('pid', 'i8')])
    idx = np.argsort(-jets['pt'])  # The negative sign is to sort in descending order
    return jets[idx]

