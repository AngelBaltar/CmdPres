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

	def addMenuItem(self,title,but,fun):
		item={
			"name":title,
			"function":fun,
			"button":but
		}
		self._items.append(item)

	def setSlides(self,n):
		self._nSlides=n

	def setCountSlide(self,n):
		self._countSlide=n

	def show(self):
		 from PresUtils.Screen import *
		 x=0
		 y=Screen.Instance().getHeigh()-2
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
		 slide_str="Slide:"+str(self._countSlide)+"/"+str(self._nSlides)
		 x=Screen.Instance().getWidth()-len(slide_str)
		 Screen.Instance().setCursorPosition(x,y)
		 Screen.Instance().screenPrint(slide_str,atrs)

	def update(self):
		from PresUtils.Screen import *
		c=Screen.Instance().readKey()
		for item in self._items:
			if c==item["button"]:
				item["function"]()
				break;
