from sqlalchemy.orm import Session

from models.dish_categories import DishCategory
from models.category import Category
from models.dish import Dish

def link_dish_category(session: Session, dish: Dish,
					   category: Category, profitability_rank: int):
	dish_category = DishCategory(category_id=category.id,
				dish_id=dish.id, profitability_rank=profitability_rank)
	session.add(dish_category)
	session.commit()

	return (dish_category)