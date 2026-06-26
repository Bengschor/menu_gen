# menu_gen

A dynamic weekly menu and meal planning generator designed to automatically create structured meal plans from a database of recipes and compile consolidated shopping lists.

---

## 🧠 Core Logic & Workflow

The architecture relies on two central logical components: the **Generation Engine** and the **Aggregator Engine**.

### 1. Menu Generation Logic
The selection pipeline ensures varied meal plans without manual oversight using the following execution path:
* **Constraint Filtering:** The engine queries the database, filtering recipes by specific user preferences (e.g., preparation time, historical tags, or specific meal types).
* **Randomized Unique Selection:** To populate a new menu, the generator samples unique recipe records randomly. It implements a lookback buffer by checking recent menu history to ensure recipes used in the previous cycle are excluded from the current generation pool.
* **Slot Mapping:** The selected recipes are mapped sequentially to open day/meal configurations and committed as transactions to the scheduled menu.

### 2. Shopping List Aggregation Logic
Once a menu is finalized, a consolidated grocery checklist is compiled via an aggregation pipeline:
1. **Fetch Menu Items:** Resolves all recipes tied to the target menu timeframe.
2. **Resolve and Scale Ingredients:** Gathers ingredient dependencies for all selected meals. If a user adjusts the default menu scaling (e.g., doubling servings), the engine scales the required quantities mathematically.
3. **Unit Grouping:** Sums identical ingredient quantities together if their measurement units match.
4. **Categorized Output:** Groups items by their ingredient category to streamline real-world shopping navigation.

---

## 🗄️ Database Structure

The database uses a relational schema designed to separate recipes and their foundational ingredients from the scheduled instances of menus. 

### 1. Core Recipe Entities
* **`recipes`**: Stores the metadata for unique dishes.
  * `id` (UUID, PK)
  * `title` (VARCHAR)
  * `instructions` (TEXT)
  * `prep_time_mins` (INT)
  * `servings` (INT)
* **`ingredients`**: A master look-up table of all standalone culinary items to prevent text duplication.
  * `id` (UUID, PK)
  * `name` (VARCHAR, UNIQUE)
  * `category` (VARCHAR) — *e.g., Produce, Dairy, Meat (used for sorting shopping lists)*
* **`recipe_ingredients`**: Join table mapping ingredients to recipes with specific quantities.
  * `recipe_id` (UUID, FK -> `recipes.id`)
  * `ingredient_id` (UUID, FK -> `ingredients.id`)
  * `quantity` (DECIMAL)
  * `unit` (VARCHAR) — *e.g., grams, tbsp, pieces*

### 2. Menu Planning Entities
* **`menus`**: Represents a scheduled structural week or planning block.
  * `id` (UUID, PK)
  * `start_date` (DATE)
  * `created_at` (TIMESTAMP)
* **`menu_meals`**: Links specific recipes to designated slots within a generated menu.
  * `id` (UUID, PK)
  * `menu_id` (UUID, FK -> `menus.id`)
  * `recipe_id` (UUID, FK -> `recipes.id`)
  * `day_of_week` (ENUM) — *e.g., Monday, Tuesday*
  * `meal_type` (ENUM) — *e.g., Breakfast, Lunch, Dinner*

---

## 🚀 Getting Started

### Prerequisites
* Python 3.10+
* PostgreSQL / SQLite

### Quick Start
1. Clone the repository:
   ```bash
   git clone [https://github.com/Bengschor/menu_gen.git](https://github.com/Bengschor/menu_gen.git)
   cd menu_gen
