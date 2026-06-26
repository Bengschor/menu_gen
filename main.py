import os
from datetime import date, timedelta
from decimal import Decimal
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from db.database import Base, SessionLocal
# from db.population import db_populate
# from db.populate_2 import populate_2

from models.menu import Menu
from models.menu_item import MenuItem
from models.dish import Dish
from models.category import Category
from models.dish_categories import DishCategory
from models.section import Section
from models.menu_section import MenuSection

from repository.menu_repo import create_menu
from repository.dish_repo import create_dish
from repository.category_repo import create_category
from repository.dish_category_repo import link_dish_category
from repository.section_repo import create_section, disable_section
from repository.menu_section_repo import add_section
from repository.menu_item_repo import register_item

from print_menu import print_menu

def main():
    # Open session
    with SessionLocal() as session:
        #    db_populate(session)
        #    populate_2(session)
        print_menu(session, date.today() - timedelta(days=1))
    
if __name__ == "__main__":
    main()