from foata_form_resolver import depends_on

class Edge:
    def __init__(self, source, target):
        self.source = source
        self.target = target
    
    def __str__(self):
        return f"{self.source.index} -> {self.target.index};"

class Node:
    def __init__(self, value, index):
        self.value = value
        self.index = index
        self.edges = []

    def append(self, node) -> None:
        self.edges.append(node)

    def is_connected(self, node, D) -> bool:
        return any(depends_on(D, node.value, edge.value) for edge in self.edges)
    
    def __str__(self):
        return f"{self.index} [label={self.value}]"
    
def create_graph_vis_file(foata_form, D, out_file) -> None:
    word = [item for sublist in foata_form for item in sublist]
    nodes = [Node(w, i) for i, w in enumerate(word)]
    previous = []
    edges = []
    for n in nodes:
        for prev in previous:
            if depends_on(D, n.value, prev.value) and not n.is_connected(prev, D):
                n.append(prev)
                edges.append(Edge(prev, n))
        previous.insert(0, n)

    with open(f'{out_file}.dot', 'w') as file:
        file.write("digraph G {\n")
        cons = "\n  ".join(str(e) for e in edges)
        file.write(cons + "\n")
        labels = ";\n  ".join(str(n) for n in nodes)
        file.write(f"  {labels};\n}}")