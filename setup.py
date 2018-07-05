from setuptools import setup, find_packages

setup(
    name = 'PyPkgSample',
    version = '0.1.0',
    description='Sample Package for YuJunLi',
    author = 'Yu-Jun Li',
    author_email='li2566@purdue.edu',
    packages = find_packages(exclude=('tests',)),
    license = 'MIT',
    install_requires = ['requests'],
    data_files = None
    )