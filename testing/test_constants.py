"""
--------------------------
Final Project: Tester for Constants Module
--------------------------
STUDENT: Pamela Alvarez
SEMESTER: Fall 2023
"""
import constants as app

def test_simple_read() -> int:
    """
    Tests simple_read() with a sample file.

    Returns:
        int: 1 if test failed, 0 if test passed.
    """
    failed = 0
    expected = "This is the test file\nfor checking the functions\nin the constants module."
    actual = app.simple_read("test_message.txt")
    if expected != actual:
        failed += 1
        print("test_simple_read failed")
        print("expected:", expected)
        print("actual:", actual)
    return failed

def test_pet_line_read() -> int:
    """
    Tests pet_line_read() with a sample file.

    Returns:
        int: number of tests failed
    """
    failed = 0
    expected = "TestA"
    actual = app.pet_line_read("test_prompts.txt", "Pet A:")
    if expected != actual:
        failed += 1
        print("test_pet_line_read failed")
        print("expected:", expected)
        print("actual:", actual)
    expected = "TestC"
    actual = app.pet_line_read("test_prompts.txt", "Pet C:")
    if expected != actual:
        failed += 1
        print("test_pet_line_read failed")
        print("expected:", expected)
        print("actual:", actual)
    return failed

def test_get_line_number() -> int:
    """
    Tests get_line_number() with a sample file.

    Returns:
        int: number of tests failed
    """
    failed = 0
    expected = 1
    actual = app.get_line_number("test_prompts.txt", "Pet A:", 0)
    if expected != actual:
        failed += 1
        print("test_get_line_number failed")
        print("expected:", expected)
        print("actual:", actual)
    expected = 10
    actual = app.get_line_number("test_prompts.txt", "~~~", 6)
    if expected != actual:
        failed += 1
        print("test_get_line_number failed")
        print("expected:", expected)
        print("actual:", actual)
    return failed


def test_read_into_list() -> int:
    """
    Tests read_into_list() with a sample file.

    Returns:
        int: number of failed tests
    """
    failed = 0
    expected = ['1. First prompt for category 1\n', '2. Second prompt for category 1\n', '3. Third prompt for category 1\n']
    actual = app.read_into_list("test_prompts.txt", "Pet A:")
    if expected != actual:
        failed += 1
        print("test_read_into_list failed")
        print("expected:", expected)
        print("actual:", actual)
    expected = ['Testing the info\n', 'for pet 1\n', 'this is it.\n']
    actual = app.read_into_list("test_pet_info.txt", "Pet A")
    if expected != actual:
        failed += 1
        print("test_read_into_list failed")
        print("expected:", expected)
        print("actual:", actual)
    return failed

def test_confirm_prompt_number() -> int:
    """
    Tests confirm_prompt_number() with sample lists.

    Returns:
        int: number of tests failed
    """
    failed = 0
    expected = 3
    actual = app.confirm_prompt_number([1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12])
    if expected != actual:
        failed += 1
        print("test_confirm_prompt_number failed")
        print("expected:", expected)
        print("actual:", actual)
    return failed

def main():
    failed = 0
    failed += test_simple_read()
    failed += test_pet_line_read()
    failed += test_get_line_number()
    failed += test_read_into_list()
    failed += test_confirm_prompt_number()

    if failed == 0:
        print("All tests passed!")
    else:
        print("Number of tests failed:", failed)

if __name__ == "__main__":
    main()