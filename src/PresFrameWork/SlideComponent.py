#CmdPres Presentations for command line
# --  * <SlideComponent.py>
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


from PresUtils.Screen import *

class SlideComponent:
    
    #constructor for the class
    def __init__(self):
        self._positionX=0;
        self._positionY=0;
        
    #constructor with coordenates
    def __init__(self,x,y):
        self._positionX=x;
        self._positionY=y;
        
    def show(self):
        Screen.Instance().setCursorPosition(self._positionX,self._positionY);