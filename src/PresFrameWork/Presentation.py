#CmdPres Presentations for command line
# --  * <Presentation.py>
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

from lxml import etree
from PresFrameWork.Slide import *
from PresFrameWork.SlideComponent import *
from PresFrameWork.TextComponent import *

class Presentation:
    
    #constructor for the class
    def __init__(self):
        self._slides=[];
    
    #loads the presentation in the passed path
    def load(self,path):
        xmlschema_doc = etree.parse("./src/PresUtils/presSchema.xml");
        xmlschema = etree.XMLSchema(xmlschema_doc);

        doc = etree.parse(path)
        if not xmlschema.validate(doc):
            print "you are trying to load an invalid document";
            return;
        
        #here everything is ok
        xml_present=doc.getroot();
        for xml_slide in xml_present:
            slide=Slide();
            for xml_component in xml_slide:
                if xml_component.tag=="TextComponent":
                    posx=int(xml_component.get("positionX"));
                    posy=int(xml_component.get("positionY"));
                    component=TextComponent(posx,posy,xml_component.text);
                if not (component is None):
                    slide.append(component);
            self.append(slide)
                
        
    def open(self):
        for s in self._slides:
            s.show()
        
    def append(self,slide):
        self._slides.append(slide)