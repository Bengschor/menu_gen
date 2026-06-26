from sqlalchemy.orm import Session

from models.category import Category

def create_category(session: Session, name: str, type: str):
	category = Category(name=name, type=type)
	session.add(category)
	session.commit()
	session.refresh(category)

	return (category)