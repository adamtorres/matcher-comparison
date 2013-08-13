from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(name='MatcherCompare',
      version=version,
      description="Basic comparison of matcher libraries.",
      long_description="""Compares common features of various matcher libraries.""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='should-dsl sure hamcrest compare describe',
      author='Adam Torres',
      author_email='atorres@amplify-nation.com',
      url='www.amplify-nation.com',
      license='None',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=True,
      install_requires=[
          "pyHamcrest",
          "pyshould",
          "should-dsl",
          "sure"
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
