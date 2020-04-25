import os
from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = f.readlines()

with open(os.path.join('.', 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='etabar',
    version='0.0.2',
    author='Mayank Vaidya',
    author_email='mayank8318@gmail.com',
    url='https://github.com/mayank8318/ETABar',
    description='A simple library to display an eta bar',
    long_description=long_description,
    long_description_content_type="text/markdown",
    license='MIT',
    packages=find_packages(),
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ),
    keywords='etabar progressbar bar python package mayank8318',
    install_requires=requirements,
    zip_safe=False,
    include_package_data=True
)
