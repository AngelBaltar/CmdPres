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
from lxml import etree

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
        
        color_map={
            "black":curses.COLOR_BLACK,
            "red":curses.COLOR_RED,
            "white":curses.COLOR_WHITE,
            "blue":curses.COLOR_BLUE,
            "green":curses.COLOR_GREEN,
            "yellow":curses.COLOR_YELLOW
            }

        try:
            return color_map[c]
        except KeyError:
            for k,cl in color_map.iteritems():
                if cl==c:
                    return k
    
    def _attributesMap(self,c):
        """ maps string attributes to curses attributes"""
        atr_map={
            "bold":curses.A_BOLD,
            "underline":curses.A_UNDERLINE
            }
        try: 
            return atr_map[c]
        except KeyError:
             for k,atr in atr_map.iteritems():
                if atr==c:
                    return k
    
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
        return startx+len(self._text),starty

    def editCharacter(self,ch,posx,posy):
        startx,starty=self.getPosition()
        xoffset=posx-startx-1
        list_str=list(self._text)
        if xoffset<0:
            xoffset=0
        if ch==curses.KEY_BACKSPACE:
            if xoffset!=0:
                list_str.pop(xoffset+1)
        else:
            list_str.insert(xoffset,chr(ch))
        self._text="".join(list_str)

    def save(self,root):
        textcomp=etree.Element("TextComponent")
        textcomp.text=self._text
        posx,posy=self.getPosition()
        colors=self._colorsMap(self._color1)
        if colors!=None:
            colors=colors+","
            colors=colors+self._colorsMap(self._color2)
        attributes=self._attributesMap(self._atrs)
        textcomp.set("positionX",str(posx))
        textcomp.set("positionY",str(posy))
        if colors!=None:
            textcomp.set("colors",colors)
        if attributes!=None:
            textcomp.set("attributes",attributes)
        root.append(textcomp)