#CmdPres Presentations for command line
# --  * <menu.py>
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

import curses

class Menu:
	
	def __init__(self):
		self._items=[]
		self._countSlide=1
		self._nSlides=0
		self._heigh=2
		self._saveMode=False
		self._pathSave=""
		self._saveChr=False

	def addMenuItem(self,title,but,fun):
		item={
			"name":title,
			"function":fun,
			"button":but
		}
		self._items.append(item)

	def dropMenuItem(self,title):
		to_drop=None
		for el in self._items:
			if el["name"]==title:
				to_drop=el
				break
		if to_drop!=None:
			self._items.remove(to_drop)

	def save(self):
		from PresUtils.Screen import *
		self._saveMode=not self._saveMode
		if not self._saveMode:
			#save the thing into the path
			Screen.Instance().savePres(self._pathSave)
		else:
			self._saveChr=False
		

	def setSlides(self,n):
		self._nSlides=n

	def setCountSlide(self,n):
		self._countSlide=n

	def getHeigh(self):
		return self._heigh

	def show(self):
		 from PresUtils.Screen import *
		 #make screen not consider the menu
		 self._heigh=0
		 backup_x,backup_y=Screen.Instance().getCursorPosition()
		 x=0
		 y=Screen.Instance().getHeigh()-self.getHeigh()
		 Screen.Instance().setCursorPosition(x,y)
		 Screen.Instance().clearFromCursor()
		 first=True
		 atrs=Screen.Instance().getCustomColorAtr(curses.COLOR_WHITE,curses.COLOR_RED)|curses.A_BOLD
		 for item in self._items:
		 	Screen.Instance().setCursorPosition(x,y)
		 	if not first:
		 		Screen.Instance().screenPrint("|",atrs)
		 		x+=1
		 		Screen.Instance().setCursorPosition(x,y)

		 	Screen.Instance().screenPrint(item["name"],atrs)
		 	x+=len(item["name"])
		 	first=False
		 if self._saveMode:
		 	x=0
		 	y+=1
		 	save_str="Enter the path to save:\""+self._pathSave+"\" ^w to save"
		 	Screen.Instance().setCursorPosition(x,y)
		 	Screen.Instance().screenPrint(save_str,atrs)
		 	y-=1
		 slide_str="Slide:"+str(self._countSlide)+"/"+str(self._nSlides)
		 x=Screen.Instance().getWidth()-len(slide_str)
		 Screen.Instance().setCursorPosition(x,y)
		 Screen.Instance().screenPrint(slide_str,atrs)

		 Screen.Instance().setCursorPosition(backup_x,backup_y)
		 #make screen consider the menu again
		 self._heigh=2

	def update(self,c):
		for item in self._items:
			if c==item["button"]:
				item["function"]()
				break;

	def setPathSave(self,path):
		self._pathSave=path

	def isSaveMode(self):
		return self._saveMode

	def saveChar(self,c):
		if not self._saveChr:
			self._pathSave=chr(c)
			self._saveChr=True
		else:
			self._pathSave=self._pathSave+chr(c)
