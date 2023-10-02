""" Testing functions for MacroDiary program in project.py file """
from project import get_food, get_food_data, get_quantity, get_selection_first_action, add_food, get_selection_second_action


def test_get_food():
    """ get_food should only return stirngs containing alphabetic characters """
    assert get_food("apple") == "apple"


def test_get_food_data():
    """ proteins, fats, and carbs should be returned """
    assert get_food_data("apple") == ("0.00", "0.65", "14.30")


def test_get_quantity():
    """ an "s" should be added to the end of the food searched if greater than 1 """
    assert get_quantity(1, "apple") == "1 apple"
    assert get_quantity(2, "apple") == "2 apples"


def test_get_selection_first_action(mocker): 
    """ first action selected by user could involve calling add_food function """
    mocker.patch("project.add_food", return_value = "Macronutrient data for 1 apple has been added to your MacroDiary!")
    expected = 1
    actual = get_selection_first_action(1, '1 apple', '0.00', '0.65', '14.30')
    assert expected == actual


def test_add_food():
    """ once complete, function should let user know their data has been added """
    assert add_food("1 apple", "0.00", "0.65", "14.30") == "\nMacronutrient data for 1 apple has been added to your MacroDiary!\n"
    assert add_food("2 apples", "0.00", "0.65", "14.30") == "\nMacronutrient data for 2 apples has been added to your MacroDiary!\n"


def test_get_selection_second_action():
    """ program should end after diary PDF is created """
    assert get_selection_second_action(2) is False
