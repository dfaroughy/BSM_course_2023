import matplotlib.pyplot as plt
import numpy as np
from particle import Particle
import seaborn as sns
import matplotlib.patches as patches

# def event_display(event, point_sizes=(2, 200), ax=None, grid=False, marker='o', lw=0):

#     labels = np.unique(np.abs(event['pid']))
#     # class_names = [Particle.from_pdgid(p).pdg_name for p in labels if p > 10 else 'jet' ]
#     class_names = [Particle.from_pdgid(p).pdg_name if p > 10 else 'jet' for p in labels]
#     class_names = Particle.from_pdgid(p).pdg_name
#     colors = sns.color_palette('hls', len(labels))
#     sns.scatterplot(x=event['eta'], 
#                     y=event['phi'], 
#                     hue=np.abs(event['pid']), 
#                     palette=colors, 
#                     size=event['pt'], 
#                     sizes=point_sizes, 
#                     marker=marker,
#                     linewidth = lw,
#                     ax=ax)
#     ax.set_xlim(-7, 7)
#     ax.set_ylim(-np.pi, np.pi)
#     ax.set_xlabel(r'$\eta$')
#     ax.set_ylabel(r'$\phi$')
#     ax.set_title(r'num particles: ${}$'.format(len(event['pt'])), fontsize=10)
#     ax.minorticks_on()
#     if grid:
#         ax.grid(which='minor', color='lightgray', linewidth=0.4, linestyle='-')
#         ax.grid(color='gray', linewidth=0.4, linestyle='-')
#     ax.set_facecolor('#f0f0f0')
#     handles = [ax.plot([],[], marker=marker, ls="", color=colors[i],  markersize=5)[0] for i in range(len(labels))]
#     ax.legend(handles, class_names, loc='upper left', bbox_to_anchor=(0, 1.0), ncol=1, fontsize=7)

def event_display(event, point_sizes=(2, 200), ax=None, grid=False, marker='o', lw=0):

    event = np.array(event)
    labels = np.unique(np.abs(event['pid']))
    class_names = [Particle.from_pdgid(p).pdg_name if p > 10 else 'jet' for p in labels]
    colors = sns.color_palette('hls', len(labels))
    if len(event) == 1:
        # When only one point is present
        color = colors[0]
        size = event['pt'][0]
        ax.scatter(event['eta'][0], event['phi'][0], sizes=point_sizes,  color=color, s=size, marker=marker, linewidth=lw, ax=ax)
    else:
        sns.scatterplot(x=event['eta'], 
                        y=event['phi'], 
                        hue=np.abs(event['pid']), 
                        palette=colors, 
                        size=event['pt'], 
                        sizes=point_sizes, 
                        marker=marker,
                        linewidth = lw,
                        ax=ax)
    ax.set_xlim(-5, 5)
    ax.set_ylim(-5, 5)
    ax.set_xlabel(r'$\eta$')
    ax.set_ylabel(r'$\phi$')
    ax.set_title(r'num particles: ${}$'.format(len(event['pt'])), fontsize=10)
    ax.minorticks_on()
    if grid:
        ax.grid(which='minor', color='lightgray', linewidth=0.4, linestyle='-')
        ax.grid(color='gray', linewidth=0.4, linestyle='-')
    ax.set_facecolor('#f0f0f0')
    handles = [ax.plot([],[], marker=marker, ls="", color=colors[i],  markersize=5)[0] for i in range(len(labels))]
    ax.legend(handles, class_names, loc='upper left', bbox_to_anchor=(0, 1.0), ncol=1, fontsize=7)



def event_display_grid(events, nrows, ncols, point_sizes=(2, 200), figsize=(10, 10), grid=False, marker='o', lw=1):
    fig, axs = plt.subplots(nrows=nrows, ncols=ncols, figsize=figsize)
    for i, event in enumerate(events):
        ax = axs[i // ncols, i % ncols]
        event_display(event, point_sizes, ax, grid, marker, lw)
    plt.tight_layout()
    plt.show()

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
            circle = patches.Circle((lepton['eta'], lepton['phi']), R_iso, fill=False, color=color, linestyle='dotted')
            ax.add_patch(circle)
            ax.scatter(hadrons['eta'][dR < R_iso], hadrons['phi'][dR < R_iso], s=hadrons['pt'][dR < R_iso], c=color, marker='o', label=f'Hadrons near Lepton {i}')        
            ax.scatter(lepton['eta'], lepton['phi'], s=lepton['pt'], c=color , marker='o', label=f'isolated lepton {i}')
        else:
            circle = patches.Circle((lepton['eta'], lepton['phi']), R_iso, fill=False, color='r', linestyle='dotted')
            ax.add_patch(circle)
            ax.scatter(hadrons['eta'][dR < R_iso], hadrons['phi'][dR < R_iso], s=hadrons['pt'][dR < R_iso], c='r', marker='o', label=f'Hadrons near Lepton {i}')   
            ax.scatter(lepton['eta'], lepton['phi'], s=lepton['pt'], c='r' , marker='x', label=f'isolated lepton {i}')

    ax.set_xlabel('eta')
    ax.set_ylabel('phi')
    ax.set_title('Isolation Visualization')
    ax.set_xlim(xlim)
    ax.set_ylim(ylim)
    plt.show()


def delta_phi(phi1, phi2):
    """Compute delta phi between two phi values (both arrays) and handle wrapping."""
    dphi = phi1 - phi2
    dphi = np.where(dphi > np.pi, dphi - 2 * np.pi, dphi)
    dphi = np.where(dphi <= -np.pi, dphi + 2 * np.pi, dphi)
    return dphi

def delta_R(eta1, phi1, eta2, phi2):
    """Compute delta R between two sets of eta and phi values."""
    deta = eta1 - eta2
    dphi = delta_phi(phi1, phi2)
    return np.sqrt(deta**2 + dphi**2)