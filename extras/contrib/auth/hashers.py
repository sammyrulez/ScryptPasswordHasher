
from django.contrib.auth import hashers
import random

class SCryptPasswordHasher(hashers.BasePasswordHasher):
    """SCryptPasswordHasher for django authentication"""

    algorithm = "scrypt"
    library = ("scrypt", "scrypt",)
    maxtime=0.5
    std_length = 64

    def _randstr(length):
        return ''.join(chr(random.randint(0,255)) for i in range(length))

    def salt(self):
        """
        Generates a cryptographically secure nonce salt in ascii
        """
        scrypt = self._load_library()
        return _randstr(self.std_length)

    def encode(self, password, salt):
        scrypt = self._load_library()
        data =  scrypt.encrypt(salt, password, maxtime=self.maxtime)
        return "%s$%s" % (self.algorithm, data)


    def safe_summary(self, encoded):
        """
        Returns a summary of safe values

        The result is a dictionary and will be used where the password field
        must be displayed to construct a safe representation of the password.
        """
        algorithm, empty, algostr, maxtime, data = encoded.split('$', 4)
        assert algorithm == self.algorithm
        salt, checksum = data[:22], data[22:]
        return SortedDict([
            (_('algorithm'), algorithm),
            (_('maxtime'), maxtime),
            (_('salt'), mask_hash(salt)),
            (_('checksum'), mask_hash(checksum)),
        ])
