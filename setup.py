from setuptools import setup, find_packages
from os import path

requires = ['argparse','socket']

dist = setup(
    name='scanner',
    version='0.0.1',
    description="A simple port scanner",
    author="Tamir Ben Lulu",
    author_email="tbenlulu@email.com",
    packages=find_packages(),
    install_requires=requires,
    zip_safe=False,
    entry_points={
        'console_scripts': [
            'scanner = scanner:main',
        ],
    },
)