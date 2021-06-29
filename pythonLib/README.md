# Advanced Algorithms Code

This repository contains code written to support the programming exercises in Advanced Algorithms.

## Structure
Everything the students need to make their implementations and experiments easier is in the advalg package. Besides supporting code, the package also contains test files. The files prefixed with "solution" are my solutions written with the supporting code.

## Dependencies

The package has 4 dependencies which must be installed.

- NumPy (https://numpy.org/)
- Matplotlib (https://matplotlib.org/)
- LP_Solve (https://sourceforge.net/projects/lpsolve/)
- Minisat (http://minisat.se/)

## Installation
LP_Solve and Minisat are standalone programs. Download the programs from the links above and follow their installation instructions. The programs should be included in your PATH variable. To check that both programs are installed properly you can run:

`minisat --help`  
`lp_solve -h`

The codebase comes with a `setup.py` file. The package can be installed by running:

`python setup.py install`

Numpy and Matplotlib are python packages and should be installed automatically by running the setup script. Otherwise, they can be installed by running:

`pip3 install numpy matplotlib`

## Documentation
The documentation for the package can be found in the docs folder. Additionally, the files `sat_example.py` and `lp_examples.py` contain examples for the SAT-solver and LP-solver respectively.
