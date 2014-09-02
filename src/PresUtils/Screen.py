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

import curses.ascii

from PresUtils.Utils import *
from PresUtils.Menu import *

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
        self._menu=Menu()
        self._colorIdx=0
        self._editMode=False


    def quitEdit(self):
        self._editMode=False
        self._pres.setEdit(self._editMode)
        self._menu.dropMenuItem("presMode(^e)")
        self._menu.addMenuItem("editMode(^e)",ord(curses.ascii.ctrl('e')),self.edit)

    def edit(self):
        self._editMode=True
        self._pres.setEdit(self._editMode)
        self._menu.dropMenuItem("editMode(^e)")
        self._menu.addMenuItem("presMode(^e)",ord(curses.ascii.ctrl('e')),self.quitEdit)
        self.setCursorPosition(0,0)
        self.clearScreen()
    
    def openScreen(self,pres):
        locale.setlocale(locale.LC_ALL, '')
        code = locale.getpreferredencoding()
        curses.start_color()
        curses.noecho()
        curses.cbreak() 
        curses.curs_set(2)
        self._screen.keypad(1)
        self._pres=pres

        self._menu.addMenuItem("prev(<-)",curses.KEY_LEFT, self._pres.prevSlide)
        self._menu.addMenuItem("next(->)",curses.KEY_RIGHT,self._pres.nextSlide)
        self._menu.addMenuItem("quit(^a)",ord(curses.ascii.ctrl('a')),self._pres.quit)

        ## DISABLE EDIT MODE, ITS UNDER CONSTRUCTION NOT FINISHED YET
        #self._menu.addMenuItem("editMode(^e)",ord(curses.ascii.ctrl('e')),self.edit)
        
        
    def closeScreen(self):
        curses.endwin()
        
    def updateScreen(self):
        self._screen.refresh()
        self._menu.show()
        c=self.readKey()
        
        #be sure update the screen dimensions
        self._height,self._width = self._screen.getmaxyx();
        self._height=self._height-1
        self._width=self._width-1

        if curses.ascii.isctrl(c) or curses.ascii.ismeta(c):
            self._menu.update(c)
        else:
            if self._editMode:
                self.setCursorPosition(self._xpos,self._ypos)
                self.screenPrint(chr(c))
                if c=='\n':
                    self.setCursorPosition(self._xpos,self._ypos+1)
                else:
                    self.setCursorPosition(self._xpos+1,self._ypos)
    
    #sets the cursor in the position you pass
    def setCursorPosition(self,x,y):
        if x>=self._width or y>=self._height:
            return
        if x<0 or y<0:
            return
        self._xpos=x
        self._ypos=y
        curses.setsyx(y,x)

    def getCursorPosition(self):
        return self._xpos,self._ypos

    def screenPrint(self,msg,attribute=None):
        if(attribute):
            self._screen.addstr(self._ypos, self._xpos,msg,attribute)
        else:
            self._screen.addstr(self._ypos, self._xpos,msg)
        self._screen.refresh()
    
    #clears the screen
    def clearScreen(self):
        #erase the screen
        self._screen.clear()

    def getHeigh(self):
        return self._height

    def getWidth(self):
        return self._width
            
    def readKey(self):
        c=self._screen.getch()
        return c
    
    def _findColor(self,color1,color2):
        for i in range(1,curses.COLOR_PAIRS):
            f,b=curses.pair_content(i)
            if f==color1 and b==color2:
                return i
        return -1

        
    def getCustomColorAtr(self,color1,color2):
        cl=self._findColor(color1,color2)
        if cl==-1:
            curses.init_pair(self._colorIdx+1, color1, color2)
            self._colorIdx+=1
            self._colorIdx%=curses.COLOR_PAIRS
            return curses.color_pair(self._findColor(color1,color2))
        else:
            return curses.color_pair(cl)

    def getMenu(self):
        return self._menu
