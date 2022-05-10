# coding: utf-8

from setuptools import setup, find_packages
from pypi import __VERSION__


def _requires_from_file(filename):
    return open(filename).read().splitlines()


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license_txt = f.read()

setup(
    name='pypi',
    version=__VERSION__,
    description='Fill in your project description',
    entry_points={
        "console_scripts": [
            "pypi = pypi.pypi:main"
        ]
    },
    long_description=readme,
    author='Kyohei Horikawa',
    author_email='kyohei3430@gmail.com',
    url='https://github.com/kyohei-horikawa/pypi',
    license=license_txt,
    packages=find_packages(exclude=('sample',)),
    # install_requires=_requires_from_file('requirements.txt')
)
