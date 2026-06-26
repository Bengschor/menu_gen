from sqlalchemy.orm import Session
from typing import TYPE_CHECKING

from models.menu import Menu
from models.menu_item import MenuItem
from models.dish import Dish

def register_item(session: Session, menu: Menu, dish: Dish,
				  	group_i: int, sort_i: int):
	menu_item = MenuItem(date=menu.date, dish_id=dish.id,
					  	group_index=group_i, sort_index=sort_i)
	session.add(menu_item)
	session.commit()

	return (menu_item)


