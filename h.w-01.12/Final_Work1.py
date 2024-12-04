# Ex 1:
for num in range(12, 25):
    print(num, end=' ')
print()

# Ex 2:
for num_odd in range(7, 32, 2):
    print(num_odd, end=' ')
print()

# Ex 3:
for num_even in range(10, -21, -2):
    print(num_even, end=' ')
print()

# Ex 4:
for i in range(1, 46):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz", end=', ')
    elif i % 3 == 0:
        print("Fizz", end=', ')
    elif i % 5 == 0:
        print("Buzz", end=', ')
    else:
        print(i, end=', ')
print()


# Ex 5:
def calc_sum(list1: list[int]) -> int:
    nums = 0
    for num in list1:
        nums += num
    return nums


numbers = [1, 13, 22, 123, 49, 34, 5, 24, 57, 45]
result = calc_sum(numbers)
print(result)

# Ex 6:
students = [
    {'id': 123, 'firstName': 'Karin', 'lastName': 'Shaham', 'age': 41, 'country': 'Israel', 'city': 'Rehovot'},
    {'id': 101112, 'firstName': 'Ben', 'lastName': 'Smith', 'age': 22, 'country': 'Canada', 'city': 'Toronto'},
    {'id': 202122, 'firstName': 'Alice', 'lastName': 'Johnson', 'age': 36, 'country': 'UK', 'city': 'London'}
]


# 1.
def del_property(students: list[str], prop_to_del: str) -> None:
    """
    Function that removes a specified property from each object in the list.

    Param:
    students (list): A list of objects, where each object represents a student.
    prop_to_del (str): The name of the property to remove from each student object.

    No return value; the function modifies the list in place.
    """
    for student in students:
        if prop_to_del in student:
            student.pop(prop_to_del)
    print(f"Updated students after removing '{prop_to_del}':")
    print(students)


del_property(students, 'city')


# 2.
def print_student_proper(students: list[str]) -> None:
    """
    Function that prints all properties of each student in the list.

    Param:
    students (list): A list of objects, where each object represents a student.

    No return value; the function prints the properties to the console.
    """
    for student in students:
        for key, value in student.items():
            print(f"{key}: {value}")


print_student_proper(students)


# 3.
def sort_students_by_age(students: list[int]) -> list[int]:
    """
    Function that sorts students by their age in descending order (oldest first).

    Param:
    students (list): A list of objects, where each object represents a student.

    Returns:
    list: A new list of students, sorted by age in descending order.
    """
    sorted_students = sorted(students, key=lambda student: student['age'], reverse=True)
    print(sorted_students)
    return sorted_students


sorted_students = sort_students_by_age(students)


# Ex 7:
our_pets = [{
    "animal_type": "cat",
    "names": ["Meowzer", "Fluffy", "Kit-Cat"]},
    {
        "animal_type": "dog",
        "names": ["Spot", "Bowser", "Frankie"]}]


# 1.
def print_cats(pets: list[str]) -> None:
    """
    Function that prints all pets with the animal type 'cat' from the list.

    Parameters:
    pets (list): A list of dictionaries where each dictionary contains information about an animal.

    No return value; the function prints the names of cats.
    """
    for pet in pets:
        if pet["animal_type"] == "cat":
            print(f"Animal Type: {pet["animal_type"]}")
            for name in pet["names"]:
                print(f"Name: {name}")


print_cats(our_pets)


# 2.
def print_animal_names(pets: list[str], animal_type: str) -> None:
    """
    Function that prints all names of a specified animal type.

    Parameters:
    pets (list): A list of dictionaries where each dictionary contains information about an animal.
    animal_type (str): The type of animal to print names for.

    No return value; the function prints the names of the specified animal type.
    """
    for pet in pets:
        if pet["animal_type"] == animal_type:
            print(f"Animal Type: {pet['animal_type']}")
            for name in pet["names"]:
                print(f"Name: {name}")


print_animal_names(our_pets, "dog")


# 3.
def add_animal_name(pets: list[str], animal_name: str) -> None:
    """
    Function that adds a specified animal name to each animal's 'names' array if it doesn't exist.

    Parameters:
    pets (list): A list of dictionaries where each dictionary contains information about an animal.
    animal_name (str): The name of the animal to add to the 'names' array.

    No return value; the function modifies the 'names' arrays in place.
    """
    for pet in pets:
        if animal_name not in pet["names"]:
            pet["names"].append(animal_name)
    print(pets)


add_animal_name(our_pets, "Yogi")
