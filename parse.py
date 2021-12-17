import re

def parse(txt) :
    # separators = re.compile(r'\^(-?\d*)([a-zA-Z])\^2 *([+-] *\d*)\2 *([+-] *\d+) *= *0$')
    separators = r'([\=\+\-\^\*])'
    x = re.split(separators, txt.replace(" ", ""))
    print(x, "\n")
    s1 = ""
    s2 = ""
    founderror = 0
    count = 0
    for i in range(len(x)) :
        if x[i] == "":
            print("error")
            founderror = 1
            return
        if x[i] == "=":
            count += 1
            if count == 2:
                return
    if (founderror == 0) :
        for i in range(len(x)) :
            if (count > 1) :
                break
            elif x[i] != "=" :
                s1 += x[i]
            else :
                j = i + 1
                count = count + 1
                for n in range(j,len(x)) :
                    s2 += x[n]
        print(s1, "\n")
        print(s2)

txt = "5 * X^0 - 6 * X^1 + 0 * X^2 - 5.6 * X^3 = 5"
parse(txt)
