import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from particle import PDGID

# def delta_phi(phi1, phi2):
#     """Compute delta phi between two phi values (both arrays) and handle wrapping."""
#     dphi = phi1 - phi2
#     dphi = np.where(dphi > np.pi, dphi - 2 * np.pi, dphi)
#     dphi = np.where(dphi <= -np.pi, dphi + 2 * np.pi, dphi)
#     return dphi

def delta_phi(phi1, phi2):
    """get the correct delta phi between [-pi, pi]] for both numbers and arrays."""
    dphi = np.abs(phi1 - phi2)
    return np.where(dphi > np.pi, 2 * np.pi - dphi, dphi)

def delta_R(eta1, phi1, eta2, phi2):
    """Compute delta R between two sets of eta and phi values."""
    deta = eta1 - eta2
    dphi = delta_phi(phi1, phi2)
    return np.sqrt(deta**2 + dphi**2)

def isolated_object(isolated_candidates, hadrons, R_iso=0.4, threshold=0.05, pt_min=1.0):
    """    
    Args:
    - isolated_candidates: The lepton/photon array.
    - hadrons: The hadron array.
    - R_iso: Isolation radius.
    - threshold: Isolation cut.
    """

    n_cand = len(isolated_candidates)
    is_isolated = np.zeros(n_cand, dtype=bool)

    for idx, cand in enumerate(isolated_candidates):
        dR = delta_R(cand['eta'], cand['phi'], hadrons['eta'], hadrons['phi'])
        hadrons_nearby = hadrons[(dR < R_iso) & (hadrons['pt'] > pt_min)]
        
        if np.sum(hadrons_nearby['pt']) / cand['pt'] <= threshold: is_isolated[idx] = True
        else: hadrons = np.append(hadrons, cand)

    isolated = isolated_candidates[is_isolated]
    idx = np.argsort(-isolated['pt'])  # The negative sign is to sort in descending order
    
    return isolated[idx], hadrons


def isolated_object_bool(event, pid, R_iso=0.4, threshold=0.05, pt_min=0.5):

    isolated = np.zeros(len(event), dtype=bool)
    mask = abs(event['pid']) == pid  # issue!!!!!!!!!!!!!!

    for idx, cand in enumerate(event[mask]):
        hadrons = event[~mask]
        dR = delta_R(cand['eta'], cand['phi'], hadrons['eta'], hadrons['phi'])
        hadrons_nearby = hadrons[(dR < R_iso) & (hadrons['pt'] > pt_min)]
        isolated[idx] = np.sum(hadrons_nearby['pt']) / cand['pt'] <= threshold 

    return isolated

    
def plot_isolation(leptons, hadrons, R_iso, threshold, figsize=(5, 5), xlim=[-3.5, 3.5], ylim=[-np.pi, np.pi]):
    """
    Visualize the isolation of leptons with nearby hadrons.
    
    Args:
    - leptons: The lepton array.
    - hadrons: The hadron array.
    - R: Isolation radius.
    """
    
    fig, ax = plt.subplots(figsize=figsize)
    ax.scatter(hadrons['eta'], hadrons['phi'], s=hadrons['pt'], c='grey', label='Hadrons (outside R)')
    colors = plt.cm.viridis(np.linspace(0, 1, len(leptons)))  # Generate a unique color for each lepton
    
    # For each lepton, draw a circle and plot nearby hadrons within the circle

    for i, lepton in enumerate(leptons):
        color = colors[i]
        dR = delta_R(lepton['eta'], lepton['phi'], hadrons['eta'], hadrons['phi'])
        if np.sum(hadrons['pt'][dR < R_iso]) / lepton['pt'] <= threshold:
            circle = patches.Circle((lepton['eta'], lepton['phi']), R_iso, fill=False, color=color, linestyle='dashed')
            ax.add_patch(circle)
            ax.scatter(hadrons['eta'][dR < R_iso], hadrons['phi'][dR < R_iso], s=hadrons['pt'][dR < R_iso], c=color, marker='o', label=f'Hadrons near Lepton {i}')        
            ax.scatter(lepton['eta'], lepton['phi'], s=lepton['pt'], c=color , marker='o', label=f'isolated lepton {i}')
        else:
            circle = patches.Circle((lepton['eta'], lepton['phi']), R_iso, fill=False, color='r', linestyle='dashed')
            ax.add_patch(circle)
            ax.scatter(hadrons['eta'][dR < R_iso], hadrons['phi'][dR < R_iso], s=hadrons['pt'][dR < R_iso], c='r', marker='o', label=f'Hadrons near Lepton {i}')   
            ax.scatter(lepton['eta'], lepton['phi'], s=lepton['pt'], c='r' , marker='x', label=f'isolated lepton {i}')

    ax.set_xlabel('eta')
    ax.set_ylabel('phi')
    ax.set_title('Isolation Visualization')
    ax.set_xlim(xlim)
    ax.set_ylim(ylim)
    plt.show()
