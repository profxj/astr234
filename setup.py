#!/usr/bin/env python

import sys
import numpy as np

from   setuptools import setup, find_packages

setup(name             = 'astr234',
      version          = 'v0.1',
      description      = 'Files and Python code for ASTR 234',
      author           = 'J. Xavier Prochaska and Andrew Skemer',
      author_email     = 'jxp@ucsc.edu',
      url              = 'https://github.com/profxj/astr234',
      packages         = find_packages( include=['*.py'] ),
      install_requires = [ 'astropy',
                           'emcee',
                           'numpy',
                           'scipy',
                           'tqdm',
                           'matplotlib',
                           'extinction',
                         ])

print ('********************************************************************')
print ('astr234 package has been successfully installed to your machine. Enjoy!')
print ('********************************************************************')