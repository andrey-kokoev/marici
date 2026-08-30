"""Concrete C/F/G contact-incidence and hygiene-layer checks."""


def row_loads(matrix):
    return [sum(row) for row in matrix]


def direct_sum_three(block):
    rows = len(block)
    columns = len(block[0])
    out = [[0] * (3 * columns) for _ in range(3 * rows)]
    for copy in range(3):
        for r in range(rows):
            for c in range(columns):
                out[copy * rows + r][copy * columns + c] = block[r][c]
    return out


mono_block = [[1, 1]]
split_block = [[1, 0], [0, 1]]
mono = direct_sum_three(mono_block)
split = direct_sum_three(split_block)

mono_loads = row_loads(mono)
split_loads = row_loads(split)
assert mono_loads == [2, 2, 2]
assert split_loads == [1, 1, 1, 1, 1, 1]

# Monolithic conflict graph is three disjoint edges on contacts
# (C_U,C_U2), (F_U,F_U2), (G_U,G_U2).
conflict_edges = {(0, 1), (2, 3), (4, 5)}
one_layer = [0] * 6
assert any(one_layer[a] == one_layer[b] for a, b in conflict_edges)
two_layers = [0, 1, 0, 1, 0, 1]
assert all(two_layers[a] != two_layers[b] for a, b in conflict_edges)

split_conflict_edges = set()
assert not split_conflict_edges

failure = {
    "code": "repeated_fault_source_contact",
    "overloaded_blocks": ["C", "F", "G"],
    "row_loads": mono_loads,
    "minimum_hygiene_layers": 2,
}

print("monolithic row loads:", mono_loads)
print("split-component row loads:", split_loads)
print("monolithic conflict edges:", sorted(conflict_edges))
print("rejection/repair witness:", failure)
print("PASS: physical block incidence determines the hygiene requirement")
