# Exercise 1, Extra Credit

# Create a class whose "public" attributes are the options for statuses
class PrintStatus:
    def __init__(self):
        self._GREEN = '\033[92m'
        self._RED = '\033[91m'
        self._END = '\033[0m'

        self.SUCCESS = self._GREEN
        self.ERROR = self._RED


class ColorPrinter:
    def __init__(self):
        # make an instance of PrintStatus a class attribute. This allows
        # us to retrieve a PrintStatus object directly from a ColorPrinter instance.
        self.PRINT_STATUS = PrintStatus()

    def print(self, content: str, status: str = None):
        # input validation for status parameter
        assert status in self.PRINT_STATUS.__dict__.values(), \
            "status must be an option from self.PRINT_STATUS"

        if status:
            print(f"{status}{content}{self.PRINT_STATUS._END}")
        else:
            print(content)
