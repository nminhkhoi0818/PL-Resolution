from algo import PL_RESOLUTION

#Read input
def read_input():
    f = open("PL-Resolution\input.txt", "r")
    line = f.readline() #Get alpha
    alpha = ""
    for w in line.split():
        if w != "\n":
            alpha += w
    if alpha[0] == "-":
        alpha = alpha[1:]
    else:
        alpha = "-" + alpha
    num = f.readline()
    KB = set()
    while True:
        line = f.readline()
        if not line:
            break
        temp_list = []
        for w in line.split():
            if w != "OR":
                temp_list.append(w)
        KB.add(tuple(temp_list))
    result = PL_RESOLUTION(KB, str(alpha))
    print(result)
        
read_input()