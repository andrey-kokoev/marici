"""Exact trial energy descent on nested Euclidean spaces R^12 -> ... -> R^4.

A rung retains coordinates 0..r-1. Removed coordinates become records.
The quadratic metric and energy conversion coefficient stay fixed.
This is a test tower, not a derivation of carrier restriction maps.
"""
from fractions import Fraction as F

TOP, FLOOR = 12, 4


def trace(c, indices):
    return sum((c[i][i] for i in indices), F(0))


def descent(c):
    total = trace(c, range(TOP))
    result = {}
    for r in range(TOP, FLOOR-1, -1):
        retained = trace(c, range(r))
        recorded = trace(c, range(r, TOP))
        assert retained+recorded == total
        if r < TOP:
            assert result[r+1][0]-retained == c[r][r]
        result[r] = (retained, recorded)
    return result


isotropic = [[F(i == j) for j in range(TOP)] for i in range(TOP)]
uniform = descent(isotropic)
for r in range(FLOOR, TOP+1):
    assert uniform[r][0]/TOP == F(r, TOP)
    if r > FLOOR:
        assert uniform[r-1][0]/uniform[r][0] == F(r-1, r)

# Positive semidefinite rank-one covariance: coherent, non-isotropic energy.
v = [F(i+1) for i in range(TOP)]
coherent = [[a*b for b in v] for a in v]
uneven = descent(coherent)
assert trace(coherent, range(TOP)) == 650
assert uneven[4][0] == 30
assert uneven[4][0]/650 == F(3, 65)
reversed_cov = [list(reversed(row)) for row in reversed(coherent)]
reverse = descent(reversed_cov)
assert reverse[4][0]/650 == F(223, 325)

# Rank-one states wholly inside the retained or discarded sector show bounds.
for index, expected in [(0, F(1)), (11, F(0))]:
    c = [[F(i == index and j == index) for j in range(TOP)] for i in range(TOP)]
    out = descent(c)
    assert out[4][0] == expected

print('r | isotropic retained/top | isotropic records/top | coherent retained/top')
for r in range(TOP, FLOOR-1, -1):
    print(f'{r:2} | {str(uniform[r][0]/TOP):>8} | '
          f'{str(uniform[r][1]/TOP):>8} | {uneven[r][0]/650}')
print('Reversing the coherent coordinate order changes E4/E12 from 3/65 to 223/325.')
print('Concentrated-state E4/E12 endpoints: 0 and 1.')
print('All nested projection and retained-plus-record conservation checks passed exactly.')
print('Linear r/12 descent requires equal diagonal energy in this basis; absolute energy is free.')
