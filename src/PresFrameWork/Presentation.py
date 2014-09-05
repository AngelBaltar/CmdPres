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


from PresUtils.Screen import *;

class Presentation:
    
    #constructor for the class
    def __init__(self):
        self._slides=[]
        self._sl=0
        self._quit=False
        self._edit=False
    
    #loads the presentation in the passed path
    def load(self,path):
        schema_path=os.path.dirname(os.path.abspath(__file__))
        schema_path+="/../PresUtils/presSchema.xml";
        xmlschema_doc = etree.parse(schema_path);
        xmlschema = etree.XMLSchema(xmlschema_doc);

        doc = etree.parse(path)
        if not xmlschema.validate(doc):
            return False;
        
        #here everything is ok
        xml_present=doc.getroot();
        for xml_slide in xml_present:
            slide=Slide();
            for xml_component in xml_slide:
                if xml_component.tag=="TextComponent":
                    posx=int(xml_component.get("positionX"));
                    posy=int(xml_component.get("positionY"));
                    atrs=xml_component.get("attributes");
                    colors=xml_component.get("colors");
                    component=TextComponent(posx,posy,xml_component.text,atrs,colors);
                if not (component is None):
                    slide.append(component);
            self.append(slide)
        Screen.Instance().getMenu().setSlides(len(self._slides))
        Screen.Instance().getMenu().setCountSlide(self._sl+1)
        return True
                
    def prevSlide(self):
        self._sl-=1
        if self._sl<0:
            self._sl=0
        Screen.Instance().getMenu().setCountSlide(self._sl+1)
        Screen.Instance().clearScreen()

    def nextSlide(self):
        self._sl+=1
        if self._sl>=len(self._slides):
            self._sl=len(self._slides)-1
        Screen.Instance().getMenu().setCountSlide(self._sl+1)
        Screen.Instance().clearScreen()

    def setEdit(self,ed):
        self._edit=ed

    def quit(self):
        self._quit=True

    def save(self,path):
        root = etree.Element("presentation")
        for sl in self._slides:
            sl.save(root)
        fich=open(str(path),str('w'))
        fich.write(etree.tostring(root))
        fich.close()


    def editCharacter(self,ch,posx,posy):
        if not self._edit:
            return
        self._slides[self._sl].editCharacter(ch,posx,posy)


    def open(self):
        sl=0;
        while not self._quit:
            #if not self._edit:
            self._slides[self._sl].show()
            Screen.Instance().updateScreen()
        
    def append(self,slide):
        self._slides.append(slide)