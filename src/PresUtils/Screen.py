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

from PresUtils.Utils import *


@Singleton
class Screen:
    
    def __init__(self):
        self._begin_x =0; 
        self._begin_y = 0
       
        self._screen=curses.initscr();
        self._height,self._width = self._screen.getmaxyx();
        self._height=self._height-1
        self._width=self._width-1
        self._xpos=0;
        self._ypos=0;
    
    def openScreen(self):
        locale.setlocale(locale.LC_ALL, '')
        code = locale.getpreferredencoding()
        curses.start_color()
        curses.noecho()
        curses.cbreak() 
        curses.curs_set(0)
        self._screen.keypad(1)
        
        
    def closeScreen(self):
        curses.endwin()
        
    def updateScreen(self):
        self._screen.refresh()
    
    #sets the cursor in the position you pass
    def setCursorPosition(self,x,y):
        if x>=self._width or y>=self._height:
            return
        if x<0 or y<0:
            return
        self._xpos=x
        self._ypos=y
        
    def screenPrint(self,msg,attribute=None):
        if(attribute):
            self._screen.addstr(self._ypos, self._xpos,msg,attribute)
        else:
            self._screen.addstr(self._ypos, self._xpos,msg)
        self.updateScreen();
    
    #clears the screen
    def clearScreen(self):
        #erase the screen, be sure update the screen dimensions
        self._height,self._width = self._screen.getmaxyx();
        self._height=self._height-1
        self._width=self._width-1
        for y in range(self._begin_y,self._height):
            self._screen.addstr(y,0,"\n");
            
    def readKey(self):
        return self._screen.getch()
    
    def setCustomColor(self,color1,color2):
        curses.init_pair(1, color1, color2)
        
    def getCustomColorAtr(self):
        return curses.color_pair(1)
