#CmdPres Presentations for command line
# --  * <Slide.py>
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

from PresUtils.Screen import *
from PresFrameWork.TextComponent import *
from lxml import etree

class Slide:
    
    NEXT_SLIDE=1
    PREV_SLIDE=-1
    QUIT_PRES=2
    
    #constructor for the class
    def __init__(self):
        self._components=[]
        
    #shows the slide
    def show(self):
        Screen.Instance().clearScreen()
        for c in self._components:
            c.show();

    def _findComponent(self,posx,posy):
        endx=0
        endy=0
        startx=0
        starty=0
        for comp in self._components:
            endx,endy=comp.getEnd()
            startx,starty=comp.getPosition()
            if posx>=startx and posx<=endx and posy>=starty and posy<=endy:
                return comp
        return None

    def _findExtendComponent(self,posx,posy):
        endx=0
        endy=0
        startx=0
        starty=0
        for comp in self._components:
            endx,endy=comp.getEnd()
            startx,starty=comp.getPosition()
            startx-=1
            endx+=1
            if posx>=startx and posx<=endx and posy>=starty and posy<=endy:
                return comp
        return None

    def editCharacter(self,ch,posx,posy):
        comp=self._findComponent(posx,posy)
        if comp!=None:
            comp.editCharacter(ch,posx,posy)
        else:
            comp=self._findExtendComponent(posx,posy)
            if comp!=None:
                comp.editCharacter(ch,posx,posy)
            else:
                txt_str=""+chr(ch)
                #posx-1 because thex position was already incremented
                #by the screen editor so place the text in the right position
                new_txt=TextComponent(posx-1,posy,txt_str);
                self.append(new_txt)
                #raise Exception("component to edit not found")

    def editAttribute(self,posx,posy):
        comp=self._findComponent(posx,posy)
        if comp!=None:
            comp.editAttribute()

    def editColor(self,posx,posy,bg):
        comp=self._findComponent(posx,posy)
        if comp!=None:
            comp.editColor(bg)
    
    #updates the slide reading from devices
    def update(self):
        c=Screen.Instance().readKey()
        if c==ord('q'):
            return Slide.QUIT_PRES;
        if c==curses.KEY_RIGHT:
            return Slide.NEXT_SLIDE;
        if c==curses.KEY_LEFT:
            return Slide.PREV_SLIDE; 
    
    #adds a component for the slide
    def append(self,component):
        self._components.append(component);

    def save(self,root):
        slide=etree.Element("slide")
        for comp in self._components:
            comp.save(slide)
        root.append(slide)