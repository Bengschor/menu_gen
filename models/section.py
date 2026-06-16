from db.database import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Identity, String, Integer, Boolean

from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from models.menu import Menu

class Section(Base):
	__tablename__ = "sections"

	id: Mapped[int] 			= mapped_column(Identity(always=True), primary_key=True)
	type: Mapped[str]			= mapped_column(String(32), nullable=False)
	sub_type: Mapped[str]		= mapped_column(String(32), nullable=False)
	value_fr: Mapped[str]		= mapped_column(String(32), nullable=False)
	value_nl: Mapped[str]		= mapped_column(String(32), nullable=False)
	label_fr: Mapped[str]		= mapped_column(String(64), nullable=False)
	label_nl: Mapped[str]		= mapped_column(String(64), nullable=False)
	negative: Mapped[bool]		= mapped_column(Boolean, nullable=False)
	dish_count: Mapped[int]		= mapped_column(Integer, nullable=False)
	is_active: Mapped[bool]		= mapped_column(Boolean, default=True)

	menu: Mapped["Menu"] = relationship("Menu", secondary="menu_sections", back_populates="sections")

	def __repr__(self):
		return f"Category(id={self.id}, label={self.label_fr})"