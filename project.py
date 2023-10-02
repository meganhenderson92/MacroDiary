""" MacroDiary """
import requests
from fpdf import FPDF


api_key = "712OtioTu1vbpN2Dr2ywXIxbrP9WghOBwZBp5K4S"
diary_heading = [["Food", "Protein (g)", "Fat (g)", "Carbs (g)"]]
diary = []
print("Welcome to MacroDiary!")


def main():
    """ overall process of user inputting food to search, retrieving data for that food, and deciding what they want to do with that info """
    food = input("Input the food item that you would like macronutrient data for: ")
    protein, fat, carbs = get_food_data(get_food(food))
    quantity = int(input("Quantity: "))
    food_quantity = get_quantity(quantity, food)
    print(f"\nMacronutrient data for {food_quantity}: {protein} grams of protein, {fat} grams of fat, and {carbs} grams of carbohydrates.\n")
    print("Select an option: ")
    print("[1] Add data to MacroDiary & search for another food item")
    print("[2] Add data to MacroDiary & print MacroDiary")
    print("[3] Do not add data to MacroDiary & search for another food item")
    print("[4] Do not add data to MacroDiary & print MacroDiary")
    get_selection_second_action(get_selection_first_action(int(input("Selection: ")), food_quantity, protein, fat, carbs))


def get_food(s):
    """ make sure user inputs valid food item to search for """
    while True:
        try:
            if str.isnumeric(s) is False:
                break
        except (AssertionError, ValueError, TypeError):
            print("Your search should contain alphabetic characters only.")
    return s


def get_food_data(s):
    """ Retrieve macro data for food item input by user using FoodData Central API """
    url = f"https://api.nal.usda.gov/fdc/v1/foods/search?query={s}&api_key={api_key}"
    while True:
        try:
            response = requests.get(url, timeout=3)
            if response.status_code == 200:
                f = response.json()
                if f.get("foods"):
                    first_result = f["foods"][0]
                    #description = first_result["description"].lower()
                    nutrients = first_result["foodNutrients"]
                    protein = [nutrient["value"] for nutrient in nutrients if nutrient["nutrientId"] == 1003]
                    fat = [nutrient["value"] for nutrient in nutrients if nutrient["nutrientId"] == 1004]
                    carbs = [nutrient["value"] for nutrient in nutrients if nutrient["nutrientId"] == 1005]
                    break
                else: 
                    print(f"No result found for {s}")
                    main()
                    break
        except (ValueError, TimeoutError):
            print("Response Failed")
            main()
    return f"{protein[0]:.2f}", f"{fat[0]:.2f}", f"{carbs[0]:.2f}"


def get_quantity(x, s):
    """ add "s" to the end of the food if user input is more than one for an accurate description in print messages """
    if x > 1:
        s = f"{x} {s}" + "s"
    else: 
        s = f"{x} {s}"
    return s

def get_selection_first_action(x, s, p, f, c):
    """ first action in option selected by user """
    while True:
        try:
            if x in [1, 2, 3, 4]:
                if x == 1 or x == 2:
                    print(add_food(s, p, f, c))
                    break
                elif x == 3 or x == 4:
                    break
        except ValueError:
            print("Please make a selection from the options provided")
    return x


def add_food(s, p, f, c):
    """ adding food data to diary """
    entry = [s, p, f, c]
    diary.append(entry)
    return f"\nMacronutrient data for {s} has been added to your MacroDiary!\n"


def get_selection_second_action(x):
    """ second action in option selected by user """
    while True:
        if x == 1 or x == 3:
            main()
            break
        elif x == 2 or x == 4:
            total_proteins = sum([float(entry[1]) for entry in diary])
            total_fats = sum([float(entry[2]) for entry in diary])
            total_carbs = sum([float(entry[3]) for entry in diary])
            last_entry = ["TOTALS:", f"{total_proteins:.2f} grams", f"{total_fats:.2f} grams", f"{total_carbs:.2f} grams"]
            diary.append(last_entry)
            print("Your MacroDiary PDF file has been created! Thank you :)")
            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("helvetica", "B", size=55)
            pdf.cell(w=0, h=31, txt="MacroDiary", align="C")
            pdf.ln()
            pdf.set_font("helvetica", size=14)
            with pdf.table() as table:
                for data_row in diary_heading:
                    row = table.row()
                    for datum in data_row:
                        row.cell(datum)
            pdf.set_font("helvetica", size=14)
            with pdf.table(first_row_as_headings=False) as table:
                for data_row in diary:
                    row = table.row()
                    for datum in data_row:
                        row.cell(datum)
            pdf.output("MacroDiary.pdf")
            break
    return False


if __name__ == "__main__":
    main()
