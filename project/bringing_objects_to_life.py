# TODO: Stage 3 - Bringing Objects to Life!
# 
# In this stage, you'll learn about:
# - Instantiation: Creating objects from classes
# - Methods: Functions that belong to objects
# - Accessors vs Mutators: Methods that read vs methods that modify
# - Method chaining: Calling multiple methods in sequence
#
# Instructions:
# Complete all the functions below. Read the docstrings carefully and implement
# the logic using concepts you've learned about instantiation and methods.


def compare_literal_vs_constructor():
    """
    Create an int using literal form (42) and constructor form (int(42)),
    then verify they represent the same value.
    
    Returns:
        A tuple (literal_int, constructor_int, are_equal) where:
        - literal_int: An integer created using literal form (e.g., 42)
        - constructor_int: An integer created using constructor form (e.g., int(42))
        - are_equal: True if both represent the same value, False otherwise
    
    Hint:
    1. Create an integer using literal form: number = 42
    2. Create an integer using constructor form: number2 = int(42)
    3. Compare them using == to check if they have the same value
    4. Return all three values
    """
    # TODO: Implement this function
    pass


def instantiate_list_with_items():
    """
    Create a list with initial values [1, 2, 3] using literal form.
    
    Returns:
        A list containing the integers 1, 2, and 3
    
    Hint: Use literal form to create a list: [1, 2, 3]
    """
    # TODO: Implement this function
    pass


def call_accessor_methods(data_list, value_to_count, text_string):
    """
    Call accessor methods on a list and a string.
    Accessor methods return information but don't modify the object.
    
    Args:
        data_list: A list of values
        value_to_count: The value to count occurrences of in data_list
        text_string: A string to process
    
    Returns:
        A tuple (count_result, upper_result, lower_result) where:
        - count_result: Number of times value_to_count appears in data_list (using .count())
        - upper_result: text_string converted to uppercase (using .upper())
        - lower_result: text_string converted to lowercase (using .lower())
    
    Hint:
    1. Use data_list.count(value_to_count) to count occurrences
    2. Use text_string.upper() to get uppercase version
    3. Use text_string.lower() to get lowercase version
    """
    # TODO: Implement this function
    pass


def call_mutator_methods(data_list, item_to_add):
    """
    Call mutator methods on a list.
    Mutator methods modify the object and typically return None.
    
    Args:
        data_list: A list to modify (will be modified in place)
        item_to_add: An item to add to the list
    
    Returns:
        A tuple (list_after_append, list_after_sort) where:
        - list_after_append: The list after calling .append(item_to_add)
        - list_after_sort: The list after calling .sort()
    
    Hint:
    1. Create a copy of data_list first (using .copy() or list(data_list))
    2. Call .append(item_to_add) on the copy
    3. Store the result (it will be None, but the list is modified)
    4. Call .sort() on the list
    5. Return the modified list (not the return value of the methods)
    
    Note: Since mutators modify the list, you may need to work with copies
    to avoid modifying the original input.
    """
    # TODO: Implement this function
    # Step 1: Create a copy of data_list
    # Step 2: Call .append(item_to_add) on the copy
    # Step 3: Call .sort() on the copy
    # Step 4: Return the modified copy
    pass


def chain_string_methods(text_string, char_to_replace, replacement_char):
    """
    Chain multiple string methods together.
    Given a string, apply .lower(), then .strip(), then .replace() in sequence.
    
    Args:
        text_string: A string to process
        char_to_replace: Character to replace in the string
        replacement_char: Character to replace with
    
    Returns:
        The final string after applying .lower().strip().replace(char_to_replace, replacement_char)
    
    Hint: Chain the methods: text_string.lower().strip().replace(char_to_replace, replacement_char)
    """
    # TODO: Implement this function
    pass


def process_list_of_strings(string_list):
    """
    Process a list of strings using methods:
    1. Convert all strings to uppercase
    2. Filter out empty strings
    3. Sort the result
    
    Args:
        string_list: A list of strings to process
    
    Returns:
        A new list with all strings uppercase, empty strings removed, and sorted
    
    Hint:
    1. Create a new list (or copy the original)
    2. Convert each string to uppercase (you can use a list comprehension or loop)
    3. Filter out empty strings (you can use a list comprehension with a condition)
    4. Sort the result using .sort() or sorted()
    5. Return the processed list
    """
    # TODO: Implement this function
    # Step 1: Convert all strings to uppercase
    # Step 2: Filter out empty strings
    # Step 3: Sort the result
    pass


def string_manipulation_chain(text_string):
    """
    Chain string methods to process a string:
    1. Strip whitespace from both ends
    2. Convert to lowercase
    3. Replace spaces with underscores
    
    Args:
        text_string: A string with mixed case and spaces
    
    Returns:
        The processed string after: strip, lower, replace spaces with underscores
    
    Hint: Chain the methods: text_string.strip().lower().replace(' ', '_')
    """
    # TODO: Implement this function
    pass

