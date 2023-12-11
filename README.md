# Final Project Report

* Student Name: Pamela Alvarez
* Github Username: pamach
* Semester: Fall 2023
* Course: CS 5001



## Description 

This program uses a common survey framework to help users (target audience children) choose the right pet for them. The inspiration for this program can be seen in program_inspiration.pdf in this repository. By designating certain prompts to specific pet categories, we can replicate the way this survey works. Because there are so many different kinds of pets, and children of different ages will have different skillset and needs when it comes to their pets, I wanted to ensure that this program was easily customizable. The idea is that a parent sets up the program with the pet types they are comfortable with their child having, and writes a number of prompts for each pet type that the child will respond to. For example, a good prompt for a "Lizard" pet category would be "I don't want a furry pet". The pet info provided in pet_info.txt was obtained from petmd.com: https://www.petmd.com/dog/pet-lover/these-are-best-pets-kids-each-age


## Key Features
This program is highly customizable. Users can follow a simple format to change the pet categories and prompts. They can choose to survey for any four pet types, and include any number of prompts as long as each pet type has the same number of prompts. 

The program builds constants in constants.py by reading from several .txt files. The prompts.txt file must follow a simple format in order to be read correctly. Because the program is not hard-coded to read from "line 5 - line 10" for Pet A prompts, the number of prompts can vary as long as the number of prompts for each pet type is the same. 

As a result, this program can easily be used as a framework for creating surveys of any kind. The limitations are that there must be four categories: four possible outcomes, the number of prompts for each category must be the same, and a number rating system of 1, 2 or 3 must be used. Additionally, the results are by default the highest scores obtained, so users should take care to design their surveys accordingly. The printouts to the user in the print_pet_match() function and print_pet_info() function can be made less 'pet-specific' as well. 

## Guide
The program will run upon opening from the terminal, as long as python is installed. Ensure you are in the right file directory, where all the program files have been downloaded, and initiate the program from the terminal. 

You can customize this program easily, and add your own pet types and prompts. Below is a set of guidelines on how to do so.
* There must be a total of four pet categories. 
* A pet category must be only one word
* In prompts.txt the first word following the colon after each "Pet []:" must be the pet category
  * For example "Pet A: Snakes" is valid, but "Pet A: Small mammals" is not valid. 
* Each line following the "Pet []:" line, until the "~~~" line must containing exactly one prompt for that pet category. 
  * Prompts cannot be written on multiple lines. 
  * You must 'sandwhich' your prompts directly between a "Pet []:" line and a "~~~" line.
* The number of prompts must be the same for each category
* Update the pet_info.txt file following the same format, where the content for "Pet A" is found between the "Pet A" line and the "~~~" line.

## Installation Instructions
Download every file in the "program" folder and ensure they are all in the same location on your computer. The program pet_matcher.py can then be run from your IDE. If running from the terminal, ensure that you are in the correct directory and that all files are in the same location. 

## Code Review
The most important function in this program is get_prompt_answers()

```python
def get_prompt_answers() -> list:
    """
    Obtains the user's response to each prompt. Asks the prompts in a rotating
    order, starting with a prompt for Pet A, then a prompt for Pet B, and so on
    until all prompts have been asked. Stores the ordered answers in a list. Returns this list.

    Args:
        None

    Returns:
        list [int]: a list of integers. Each integer is the user's response to a prompt.
            The order of the elements in this list is [answer_A, answer_B, answer_C, answer_D] and rotates 
            in this pattern until an answer for all prompts is obtained.
    """
    list = []
    # the loop iterations must line up with the number of prompts for each pet category
    for i in range(0, constants.NUMBER_OF_PROMPTS):
        # rotate through the prompts so that all the prompts for
        # a pet category are not asked all at the same time, all in a row.
        answer_A = validate_input(constants.PET_A_PROMPTS[i])
        answer_B = validate_input(constants.PET_B_PROMPTS[i])
        answer_C = validate_input(constants.PET_C_PROMPTS[i])
        answer_D = validate_input(constants.PET_D_PROMPTS[i])
        # keep the list in a clear order to make finding the total sums
        # for each pet category easier
        list.extend([answer_A, answer_B, answer_C, answer_D])
    return list  
```

This function asks the user to respond to each prompt, and record the user's response in an ordered list. It depends on another function: validate_input() which we will explore next. Technically, it is validate_input() that is asking the prompts and returning the user's response, but it truly is get_prompt_answers() that runs the show. We see that this function tells validate_input() exactly what to ask, in what order, and where to store the response. For each loop, this function obtains a response for each of the four pet categories *first*, and *then* adds the values to a list for storage. This kills two birds with one stone: we are able to alternate the category of prompt being asked, and keep track of each answer in an organized way. 

Within get_prompt_answers(), we see that validate_input() is called to obtain a value from the user. 

```python
def validate_input(prompt: str) -> int:
    """
    Ensures that the user provides a valid answer: 1, 2 or 3. If an invalid answer 
    is entered, a custom message prints to the user and prompts them to provide an answer again.

    Args:
        prompt (str): a string containing the message to be printed to the user.
        The user will respond to this message with a 1, 2 or 3. If anything else is entered, 
        the user is prompted to choose a valid answer. 

    Returns:
        int: the integer value 1, 2 or 3 based on the user's answer
    """
    user_answer = input(prompt)
    if user_answer.isnumeric():
        number = int(user_answer)
        if number > 0 and number < 4:
            return number
        else:
            print("Your answer must be 1, 2, or 3.")
            # provide the same prompt to user until a valid input is entered
            return validate_input(prompt)
    else:
        print("Your answer cannot contain letters. It must be the whole number '1', '2' or '3'")
        # provide the same prompt to user until a valid input is entered
        return validate_input(prompt) 
```

There are two recursive return statements in this function. These are found within if statements that help to ensure the user provided a valid response. We are able to provide a more individualized message to the user thanks to these separate if statements. For example, in the nested if statement, we know that the user did in fact provide a numeric answer. However, the user provided a number that was not in our specified range. We can therefore print a simple reminder to use 1, 2 or 3, and recurse back through the validate_input() function to ask the same prompt again. 

In the case that the user's answer is *not* a number, the first if statement determined that the answer contained non-numeric characters, and the outermost "else" block was executed. Here, the message to the user is more specific. They likely entered "one" or another non-numeric version of their intended response, so we can clarify "Your answer cannot contain letters. It must be the whole number '1', '2' or '3'"


Once the user has answered all prompts with valid inputs, main() processes the results to obtain the user's 'pet match'. We create a dictionary and store it in the variable "results". Two functions directly affect the formation of the dictionary: sum_results() and log_scores(). sum_results() takes two parameters: a list of all the user answers and the integer of the index at which the first answer to be summed is found. We provide sum_results() with the list of all answers, the integer 1, and it will return the sum of the user's responses to all the Pet B prompts. In the code from log_scores() we can see that the 0 index corresponds to Pet A, 1 corresponds to Pet B, and so on. 

```python
    results = {}
    # we know the exact starting index where each pet category
    # has its first value stored in the list
    # according to the list order built in get_prompt_answers()
    results[constants.PET_A] = sum_results(list, 0)
    results[constants.PET_B] = sum_results(list, 1)
    results[constants.PET_C] = sum_results(list, 2)
    results[constants.PET_D] = sum_results(list, 3)
    return results
```

Above, we can see that log_scores creates a dictionary in a very simple way: adding keys and values to the empty dictionary intialized in the "results" variable. 

From here, we want to find the highest value in the dictionary, and return the key corresponding to that value. Since it is possible for there to a tie, we want to record all the keys in a list. This is what find_pet_match() does:

```python
def find_pet_match(dict: {str: int}) -> list:
    """
    Takes a dictionary and finds the highest value in the dictionary. Returns a list
    where each element is a key corresponding to the highest value in the dictionary. 
    If the highest score is 10, and only one pet type has that value, only that pet type
    is returned in the list. If there is a tie, then all the pet types with the tied high 
    score are returned in the list.  

    Example:
    sample = {'Cat': 4, 'Reptile': 5, 'Hamster': 2, 'Rabbit': 4}
    >>> find_pet_match(sample)
    ['Reptile']

    Args:
         dict {str: int}: a dictionary where each key is a pet type, and each value is the sum 
            of the user's responses to this pet type's prompts.

    Returns:
        list [str]: a list containing the key(s) in the dictionary with the highest value. If there
            is a tie for the highest value, all the keys with that value are returned in the list.
    """
    max_score = max(dict.values())
    match = []  # build a list to store the keys in because there may be ties for highest score
    for key in dict:
        if dict[key] == max_score:
            match.append(key)
    return match
```

The last two functions print out relevant information based on the results from find_pet_match(). print_pet_match() informs the user what their pet match was, and print_pet_info gives the user additional information based on their pet match. 

Importantly, constants are initialized in constants.py. The constants module is responsible for reading our .txt files and compiling the various strings used in pet_matcher.py. Since we want the users to be able to customize this program, there is some error handling necessary in constants.py. 

For example, the NameError in pet_line_read() ensures that each pet category is provided a value. The IndexError ensures that the pet category is only one word long. 

```python
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
```


### Major Challenges

With the goal of having the .txt files be easily customizable, I had to keep in mind a format for the file that would be easy for the user to pick up on, and easy for my program to read. It made the most sense to have the prompts for each category directly follow the "Pet []:" line in prompts.txt, and a simple line of "~~~" characters easily denotes the separation of sections. However, the simple organization of the prompts in this way made it hard to 'mix up' the order that the prompts would be asked in. Even a child can quickly catch on to a series of 4 prompts all asking how they feel about the same type of animal. 

While my first thought was to use the random.py module to create some pseudo-randomness, I quickly saw that it would mean extra layers of work needed to both randomize and keep track of the prompts. Given the time constraints for this project, the simplest solution was to ask a prompt from each category, in order, and keep track of those answers. This is seen in get_prompt_answers(). 

## Example Runs
Program was run on terminal and text output from terminal was recorded and saved as .txt files labelled "terminal_test_run_1" and so on. A successful program run will ask the user prompts one at a time. As documented in terminal_test_run_2, if the user does not provide a valid response of 1, 2 or 3, then they are given individualized feedback and prompted to respond until a valid answer is given. 

## Testing
Code was tested in two ways: either in a code testing function or in the interactive window on VScode. The testing functions are found in test_constants.py and test_pet_matcher_app.py. Documentation of specific function printouts can be found in pet_matcher_testing_documentation_1.pdf and pet_matcher_testing_documentation_2.pdf


## Missing Features / What's Next
A major limitation is that the number of pet categories must be exactly four. Were there more time, I would have liked to come up with a way to make even the number of categories customizable as well. Additionally, it would be useful to have a way of randomizing the order that the prompts are posed to the user, while still keeping track of the category that each prompt belongs to. Another feature that would be nice is to have pet types be longer than one word. While multiple words could be combined to make the current program still work, like writing "BeardedDragon" as one word instead, it would be much more convenient to be able to have the code handle multiple words for the pet category. Lastly, the rating system could also be expanded to be any range of numbers, as long as it makes sense for the type of survey the user has in mind. 

## Final Reflection
The biggest takeaway from this course for me is how to think about a problem. Building this program was extremely satisfying: watching all the pieces fit together like a puzzle. Additionally, while I am not the expert on python (or any other programming language for that matter), I am confident in my understanding of good program writing and efficiency. For example, the first version of the program I wrote was able to achieve the pet matching goal, but it was not versatile at all. I saw how much more useful it could be if different pieces of the 'survey' were able to be modified. This really drove home the significance of modular design to me. 

At this time, I would benefit the most just from practicing the skills I learned this semester. I am taking a leave of absence next semester, so while I won't be participating in an intensive course, I plan on becoming even more comfortable with python and explore other languages too. 
