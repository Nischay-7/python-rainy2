"""
Stage 1 Tests: Indentation Essentials

This test suite verifies that students can fix indentation errors and complete functions with correct indentation.
"""
import pytest
from project.code_structure import check_grade, print_numbers, countdown, is_even
from io import StringIO
import sys


def test_check_grade_function_exists():
    """
    Test that check_grade function exists and is callable.
    """
    assert callable(check_grade), "check_grade should be a callable function"


def test_check_grade_returns_a():
    """
    Test that check_grade returns "A" for scores >= 90.
    """
    assert check_grade(95) == "A", "check_grade(95) should return 'A'"
    assert check_grade(90) == "A", "check_grade(90) should return 'A'"
    assert check_grade(100) == "A", "check_grade(100) should return 'A'"


def test_check_grade_returns_b():
    """
    Test that check_grade returns "B" for scores >= 80 and < 90.
    """
    assert check_grade(85) == "B", "check_grade(85) should return 'B'"
    assert check_grade(80) == "B", "check_grade(80) should return 'B'"
    assert check_grade(89) == "B", "check_grade(89) should return 'B'"


def test_check_grade_returns_c():
    """
    Test that check_grade returns "C" for scores >= 70 and < 80.
    """
    assert check_grade(75) == "C", "check_grade(75) should return 'C'"
    assert check_grade(70) == "C", "check_grade(70) should return 'C'"
    assert check_grade(79) == "C", "check_grade(79) should return 'C'"


def test_check_grade_returns_f():
    """
    Test that check_grade returns "F" for scores < 70.
    """
    assert check_grade(65) == "F", "check_grade(65) should return 'F'"
    assert check_grade(50) == "F", "check_grade(50) should return 'F'"
    assert check_grade(0) == "F", "check_grade(0) should return 'F'"


def test_print_numbers_function_exists():
    """
    Test that print_numbers function exists and is callable.
    """
    assert callable(print_numbers), "print_numbers should be a callable function"


def test_print_numbers_output(capsys):
    """
    Test that print_numbers correctly prints numbers from 1 to n.
    """
    print_numbers(5)
    captured = capsys.readouterr()
    output = captured.out.strip()
    expected = "1\n2\n3\n4\n5"
    assert output == expected, f"Expected '{expected}' but got '{output}'"


def test_print_numbers_single_number(capsys):
    """
    Test that print_numbers works with n=1.
    """
    print_numbers(1)
    captured = capsys.readouterr()
    output = captured.out.strip()
    assert output == "1", f"Expected '1' but got '{output}'"


def test_countdown_function_exists():
    """
    Test that countdown function exists and is callable.
    """
    assert callable(countdown), "countdown should be a callable function"


def test_countdown_output(capsys):
    """
    Test that countdown correctly prints countdown and "Blast off!".
    """
    countdown(3)
    captured = capsys.readouterr()
    output = captured.out.strip()
    expected = "3\n2\n1\nBlast off!"
    assert output == expected, f"Expected '{expected}' but got '{output}'"


def test_countdown_single_number(capsys):
    """
    Test that countdown works with start=1.
    """
    countdown(1)
    captured = capsys.readouterr()
    output = captured.out.strip()
    expected = "1\nBlast off!"
    assert output == expected, f"Expected '{expected}' but got '{output}'"


def test_is_even_function_exists():
    """
    Test that is_even function exists and is callable.
    """
    assert callable(is_even), "is_even should be a callable function"


def test_is_even_returns_true_for_even_numbers():
    """
    Test that is_even returns True for even numbers.
    """
    assert is_even(2) == True, "is_even(2) should return True"
    assert is_even(4) == True, "is_even(4) should return True"
    assert is_even(0) == True, "is_even(0) should return True"
    assert is_even(100) == True, "is_even(100) should return True"


def test_is_even_returns_false_for_odd_numbers():
    """
    Test that is_even returns False for odd numbers.
    """
    assert is_even(1) == False, "is_even(1) should return False"
    assert is_even(3) == False, "is_even(3) should return False"
    assert is_even(99) == False, "is_even(99) should return False"
    assert is_even(101) == False, "is_even(101) should return False"


def test_is_even_handles_negative_numbers():
    """
    Test that is_even works with negative numbers.
    """
    assert is_even(-2) == True, "is_even(-2) should return True"
    assert is_even(-3) == False, "is_even(-3) should return False"
