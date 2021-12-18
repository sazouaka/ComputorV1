import re

# I GOT THE COEF NOW I NEED TO GET THE POWER


#function to get the coef
def check_syntax_error(right_subgroups_str) :

    i = 1
    coef = ""
    is_float = False
    while i < len(right_subgroups_str) and right_subgroups_str[i] != "*":
        if right_subgroups_str[i].isdigit() or (right_subgroups_str[i] == '.' and is_float == False) :
            coef += right_subgroups_str[i]
            if (right_subgroups_str[i] == '.') :
                is_float = True
        else :
            print(right_subgroups_str[i])
            print("error")
            return
        i += 1
    return float(coef)

def parse(txt) :

    #split by =
    equation_pairs = txt.replace(" ", "").split("=")

    #error handler
    if len(equation_pairs) != 2:
        print("error")
        return

    #get right and left of =
    right_pair = equation_pairs[0]
    left_pair = equation_pairs[1]

    #error handler
    for i in range(len(right_pair)) :
        if ((right_pair[i] == "-" or right_pair[i] == "+" or right_pair[i] == "*" or right_pair[i] == "^") and
        (right_pair[i + 1] == "-" or right_pair[i + 1] == "+" or right_pair[i + 1] == "*" or right_pair[i + 1] == "^")) :
            print("error")
            return
    for i in range(len(left_pair)) :
        if ((left_pair[i] == "-" or left_pair[i] == "+" or left_pair[i] == "*" or left_pair[i] == "^") and
        (left_pair[i + 1] == "-" or left_pair[i + 1] == "+" or left_pair[i + 1] == "*" or left_pair[i + 1] == "^")) :
            print("error")
            return
    print("\n")
    print("right pair : ", right_pair,"\n" + "left pair  : ",  left_pair,"\n")

    #add + in at start
    for i in range(len(right_pair)) :
        if right_pair[0] != "-" and right_pair[0] != "+" :
            right_pair = "+" + right_pair

    #split by - and + then get the coef
    i = 1
    right_subGroups_lst = []
    right_subGroups = right_pair[0]
    while i < len(right_pair) :
        if (right_pair[i] != "-" and right_pair[i] != "+") :
            right_subGroups += right_pair[i]
        else :
            right_subGroups_lst.append(right_subGroups)
            right_subGroups = right_pair[i]
        i += 1
    right_subGroups_lst.append(right_subGroups)
    i = 0
    coef_lst = []
    while i < len(right_subGroups_lst) :
        coef_lst.append(check_syntax_error(right_subGroups_lst[i]))
        i += 1
    print(coef_lst)


txt = "-15 * x^0  - 6 * X^1 + 0 * X^2 - 5.6 * X^1 = 9 * X^0"
parse(txt)
