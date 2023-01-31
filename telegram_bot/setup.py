# coding: utf-8

import os

from pkg_resources import parse_requirements
from setuptools import setup, find_packages


def load_requirements(fname: str) -> list:
    requirements = []
    with open(fname, 'r') as fp:
        for req in parse_requirements(fp.read()):
            extras = '[{}]'.format(','.join(req.extras)) if req.extras else ''
            requirements.append(
                '{}{}{}'.format(req.name, extras, req.specifier)
            )
    return requirements


PKG_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT_DIR = os.path.dirname(os.path.dirname(PKG_DIR)).strip('/')
SETUP_KWARGS = dict(
    name='telegram_bot',
    author='Karina Gordeeva',
    license='MIT',
    python_requires='>=3.8',
    packages=find_packages(exclude=[]),
    include_package_data=True,
    install_requires=load_requirements('requirements.txt')
)


if __name__ == '__main__':
    setup(**SETUP_KWARGS)
