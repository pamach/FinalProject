"""
--------------------------
Final Project: Constants
--------------------------
STUDENT: Pamela Alvarez
SEMESTER: Fall 2023

Constants used in the Pet Matcher App
"""


def simple_read(file_name: str) -> str:
    """
    Reads the file named 'file_name' in its entirety and 
    returns one string containing the file text.

    Args:
       file_name (str): the name of the file to be read. Must end in '.txt'

    Returns:
        str: a single string containing the message in file_name
    """
    with open(file_name) as f:  # use with open() to ensure file is safely closed each time
        return f.read()


def pet_line_read(file_name: str, pet_category: str) -> str:
    """
    Searches for a line containing the target pet category in a file and returns 
    the third word in that line. The third word in the line is the pet type
    assigned to that pet category. Errors are raised if there are not exactly three 
    words in the line. 

    Example:
    prompts.txt contains the line "Pet A: Reptiles"
        >>> pet_line_read("prompts.txt", "Pet A:")
        'Reptiles'

    Args:
        file_name (str): the name of the file to be searched. Must end in '.txt'
        pet_category (str): a string denoting the pet category to look for. Ex: 'Pet A:'

    Returns: 
        str: the pet type assigned to the given pet category. Ex: 'Reptiles'    
    """
    pet_string = ""
    with open(file_name) as f:
        for line in f:
            if pet_category in line:
                pet_string = line
    list = pet_string.split()
    if len(list) == 2:
        raise NameError(
            "The '{}' category is missing a value. Insert a pet type after the colon. Ex: 'Pet A: InsertPetType'".format(pet_category))
    if len(list) > 3:
        raise IndexError(
            "The '{}' category has a pet type longer than one word. The pet type must be one word only. Ex: 'Pet A: Snakes'".format(pet_category))
    pet_type = list[2]
    return pet_type


def get_line_number(file_name: str, phrase: str, start_line_number: int) -> int:
    """
    Searches a file for a target phrase and returns the line number where the 
    target phrase appears for the first time after a given line number.

    Example:
    Line 7 in prompts.txt is "Pet B: Dogs"
        >>> get_line_number("prompts.txt", "Pet B:", 0)
        7

    Line 6, 12, 18 and 24 in prompts.txt contain "~~~~~~~"
        >>> get_line_number("prompts.txt", "~~~", 15)
        18

    Args:
        file_name (str): the name of the file to be searched. Must end in '.txt'
        phrase (str): the specific characters to search for
        start_line_number (int): the line number where the search should begin. If phrase appears 
            before this line number, nothing will be returned. 

    Returns: 
        int: the number of the line after the start_line_number where the phrase appears for the first time 
    """
    target_line = 0
    with open(file_name) as f:
        for line in f:
            target_line += 1
            if phrase in line and target_line > start_line_number:
                return target_line


def read_into_list(file_name: str, pet_category: str) -> list:
    """
        Searches a file for a target pet category and returns a list where each element is a line between
        the pet category line and the ending sequence line '~~~'

        Example:
        prompts.txt contains the following excerpt: 
        'Pet B: Dogs
        Question 1 about dogs
        Question 2 about dogs
        Question 3 about dogs
        ~~~~~~~~~~~~~~~~~~~~~~
        Pet C: Reptiles
        Question 1 about reptiles'

            >>> read_into_list("prompts.txt", "Pet B:")
            ['Question 1 about dogs\n', 'Question 2 about dogs\n', 'Question 3 about dogs\n']

        Args:
            file_name (str): the name of the file to be searched. Must end in '.txt'
            pet_category (str): a string denoting the pet category to look for. Ex: 'Pet B:'

        Returns: 
            list [str]: a list of strings where each element is a line in file_name. Specifically, these 
                are the lines in between the pet category line and the ending sequence line: '~~~'
    """
    start_line = get_line_number(file_name, pet_category, 0)
    # subtract 1 because we don't want to include the '~~~' line
    end_line = get_line_number(file_name, "~~~", start_line) - 1
    list = []
    with open(file_name) as f:
        list = f.readlines()[start_line:end_line]
    return list


def confirm_prompt_number(list_A: [str], list_B: [str], list_C: [str], list_D: [str]) -> int:
    """
    Checks 4 lists to ensure they are all the same length, and provides the length as an int.
    Raises an error is the list lengths do not match.
    Example:
    list_A = ['a', 'b', 'c']
    list_B = ['e', 'f', 'g']
    list_C = ['h', 'i', 'j']
    list_D = ['k', 'l', 'm']

    >>> confirm_prompt_number(list_A, list_B, list_C, list_D)
    3

    Args:
       list_A [str]: a list consisting of strings. 
       list_B [str]: a list consisting of strings.
       list_C [str]: a list consisting of strings. 
       list_D [str]: a list consisting of strings.  

    Returns:
        int: the length of a single list if the length of each list is the same. 
    """
    list_A_length = len(list_A)
    list_B_length = len(list_B)
    list_C_length = len(list_C)
    list_D_length = len(list_D)
    if list_A_length == list_B_length == list_C_length == list_D_length:
        return list_A_length
    else:
        raise IndexError("Each pet category must have the same number of prompts. Currently, {0} has {4} prompts, {1} has {5} prompts, {2} has {6} prompts, and {3} has {7} prompts.".format(
            PET_A, PET_B, PET_C, PET_D, list_A_length, list_B_length, list_C_length, list_D_length))


WELCOME_MESSAGE = simple_read("welcome_message.txt")
GOODBYE_MESSAGE = simple_read("goodbye_message.txt")
PET_A = pet_line_read("prompts.txt", "Pet A:")
PET_B = pet_line_read("prompts.txt", "Pet B:")
PET_C = pet_line_read("prompts.txt", "Pet C:")
PET_D = pet_line_read("prompts.txt", "Pet D:")

PET_A_PROMPTS = read_into_list("prompts.txt", "Pet A")
PET_B_PROMPTS = read_into_list("prompts.txt", "Pet B")
PET_C_PROMPTS = read_into_list("prompts.txt", "Pet C")
PET_D_PROMPTS = read_into_list("prompts.txt", "Pet D")

NUMBER_OF_PROMPTS = confirm_prompt_number(
    PET_A_PROMPTS, PET_B_PROMPTS, PET_C_PROMPTS, PET_D_PROMPTS)

PET_A_INFO = ''.join(read_into_list("pet_info.txt", "Pet A:"))
PET_B_INFO = ''.join(read_into_list("pet_info.txt", "Pet B:"))
PET_C_INFO = ''.join(read_into_list("pet_info.txt", "Pet C:"))
PET_D_INFO = ''.join(read_into_list("pet_info.txt", "Pet D:"))
