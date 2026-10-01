"""Finite section-to-field promotion of labelled records.

For selected p:E->X, S=product_x Fiber(p,x). New rows are (sigma,x),
with evaluation sigma(x) in E. The selected field becomes sigma; the other
fields are read from the evaluated old row. Keep x as provenance.
Explicit successor rule, distinct from dependent-total reconstruction.
"""
from itertools import product
from math import prod


def promote(domains, rows, k):
    fibers = [[i for i, row in enumerate(rows) if row[k] == x] for x in domains[k]]
    sections = list(product(*fibers))
    new_domains = list(domains)
    new_domains[k] = tuple(sections)
    new_rows, provenance = [], []
    for sigma in sections:
        for index, x in enumerate(domains[k]):
            e = sigma[index]
            row = list(rows[e])
            row[k] = sigma
            new_rows.append(tuple(row))
            provenance.append((sigma, x, e))
    return tuple(new_domains), new_rows, provenance, fibers


tables = cases = erased = duplicated = 0
for nl, na, nb in product(range(3), repeat=3):
    domains = tuple(tuple(range(n)) for n in (nl, na, nb))
    endpoints = list(product(domains[1], domains[2]))
    for labels in product(range(-1, nl), repeat=len(endpoints)):
        rows = [(l,a,b) for (a,b),l in zip(endpoints,labels) if l >= 0]
        tables += 1
        for k in range(3):
            nd, nr, history, fibers = promote(domains, rows, k)
            cases += 1
            assert len(nd[k]) == prod(map(len, fibers))
            assert len(nr) == len(domains[k])*len(nd[k])
            for row, (sigma,x,e) in zip(nr,history):
                assert rows[e][k] == x and row[k] == sigma
                assert all(row[j] == rows[e][j] for j in range(3) if j != k)
            for e, row in enumerate(rows):
                pos = domains[k].index(row[k])
                multiplicity = prod(len(f) for j,f in enumerate(fibers) if j != pos)
                assert sum(item[2] == e for item in history) == multiplicity
            erased += bool(rows) and not nr
            duplicated += len(nr) > len(rows)
assert (tables,cases) == (147,441)
# A singleton-fiber table supports all eight successive promotions with recovery.
domains = ((0,1),(0,1),(0,1))
rows = [(0,0,0),(1,1,1)]
counts = []
for depth in range(8):
    domains, rows, history, fibers = promote(domains,rows,depth%3)
    assert len(rows) == 2
    assert sorted(e for _,_,e in history) == [0,1]
    counts.append(len(domains[depth%3]))
# Empty fiber prevents any section even when some records exist.
_, empty, _, _ = promote(((0,),(0,1),(0,1)),[(0,0,0),(0,0,1)],1)
assert not empty
# Balanced two-element fibers: 4 sections, 8 evaluations from 4 original rows.
_, enlarged, _, _ = promote(((0,1),(0,1),(0,1)),
                            [(0,0,0),(0,0,1),(1,1,0),(1,1,1)],0)
assert len(enlarged) == 8
print(f'{tables} tables; {cases} section-promotion checks passed.')
print(f'Nonempty inputs erased by empty fibers: {erased}; row-expanding cases: {duplicated}.')
print('Eight-step cyclic singleton-fiber example: row counts remain 2; each evaluated old row recovered once.')
print('Two fibers of size2: 4 section values and 8 evaluation rows from 4 old rows.')
print('Field type promotion is explicit; universal row equivalence and universal doubling do not hold.')
