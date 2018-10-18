import unittest
from Spec_GooglePage import TestGooglePage
from Spec_GooglePageTwo import TestGooglePageTwo
import os
import glob
import sys
import xmlrunner

if __name__=="__main__":
    # To load specs dynamically without manually editting this file
    #==============================================================
    #test_dir = os.path.dirname(os.path.abspath(__file__))
    #test_files = glob.glob(os.path.join(test_dir, 'Spec_*.py'))
    #test_names = [ os.path.basename(f)[:-3] for f in test_files]
    #sys.path.insert(0, os.path.join(test_dir, '..'))

    test_names=['Spec_GooglePage', 'Spec_GooglePageTwo']
    suite = unittest.defaultTestLoader.loadTestsFromNames(test_names)

    # run with text mode
    #====================
    result = unittest.TextTestRunner().run(suite)
    
    # run and generate xml report
    #====================
        #todo: combine all results in one XML report
    #result =xmlrunner.XMLTestRunner(verbosity=2, output='reports').run(suite)
    #sys.exit(1 if (result.errors or result.failures) else 0)