from db.database import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, Date
from datetime import date

from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from models.section import Section
	from models.menu_item import MenuItem

class Menu(Base):
	__tablename__ = "menus"

	date: Mapped[date]		= mapped_column(Date, primary_key=True)

	sections: Mapped[list["Section"]] = relationship(
        "Section", secondary="menu_sections",
        back_populates="menu"
    )

	items: Mapped[list["MenuItem"]]	= relationship(
		"MenuItem", back_populates="menu"
	)

	def __repr__(self):
		return f"Menu(date={self.date})"
	
	@property
	def categories(self):
		n = len(self.sections) // 2
		return self.sections[:n]

	@property
	def filters(self):
		n = len(self.sections) // 2
		return self.sections[n:]