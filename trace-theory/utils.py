import re

class TaskInputs:
    def __init__(self):
        self.alphabet = set()
        self.word = None
        self.transactions = []

    def validate(self) -> None:
        if not self.alphabet or self.word is None or not self.transactions:
            raise Exception("Invalid input or error while parsing input file")

def read_data(filename: str) -> TaskInputs:
    taskInputs = TaskInputs()
    with open(filename, 'r') as f:
        for line in f.readlines():
            if re.search(r":=", line):
                filtered_line = re.findall(r'[a-zA-Z]', line)
                name, result, dependecies = filtered_line[0], filtered_line[1], filtered_line[2:]
                taskInputs.transactions.append([name, result, dependecies])
            elif re.search(r"^A", line):
                taskInputs.alphabet.update(c for c in line[1:] if c.isalpha())
            elif re.search(r"^w", line):
                taskInputs.word = line.split('=')[1].strip()
    
    taskInputs.validate()
    taskInputs.transactions.sort()    
    return taskInputs