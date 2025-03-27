import math



def factorial(x):


    if x == 0 or x == 1:
        return 1

    else:

        return x * factorial(x - 1)

num = int(input("enter a number to calculate factorial: "))
print("factorial of " + num.__str__() + " = " + factorial(num).__str__())





sineFunction = lambda x, n: ((-1) ** n) * (x ** (2 * n + 1)) / factorial(2 * n + 1)

print(sineFunction(1,12))


def sine_x(x, n):
    radianx = math.radians(x)
    if n == 0:
        return 0
    else:
        return sineFunction(radianx, n - 1) + sine_x(x, n - 1)



x = float(input("enter the angle as degree: "))
n = float(input("enter the number of terms: "))
result = sine_x(x, n)
print("sine of " + x.__str__()+ " with terms " + n.__str__()  + " is = " + result.__str__())

keke = 0;

def overone(numberToCalculate):

    ''' it takes number from user and add it to global variable keke with calculation 1/numberToCalculate and then
     it call own recursive function with -1 to calculate every number between numberToCalculate and 0 and when it comes to 0
     it ends the function'''

    global keke
    if numberToCalculate == 0:
        return
    else:
            keke += 1/numberToCalculate
            overone(numberToCalculate - 1)

overone(4)
print(keke)

