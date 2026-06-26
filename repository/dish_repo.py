from sqlalchemy.orm import Session
from decimal import	Decimal

from models.dish import Dish

def create_dish(session: Session, name_fr: str, name_nl: str,
				price: Decimal, restaurant: str, has_allergen: bool,
				is_signature: bool, is_vegan: bool, popularity: int):
	dish = Dish(name_fr=name_fr, name_nl=name_nl, price=price,
			 	restaurant=restaurant, has_allergen=has_allergen,
				is_signature=is_signature, is_vegan=is_vegan,
				popularity=popularity)
	session.add(dish)
	session.commit()
	session.refresh(dish)

	return (dish)