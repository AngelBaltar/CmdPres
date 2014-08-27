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