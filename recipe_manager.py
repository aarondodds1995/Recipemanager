import json
import os

DATA_FILE = "data/recipes.json"


# Ensure data directory and file exist
def initialize_file():
    os.makedirs("data", exist_ok=True)

    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, "w") as file:
            json.dump([], file)


# Load recipes from JSON file
def load_recipes():
    with open(DATA_FILE, "r") as file:
        return json.load(file)


# Save recipes to JSON file
def save_recipes(recipes):
    with open(DATA_FILE, "w") as file:
        json.dump(recipes, file, indent=4)


# Add a new recipe
def add_recipe():
    recipes = load_recipes()

    title = input("Enter recipe title: ")
    ingredients = input("Enter ingredients (comma separated): ")
    instructions = input("Enter cooking instructions: ")

    recipe = {
        "title": title,
        "ingredients": ingredients.split(","),
        "instructions": instructions
    }

    recipes.append(recipe)
    save_recipes(recipes)

    print("Recipe added successfully!")


# View all recipes
def view_recipes():
    recipes = load_recipes()

    if not recipes:
        print("No recipes found.")
        return

    for index, recipe in enumerate(recipes, start=1):
        print(f"\nRecipe {index}")
        print("Title:", recipe["title"])
        print("Ingredients:", ", ".join(recipe["ingredients"]))
        print("Instructions:", recipe["instructions"])


# Search recipes
def search_recipe():
    recipes = load_recipes()

    keyword = input("Enter title or ingredient to search: ").lower()

    found = False

    for recipe in recipes:
        if (
            keyword in recipe["title"].lower()
            or any(keyword in item.lower() for item in recipe["ingredients"])
        ):
            print("\nRecipe Found:")
            print("Title:", recipe["title"])
            print("Ingredients:", ", ".join(recipe["ingredients"]))
            print("Instructions:", recipe["instructions"])
            found = True

    if not found:
        print("No matching recipes found.")


# Edit a recipe
def edit_recipe():
    recipes = load_recipes()

    title = input("Enter recipe title to edit: ").lower()

    for recipe in recipes:
        if recipe["title"].lower() == title:

            recipe["title"] = input("New title: ")
            recipe["ingredients"] = input(
                "New ingredients (comma separated): "
            ).split(",")
            recipe["instructions"] = input(
                "New instructions: "
            )

            save_recipes(recipes)

            print("Recipe updated successfully!")
            return

    print("Recipe not found.")


# Delete a recipe
def delete_recipe():
    recipes = load_recipes()

    title = input("Enter recipe title to delete: ").lower()

    for recipe in recipes:
        if recipe["title"].lower() == title:

            recipes.remove(recipe)
            save_recipes(recipes)

            print("Recipe deleted successfully!")
            return

    print("Recipe not found.")


# Main menu
def main():
    initialize_file()

    while True:
        print("\n===== Recipe Manager =====")
        print("1. Add Recipe")
        print("2. View Recipes")
        print("3. Search Recipe")
        print("4. Edit Recipe")
        print("5. Delete Recipe")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_recipe()

        elif choice == "2":
            view_recipes()

        elif choice == "3":
            search_recipe()

        elif choice == "4":
            edit_recipe()

        elif choice == "5":
            delete_recipe()

        elif choice == "6":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


# Run application
if __name__ == "__main__":
    main()
