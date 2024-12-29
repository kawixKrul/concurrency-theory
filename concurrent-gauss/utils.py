def parse_input(filename):
    with open(filename, 'r') as f:
        n = int(f.readline().strip())
        A = []
        for _ in range(n):
            row = list(map(lambda x: float(x.strip()), f.readline().split(' ')))
            A.append(row)
        b = list(map(lambda x: float(x.strip()), f.readline().split(' ')))
        return A, b

def write_result(filename, result):
    with open(filename, 'w') as f:
        n = len(result)
        f.write(str(n)+'\n')
        b = [row.pop() for row in result]
        for row in result:
            for x in row:
                f.write(str(x)+' ')
            f.write('\n')
        for x in b:
            f.write(str(x)+' ')      