a = 10
class NotException(Exception):
    def __init__(self, message="A custom error occurred."):
        self.message = message
        # super().__init__(self.message)

try:
    if a == 10:
        raise NotException("Value of 'a' is equal to 10.")
except NotException as e:
    print(e)
