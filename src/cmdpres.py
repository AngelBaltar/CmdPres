#!/usr/bin/python

#CmdPres Presentations for command line
# --  * <cmdpres.py>
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
import sys
import traceback    

from PresFrameWork.Presentation import *;
from PresUtils.Screen import *;
from PresUtils import Utils;

__author__="angel"
__date__ ="$22-ago-2014 12:39:52$"


#does the main thing, view and edit presentations
def doPresentation(pres_path=None):
    try:
        pres=Presentation();
        if pres_path==None:
                if not  pres.loadEmpty():
                    raise Exception("Cant load empty presentation ") 
        else:
            if not pres.load(pres_path):
                raise Exception("Cant load the presentation ")
        Screen.Instance().openScreen(pres);
        pres.open();
        Screen.Instance().closeScreen()
    except Exception as ex:
        Screen.Instance().closeScreen()
        traceback.print_exc()
        print str(ex)
    finally:
        pass

#prints the program command line help
def printHelp():
    print "CmdPres ",Utils.VersionNumber," Command line Presentations"
    print "Usage: cmdpres.py [path_to_presentation]"

#main for the program
if __name__ == "__main__":
    if len(sys.argv)>2:
        print "wrong parameters"
    else:
        if len(sys.argv)<2:
            doPresentation()
        else:
            pres_path=sys.argv[1]
            if(pres_path=="--help" or pres_path=="-h"):
                printHelp()
            else:
                doPresentation(pres_path)
