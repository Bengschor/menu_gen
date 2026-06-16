from db.database import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, Date
from datetime import date

from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from models.menu import Menu
	from models.section import Section

class MenuSection(Base):
	__tablename__ = "menu_sections"

	menu_id: Mapped[date]	= mapped_column(ForeignKey("menus.date"), primary_key=True)
	section_id: Mapped[int]	= mapped_column(ForeignKey("sections.id"), primary_key=True)

	# menu: Mapped["Menu"] = relationship("Menu", back_populates="sections")
	# section: Mapped["Section"] = relationship("Section")