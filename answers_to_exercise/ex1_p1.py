# Exercise 1, Part 1
#
# starter code
class ColorPrinter:
    # Put these at the beginning and end of the content of your print statement
    _GREEN = '\033[92m'
    _RED = '\033[91m'
    _END = '\033[0m'

    def print(self, content: str, status: str = None):

        # WRITE YOUR CODE HERE.
        if status == "success":
            print(f"{self._GREEN}{content}{self._END}")
        elif status == "error":
            print(f"{self._RED}{content}{self._END}")
        else:
            print(content)
