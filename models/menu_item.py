from db.database import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, String, ForeignKey, Date
from datetime import date

from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from models.menu import Menu
	from models.dish import Dish

class MenuItem(Base):
	__tablename__ = "menu_items"

	date: Mapped[Date]		= mapped_column(ForeignKey("menus.date"), primary_key=True)
	dish_id: Mapped[int]	= mapped_column(ForeignKey("dishes.id"), primary_key=True)
	grouped_by: Mapped[str]	= mapped_column(String(64), nullable=False)
	sorted_by: Mapped[str]	= mapped_column(String(64), nullable=False)

	menu: Mapped[list["Menu"]]	= relationship("Menu", back_populates="items")
	dish: Mapped["Dish"]		= relationship("Dish", back_populates="menu_items")

	def __repr__(self):
		return f"MenuItem(id={self.date, self.dish_id})"