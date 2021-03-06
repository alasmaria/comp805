"""
Lab 2
lab2.py
Abdullah Alasmari
1/30/2018
"""

def squared_nums(num_list):
    """
    Squares numbers in num_list
    num_list: list of numbers
    Returns: list of these numbers squared
    """
    return_list = []
    for number in num_list:
        return_list.append(number ** 2)

    return return_list

def check_title(title_list):
    """
    Removes strings in title_list that have numbers and aren't title case
    title_list: list of strings
    Returns: list of strings that are titles
    """
    return_list = []
    numbers = "0123456789"
    for title in title_list:
        remove_title = False
        for number in numbers:
            if number in title:
                remove_title = True
        if title.istitle() == True and remove_title == False:
            return_list.append(title)
    return return_list

def restock_inventory(inventory):
    """
    Increases inventory of each item in dictionary by 10
    inventory: a dictionary with:
    ** key: string that is the name of the inventory item**
    ** value: integer that equals the number of that item currently on hand**
    Returns: updated dictionary where each inventory item is restocked
    """
    return_dict = {}
    for key, value in inventory.items():
        return_dict[key] = inventory[key] + 10
    return return_dict

def filter_0_items(inventory):
    """
    Removes items that have a value of 0 from a dictionary of inventories
    inventory: dictionary with:
    ** key: tring that is the name of the inventory item**
    ** value: nteger that equals the number of that item currently on hand**
    Returns: the same inventory_dict with any item that had 0 quantity removed
    """
    return_dict = {}
    for key, value in inventory.items():
        if inventory[key] != 0:
            return_dict[key] = inventory[key]
    return return_dict

def average_grades(grades):
    """
    Takes grade values from a dictionary and averages them into a final grade
    grades: a dictionary of grades with:
    key: string of students name
    value: list of integer grades received in class
    Returns: dictionary that averages out the grades of each student
    """
    return_dict = {}
    for student, grades in grades.items():
        these_grades = 0
        num_grades = 0
        for grade in grades:
            num_grades += 1
            these_grades += grade
        final_grade = these_grades / num_grades
        return_dict[student] = final_grade
return return_dict
