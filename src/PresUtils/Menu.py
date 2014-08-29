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


class Menu:
	
	def __init__(self):
		self._items=[]

	def addMenuItem(self,title,but,fun):
		item={
			"name":title,
			"function":fun,
			"button":but
		}
		self._items.append(item)

	def show(self):
		 from PresUtils.Screen import *
		 x=0
		 y=Screen.Instance().getHeigh()-2
		 first=True
		 for item in self._items:
		 	Screen.Instance().setCursorPosition(x,y)
		 	if not first:
		 		Screen.Instance().screenPrint("|")
		 		x+=1
		 		Screen.Instance().setCursorPosition(x,y)

		 	Screen.Instance().screenPrint(item["name"])
		 	x+=len(item["name"])
		 	first=False

	def update(self):
		from PresUtils.Screen import *
		c=Screen.Instance().readKey()
		for item in self._items:
			if c==item["button"]:
				item["function"]()
				break;
