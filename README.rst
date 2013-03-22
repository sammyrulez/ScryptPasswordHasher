##############################################
SCryptPasswordHasher for django authentication
##############################################


image:: https://travis-ci.org/sammyrulez/ScryptPasswordHasher.png?branch=master

Django provides a flexible password storage system and uses PBKDF2 by default.

Those are the components used for storing a User’s password, separated by the dollar-sign character and consist of: the hashing algorithm, the number of algorithm iterations (work factor), the random salt, and the resulting password hash. The algorithm is one of a number of one-way hashing or password storage algorithms Django can use.

This module enable the use of `scrypt <http://en.wikipedia.org/wiki/Scrypt>`_ algoritym

1 install this module

2 Add  **SCryptPasswordHasher** as the first entry in PASSWORD_HASHERS:

PASSWORD_HASHERS = (
    'myproject.hashers.MyPBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
    'django.contrib.auth.hashers.BCryptPasswordHasher',
    'django.contrib.auth.hashers.SHA1PasswordHasher',
    'django.contrib.auth.hashers.MD5PasswordHasher',
    'django.contrib.auth.hashers.CryptPasswordHasher',
)



It uses

`scrypt <https://pypi.python.org/pypi/scrypt/>`_ python package by  Magnus Hallin