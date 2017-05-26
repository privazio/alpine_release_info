import unittest

from alpine_release_info import info, defaults

version_re = '\d+\.\d+\.\d+'


class TestAlpineReleaseInfo(unittest.TestCase):

    def test_latest_default_release(self):
        v = info(defaults['mirror'], defaults['branch'], defaults['arch'], defaults['flavor'], 'version')
        self.assertRegexpMatches(v, version_re)

    def test_latest_default_release_queries(self):
        for query in ['url','sha512','sha256','gpgsig']:
            r = info(defaults['mirror'], defaults['branch'], defaults['arch'], defaults['flavor'], query)
            self.assertIsNotNone(r)


    def test_known_queries(self):
        for branch in ['v3.5', 'v3.6']:
            for arch in ['armhf', 'x86', 'x86_64']:
                v = info(defaults['mirror'], branch, arch, 'alpine-minirootfs', 'version')
                self.assertRegexpMatches(v, version_re)

    def test_invalid_branch(self):
        with self.assertRaisesRegexp(ValueError, 'branch'):
            v = info(defaults['mirror'], 'v1.0', defaults['arch'], defaults['flavor'], 'version')

    def test_invalid_architecture(self):
        with self.assertRaisesRegexp(ValueError, 'arch'):
            v = info(defaults['mirror'], defaults['branch'], '8086', defaults['flavor'], 'version')

    def test_invalid_flavor(self):
        with self.assertRaisesRegexp(ValueError, 'flavor'):
            v = info(defaults['mirror'], defaults['branch'], defaults['arch'], 'alpine-floppy', 'version')

    def test_missing_arch_download(self):
        with self.assertRaisesRegexp(ValueError, 'No latest-releases'):
            v = info(defaults['mirror'], 'v3.4', 'ppc64le', defaults['flavor'], 'version')

    def test_missing_flavor_download(self):
        with self.assertRaisesRegexp(ValueError, 'No release'):
            v = info(defaults['mirror'], 'v3.4', defaults['arch'], 'alpine-minirootfs', 'version')


if __name__ == '__main__':
    unittest.main()