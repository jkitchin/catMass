#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = ['Click>=7.0', ]

test_requirements = [ ]

setup(
    author="Adam S. Hoffman",
    author_email='ashoff@slac.stanford.edu',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="Py Qt package for calculating the proper loading of samples for XAS measuremnts",
    entry_points={
        'console_scripts': [
            'catmass=catmass.cli:main',
        ],
    },
    install_requires=requirements,
    license="GNU General Public License v3",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='catmass',
    name='catmass',
    packages=find_packages(include=['catmass', 'catmass.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/ahoffm02/catmass',
    version='0.1.0',
    zip_safe=False,
)
