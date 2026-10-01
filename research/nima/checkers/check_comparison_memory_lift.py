"""Exact reversible memory lift of the existing comparison projections.

One scalar record per comparison; standard library only. The lift preserves
weighted squared norm. Its record variables are not assumed to be momenta.
"""
from fractions import Fraction as F
from pathlib import Path
import runpy

source = runpy.run_path(str(Path(__file__).with_name('check_comparison_energy_spectrum.py')))
rows = source['rows']


def dot(a, b):
    return sum(x*y for x, y in zip(a, b))


def lift(q, z, r):
    n = dot(r, r)
    mismatch = dot(r, q)/n
    return [x + t*(z-mismatch) for x, t in zip(q, r)], mismatch


def total(q, records):
    return dot(q, q) + sum(dot(r, r)*z*z for r, z in zip(rows, records))


q0 = list(map(F, [1, -2, 0, 1, 3, -1]))
q = q0[:]
records = [F(0)]*len(rows)
initial = total(q, records)
projected = q0[:]
for i, r in enumerate(rows):
    before = q[:], records[i]
    q, records[i] = lift(q, records[i], r)
    assert lift(q, records[i], r) == before  # same operation is inverse
    assert dot(r, q) == 0  # initially empty record enforces comparison
    assert total(q, records) == initial
    mismatch = dot(r, projected)/dot(r, r)
    projected = [x-t*mismatch for x, t in zip(projected, r)]
    assert q == projected
assert any(records)
assert initial-dot(q, q) == sum(dot(r, r)*z*z for r, z in zip(rows, records))
for i in reversed(range(len(rows))):
    q, records[i] = lift(q, records[i], rows[i])
assert q == q0 and records == [0]*len(rows)

# A populated record returns its old mismatch to the carrier on reuse.
r = rows[0]
z = F(2, 3)
q1, z1 = lift(q0, z, r)
assert dot(r, q1) == dot(r, r)*z
assert dot(q1, q1)+dot(r, r)*z1*z1 == dot(q0, q0)+dot(r, r)*z*z
print('153 projections reproduced exactly using initially empty records.')
print('Discarded squared norm equals stored record budget exactly.')
print('Reverse sweep restores carrier and clears every record exactly.')
print('Reused records return previous mismatch; a full lift has memory feedback.')
print('Record storage supplies reversibility, not a canonical momentum or clock.')
