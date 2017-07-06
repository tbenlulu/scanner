from setuptools import setup, find_packages
from os import path

requires = ['argparse','socket']

dist = setup(
    name='scanner',
    version='0.0.1',
    description="A system for controlling process state under UNIX",
    author="Chris McDonough",
    author_email="chrism@plope.com",
    packages=find_packages(),
    install_requires=requires,
    zip_safe=False,
    test_suite="supervisor.tests",
    entry_points={
        'console_scripts': [
            'scanner = portscan:main',
        ],
    },
)