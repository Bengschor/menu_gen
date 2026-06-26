from sqlalchemy.orm import Session
from datetime import date

from models.menu import Menu

def create_menu(session: Session, date_: date = date.today()):
	menu = Menu(date=date_)
	session.add(menu)
	session.commit()
	
	return (menu)
