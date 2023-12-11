"""
--------------------------
Final Project: Tester for Pet Matcher App
--------------------------
STUDENT: Pamela Alvarez
SEMESTER: Fall 2023
"""
import pet_matcher as app

def test_sum_results() -> int:
    """
    Tests sum_results() with a sample list. 

    Returns:
        int: number of tests failed.
    """
    failed = 0
    expected = 3
    actual = app.sum_results([1, 2, 2, 2, 1, 2, 2, 2, 1, 2, 2, 2], 0)
    if expected != actual:
        failed += 1
        print("test_sum_results failed")
        print("expected:", expected)
        print("actual:", actual)
    expected = 6
    actual = app.sum_results([1, 1, 1, 2, 1, 1, 1, 2, 1, 1, 1, 2], 3)
    if expected != actual:
        failed += 1
        print("test_sum_results failed")
        print("expected:", expected)
        print("actual:", actual)
    return failed

def test_find_pet_match() -> int:
    """
    Tests find_pet_match() with a sample dictionary. 

    Returns:
        int: number of tests failed.
    """
    failed = 0
    expected = ['Reptile']
    actual = app.find_pet_match({'Cat': 4, 'Reptile': 5, 'Hamster': 2, 'Rabbit': 4})
    if expected != actual:
        failed += 1
        print("test_find_pet_match failed")
        print("expected:", expected)
        print("actual:", actual)
    expected = ['Cat', 'Hamster']
    actual = app.find_pet_match({'Cat': 6, 'Reptile': 5, 'Hamster': 6, 'Rabbit': 4})
    if expected != actual:
        failed += 1
        print("test_find_pet_match failed")
        print("expected:", expected)
        print("actual:", actual)
    return failed

def main():
    failed = 0
    failed += test_sum_results()
    failed += test_find_pet_match()

    if failed == 0:
        print("All tests passed!")
    else:
        print("Number of tests failed:", failed)

if __name__ == "__main__":
    main()
