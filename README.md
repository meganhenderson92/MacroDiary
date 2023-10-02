# MacroDiary
Video Demo: https://youtu.be/XzZ2FGWnT9g

## Description
This project allows a user to search for a food item, receive the macronutrients of that food item, and they are given four options on what to do with that data: 
    
1. Add data to diary and search for another food item
2. Add data to diary and print diary
3. Do not add data to diary and search for another food item
4. Do not add data to diary and print diary

When the user selects option 2 or 4, a file called "MacroDiary.pdf" is created. 
    
Project structure:

    project.py
    test_project.py
    requirements.txt
    README.md

## Libraries
Libraries used to create this project include: 

    requests
    fpdf

## API
This project utilizes the FoodData Central public API to retrieve the macronutrient data of the food input by the user.

## Functions
This project contains 7 functions, including the main function. All functions except for the main function are included in the test_project.py file. 

### main()
User input, variable setting, and all functions begining with "get_" are called within the main function. With this design, it is easy to look at the main function and understand how the overall program works:
    
user input food item > get macro data of that food item > quantity of that food item > display macro data of the quantity of that food > user decided if they want to add or not add this data to their diary and either search for another food item or print their diary. 
    
This was also the optimal way for pytest to be able to test the rest of the functions in test_project.py 

### get_food()
This function handles errors that may occur when the user inputs a food item (i.e. an input that is not alphabetic characters only). "str.isnumeric() is False" is used as opposed to "str.isalpha() is True" to allow for input that may contain a space (i.e. sweet potato). 

### get_food_data()
This function uses the FoodData Central API to retrieve the macronutrient values of the food item input by user. This program only looks at the first result found in the search. More robust code is needed to filter all results found for the best possible match, which I may try to implement in a future version of this project. 

### get_quantity()
This function ensures that from this point on whenever the food item is mentioned, it's quantity is displayed with it and it's also made plural if the user input was greather than 1. 

### get_selection_first_action()
This function handles the first action of the option the user chooses to do with their data - to add or not add their data. If the user selects option 1 or 2, the add_food() function is called. If the user selects option 3 or 4, the program goes straight to the get_selection_second_action() function. 

### add_food()
When called, this function appends the quantity of the food item and its macronutrient data as an entry to the diary. The diary begins as an empty list at the beginning of the program. 

### get_selection_second_action()
The function handles the second action of the option the user chose - to search for another food item or print their diary. If the user selected option 1 or 3, this function calls main() to repeat the entire process. if the user selected option 2 or 4 - totals of each macro are calculated, appended to the diary, and formatted PDF titled "MacroDiary" is created. 

## Conclusion
This was my first personal project and I created it accoridng to the CS50P final project requirements and guidelines. I am a self-taught software engineer and CS50P was the first major resource I used to get myself started. Feedback from anyone who comes across this project is more than welcome. Thank you! 
