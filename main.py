def PL_RESOLUTION(KB, alpha):
    clauses = KB.copy()
    clauses.add((alpha,))  # add negation of alpha to clauses
    while True:
        new = set()
        pairs = [(ci, cj) for ci in clauses for cj in clauses if ci != cj]
        for ci, cj in pairs:
            resolvents, check = resolve(ci, cj, clauses)
            if check == True:
                return True
            new.update(resolvents)
        print(len(new) + len(clauses))
        print(new)
        print(clauses)
        if new.issubset(clauses):
            return False
        clauses.update(new)


def check_valid(resolvent):
    for el1 in resolvent:
        for el2 in resolvent:
            if el1 == "~" or el2 == "~" + el1:
                return False
    return True

def check_in_clause(resolvent, clauses):
    for cl in clauses:
        if resolvent == set(cl):
            return False
    return True
        

def resolve(ci, cj, clauses):
    resolvents = set()
    for di in ci:
        for dj in cj:
            if di == "~" + dj or dj == "~" + di:  # check if literals are complementary
                resolvent = (set(ci) | set(cj)) - {di, dj}
                if not resolvent:  # check for empty clause
                    return (), True
                if check_valid(resolvent) == True and check_in_clause(set(tuple(resolvent)), clauses) == True and set(tuple(resolvent)) not in resolvents:
                    resolvents.add(tuple(resolvent))
    return resolvents, False

# Example knowledge base and query
KB = {('~A', 'B'), ('~C', 'B'), ('A', 'C', '~B'), ('~B',)}

alpha = "A"

# Check if KB entails alpha
result = PL_RESOLUTION(KB, alpha)

# Expected output: True
print(result)
