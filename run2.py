import unittest
from Spec_GooglePage import TestGooglePage
from Spec_GooglePageTwo import TestGooglePageTwo
import os
import glob
import sys
import xmlrunner

if __name__=="__main__":
    test_classes_to_run = [TestGooglePage, TestGooglePageTwo]
    loader = unittest.TestLoader()

    suites_list = []
    for test_class in test_classes_to_run:
        suite = loader.loadTestsFromTestCase(test_class)
        suites_list.append(suite)

    big_suite = unittest.TestSuite(suites_list)

    #runner = unittest.TextTestRunner()
    #result =xmlrunner.XMLTestRunner(verbosity=2, output='reports').run(big_suite)
    #results = runner.run(big_suite)

    result = unittest.TextTestRunner().run(big_suite)
