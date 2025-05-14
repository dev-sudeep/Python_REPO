from setuptools import setup
from Cython.Build import cythonize
import sys

setup(
    ext_modules=cythonize(sys.argv[2]),  # Replace with your .pyx file
)