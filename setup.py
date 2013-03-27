# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


setup(
    name='scrypt_djnago_password_hasher',
    version='0.0.2',
    description='Djnago password hasher with scrypt algorithm',
    author='sammyrulez',
    url='https://github.com/sammyrulez/ScryptPasswordHasher',
    license='BSD',
    packages=find_packages(exclude=('tests')),
    py_modules=['extras'],
    install_requires=['scrypt','django']
)