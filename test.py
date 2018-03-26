import doctest
import unittest

from diskdict import diskdict


def suitefn():
    suite = unittest.TestSuite()
    suite.addTests(doctest.DocTestSuite(diskdict))

    return suite


if __name__ == "__main__":
    doctest.testmod(diskdict)
