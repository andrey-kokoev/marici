"""Finite set model of retained label/from/to cyclic fibration.

Each step fibers the current rows by the selected inherited field and keeps
its dependent total (key, current_row) for the next step. This explicitly
chooses the successor presentation; it does not equate total rows with sections.
Tests all endpoint-unique tables on label/source/target sets of sizes 0..2.
"""
from itertools import product

names = ('label', 'from', 'to')
tables = 0
steps = 0


def original(row, depth):
    for _ in range(depth):
        row = row[1]
    return row


for nl, ns, nt in product(range(3), repeat=3):
    domains = (range(nl), range(ns), range(nt))
    endpoints = list(product(range(ns), range(nt)))
    for assignment in product(range(-1, nl), repeat=len(endpoints)):
        initial = [(label, a, b) for (a, b), label in zip(endpoints, assignment) if label >= 0]
        current = initial[:]
        tables += 1
        history = []
        for depth in range(8):
            column = depth % 3
            family = {key: [] for key in domains[column]}
            for row in current:
                family[original(row, depth)[column]].append(row)
            successor = [(key, row) for key, fiber in family.items() for row in fiber]
            assert len(successor) == len(initial)
            assert {row for key, row in successor} == set(current)
            for key, row in successor:
                assert original(row, depth)[column] == key
            assert {original(row, depth+1) for row in successor} == set(initial)
            history.append(names[column])
            current = successor
            steps += 1
        assert history == ['label','from','to','label','from','to','label','from']
assert tables == 147 and steps == 1176

# Sections differ from total rows even for endpoint-unique tables.
# One label, two rows: fibering by source over {0,1} has fiber sizes [2,0].
example = [(0,0,0),(0,0,1)]
fiber_sizes = [sum(row[1] == a for row in example) for a in range(2)]
assert sum(fiber_sizes) == 2
sections = 1
for size in fiber_sizes:
    sections *= size
assert sections == 0
print(f'{tables} tables, {steps} cyclic fibration steps: field-preserving reconstruction passed.')
print('Every dependent total retains the original row cardinality; selected-field provenance is explicit.')
print('Nine rung presentations require eight transitions from the initial rung12 table.')
print('Control: two total rows can have zero sections. Sigma-total cannot be replaced by Pi-sections.')
print('No 1,2,4 multiplicity follows from row cardinality in this retained-total recurrence.')
