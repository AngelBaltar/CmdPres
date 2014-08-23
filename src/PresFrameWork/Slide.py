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

__author__="${user}"
__date__ ="$${date} ${time}$"

if __name__ == "__main__":
    print "Hello World"

class Slide:
    
    #constructor for the class
    def __init__(self):
        self._components=[]
        
    #shows the slide
    def show(self):
        for c in self._components:
            c.show();
    
    #updates the slide reading from devices
    def update(self):
        pass;
    
    #adds a component for the slide
    def append(self,component):
        self._components.append(component);