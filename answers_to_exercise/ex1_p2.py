# Exercise 1, Part 2

# --------
# Contents below would be found in a module color_printer.py, or similar.
# This is a case when a module containing related functions may be preferred
# over a class.

#   - A function's local variables can't be accessed directly like in classes
#   - The properties of our ColorPrinter class don't need to be stateful,
#     i.e. changes to their values don't need to be remembered between uses,
#     because we don't expect them to be changed.
#   - Any memory used during the execution of a function will be cleared
#     upon its termination, making memory leaks less likely
# --------


# Don't want naming conflict with built-in print fct
def printc(content: str, status: str):
    # Color encodings
    _GREEN = '\033[92m'
    _RED = '\033[91m'
    _END = '\033[0m'

    # control flow
    if status == "success":
        print(f"{_GREEN}{content}{_END}")
    elif status == "error":
        print(f"{_RED}{content}{_END}")
    else:
        print(content)



