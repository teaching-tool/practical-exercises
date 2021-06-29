# Advanced Algorithms Code

This repository contains code written to support the programming exercises in Advanced Algorithms.

## Structure
Everything the students need to make their implementations and experiments easier is in the advalg package. Besides supporting code, the package also contains test files. The files prefixed with "solution" are my solutions written with the supporting code. Files prefixed with "skeleton" are code skeletons which should be given to students.

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

The codebase comes with a *<nolink>setup.py</nolink>* file. The package can be installed by running:

`python setup.py install`

Alternatively, the setup file can be used to create a python wheel:

`pip install wheel`  
`python setup.py bdist_wheel`

This will create a folder called *dist* with the file *advalg-1.0-py3-none-any.whl*, which can be given to students and installed using:

`pip install advalg-1.0-py3-none-any.whl`

After that, the advalg package will be available. The following code should work in a python terminal:

```python
from advalg.helpers import subsets
for s in subsets(['a','b','c']):
    print(s)
```

Numpy and Matplotlib are python packages. They should automatically be installed with the rest of the code. Otherwise, they can be installed manually by running:

`pip install numpy matplotlib`

## Documentation
The documentation for the package can be found in the docs folder. Additionally, the files *sat_example.py* and *lp_example.py* contain examples for the SAT-solver and LP-solver respectively.
