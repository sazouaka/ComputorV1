import re

# I GOT THE COEF NOW I NEED TO GET THE POWER



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

    # line = "-15*x^0-6*X^1+0*X^2-5.6*X^1"
    # d = "-"
    # s1 =  [d+e for e in line.split(d) if e]
    # print(s1)

    # for i in range(len(s1)) :
    #     for j in range(len(s1[i])) :
    #         if s1[i][j] == "+" :
    #             plus_found = 1
    #         else :
    #             plus_found = 0
    #     if plus_found == 1 :
    #         print("found")


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


    
    
    # right_subGroups =  right_pair.split("- | +")
    # print("right_subGroup : ", right_subGroups,"\n")
    
    # left_subGroups =  re.split(r'([\+\-])', left_pair)
    # print("left_subGroup : ", left_subGroups,"\n")

    # coef_lst = []
    # pow_lst = []
    # i = 0
    # while i < len(right_subGroups) :
    #     j = 0
    #     while j < len(right_subGroups[i]) :
    #         if (right_subGroups[i][j] == "^") :
    #             coef_lst += right_subGroups[i].split("*")
    #             pow_lst += right_subGroups[i][j + 1]
    #         j += 1
    #     i += 1


txt = "-15 * x^0  - 6 * X^1 + 0 * X^2 - 5.6 * X^1 = 9 * X^0"
parse(txt)
