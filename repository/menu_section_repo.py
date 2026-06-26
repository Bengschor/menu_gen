from sqlalchemy.orm import Session

from models.menu import Menu
from models.section import Section
from models.menu_section import MenuSection

def add_section(session: Session, menu: Menu, section: Section):
	menu_section = MenuSection(menu_id=menu.date, section_id=section.id)
	session.add(menu_section)
	session.commit()
	
	return(menu_section)