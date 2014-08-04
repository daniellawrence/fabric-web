#!/usr/bin/env python
from setuptools import setup, find_packages

setup(
    name="Fabric-Web",
    version="0.0.1",
    packages=find_packages(),
    include_package_data=True,
    author="Daniel Lawrence",
    author_email="dannyla@linux.com",
    description="Throwing fabric up as a website",
    license="MIT",
    keywords="fabric",
    url="http://github.com/daniellawrence/fabric-web",
    install_requires=[
        'fabric',
        'flask'
    ],
)
