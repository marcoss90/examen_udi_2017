# -*- coding: utf-8 -*-

import unittest


class BasicTestsCase(unittest.TestCase):

    def test_1(self):

        self.assertTrue(1.5 > 1)
        self.assertTrue(True)
        self.assertTrue(11 > 1.5)
        self.assertFalse(11 < 1)
        self.assertNotEqual(11, 10 + 4)
        self.assertNotEqual(12, 10 + 3)

    def test_2(self):
        self.assertNotIn(1, [3, 4, 5])
        self.assertNotIn(1, [6, 7, 9])
        self.assertNotIn(1, [2, 2, 2])
        self.assertIn('a', 'abcd')
        self.assertIn('z', 'abcz')
        self.assertNotIn('a', 'bcdd')


class LinuxCommandsTestsCase(unittest.TestCase):

    def test_1(self):
        parametros_de_ls = ['-a', '-l', '-x', '-la']

        self.assertIn('-a', parametros_de_ls)
        self.assertIn('-l', parametros_de_ls)
        self.assertNotIn('x', parametros_de_ls)

    def _num_to_perm(self, num):
        # Don't touch this method
        d = {'7':'rwx', '6': 'rw-', '5': 'r-x', '4': 'r--', '0': '---'}
        return ''.join(d.get(x, '') for x in num)

    def test_2(self):
        c = self._num_to_perm('777')
        self.assertEqual(c, 'rwxrwxrwx')
        c = self._num_to_perm('775')
        self.assertEqual(c, 'rwxrwxr-x')
        c = self._num_to_perm('644')
        self.assertEqual(c, 'rw-r--r--')

    def test_3(self):
        c = self._num_to_perm('400')
        self.assertEqual(c, 'r--------')
        c = self._num_to_perm('555')
        self.assertEqual(c, 'r-xr-xr-x')
        c = self._num_to_perm('744')
        self.assertEqual(c, 'rwxr--r--')


class GitCommandsTestsCase(unittest.TestCase):

    def test_1(self):
        valid_commands = ['add', 'rm', 'commit', 'pull', 'pull']

        self.assertEqual('git ' + valid_commands[0], 'git add')
        self.assertEqual('git ' + valid_commands[1], 'git rm')
        self.assertEqual('git ' + valid_commands[2], 'git commit')
        self.assertEqual('git ' + valid_commands[3], 'git pull')

unittest.main()
