# -*- coding: utf-8 -*-
from distutils.core import setup

setup(
    name='esgp',
    version='0.1',
    packages=['pydenticon5'],
    url='https://git.ercpe.de/ercpe/pydenticon5',
    license='GPL-3',
    author='Johann Schmitz',
    description='Python implementation of the identicon5 javascript library',
    install_requires = [
        'Pillow'
    ]
)
