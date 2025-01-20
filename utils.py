#Utility

def random_list(size,lower,upper):
    import random
    arr = []
    for i in range(size):
        num = random.randint(lower,upper)
        arr.append(num)

def validate_input(input_str):
    try:
        value = int(input_str)
        if value <= 0:
            raise ValueError("Input must be a positive integer.")
        return value
    except ValueError:
        raise ValueError


def print_list(lst):
    string_elements = []
    for element in lst:
        string_elements.append(str(element))
    formatted_string = ", ".join(string_elements)
    
    result = f"List: {formatted_string}"
    return result
