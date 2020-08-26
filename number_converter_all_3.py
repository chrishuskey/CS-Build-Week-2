# Import libraries, packages, modules, functions:
import math
import sys


# Fixed constants:
HEX_DIGITS_TO_DECIMAL = {
    "0": 0, 
    "1": 1, 
    "2": 2, 
    "3": 3, 
    "4": 4, 
    "5": 5, 
    "6": 6, 
    "7": 7, 
    "8": 8, 
    "9": 9, 
    "A": 10, 
    "B": 11, 
    "C": 12, 
    "D": 13, 
    "E": 14, 
    "F": 15
}

DECIMAL_TO_HEX = {
    0: "0", 
    1: "1", 
    2: "2", 
    3: "3", 
    4: "4", 
    5: "5", 
    6: "6", 
    7: "7", 
    8: "8", 
    9: "9", 
    10: "A", 
    11: "B", 
    12: "C", 
    13: "D", 
    14: "E", 
    15: "F"
}

def to_decimal(number, base_of_input:int):
    """
    Converts numbers of multiple types (binary, decimal, hexadecimal) 
    into decimal numbers.
    """

    # Handle string input type (e.g., of binary or hex as string):
    if type(number) is int:
        if base_of_input == 2:
            number = bin(number)
        elif base_of_input == 10:
            number = str(number)
        elif base_of_input == 16:
            number = hex(number)
    if number[:2] in ["0b", "0B", "0x", "0X"]:
        number = number[2:]
    
    # Convert input number to list of digits:
    input_as_list = list(number)
    # If hexadecimal input, convert letters to equivalent decimal numbers:
    if base_of_input == 16:
        for i in range(len(input_as_list)):
            input_as_list[i] = HEX_DIGITS_TO_DECIMAL[str(input_as_list[i]).upper()]

    # Convert to decimal number:
    number_as_decimal = 0
    for i in range(-1, -len(input_as_list) - 1, -1):
        number_as_decimal += int(input_as_list[i]) * base_of_input**abs(i+1)
    
    return number_as_decimal


def convert_number(number, base_of_input:int, base_of_output:int):
    """
    Converts input number (of type binary, decimal or hexadecimal) into 
    same number as specified output type (binary, decimal or hex).
    Returns the string version of the output number.
    """

    # Convert from input type (binary, decimal or hex) into decimal, to work with:
    number_as_decimal = to_decimal(number=number, base_of_input=base_of_input)

    # Convert into list of digits in the right base (the specified base_output):
    num_digits = math.floor(math.log(number_as_decimal, 2)) + 1
    converted_as_list = [0] * num_digits
    n = num_digits - 1
    total = 0
    for index in range(len(converted_as_list)):
        while total + converted_as_list[index] * base_of_output**n + base_of_output**n <= number_as_decimal:
            converted_as_list[index] += 1
        # Update total to include that digit:
        total += converted_as_list[index] * base_of_output**n
        # Decrement n (exponent) before we move to the right 1 place:
        n -= 1
    
    # If output base is hex, change decimals > 9 to the corresponding letters:
    if base_of_output == 16:
        converted_as_list = [DECIMAL_TO_HEX[digit] for digit in converted_as_list]
    
    # --> To string version: Concatenate the list digits together into the output number:
    converted_as_string = "".join([str(digit) for digit in converted_as_list])
    converted_as_string = converted_as_string.lstrip("0")
    # If output base is binary or hex, add appropriate prefix (0b or 0x):
    if base_of_output == 2:
        return "0b" + converted_as_string
    elif base_of_output == 10:
        return converted_as_string
    elif base_of_output == 16:
        return "0x" + converted_as_string
    
    return converted_as_string


if __name__ == "__main__":
    result = convert_number(number=252, base_of_input=10, base_of_output=16)
    print(result)
