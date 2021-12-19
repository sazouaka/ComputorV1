import re
import sys

def sqrt(x):
    return x**0.5
    
def solution(a, b, c) :
    if a == 0 and b == 0 :
        if c == 0 :
            print(' \u001b[36m' + "\nEach real number is a solution\n")
            return
        else :
            print(' \u001b[35m' + "\nEquation has no solution\n")
            return
    elif a == 0 and b != 0 :
        print('\u001b[32m')
        print("\nThe solution is:\n")
        print((-c) / (b), "\n")
        return
    else :
        delta = b ** 2 - 4 * a * c

    if delta < 0 :
        x1 = ((-b) / (2 * a))
        y1 = (sqrt(-delta) / (2 * a))
        print(' \u001b[36m' + "\nDiscriminant is strictly negative, there is two complexe solutions:\n")
        if x1 == 0 :
            print('\u001b[32m')
            print("+",y1,"* i", "\n")
            print("-",y1,"* i", "\n")
            return
        else :
            print('\u001b[32m')
            print(x1, "+", y1,"* i", "\n")
            print(x1, "-", y1,"* i", "\n")
            return

    elif delta == 0 :
        x = (-b) / (2 * a)
        print(' \u001b[36m' + "\nDiscriminant is equal to zero, there is one solution: ",  x, "\n")
        return

    else :
        x1 = ((-b) - sqrt(delta)) / (2 * a)
        x2 = ((-b) + sqrt(delta)) / (2 * a)
        print(' \u001b[36m' + "\nDiscriminant is strictly positive, there are two solutions:\n")
        print('\u001b[32m')
        print("first solution: ", x1 , "\n")
        print("seconde solution: ",x2 , "\n")
        return
