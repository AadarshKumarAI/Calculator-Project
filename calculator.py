print("===Welcome to Calculator===")
print("You write simple arguments : for example, ")
print("3 * 3 and calculator gives you your andswer for example 9")
print("Here is simple rule,\nYou write here 2 numbers like (1, 2) and before it you write what do you want for example sum(2, 4), substract(3, 5), etc.")
def sum(a, b):
    return(a + b)
def substract(a, b):
    return(a - b)
def multiply(a, b):
    return(a * b)
def devide(a, b):
    return(a / b)
def power(a, b):
    return(a ** b)
def give_remidnder(a, b):
    return(a // b)
print("You can sumply give instruction to this calculator add like :- \nsum(a + b) there a and b are variables\n substact(a, b) it returns a =b, hou can simpy give any number")
print("You can do any applications")
try: 
    a = input("Enter what you want")
    print(a)ba
except:
    print("give a valid argument.")

