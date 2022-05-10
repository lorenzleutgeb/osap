from distutils.core import setup
from setuptools import find_packages

setup(
    name='xdl',
    version='1.0.0',
    description='Package for working with XDL (chemical descriptive language).',
    author='Matthew Craven',
    author_email='matthew.craven@glasgow.ac.uk',
    packages=find_packages(),
    package_data={
        'xdl': ['localisation/*.json'],
    },
    python_requires=">=3.7.0",
    include_package_data=True,
    install_requires=[
        'networkx>=2',
        'appdirs>=1',
        'termcolor>=1',
        'tabulate>=0.8.7',
        'pandas>=1.2.3'
        # The reason these are == instead of >= is I am much more paranoid about
        # socket.io stuff breaking than other stuff breaking.
        'python-socketio==4.6.0',
        'websocket-client==0.57.0'
    ],
    extras_require={
        'chemputer': [
            'SerialLabware @ git+ssh://git@gitlab.com/croningroup/chemputer/seriallabware.git@SerialLabware2',
            'ChemputerAPI @ git+ssh://git@gitlab.com/croningroup/chemputer/chemputerapi.git@master',
            'chempiler @ git+ssh://git@gitlab.com/croningroup/chemputer/chempiler.git@master',
            'commanduinolabware @ git+ssh://git@gitlab.com/croningroup/chemputer/commanduinolabware.git@master',
            'AnalyticalLabware @ git+ssh://git@gitlab.com/croningroup/chemputer/analyticallabware.git#egg=AnalyticalLabware[oceanoptics,spinsolve,agilent,test]',
            'chemputerxdl @ git+ssh://git@gitlab.com/croningroup/chemputer/chemputerxdl.git@master'
        ]
    }
)
