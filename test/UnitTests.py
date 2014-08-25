'''
Created on 25/8/2014

@author: angel
'''

import os, sys, unittest
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(CURRENT_DIR)+"/src/")

from PresFrameWork.Presentation import *;


class Test(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass


    def testXmlSchema1(self):
        pres=Presentation();
        self.assertTrue(pres.load("./test/pres_ok1.xml"))
        
    def testXmlSchema2(self):
        pres=Presentation();
        self.assertFalse(pres.load("./test/pres_fail1.xml"))


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()