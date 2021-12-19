import sys
import equation_solution

#9ADI REDUCED FOOORM

#function to check coef error get the coef
def check_coef_error(subgroups) : # a * x^p

    i = 1
    coef = subgroups[0]
    is_float = False
    while i < len(subgroups) and subgroups[i] != "*" :
        if subgroups[i].isdigit() or (subgroups[i] == '.' and is_float == False) :
            coef += subgroups[i]
            if (subgroups[i] == '.') :
                is_float = True
        else :
            print('\u001b[31m' + "ERROR : You must enter a number for coefficient")
            exit()
        i += 1
    if (i + 3 >= len(subgroups) or subgroups[i] != '*' or (subgroups[i + 1] != 'X'
    and subgroups[i + 1] != 'x') or subgroups[i + 2] != '^'):
        print('\u001b[31m' + "ERRO : Incorrect format. You must respect the form 'd * x^n'")
        exit()
    return float(coef)

#function to check power error and get pow
def check_pow_error(subgroups) :
    i = 0
    pow = ""
    is_float = False
    while i < len(subgroups) and subgroups[i] != "^":
        i += 1
    if subgroups[i + 1] == "-" or subgroups[i + 1] == "+":
        pow = subgroups[i + 1]
        i += 2
    else:
        i +=1
    if (i >= len(subgroups)):
        print('\u001b[31m' + "ERRO : Incorrect format. You must respect the form 'd * x^n'")
        exit()
    while i < len(subgroups) :
        if subgroups[i].isdigit() or (subgroups[i] == '.' and is_float == False) :
            pow += subgroups[i]
            if (subgroups[i] == '.') :
                is_float = True
        else :
            print('\u001b[31m' + "ERROR : You must enter a number for power")
            exit()
        i += 1
    return float(pow)

#handle some errors in right and left pairs
def error_handler(pair) :
    i = 0
    while i + 1  < len(pair) :
        if ((pair[i] == "-" or pair[i] == "+" or pair[i] == "*" or (pair[i] == "^" and pair[i + 1] == "*")) and
        (pair[i + 1] == "-" or pair[i + 1] == "+" or pair[i + 1] == "*" or pair[i + 1] == "^")) :
            print('\u001b[31m' + "ERROR : Syntax error. Double sign")
            exit()
        i += 1

#add + in at start
def add_sign(pair) :
    for i in range(len(pair)) :
        if pair[0] != "-" and pair[0] != "+" and pair[1].isdigit() :
            pair = "+" + pair
    return(pair)

#spliting left and right pairs by + - ^
def sign_split(pair) :

    subGroups_lst = []
    subGroups = pair[0]
    i = 1
    while i < len(pair) :
        if (pair[i] != "-" and pair[i] != "+") or pair[i - 1] == '^' :
            subGroups += pair[i]
        else :
            subGroups_lst.append(subGroups)
            subGroups = pair[i]
        i += 1
    subGroups_lst.append(subGroups)
    return(subGroups_lst)

#split by - and + then get the coef
def get_coef(pair) :

    subGroups_lst = []
    subGroups_lst = sign_split(pair)
    i = 0
    coef_lst = []
    while i < len(subGroups_lst) :
        coef_lst.append(check_coef_error(subGroups_lst[i]))
        i += 1
    return(coef_lst)

#split by - and + then get the power
def get_pow(pair) :

    subGroups_lst = []
    subGroups_lst = sign_split(pair)
    i = 0
    pow_lst = []
    while i < len(subGroups_lst) :
        pow_lst.append(check_pow_error(subGroups_lst[i]))
        i += 1
    return(pow_lst)

def coef_power(right_pair, left_pair) :

    left_coef_lst = []
    left_coef_lst = get_coef(left_pair)

    #move left pair to right changing the sign of coefficient
    i = 0
    while i < len(left_coef_lst) :
        left_coef_lst[i] *= -1
        i += 1
    coef_list = get_coef(right_pair) + left_coef_lst
    pow_list = get_pow(right_pair) + get_pow(left_pair)
    return coef_list, pow_list

def find_in_list(my_list, power):
    for i in range(len(my_list)):
        if (my_list[i][1] == power):
            return i
    return -1

def sort_func(elem): #(coef,power)
    return elem[1] #returns the subelement in position 1 which is power

def merge_lists(coef, power):

    if len(coef) != len(power):
        print("Unknowen Error. merg lists")
        exit()
    merged_list = [(0,2), (0,1), (0,0)] # (coef, power)
    for i in range(len(coef)):
        index = find_in_list(merged_list, power[i])
        if index == -1:
            merged_list.append((coef[i],power[i]))
        else:
            merged_list[index] = (coef[i] + merged_list[index][0], merged_list[index][1])

    merged_list.sort(key=sort_func, reverse=True) #sort passes element by element to sort_func
                                                  #that returns second position of the element which is power
    return merged_list
   
def print_polynomial_degree(list):

    if list[0][0] != 0: print(' \u001b[35m' + "\nPolynomial degree: 2")
    elif list[1][0] != 0: print(' \u001b[35m' + "\nPolynomial degree: 1")
    elif list[2][0] == 0:
        print(' \u001b[36m' + "Each real number is a solution")
        exit()
    else:
        print(' \u001b[35m' + "Equation has no solution")
        exit()
    return list[0][0],list[1][0],list[2][0]

def reduced_form(a,b,c) :
    str_a = str_b = str_c = ""
    if a != 0: str_a = str(a) + "X^2"
    if b != 0: str_b = str(b) + "X"
    if c != 0: str_c = str(c)
    print(' \u001b[34m')
    print("\nRedueced form:",str_a,str_b,str_c)

def parse(txt) :

    #split by =
    equation_pairs = txt.replace(" ", "").split("=")

    #error handler if there is more than one =
    if len(equation_pairs) != 2 or equation_pairs[0] == "" or equation_pairs[1] == "" :
        print('\u001b[31m' + "ERROR : Invalid equation")
        exit()

    #get right and left of =
    right_pair = equation_pairs[0]
    left_pair = equation_pairs[1]

    #error handler
    error_handler(right_pair)
    error_handler(left_pair)

    #add + and - signs
    right_pair = add_sign(right_pair)
    left_pair = add_sign(left_pair)

    #get coefficient list and power list
    coef_power(right_pair, left_pair)

    coef , power = coef_power(right_pair, left_pair)
    list_power_coef = merge_lists(coef, power)

    for element in list_power_coef[:] :
        if (element[1] > 2 or element[1] < 0):
            if (element[0] != 0) :
                print(' \u001b[35m')
                print("\nPolynomial degree: ", element[1])
                print("The polynomial degree is strictly greater than 2, I can't solve.")
                exit()
            else :
                list_power_coef.remove(element)
    
    a,b,c = print_polynomial_degree(list_power_coef)
    reduced_form(a,b,c)
    equation_solution.solution(a,b,c)



if (len(sys.argv) != 2):
    print('\u001b[33m' + 'ERROR: You must enter 3 arguments')
    exit()

try:
    parse(sys.argv[1])  
except:
    print('\u001b[33m' + "ERROR: Plz enter a valid equation(a * x^p)")

# a ∗ x^p