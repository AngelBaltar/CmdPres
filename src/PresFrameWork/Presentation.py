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


from lxml import etree
import os

from PresFrameWork.Slide import * 
from PresFrameWork.TextComponent import * 
from PresUtils import Screen;

class Presentation:
    
    #constructor for the class
    def __init__(self):
        self._slides=[];
    
    #loads the presentation in the passed path
    def load(self,path):
        schema_path=os.path.dirname(os.path.abspath(__file__))
        schema_path+="/../PresUtils/presSchema.xml";
        xmlschema_doc = etree.parse(schema_path);
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
        sl=0;
        while True:
            self._slides[sl].show()
            c=self._slides[sl].update()
            if c==Slide.QUIT_PRES:
                break;
            if c==Slide.NEXT_SLIDE or c==Slide.PREV_SLIDE:
                sl=sl+c;
                Screen.clearScreen()
            sl=sl%len(self._slides)
        
    def append(self,slide):
        self._slides.append(slide)