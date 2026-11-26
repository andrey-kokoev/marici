"""Do not forget row labels or which observed supports lie on the boundary."""
from contextlib import redirect_stdout
from io import StringIO
from collections import Counter
from itertools import combinations
from ramsey38_compare_support_fillings import main as enumerate_fillings, boundary, rows, fmt
from ramsey38_support_ball_completion import N

def report():
    with redirect_stdout(StringIO()): sols=enumerate_fillings()
    obs={frozenset(N[1]&N[v]):v for v in N if v!=1 and v not in N[1]}
    hidden=[]
    for i,s in enumerate(sols):
        bd=boundary(s);inside=[r for r in rows if len(r)<4 and not any(r<=f for f in bd)]
        hidden.append({obs[r] for r in inside})
        print('ABCDEFG'[i], 'interior short rows:', sorted(obs[r] for r in inside),'sizes:',sorted(map(len,inside)), 'missing faces on boundary by size:',sorted(Counter(len(f) for f in bd if f not in rows).items()))
    assert all({6,17}&h for h in hidden) and {6} in hidden and {17} in hidden
    for v in (6,13,17):print('row',v,'support',sorted(N[1]&N[v]))
    for t in sols[3]^sols[4]:
        print('exchanged',sorted(t),'marked proper subfaces',sorted((len(r),obs[r]) for r in rows if r<t))
    for i in [3,4]:
        print('DE'[i-3], 'boundary delta',fmt(boundary(sols[i])-boundary(sols[7-i])))
if __name__=='__main__':report()
