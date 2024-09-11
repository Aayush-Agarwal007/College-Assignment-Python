def swap_case(string):
    
    swapped_string = string.swapcase()
    return swapped_string
user_input = input("Enter a string: ")
result = swap_case(user_input)
print("Swapped case string:", result)
