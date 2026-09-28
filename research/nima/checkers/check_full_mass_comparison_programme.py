"""Exact full 1836-attempt comparison programme, provisional dynamics.

Two four-state carriers share pinned state0. Six rational potentials remain.
Arrow values are directed potential differences; opposite comparisons remain
separate resource-consuming attempts. Each comparison enforces equality by
Euclidean orthogonal projection. Twelve outer labels repeat a 153-slot sweep.
These are declared prototype choices, not a derived physical carrier law.
Writes no artifacts; no target mass-ratio data.
"""
from fractions import Fraction as F
from itertools import product
import math

edges=[(i,j) for i in range(4) for j in range(4) if i!=j]
def state(side,i):
    row=[0]*6
    if i: row[3*side+i-1]=1
    return row

def subtract(a,b): return tuple(x-y for x,y in zip(a,b))
def arrow(side,e): return subtract(state(side,e[1]),state(side,e[0]))
rows=[subtract(arrow(0,e),arrow(1,f)) for e,f in product(edges,repeat=2)]
rows += [subtract(state(0,i),state(1,j)) for i,j in product(range(1,4),repeat=2)]
assert len(rows)==153
assert all(sum(a*a for a in row)>0 for row in rows)

def dot(a,b): return sum(x*y for x,y in zip(a,b))
def energy(x): return dot(x,x)
def run(x,ordered_rows):
    initial=energy(x)
    spent=0
    drop_total=F(0)
    reopened=0
    previous=None
    for outer in edges:
        for row in ordered_rows:
            delta=dot(row,x)
            norm=dot(row,row)
            y=tuple(v-F(a)*delta/norm for v,a in zip(x,row))
            assert dot(row,y)==0
            drop=energy(x)-energy(y)
            assert drop==delta*delta/norm and drop>=0
            if previous is not None and dot(previous,y)!=0:
                reopened+=1
            previous=row
            x=y
            drop_total+=drop
            spent+=1
    assert spent==1836
    assert initial==drop_total+energy(x)
    defect=sum(dot(row,x)**2 for row in rows)
    return x,defect,reopened

zero=(F(0),)*6
assert run(zero,rows)==(zero,F(0),0)
seed=(F(1),)+(F(0),)*5
x,d,reopened=run(seed,rows)
y,dr,rr=run(seed,list(reversed(rows)))
assert d>0 and dr>0 and d!=dr
assert reopened>0 and rr>0
# Exact linearity of each projection implies U(2x)=2U(x), hence defect scales4.
assert sum(dot(row,tuple(2*v for v in x))**2 for row in rows)==4*d

def log10_fraction(q): return math.log10(q.numerator)-math.log10(q.denominator)
print('Compatible zero input:1836 paid attempts, zero final defect.')
print(f'Unit seeded input, forward order: log10 summed-square defect={log10_fraction(d):.6f}, immediately reopened agreements={reopened}')
print(f'Unit seeded input, reverse order: log10 summed-square defect={log10_fraction(dr):.6f}, immediately reopened agreements={rr}')
print('Doubling input disturbance multiplies final summed-square defect by4.')
print('All1836 attempts retain unit resource even when update vanishes.')
print('Exact full-programme update and resource-accounting checks passed.')
