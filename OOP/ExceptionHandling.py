# Errors - compile time (syntactical errors) - logical (wrong output - error in logic of code) - run time (code gets compile correctly, occurs due to wrong input mostly - not working for specific input)
# execution stops when runtime error occurs

# in real time practice, if we open any file and exception occurs, then we should close it also...same with the database





try:
    a = int(input())
    print("res opened")
    b = int(input())
    print(b)
    print(a/b)
# except Exception as e:
#     print(e)
#     print("attempt to divide by zero!!")
except ZeroDivisionError as e:
    print("attempt to divide by zero!!\n",e)
    
except ValueError as e:
    print("value error!!\n",e)
    
except Exception as e:
    print("unknown error!\n", e)
finally:
    print("res closed (inside finally block)")

# here Exception is on top of all exception, there are specific exceptions as well