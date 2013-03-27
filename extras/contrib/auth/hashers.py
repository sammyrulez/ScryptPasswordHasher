
from django.contrib.auth import hashers
from django.utils.crypto import constant_time_compare
from django.utils.encoding import force_bytes, force_str
from django.utils.datastructures import SortedDict
import random


class SCryptPasswordHasher(hashers.BasePasswordHasher):
    """SCryptPasswordHasher for django authentication"""

    algorithm = "scrypt"
    library = ("scrypt", "scrypt",)
    maxtime=0.5
    std_length = 32

    def _randstr(self,length):
        return ''.join(chr(random.randint(0,255)) for i in range(length))

    def salt(self):
        """
        Generates a cryptographically secure nonce salt in ascii
        """
        scrypt = self._load_library()
        return self._randstr(self.std_length)

    def encode(self, password, salt):
        """
        Creates an encoded database value
        The result is normally formatted as "algorithm$salt$hash" and
        must be fewer than 128 characters.
        """
        scrypt = self._load_library()
        data =  force_str(scrypt.hash(force_bytes(password),salt ))
        return "%s$%d$%s$%s" % (self.algorithm, self.maxtime, salt, data)

    def verify(self, password, encoded):
        algorithm, local_maxtime, salt, data = encoded.split('$', 3)
        assert algorithm == self.algorithm
        scrypt = self._load_library()
        return constant_time_compare(data,force_str(scrypt.hash(force_bytes(password),salt )))

    def safe_summary(self, encoded):
        """
        Returns a summary of safe values

        The result is a dictionary and will be used where the password field
        must be displayed to construct a safe representation of the password.
        """
        algorithm, local_maxtime, salt, data = encoded.split('$', 3)
        assert algorithm == self.algorithm
        return SortedDict([
            (_('algorithm'), algorithm),
            (_('maxtime'), local_maxtime),
            (_('salt'), hashers.mask_hash(salt)),
            (_('checksum'), hashers.mask_hash(data)),
        ])
