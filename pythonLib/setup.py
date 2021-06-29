from setuptools import setup

setup(
    name = 'advalg',
    version = '1.0',
    description = "Advanced Algorithms",
    author = "Otto Clausen",
    packages = ['advalg'],
    install_requires = ['numpy', 'matplotlib'],
    setup_requires = ['numpy', 'matplotlib'],
    package_data={'advalg': ['data/*']}
)