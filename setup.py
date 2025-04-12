"""
setup.py

Configuration script for building and distributing the 'common_utils' package.
Uses setuptools to define package metadata, dependencies, and distribution behavior.
"""
from setuptools import setup, find_packages


setup(
    name='common_utils',
    version='1.3',
    packages=find_packages(),
    url='http://example.com',
    license='MIT',
    author='Oleh Pihnastyi',
    author_email='pihnastyi@gmail.com',
    install_requires=[],
    description='The source code for a reusable Python utility library designed to simplify and'
                'speed up development across multiple projects. It provides a collection of common '
                'helper functions, tools, and components that can be shared and maintained in'
                'one central place'
)
