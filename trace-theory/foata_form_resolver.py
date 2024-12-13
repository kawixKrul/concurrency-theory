def resolve_identities(transactions) -> list[list]:
    I = [
        [entry_key, neighbour_key]
        for entry_key, left, right in transactions
        for neighbour_key, neighbour_left, neighbour_right in transactions
        if not (neighbour_left == left or left in neighbour_right or neighbour_left in right)
    ]
    return I


def resolve_dependencies(transactions) -> list[list]:
    D = [
        [entry_key, neighbour_key]
        for entry_key, left, right in transactions
        for neighbour_key, neighbour_left, neighbour_right in transactions
        if neighbour_left == left or left in neighbour_right or neighbour_left in right
    ]
    return D

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
    return ''.join(map(lambda f_class: f"({''.join(f_class)})", classes))