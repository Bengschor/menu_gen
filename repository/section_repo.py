from sqlalchemy.orm import Session

from models.section import Section

def create_section(session: Session, type: str, sub_type: str,
				value_fr: str, value_nl: str, label_fr: str,
				label_nl: str, negative: bool, dish_count: int):
	section = Section(type=type, sub_type=sub_type, value_fr=value_fr,
				   value_nl=value_nl, label_fr=label_fr,
				   label_nl=label_nl, negative=negative,
				   dish_count=dish_count)
	session.add(section)
	session.commit()
	session.refresh(section)

	return (section)

def disable_section(session: Session, section: Section):
	section.is_active = False
	session.commit()

def enable_section(session: Session, section: Section):
	section.is_active = True
	session.commit()