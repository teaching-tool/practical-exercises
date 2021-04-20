from setuptools import setup

setup(
    name = 'advalg',
    version = '1.0',
    description = "A test package",
    author = "Otto Clausen",
    packages = ['advalg'],
    install_requires = ['numpy', 'matplotlib'],
    setup_requires = ['numpy', 'matplotlib']
)