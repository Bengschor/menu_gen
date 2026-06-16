from db.database import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Identity, String, Numeric, CheckConstraint, Boolean, Integer
from decimal import Decimal
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from models.menu_item import MenuItem
	from models.dish_categories import DishCategory

class Dish(Base):
	__tablename__ = "dishes"

	id: Mapped[int]				= mapped_column(Identity(always=True), primary_key=True)
	name_fr: Mapped[str]		= mapped_column(String(64), nullable=False)
	name_nl: Mapped[str]		= mapped_column(String(64), nullable=False)
	price: Mapped[Decimal]		= mapped_column(Numeric(10, 2), CheckConstraint("price >= 0"), nullable=False)
	restaurant: Mapped[str]		= mapped_column(String(64), nullable=False)
	has_allergen: Mapped[bool]	= mapped_column(Boolean, nullable=False)
	is_signature: Mapped[bool]	= mapped_column(Boolean, nullable=False)
	is_vegan: Mapped[bool]		= mapped_column(Boolean, nullable=False)
	popularity: Mapped[int]		= mapped_column(Integer)

	menu_items: Mapped[list["MenuItem"]]	= relationship("MenuItem", back_populates="dish")
	dish_category: Mapped[list["DishCategory"]]	= relationship("DishCategory", back_populates="dish")

	def __repr__(self):
		return f"Dish(Name={self.name_fr}, Id={self.id})"