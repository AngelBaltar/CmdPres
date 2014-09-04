#CmdPres Presentations for command line
# --  * <TextComponent.py>
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

import curses


from PresFrameWork.SlideComponent import *;
from PresUtils.Screen import *;


class TextComponent(SlideComponent):
    
    #constructor for the class
    def __init__(self):
        self._text="";
        self._atrs=None
        self._color1=None
        self._color2=None
        SlideComponent.__init__(self)
        
    #constructor with parameters
    def __init__(self,x,y,text,attributes=None,color=None):
        self._text=text;
        self._atrs=None
        self._color1=None
        self._color2=None
        if(attributes):
            self._atrs=self._attributesMap(attributes)
        if(color):
            self._color1=map(self._colorsMap,color.split(','))[0]
            self._color2=map(self._colorsMap,color.split(','))[1]
        SlideComponent.__init__(self,x,y)
    
    def _colorsMap(self,c):
        """ maps string colors to attribute colors"""
        if(c=="black"):
            return curses.COLOR_BLACK
        if(c=="red"):
            return curses.COLOR_RED
        if(c=="white"):
            return curses.COLOR_WHITE
        if(c=="blue"):
            return curses.COLOR_BLUE
        if(c=="green"):
            return curses.COLOR_GREEN
        if(c=="yellow"):
            return curses.COLOR_YELLOW
        return None
    
    def _attributesMap(self,c):
        """ maps string attributes to curses attributes"""
        if(c=="bold"):
            return curses.A_BOLD
        if(c=="underline"):
            return curses.A_UNDERLINE
        return None
    
    #shows the text component
    def _componentShow(self):
        atrs=self._atrs
        if self._color1!=None and self._color2!=None:
            if atrs!=None:
                atrs|=Screen.Instance().getCustomColorAtr(self._color1,self._color2)
            else:
                atrs=Screen.Instance().getCustomColorAtr(self._color1,self._color2)
        Screen.Instance().screenPrint(self._text,atrs)

    def getEnd(self):
        startx,starty=self.getPosition()
        return startx+len(self._text),starty+1

    def editCharacter(self,ch,posx,posy):
        startx,starty=self.getPosition()
        xoffset=posx-startx-1
        list_str=list(self._text)
        if xoffset==len(list_str):
            list_str.append(chr(ch))
        else:
            list_str[xoffset]=chr(ch)
        self._text="".join(list_str)