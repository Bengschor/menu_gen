from db.database import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, String, ForeignKey
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from models.dish import Dish
	from models.category import Category

class DishCategory(Base):
	__tablename__ = "dish_categories"

	dish_id: Mapped[int]			= mapped_column(ForeignKey("dishes.id"), primary_key=True)
	category_id: Mapped[int]		= mapped_column(ForeignKey("categories.id"), primary_key=True)
	profitability_rank: Mapped[int] = mapped_column(Integer)

	dish: Mapped["Dish"]	= relationship("Dish", back_populates="dish_category")
	category: Mapped["Category"]	= relationship("Category", back_populates="dish_category")

	def __repr__(self):
		return f"DishCategory(dish_id={self.dish_id}, category_id={self.category_id}, pro_rank={self.profitability_rank})"