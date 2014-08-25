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


from PresFrameWork.Presentation import *;
from PresUtils.Screen import *;

__author__="angel"
__date__ ="$22-ago-2014 12:39:52$"

if __name__ == "__main__":
    try:
        Screen.Instance().openScreen();
        pres=Presentation();
        if not pres.load("./test/pres_ok1.xml"):
            print "cant load the presentation"
        else:
            pres.open();
    except:
        Screen.Instance().screenPrint("An exception was thrown")
    finally:
        Screen.Instance().closeScreen()
