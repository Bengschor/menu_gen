from datetime import date

from sqlalchemy.orm import Session, joinedload
from sqlalchemy import select

from models.menu import Menu
from models.menu_item import MenuItem
from models.dish import Dish
from models.section import Section
from models.menu_section import MenuSection
from models.dish_categories import DishCategory
from models.category import Category


def print_menu(session: Session, day: date = None):
    if day is None:
        day = date.today()

    # ----------------------------------------------------------------
    # Fetch menu with all related data in as few queries as possible
    # ----------------------------------------------------------------
    menu = session.get(Menu, day)
    if not menu:
        print(f"\n  No menu found for {day.strftime('%A %d %B %Y')}.")
        return

    # Load sections linked to this menu, ordered by type so categories
    # come before filters
    sections: list[Section] = session.execute(
        select(Section)
        .join(MenuSection, MenuSection.section_id == Section.id)
        .where(MenuSection.menu_id == day)
        .order_by(Section.type.desc(), Section.id)   # "filter" < "category" alpha, desc puts category first
    ).scalars().all()

    # Load menu items with their dishes, ordered by group then sort index
    items: list[MenuItem] = session.execute(
        select(MenuItem)
        .options(joinedload(MenuItem.dish))
        .where(MenuItem.date == day)
        .order_by(MenuItem.group_index, MenuItem.sort_index)
    ).scalars().all()

    # Map group_index → list of dishes (preserving sort order)
    groups: dict[int, list[Dish]] = {}
    for item in items:
        groups.setdefault(item.group_index, []).append(item.dish)

    # ----------------------------------------------------------------
    # Separate sections into categories and filters
    # ----------------------------------------------------------------
    categories = [s for s in sections if s.type == "category"]
    filters    = [s for s in sections if s.type == "filter"]

    # ----------------------------------------------------------------
    # Print
    # ----------------------------------------------------------------
    WIDTH = 60
    DIVIDER     = "═" * WIDTH
    THIN_DIV    = "─" * WIDTH

    print(f"\n{'╔' + DIVIDER + '╗'}")
    title = f"MENU — {day.strftime('%A %d %B %Y').upper()}"
    print(f"║  {title:<{WIDTH - 2}}║")
    print(f"{'╠' + DIVIDER + '╣'}")

    # Active filters line
    if filters:
        active = "  ".join(f"[{f.label_fr}]" for f in filters if f.is_active)
        if active:
            print(f"║  Filtres actifs: {active:<{WIDTH - 18}}║")
            print(f"║{THIN_DIV}║")

    # Print each category group with its dishes
    for group_idx, section in enumerate(categories):
        label = f"  {section.label_fr.upper()}"
        print(f"║{label:<{WIDTH}}║")
        print(f"║  {'─' * (WIDTH - 4)}║")

        dishes = groups.get(group_idx, [])
        if not dishes:
            print(f"║  {'(aucun plat)':.<{WIDTH - 4}}║")
        else:
            for dish in dishes:
                allergen_tag = " ⚠ " if dish.has_allergen else "   "
                vegan_tag    = " 🌱" if dish.is_vegan    else "  "
                sig_tag      = " ★" if dish.is_signature else "  "
                price        = f"€{dish.price:>6.2f}"
                # name column width = total - tags - price - padding
                name_width = WIDTH - len(allergen_tag) - len(vegan_tag) - len(sig_tag) - len(price) - 4
                name = dish.name_fr[:name_width].ljust(name_width)
                print(f"║  {allergen_tag}{vegan_tag}{sig_tag}  {name}{price}  ║")

        if group_idx < len(categories) - 1:
            print(f"║{THIN_DIV}║")

    print(f"{'╚' + DIVIDER + '╝'}")

    # Legend
    print(f"\n  Legend:  ⚠  Contains allergen   🌱 Vegan   ★ Signature dish\n")