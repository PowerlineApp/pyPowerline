#!/usr/bin/env python

from setuptools import setup, find_packages
setup(name='powerline',
      version='0.1',
      packages=find_packages(),

      install_requires = ['requests'],

      license = "MIT",
      author = "Austin Papp",
      author_email = "austin@powerli.ne",
      description = "Client library to interface with PowerlineAPI",
      url = "https://github.com/PowerlineApp/pypowerline"
      )

