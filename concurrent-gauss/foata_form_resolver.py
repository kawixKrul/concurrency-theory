def depends_on(D, a, b) -> bool:
    return any(dep[0] == a and dep[1] == b for dep in D)

def resolve_foata_GH_method(word, D, alphabet) -> list[list]:
        stacks = {c: [] for c in alphabet}
        foata_form = []
        for w in word:
            stacks[w].append(w)
            for a in alphabet:  
                if depends_on(D, w, a) and a != w:
                    stacks[a].append('*')
                
        for key in stacks.keys():
            stacks[key].reverse()
        #print(stacks)

        while any(stacks.values()):  
            #print(stacks)
            step = []
            for key in stacks.keys():
                if stacks[key] and stacks[key][-1] != '*':
                    step.append(stacks[key][-1])
            
            step.sort()
            foata_form.append(step)
            for letter in step:
                stacks[letter].pop()  
                for a in alphabet:
                    if depends_on(D, letter, a) and letter != a and stacks[a] and stacks[a][-1] == '*':
                        stacks[a].pop()

        return foata_form

def pretty_foata_string(classes) -> str:
    return ''.join(map(lambda f_class: f"({', '.join(f_class)})", classes))

def alphabet(T):
    res = []
    for arr in T:
        res.extend(arr)
    return res

def transactions(n):
    T = []
    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            transaction = []
            transaction.append(f"A{i}{j}")
            for k in range(1, n + 2):
                if k >= i:
                    transaction.append(f"B{i}{k}{j}")
                    transaction.append(f"C{i}{k}{j}")
            T.append(transaction)
    return T


def resolve_dependencies(S):
    D = []
    for x in S:
        for y in S:
            if x[0] == "A" and y[0] == "C":
                if x[1:] == y[2:]:
                    D.append((x, y))
                    D.append((y, x))
                if x[1] == y[2] == y[3]:
                    D.append((x, y))
                    D.append((y, x))
            if x[0] ==  "A" and y[0] == "B":
                if x[1] == y[1] and x[2] == y[3]:
                    D.append((x, y))
                    D.append((y, x))
            if x[0] ==  "B" and y[0] == "C":
                if x[1] == y[3] and x[2] == y[2]:
                    D.append((x, y))
                    D.append((y, x))
                if x[1:] == y[1:]:
                    D.append((x, y))
                    D.append((y, x))
            if x[0] == "C" and y[0] == "C":
                if x[2:] == y[2:]:
                    D.append((x, y))
                    D.append((y, x))
    return D
