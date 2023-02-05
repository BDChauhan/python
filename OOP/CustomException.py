# class Error (Exception):
#     # print("Unknown Eror", Exception)
#     pass

# class ValueTooSmallError(Error):
#     pass
    
    
# class ValueTooLargeError(Error):
#     pass
    
# n = 45

# while True:
#     try:
#         print("Enter guessed number:")
#         guess = int(input())
#         if guess>n:
#             raise ValueTooSmallError
#         elif guess<n:
#             raise ValueTooLargeError
#         break
#     except ValueTooLargeError:
#         print("this value is too small\n")
#     except ValueTooSmallError:
#         print("this value is too large")
#         print()


##example 2

from decimal import DivisionByZero


class salaryNotInRangeError(Exception):
    def __init__(self,message="salary not in range 5000-25000"):
        self.message = message
        super().__init__(self.message)
        
    # def __str__(self):
    #     return ("This is from __str__")
    
# from distutils.errors import UnknownFileError


# class salaryNotInRangeError(Exception):
#     pass

try:
    s = int(input("Enter your salary:"))
    # if s not in range(5000,25000):
    #     raise salaryNotInRangeError

        
finally:
    print("finally block")