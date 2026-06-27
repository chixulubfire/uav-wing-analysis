# Computational Analysis and Optimization of Low-Reynolds-Number Wings for Small UAV Applications

A work-in-progress Python-based aerodynamic modeling 
framework for analyzing low-Reynolds-number
UAV wing performance using finite-wing 
theory.

### Table of Contents
- [About the Project](#about-the-project)
- [Built With](#built-with)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
- [Roadmap](#roadmap)
  - [Phase 1: Aerodynamic Foundations](#phase-1-aerodynamic-foundations)
  - [Phase 2: Finite Wing Modeling](#phase-2-finite-wing-modeling)
  - [Phase 3: Computational Analysis Framework](#phase-3-computational-analysis-framework)
  - [Phase 4: Optimization](#phase-4-optimization)
  - [Phase 5: Experimental Validation](#phase-5-experimental-validation)
  - [Future Work](#future-work)
- [References](#references)
- [Contributing](#contributing)
- [License](#license)
- [Disclaimer](#disclaimer)

### About the Project
uav-wing-analysis is a Python-based aerodynamic 
analysis framework designed to model the 
performance of finite wings operating at low Reynolds 
numbers. This model can be used to study how wing geometry
influences lift, drag, and overall aerodynamic efficiency.

### Built With
- Python 3.14.0 — simulation and modeling framework
- NumPy — numerical methods for aerodynamic computation
- Matplotlib — post-processing and visualization of aerodynamic performance
- JSON — structured configuration system for geometry, physics, and test cases

### Getting Started
#### Prerequisites
- Python 3.9.0+
- NumPy
- SciPy
- Matplotlib

#### Installation
#### 1. Clone the repo
```bash
git clone https://github.com/chixulubfire/uav-wing-analysis
cd uav-wing-analysis
```
#### 2. Create environment (optional but recommended)
```bash
python -m venv .venv
```
Windows:
```bash
.venv/Scripts/activate
```
Mac/Linux:
```bash
source .venv/bin/activate
```
#### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### Usage
#### 1. Define simulation case
Create or edit a trial JSON file in ```configs/trials```

Example ```trial1.json```:
```
{
  "airfoil": "NACA0012",
  "wing_span_m": 1,
  "root_chord_length_m": 0.2,
  "tip_chord_length_m": 0.2,
  "twist_angle_deg": 0,
  "sweep_angle_deg": 0,
  "dihedral_angle_deg": 0
}
```
#### 2. Set simulation configuration
Edit ```configs/simulation.json```:
```
{
  "trial": "../configs/trials/trial1.json",
}
```
#### 3. Run the simulation
```bash
python main.py
```
All configuration is file-driven via JSON, 
enabling rapid iteration of wing geometries 
without modifying source code.
### Roadmap
This project is under active development. The following 
milestones outline the planned progression of the 
computational model and experimental validation.
#### Phase 1: Aerodynamic Foundations
- NACA 4-digit airfoil geometry generation
- Basic lift and drag estimation using thin 
airfoil theory
#### Phase 2: Finite Wing Modeling
- Finite-wing corrections (induced drag, 
downwash effects)
- Factor in wing geometry (span, chord, taper, aspect ratio)
- Compute lift and drag for full wing configurations
#### Phase 3: Computational Analysis Framework
- Parameter sweep tools for wing design optimization
- Performance comparison across different airfoils and geometries
- Add visualization for aerodynamic outputs
#### Phase 4: Optimization
- Develop optimization routines for wing geometry
- Identify designs that maximize aerodynamic efficiency (L/D)
#### Phase 5: Experimental Validation
- Fabricate 3D-printed wing prototypes
- Conduct wind tunnel testing
- Compare experimental results with computational predictions
- Quantify error and refine model assumptions
#### Future Work
- Incorporate higher-fidelity aerodynamic methods (e.g. CFD validation)
- Investigate stall dynamics
- Package into an application

### References

1. ERAU, *Finite Wing Characteristics*.
   https://eaglepubs.erau.edu/introductiontoaerospaceflightvehicles/chapter/finite-wing-characteristics/

2. ERAU, *Computational Simulation for Aerospace Engineers*.
   https://eaglepubs.erau.edu/compsimforaero/chapter/c-3/

3. Akgün, A., *NACA 4-Digit Airfoil Generation*.
   https://web.itu.edu.tr/~atares/courses/CA/3.1.1_NACA4.html

4. Anderson, J., *Aircraft Performance and Design*
    https://soaneemrana.org/onewebmedia/AIRCRAFT%20PERFORMANCE%20AND%20DESIGN1.pdf
### Contributing
This is an independent research project.
Contributions, feedback, and suggestions are welcome, especially in areas such as:
- Aerodynamic modeling approaches and corrections
- Improvements to numerical methods or code structure
- Relevant literature or experimental references
- Bug fixes or performance optimizations

At the same time, this project follows a defined research
direction and methodology. Major changes to the core 
aerodynamic models or overall structure should be 
discussed before implementation.

To contribute, please open an issue or submit a pull request with a clear explanation of the proposed change.

### License
This project is licensed under the [MIT License](LICENSE).

### Disclaimer
This repository is part of an independent research
project. The codebase is under active development and 
should be considered experimental until validation and 
testing are completed.

