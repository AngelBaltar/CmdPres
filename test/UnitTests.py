#CmdPres Presentations for command line
# --  * <UnitTests.py>
# --  * Copyright (C) Angel Baltar Diaz
# --  *
# --  * This program is free software: you can redistribute it and/or
# --  * modify it under the terms of the GNU General Public
# --  * License as published by the Free Software Foundation; either
# --  * version 3 of the License, or (at your option) any later version.
# --  *
# --  * This program is distributed in the hope that it will be useful,
# --  * but WITHOUT ANY WARRANTY; without even the implied warranty of
# --  * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# --  * General Public License for more details.
# --  *
# --  * You should have received a copy of the GNU General Public
# --  * License along with this program.  If not, see
# --  * <http://www.gnu.org/licenses/>.

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
        Screen.Instance().openScreen(pres)
        self.assertTrue(pres.load("./test/pres_ok1.xml"))
        Screen.Instance().closeScreen()
        
    def testXmlSchema2(self):
        pres=Presentation();
        Screen.Instance().openScreen(pres)
        self.assertFalse(pres.load("./test/pres_fail1.xml"))
        Screen.Instance().closeScreen()


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()