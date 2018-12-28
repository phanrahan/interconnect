from setuptools import setup
import sys

setup(
    name='interconnect',
    version='0.0.1',
    url='https://github.com/phanrahan/interconnect',
    license='MIT',
    maintainer='Pat Hanrahan',
    maintainer_email='hanrahan@cs.stanford.edu',
    description='Island-Style FPGA Interconnects',
    packages=[
        "interconnect",
    ],
    install_requires=[
        "bit_vector==0.39a0"
    ],
    python_requires='>=3.6'
)
