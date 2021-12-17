import sys

def sqrt(x):
    return x**0.5
    
def solution(a, b, c) :
    if a == 0 and b == 0 :
        if c == 0 :
            print("\nEach real number is a solution\n")
        else :
            print("\nThere is no solution\n")
    elif a == 0 and b != 0 :
        print("\nPolynomial degree: 1\n The solution is:\n")
        print((-c) / (b), "\n")
        return
    else :
        delta = b ** 2 - 4 * a * c

    if delta < 0 :
        x1 = ((-b) / (2 * a))
        y1 = (sqrt(-delta) / (2 * a))
        print("\nDiscriminant is strictly negative, there is two complexe solutions:\n")
        if x1 == 0 :
            print("+",y1,"* i", "\n")
            print("-",y1,"* i", "\n")
        else :
            print(x1, "+", y1,"* i", "\n")
            print(x1, "-", y1,"* i", "\n")

    elif delta == 0 :
        x = (-b) / (2 * a)
        print("\nDiscriminant is equal to zero, there is one solution:\n")
        print(x, "\n")

    else :
        x1 = ((-b) - sqrt(delta)) / (2 * a)
        x2 = ((-b) + sqrt(delta)) / (2 * a)
        print("\nDiscriminant is strictly positive, there are two solutions:\n")
        print("first solution: ")
        print(x1 , "\n")
        print("seconde solution: ")
        print(x2 , "\n")

a = float(sys.argv[1])
b = float(sys.argv[2])
c = float(sys.argv[3])

solution(a, b, c)
