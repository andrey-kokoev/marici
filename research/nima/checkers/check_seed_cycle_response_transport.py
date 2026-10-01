"""Seed permutation response through the existing retained rung candidates.
No claim selecting these candidates or a physical observation metric.
"""
from fractions import Fraction as F
from pathlib import Path
from itertools import permutations
import runpy

old=runpy.run_path(str(Path(__file__).with_name('check_rung_transport_diagram.py')))
Row,Reference=old['Row'],old['Reference']
indexed,unindex=old['indexed'],old['unindex']
promote,leaves,read=old['incoming_promotion'],old['leaves'],old['read_at_four']


def compose(p,q):
    return tuple(p[q[i]] for i in range(4))


def matrix(p):
    return tuple(tuple(F(p[j]==i) for j in range(4)) for i in range(4))


def subtract(a,b):
    return tuple(tuple(x-y for x,y in zip(r,s)) for r,s in zip(a,b))


# Existing seed cycles ABC and ADB, with vertices A,B,C,D = 0,1,2,3.
g=(1,2,0,3)
h=(3,0,2,1)
left=compose(h,g)   # ABC then ADB
right=compose(g,h)  # ADB then ABC
assert left!=right
L,R=matrix(left),matrix(right)
defect=subtract(L,R)
assert sum(x*x for row in defect for x in row)==8
assert all(sum(row)==0 for row in defect)
assert all(sum(defect[i][j] for i in range(4))==0 for j in range(4))
# Represent one operator faithfully as its four labelled column contributions.
# Uniform mean of four rows reconstructs L: factor four is an encoding correction.
source=tuple(Row(('column',j,('ABC','ADB'),('ADB','ABC')),('input',j),('operator',0),
                 tuple(tuple(4*L[i][k] if k==j else F(0) for k in range(4))
                       for i in range(4)),
                 members=()) for j in range(4))
reference=Reference(4,R)  # Direct order-comparison diagnostic only.
assert old['mean'](source)==L
# Second preparation uses precisely the same column encoding and port policy.
other_source=tuple(Row(('column',j,('ADB','ABC'),('ABC','ADB')),('input',j),('operator',0),
                       tuple(tuple(4*R[i][k] if k==j else F(0) for k in range(4))
                             for i in range(4))) for j in range(4))
identity=matrix(tuple(range(4)))
fixed=Reference(4,tuple(tuple(2*x for x in row) for row in identity))
assert old['mean'](other_source)==R
for policy in ('inherited','common'):
    def t9(rows):
        return promote(promote(rows,1,policy),2,policy)
    left11=indexed(source,'source')
    left10=indexed(unindex(left11),'target')
    right6=t9(source)
    right5=indexed(right6,'source')
    right4=indexed(unindex(right5),'target')
    via_left=indexed(t9(unindex(left10)),'target')
    assert via_left==right4
    assert indexed(t9(unindex(left11)),'source')==right5
    assert leaves(unindex(right4))==source
    assert read(right4,reference)==defect
    assert read(indexed(source,'target'),reference)==defect
    other4=indexed(t9(other_source),'target')
    assert leaves(unindex(other4))==other_source
    # Both preparations see ONE fixed reference, with no reference retuning.
    residual_left=read(right4,fixed)
    residual_right=read(other4,fixed)
    assert residual_left==subtract(L,fixed.value)
    assert residual_right==subtract(R,fixed.value)
    assert subtract(residual_left,residual_right)==defect
    # Same trace and norm do not distinguish these two responses.
    assert sum(residual_left[i][i] for i in range(4))==sum(residual_right[i][i] for i in range(4))
    assert sum(x*x for row in residual_left for x in row)==sum(x*x for row in residual_right for x in row)
    # Named state preparation/readout distinguishes them: input A, output A.
    assert residual_left[0][0]-residual_right[0][0]==1
    # Normalized common-state measurement cannot see the contrast defect.
    assert sum(sum(row) for row in defect)==0
    # The matched-order control gives zero, without fitting any coefficient.
    assert read(right4,Reference(4,L))==tuple((F(0),)*4 for _ in range(4))
# Transport both actions AND the named probe under every carrier relabelling.
for p in permutations(range(4)):
    pinv=tuple(p.index(i) for i in range(4))
    gp=compose(compose(p,g),pinv)
    hp=compose(compose(p,h),pinv)
    moved=subtract(matrix(compose(hp,gp)),matrix(compose(gp,hp)))
    assert moved==tuple(tuple(defect[pinv[i]][pinv[j]] for j in range(4)) for i in range(4))
    assert moved[p[0]][p[0]]==1
# Source-selection control: preserve the actual directed seed, not arbitrary K4.
seed={(0,1),(1,2),(2,0),(0,3),(3,1),(1,0)}
autos=[p for p in permutations(range(4)) if {(p[a],p[b]) for a,b in seed}==seed]
assert autos==[(0,1,2,3),(1,0,3,2)]
swap=autos[1]
assert compose(compose(swap,g),swap)==h
assert compose(compose(swap,h),swap)==g
assert matrix(compose(compose(swap,left),swap))==R
# The entire invariant response, not just its trace, loses the ordering distinction.
def average_over_seed_symmetry(a):
    return tuple(tuple(sum(a[p.index(i)][p.index(j)] for p in autos)/len(autos)
                       for j in range(4)) for i in range(4))
assert average_over_seed_symmetry(L)==average_over_seed_symmetry(R)
assert average_over_seed_symmetry(defect)==tuple((F(0),)*4 for _ in range(4))
# Ordering the two triangle generators removes this swap, but supplies extra marking.
ordered_autos=[p for p in autos if compose(compose(p,g),tuple(p.index(i) for i in range(4)))==g
               and compose(compose(p,h),tuple(p.index(i) for i in range(4)))==h]
assert ordered_autos==[(0,1,2,3)]
print('PASS: unmarked seed symmetry exchanges the responses; invariant response averages coincide.')
print('CONTROL: retaining the ordered triangle pair removes that symmetry; this is extra provenance.')
print('PASS: seed route-order response derived from ABC and ADB, with no fitted matrix entries.')
print('left permutation:',left,'right permutation:',right)
print('defect rows:',defect)
print('PASS: existing retained transport preserves all four column records and the full response.')
print('PASS: same fixed 2I reference for both orders; residual difference equals the seed defect.')
print('CONTROL: trace, total norm and common-state reading do not distinguish the orders.')
print('PASS: named A-to-A probe distinguishes them; physical measurement selection remains open.')
print('Scope: permutation-action and mean-encoding adapter; rung4 physical metric not derived.')
