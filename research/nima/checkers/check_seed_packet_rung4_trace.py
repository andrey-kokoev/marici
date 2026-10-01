"""Trace actual seed rows through the documented retained-total candidate.
Not an identification of this schedule with the confirmed transport diagram.
"""
from check_label_from_to_fibration_tower import original

seed = ('AB', 'BC', 'CA', 'AD', 'DB', 'BA')
initial = [(e, e[0], e[1]) for e in seed]
rows = initial[:]
trace = [(12, 'initial', 'AB', 6)]
for depth in range(8):
    column = depth % 3
    previous = rows
    rows = [(original(row, depth)[column], row) for row in previous]
    assert [row for key,row in rows] == previous
    assert [original(row, depth+1) for row in rows] == initial
    selected = next(row for row in rows if original(row,depth+1)[0] == 'AB')
    trace.append((11-depth, ('label','from','to')[column], selected[0], len(rows)))
# All endpoints and comparison incidence survive to the designated rung.
recovered = [original(row,8) for row in rows]
assert recovered == initial
assert sum(row[1] == 'A' for row in recovered) == 2
assert sum(row[2] == 'B' for row in recovered) == 2
# Equality of endpoint labels survives, but supplies no new physical readout.
def incidence(table):
    return {(a[0],b[0]) for a in table for b in table if a[2] == b[1]}
assert incidence(recovered) == incidence(initial)
assert ('AB','BC') in incidence(recovered)
assert ('AB','BA') in incidence(recovered)
for rung, field, key, count in trace:
    print(f'rung {rung}: field={field}, AB outer key={key}, retained seed rows={count}')
print('PASS: all six seed packets and all composable endpoint comparisons reconstruct at rung4.')
print('Scope: retained-record realization; no physical metric, particle identity or promotion derived.')
