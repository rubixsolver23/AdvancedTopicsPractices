# Exceptions are how we handle errors created by users in a way that doesn't break the code
# zero division, file not found, value error, type error, index error can all be caught

class NegativeNumberError(Exception):
    pass

while 1:
    try:
        num = int(input("Tell me a number: "))
    except ValueError:
        print("BAD BAD BAD!!! BAD USER!!!!!!")
        continue
    else:
        break
            
while 1:
    try:
        numTwo = int(input("Tell me another one: "))
        if numTwo <= 0:
            raise NegativeNumberError("Cannot be a negative number")
    except ValueError:
        print("BAD BAD BAD!!! BAD USER!!!!!!")
        continue
    except NegativeNumberError as e:
        print(e)
    else:
        try:
            print(f"{num} divided by {numTwo} equals {num/numTwo}")
            break
        except ZeroDivisionError:
            print("You are actually stupid. You have literally 2 braincells and should stop using our intelectual program and go bang your head into a wall for a few years. Then you may come back to this after you have realized how much of an idiot you are and try again. You cannot divide by zero, you stupid dumb imbicile. You truly are dumb, you know. It's amazing how stupid somebody could possibly be and still be alive right now.")


    finally:
        print("Rate my program on the app store!!!1!!1!!11!")


