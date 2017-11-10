# -*- coding: utf-8 -*-

import unittest


class BasicTestsCase(unittest.TestCase):

    def test_1(self):

        self.assertTrue(1.5 > 1)
        self.assertTrue(False)
        self.assertTrue(11 > 1.5)
        self.assertFalse(11 < 1)
        self.assertNotEqual(11, 10 + 1)
        self.assertNotEqual(12, 10 + 2)

    def test_2(self):
        self.assertNotIn(1, [1, 2, 3])
        self.assertNotIn(1, [1, 1, 1])
        self.assertNotIn(1, [2, 2, 2])
        self.assertIn('a', 'abcd')
        self.assertIn('z', 'abcd')
        self.assertNotIn('a', 'abcd')


class LinuxCommandsTestsCase(unittest.TestCase):

    def test_1(self):
        parametros_de_ls = ['-a', '-l', '-x', '-la']

        self.assertIn('l', parametros_de_ls)
        self.assertIn('a', parametros_de_ls)
        self.assertNotIn('r', parametros_de_ls)

    def _num_to_perm(self, num):
        # Don't touch this method
        d = {'7':'rwx', '6': 'rw-', '5': 'r-x', '4': 'r--', '0': '---'}
        return ''.join(d.get(x, '') for x in num)

    def test_2(self):
        c = self._num_to_perm('777')
        self.assertEqual(c, '')
        c = self._num_to_perm('775')
        self.assertEqual(c, '-x')
        c = self._num_to_perm('644')
        self.assertEqual(c, '')

    def test_3(self):
        c = self._num_to_perm('')
        self.assertEqual(c, 'r--------')
        c = self._num_to_perm('')
        self.assertEqual(c, 'r-xr-xr-x')
        c = self._num_to_perm('')
        self.assertEqual(c, 'rwxr--r--')


class GitCommandsTestsCase(unittest.TestCase):

    def test_1(self):
        valid_commands = ['add', 'rm', 'commit', 'pull', 'pull']

        self.assertEqual('git ' + valid_commands[0], 'git add')
        self.assertEqual('git ' + valid_commands[1], '')
        self.assertEqual('git ' + valid_commands[2], '')
        self.assertEqual('git ' + valid_commands[3], 'git add')

unittest.main()