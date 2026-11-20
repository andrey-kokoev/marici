"""SAT on suffix anticommutations; an alternating binary matrix is realizable
on two qubits iff its rank is <=4. Impose rank lazily by forbidden principal
6x6 submatrices. The 40th border is unrestricted. python-sat required."""
from itertools import combinations,islice
from collections import Counter
from time import monotonic
from pysat.solvers import Solver
from exoo39_symbolic_relations import edges

def excess(rows):
    # Alternating Gaussian elimination on principal pivot pairs. Six pivots'
    # indices give a nonsingular original principal block (Schur complement).
    rows=rows[:];p=[];active=(1<<len(rows))-1
    for _ in range(3):
        pair=next(((i,(r&active&-(r&active)).bit_length()-1) for i,r in enumerate(rows) if active>>i&1 and r&active),None)
        if pair is None:return []
        a,b=pair;p.extend(pair);active^=1<<a|1<<b;x,y=rows[a],rows[b]
        for i in range(len(rows)):
            if active>>i&1:rows[i]^=(y if x>>i&1 else 0)^(x if y>>i&1 else 0)
    return p

def tens(adj):
    def walk(m,s,k):
        if not k:yield s;return
        while m.bit_count()>=k:
            b=m&-m;m^=b;yield from walk(m&~adj[b.bit_length()-1],s|b,k-1)
    yield from walk((1<<40)-1,0,10)

def run(name,role,seconds):
    E=edges();n=max(role)+1;ids={e:i+1 for i,e in enumerate(combinations(range(n),2))};nv=len(ids);clauses=set()
    def term(i,j): # red-edge indicator: signed var, or boolean constant
        if j==39:return nv+1+i
        r=(i,j) in E;a,b=sorted((role[i],role[j]));return r if a==b else (-1 if r else 1)*ids[a,b]
    def clause(es,red):
        lits=set()
        for i,j in es:
            t=term(i,j)
            if type(t)==bool:
                if t!=red:return None
            else:lits.add(-t if red else t)
        return None if any(-i in lits for i in lits) else tuple(sorted(lits))
    for vs in combinations(range(40),3):
        c=clause(combinations(vs,2),True)
        if c is not None:clauses.add(c)
    cuts=Counter();end=monotonic()+seconds
    with Solver(name='cadical195',bootstrap_with=list(sorted(clauses))) as sol:
        while monotonic()<end:
            sol.conf_budget(1000);sat=sol.solve_limited()
            if sat is None:continue
            if not sat:print(name,'UNSAT',dict(cuts),flush=True);return
            m=set(sol.get_model());rows=[0]*n
            for (i,j),k in ids.items():
                if k in m:rows[i]|=1<<j;rows[j]|=1<<i
            adj=[0]*40
            for i,j in combinations(range(40),2):
                t=term(i,j)
                if (t if type(t)==bool else t in m):adj[i]|=1<<j;adj[j]|=1<<i
            bad=False;p=excess(rows)
            if p:
                ks=[ids[tuple(sorted(e))] for e in combinations(p,2)];sol.add_clause([-k if k in m else k for k in ks]);cuts['rank']+=1;bad=True
            for s in islice(tens(adj),32):
                vs=[i for i in range(40) if s>>i&1];c=clause(combinations(vs,2),False);assert c is not None;sol.add_clause(c);cuts['blue']+=1;bad=True
            if not bad:
                assert all(not(adj[i]&adj[j]) for i,j in combinations(range(40),2) if adj[i]>>j&1);print(name,'WITNESS',rows,adj,flush=True);return
    print(name,'budget expired',dict(cuts),flush=True)
if __name__=='__main__':
    run('one suffix per pentagon', [i//5 if i<35 else 7+i-35 for i in range(39)],12)
    run('one suffix per pentagon position',[i%5 if i<35 else 5+i-35 for i in range(39)],12)
    run('unrestricted',list(range(39)),30)
