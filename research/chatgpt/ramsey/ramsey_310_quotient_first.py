"""Enumerate cyclic interaction quotients on 13 triples; phases need not be cyclic."""
from itertools import combinations
from time import monotonic
from collections import Counter
from pysat.solvers import Solver
from pysat.card import CardEnc,EncType
from ramsey_310_thirteen_triples import var,sevens
import sys

def quotient(ds):return [{(i+s*d)%13 for d in ds for s in (-1,1)} for i in range(13)]
def admissible(Q):
    if any(not 5<=len(n)<=9 for n in Q):return False
    if any(not any(b in Q[a] for a,b in combinations(U,2)) for U in combinations(range(13),4)):return False
    return all(len(set(range(13))-{i,j}-Q[i]-Q[j])<=2 for i,j in combinations(range(13),2) if j not in Q[i])

def lift(Q,seconds):
    # Absent interactions fixed false. Independent rotations of triples put
    # offset zero on every edge of one spanning tree.
    edges=[(i,j) for i,j in combinations(range(13),2) if j in Q[i]];vs=lambda i,j:[var(3*i,3*j+x) for x in range(3)];clauses=[];top=234
    for i,j in combinations(range(13),2):
        if j in Q[i]:clauses.append(vs(i,j))
        else:clauses.extend([[-v] for v in vs(i,j)])
    seen={0}
    while len(seen)<13:
        i,j=next((i,j) for i in seen for j in Q[i]-seen);clauses.append([var(3*i,3*j)]);seen.add(j)
    for i in range(13):
        lits=[v for j in Q[i] for v in vs(i,j)];enc=CardEnc.atmost(lits,9,top_id=top,encoding=EncType.seqcounter);top=enc.nv;clauses.extend(enc.clauses)
    for i,j,k in combinations(range(13),3):
        if j in Q[i] and k in Q[i]&Q[j]:
            for y in range(3):
                for z in range(3):clauses.append([-var(3*i,3*j+y),-var(3*i,3*k+z),-var(3*j+y,3*k+z)])
    start=monotonic();ct=0
    with Solver(name='cadical195',bootstrap_with=clauses) as s:
        while monotonic()-start<seconds:
            s.conf_budget(2000);ok=s.solve_limited()
            if ok is False:return 'excluded',ct
            if ok is None:continue
            p=set(s.get_model());order=[(u+3*ct)%39 for u in range(39)];A=[sum(1<<j for j,v in enumerate(order) if var(u,v) in p) for u in order];added=set()
            for m in sevens(A,k=10):
                U=[order[j] for j in range(39) if m>>j&1];c=tuple(sorted({var(i,j) for i,j in combinations(U,2) if j//3 in Q[i//3]}));added.add(c)
                if len(added)>=40:break
            if not added: print('witness offset variables',sorted(v for v in p if 1<=v<=234));return 'witness',ct
            for c in added:s.add_clause(c)
            ct+=1
    return 'open',ct
if __name__=='__main__':
    counts=Counter()
    for k in range(7):
        for ds in combinations(range(1,7),k):
            orbit={tuple(sorted(min(d*u%13,-d*u%13) for d in ds)) for u in range(1,13)}
            if ds!=min(orbit):continue
            if not admissible(quotient(ds)):counts['filtered']+=len(orbit);continue
            status,n=lift(quotient(ds),float(sys.argv[1]) if len(sys.argv)>1 else 8);counts[status]+=len(orbit);print(ds,status,n,flush=True)
    print(counts)
