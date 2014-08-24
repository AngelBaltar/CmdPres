#CmdPres Presentations for command line
# --  * <Screen.py>
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

__author__="angel"
__date__ ="$23-ago-2014 12:10:52$"

import curses
import locale

screen=curses.initscr();

def openScreen():
    locale.setlocale(locale.LC_ALL, '')
    code = locale.getpreferredencoding()
    curses.noecho()
    curses.cbreak() 
    curses.curs_set(0)
    
def closeScreen():
    curses.endwin()
    
def updateScreen():
    screen.refresh()

#sets the cursor in the position you pass
def setCursorPosition(x,y):
    screen.addstr(y, x,"")
    updateScreen();

#clears the screen
def clearScreen():
    i=0;
    while(i<60):
        print "\n";
        i=i+1;
    setCursorPosition(0,0)
        
def readKey():
    return screen.getch()
    
