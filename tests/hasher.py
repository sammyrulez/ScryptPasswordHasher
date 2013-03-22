import unittest
import os, sys
from django.conf import settings

DIRNAME = os.path.abspath(os.path.dirname('.'))

print('working DIRNAME %s' % DIRNAME)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(DIRNAME, 'database.db'),
        'USER': '',
        'PASSWORD': '',
    }
}


settings.configure(DEBUG = True,
                   DATABASES = DATABASES,
                   INSTALLED_APPS = ('django.contrib.auth',
                                     'django.contrib.contenttypes',
                                     'django.contrib.sessions',))

sys.path.insert(0, DIRNAME)

from extras.contrib.auth.hashers import SCryptPasswordHasher

class TestSCryptPasswordHasher(unittest.TestCase):

    def setUp(self):
        self.hasher = SCryptPasswordHasher()

    def test_safe_summary(self):
        #summary = self.hasher.safe_summary('RANDOM_STRING')
        pass

    def test_salt(self):
        tested_vals = []
        for t in range(1,10000):
            test_case = self.hasher.salt()
            if test_case in tested_vals:
                self.fail("%s generated twice in just %d attempts.Shouldn't happen" % (test_case,t))
            else:
                tested_vals.append(test_case)

    def test_encode(self):
         out_psw = self.hasher.encode('EASY',self.hasher.salt())
         self.assertTrue(len(out_psw) <= 128)
         self.assertTrue(self.hasher.algorithm in out_psw)
         self.assertTrue('$' in out_psw)



if __name__ == '__main__':


    unittest.main()
    #TODO clenup