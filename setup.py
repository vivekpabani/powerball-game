# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='powerball',
    version='0.1.0',
    description='Powerball Game Simulation.',
    long_description=readme,
    author='Vivek Pabani',
    author_email='vpabani@hawk.iit.edu',
    url='https://github.com/vivekpabani/powerball-game',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)
