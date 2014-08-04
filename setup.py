#!/usr/bin/env python
from setuptools import setup, find_packages

setup(
    name="Fabric-Web",
    version="0.0.1",
    packages=find_packages(),
    include_package_data=True,
    author="Daniel Lawrence",
    author_email="dannyla@linux.com",
    description="Taking the magic of fabric and throwing up as a website for ease of use",
    #scripts=[""],
    license="MIT",
    keywords="fabric",
    url="http://github.com/daniellawrence/fabric-web",
    install_requires=[
        'fabric',
        'flask'
    ],
)
