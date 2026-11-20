"""Fixed delivery facts; formal concepts; two levels of link reading. uv run --offline --with python-sat python <file>."""
from itertools import combinations, product
from collections import Counter
from pysat.solvers import Solver

region='EWW'; wants=['T','C','T'];cat='TTCCKKJTTT';ships='EWEWEWEWEW'
tea=[i for i,c in enumerate(cat) if c=='T']; C=range(3); P=range(10)
def subsets(xs):return [frozenset(t) for n in range(len(xs)+1) for t in combinations(xs,n)]
def concepts(tags):
    attrs=list(product(tags,P));has=lambda c,a:(wants[c]==cat[a[1]] if a[0]=='I' else region[c]==ships[a[1]])
    def intent(X):return frozenset(a for a in attrs if all(has(c,a) for c in X))
    def extent(Y):return frozenset(c for c in C if all(has(c,a) for a in Y))
    out={extent(intent(X)) for X in subsets(C)};assert all(extent(intent(X))==X for X in out);return out

def orbitmap(fine):
    rows=[(c,(p,)) for c,p in product(C,P)]+[(3,t) for t in combinations(tea,2)];assert len(rows)==40
    # Product profile in both contexts (cocoa and juice share an empty interest extent).
    profile=lambda p:(tuple(c for c in C if wants[c]==cat[p]),ships[p]);keys={};out={}
    for i,j in combinations(range(40),2):
        def directed(i,j):
            c,x=rows[i];d,y=rows[j];return (c,d,tuple(sorted(profile(p) for p in x)),tuple(sorted(profile(p) for p in y)),tuple(sorted(profile(p) for p in set(x)&set(y))) if fine else ())
        key=min(directed(i,j),directed(j,i));out[i,j]=keys.setdefault(key,len(keys)+1)
    return out

def solve(orb,limit):
    def lits(S):return tuple(sorted({orb[a,b] for a,b in combinations(sorted(S),2)}))
    tri={tuple(-x for x in lits(s)) for s in combinations(range(40),3)};cuts=[]
    with Solver(name='cadical195',bootstrap_with=sorted(tri)) as sol:
        for _ in range(limit+1):
            sol.conf_budget(30000);sat=sol.solve_limited()
            if sat is None:return 'OPEN (conflict budget)',len(cuts)
            if not sat:
                with Solver(name='glucose4',bootstrap_with=[*tri,*(lits(w) for w in cuts)]) as s:assert not s.solve()
                return 'UNSAT (two solvers)',len(cuts)
            red=set(sol.get_model());N=[0]*40
            for (a,b),z in orb.items():
                if z not in red:N[a]|=1<<b;N[b]|=1<<a
            def search(m,S):
                if len(S)==10:return S
                while m.bit_count()>=10-len(S):
                    v=m&-m;m^=v;i=v.bit_length()-1;t=search(m&N[i],S+[i]);
                    if t:return t
            w=search((1<<40)-1,[])
            if w is None:return ('WITNESS red orbit ids '+str(sorted(x for x in red if x>0))),len(cuts)
            if len(cuts)==limit:return 'OPEN (model budget)',len(cuts)
            sol.add_clause(lits(w));cuts.append(w)
if __name__=='__main__':
    for tags in ('I','ID'):print(tags,'closed extents',sorted(tuple(sorted(s)) for s in concepts(tags)),flush=True)
    for fine in (False,True):
        orb=orbitmap(fine);print('retains shared product identity',fine,'pair types',len(set(orb.values())),solve(orb,2000),flush=True)
