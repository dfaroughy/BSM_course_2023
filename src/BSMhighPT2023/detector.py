
    
import numpy as np
from particle import PDGID

''' The importance of calorimetry for highly-boosted jet substructure, Coleman et al, 1709.08705 
    see also 1706.04965

'''

def smear(event, eMaxTrack=220.0, eps=1e-10):
    
    # Particle type masks

    charged_mask = np.array([PDGID(p).charge != 0 for p in event['pid']]) & (event['E'] <= eMaxTrack)
    hadron_mask = np.array([PDGID(p).is_hadron for p in event['pid']])
    charged_hadron_mask = hadron_mask & charged_mask
    neutral_hadron_mask = hadron_mask & ~charged_mask 
    photon_mask = np.array([PDGID(p).is_sm_gauge_boson_or_higgs for p in event['pid']])
    lepton_mask = np.array([PDGID(p).is_sm_lepton for p in event['pid']])

    # Create an array for Gasussian covariance 
    
    sigma = np.zeros_like(event['E'])

    # Apply conditions using masks
    sigma[charged_hadron_mask] = np.sqrt((0.00025 * event['pt'][charged_hadron_mask])**2 + 0.015**2)
    sigma[neutral_hadron_mask] = np.sqrt((0.45 / np.sqrt(event['E'][neutral_hadron_mask]))**2 + 0.05**2)
    sigma[photon_mask] = np.sqrt((0.021 / np.sqrt(event['E'][photon_mask]))**2 + (0.094 / event['E'][photon_mask])**2 + 0.005**2)
    sigma[lepton_mask] = np.sqrt((0.00025 * event['pt'][lepton_mask])**2 + 0.015**2)

    # Smearing

    smear_factors = np.maximum(eps, np.random.normal(1, sigma, size=event['pt'].shape))

    event['px'] *= smear_factors
    event['py'] *= smear_factors
    event['pz'] *= smear_factors
    event['E'] *= smear_factors
    event['pt'] *= smear_factors
    event['M'] *= smear_factors

    idx = np.argsort(-event['pt'])  # The negative sign is to sort in descending order

    return event[idx]


