from db.database import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Identity, String
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from models.dish_categories import DishCategory

class Category(Base):
	__tablename__ = "categories"

	id: Mapped[int]		= mapped_column(Identity(always=True), primary_key=True)
	name: Mapped[str]	= mapped_column(String(64), nullable=False)
	type: Mapped[str]	= mapped_column(String(64), nullable=False)

	dish_category: Mapped[list["DishCategory"]]	= relationship("DishCategory", back_populates="category")

	def __repr__(self):
		return f"Category(Name'{self.name}, id={self.id}"