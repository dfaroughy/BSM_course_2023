# FeynRules

Installation is pretty sttraightforward as any other Mathematica package. Follow instructions from http://feynrules.irmp.ucl.ac.be

# MADGRAPH5

### Instructions for setting up conda environment for MadGraph (optional but recommended):


1. Install conda if not already installed:
  
  > wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh

2. Set up conda environment:
  
  > conda create -n <mg_env_name> python=2.7
  
Replace `<mg_env_name>' with whatever name you like, e.g. `madgraph_bsm_lj2023'
check that the new envirnoment was created
 
  > conda info --envs

3. Activate environment:

  > conda activate <mg_env_name>

### Instructions for downloading and running MadGraph:

1. Download MadGraph from https://launchpad.net/mg5amcnlo/2.0/2.6.x/+download/MG5_aMC_v2.6.7.tar.gz and save in root directory (the one containing setup.py)

1. enter MG5_aMC_v2_6_7 directory and run MG5:

  > ./bin/mg5_aMC

2. install pythia8 from within the MG5 prompt (say yes 'y' to every question asked by the prompt):

  `MG5_aMC> install mg5amc_py8_interface`

3. test setup by simulating 10k ttbar events:

  `MG5_aMC> generate p p > t t~`
  `MG5_aMC> output` 
  `MG5_aMC> open index.html`
  `MG5_aMC> launch` 
  `MG5_aMC> shower=Pythia8`

If everything works, you should see a browser pop up with the run results, then after a while, a value for the xsection of ~500 and event files generated at:

 - PROC_sm_0/Events/run_01/unweighted_events.lhe.gz 
 - PROC_sm_0/Events/run_01/tag_1_pythia8_events.hepmc.gz 

Once you finish your MG5 runs be sure to deactivate the environment via:

  > conda deactivate

# PYTHON SCRIPTS

### Instructions for running python scripts 
  
1. create a conda environment for python scripts (recommended) with python 3.7:

  > conda create -n <py_env_name> python=3.7

2. From the root dir (the one containing the setup.py file) activate the environment an then install the required package by running:

  > pip install -e .

