"""Search-free check of single-hub versus tuple witnesses for the omitted-row pairing."""
rows = (1, 2, 4)                 # A, B, C
cols = (6, 5, 3)                 # BC, AC, AB
B = [[int(bool(r & c)) for c in cols] for r in rows]
M = [[1 - b for b in row] for row in B]
# One ordinary hub touching all endpoints induces their Cartesian product.
hub = [[1 for _ in cols] for _ in rows]
# Three tuple witnesses, represented by the two incidence projections.
tuples = [(r,c) for r in rows for c in cols if not r & c]
via_tuples = [[sum(r == x and c == y for x,y in tuples) for c in cols] for r in rows]
assert via_tuples == M and sum(map(sum,M)) == 3
assert sum(B[i][j]*hub[i][j] for i in range(3) for j in range(3)) == 6
# One hub can instead select the doubleton type; old nonincidence decodes the pairing.
marked = {c for c in range(1,8) if sum(bool(c&r) for r in rows)==2}
assert {(r,c) for r in rows for c in marked if not r & c} == set(tuples)
print('single hub:',hub,'tuple witnesses:',via_tuples,'selector decodes:',tuples)
