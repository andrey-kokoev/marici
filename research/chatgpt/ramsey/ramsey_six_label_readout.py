"""Apply the seven-label readout question to the complete six-label duad table. Test even ALL links at a reference, not just triples."""
from itertools import combinations
from pathlib import Path
import json,z3
from ramsey_seed_affine_witness import P,T,m,mate
D=Path(__file__).parent
E=[(a,b) for a,b in combinations(range(15),2) if not set(P[a])&set(P[b])];X=[z3.Bool(f'x{i}') for i in range(len(E))];sol=z3.SolverFor('QF_FD')
for a,b,c in combinations(range(15),3):
    q=[(a,b),(a,c),(b,c)]
    if all(e in E for e in q):sol.add(z3.Or(*[z3.Not(X[E.index(e)]) for e in q]))
for k in range(1,7):
    for J in combinations(range(15),k):
        if k==6 or len(set().union(*(P[i] for i in J)))<k:sol.add(z3.Or(*[X[E.index(e)] for e in combinations(J,2) if e in E]))

def addr(i):return ''.join(map(str,P[i]))
def W(M):
    omit={tuple(sorted(P.index(d) for d in T[j-15] if d!=P[i])) for i,j in M};return sum(1<<i for i,e in enumerate(E) if e not in omit)
if __name__=='__main__':
    from collections import Counter
    A,B=W(m),W(mate);seen=[]
    while (res:=sol.check())==z3.sat:
        mod=sol.model();s=sum(1<<i for i,x in enumerate(X) if z3.is_true(mod.eval(x)));seen.append(s);sol.add(z3.Or(*[z3.Not(x) if s>>i&1 else x for i,x in enumerate(X)]))
    assert res==z3.unsat and A in seen and B in seen
    project=lambda s,I:tuple(s>>i&1 for i in I);star=[i for i,e in enumerate(E) if 0 in e];c=Counter(project(s,star) for s in seen);assert all(len({project(s,[i for i,e in enumerate(E) if v in e]) for s in seen})==len(c) for v in range(15));i=next(i for i in star if (A^B)>>i&1);out=dict(wirings=len(seen),star_neighbors=[addr(E[i][1]) for i in star],star_reading_count=len(c),fiber_sizes=dict(Counter(c.values())),row_pair_first_probe=list(map(addr,E[i])),row_bits=[A>>i&1,B>>i&1])
    for size in range(1,16):
        for roots in combinations(range(15),size):
            mask=sum(1<<i for i,(a,b) in enumerate(E) if a in roots or b in roots)
            if len({w&mask for w in seen})==len(seen):break
        else:continue
        out.update(first_separating_full_stars=list(map(addr,roots)),links_read=mask.bit_count());break
    print(out);(D/'ramsey_six_label_readout.json').write_text(json.dumps(out)+'\n')
