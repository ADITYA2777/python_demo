


cloud_serverices = ["aws","gcp","azure"]

try:
    print(cloud_serverices[1])
except:
     print("except handler is sloved")
finally:
     print("this code is run ")

     import builtins

cloud_envs = ["aws","azure","gcp"]

try:
    print(cloud_envs[200])
    raise Exception("This is a new exception")
except:
    print("exception handled")
finally:
    print("I will execute anyways")


print("This code should run")


try:
    print(cloud_envs[200])
    a = 10
    b = 0
    c = a/b
except ZeroDivisionError as e:
    print("1",e)
except IndexError as e:
    print("2",e)


print(dir(builtins))

# Trying to add an integer and a string
try:
    result = 5 + "hello"
except TypeError:
    print("TypeError: Cannot add int and str")


    # Trying to access a key that doesn't exist in a dictionary
try:
    my_dict = {'a': 1, 'b': 2}
    print(my_dict['c'])
except KeyError:
    print("KeyError: Key not found")

    # Trying to convert a string to an integer, but the string is not a valid integer
try:
    value = int("hello")
except ValueError:
    print("ValueError: Invalid literal for int()")




