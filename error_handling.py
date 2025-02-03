# abnormal termination 
# gracefull termination

# try except (syntex of error handling)

num1 : int = 10
num2 : int = 0

result = num1 / num2
print(result)
# general 
# try:
#     result = num1 / num2
#     print(result)

# except Exception as e:
#     print(e)

# types of error
# zero divison 
# key
# index
# value
# import

list = ["ali", "abdullah"]
try:
    result = num1 / num2
    print(result)
except IndexError:
    print("this is error with index")
except ZeroDivisionError:
    print("this is error for zero value")