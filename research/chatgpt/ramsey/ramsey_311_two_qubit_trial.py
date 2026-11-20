"""Find a cyclic (3,11) seed, then attempt one larger order by two-qubit edits and an arbitrary border."""
from itertools import combinations,islice
from time import monotonic
from pysat.solvers import Solver
from ramsey_310_two_qubit_coordinates import Circuit,pairing

def clique(adj,k,m):
    if k==0:yield 0;return
    while m.bit_count()>=k:
        b=m&-m;m^=b
        for s in clique(adj,k-1,m&adj[b.bit_length()-1]):yield s|b

def rows(n,d):return [((d<<i)|(d>>(n-i)))&((1<<n)-1) for i in range(n)]
def cyclic(n):
    full=(1<<n)-1
    def visit(i,d):
        if i>n//2:
            B=[full^(1<<j)^v for j,v in enumerate(rows(n,d))];return d if next(clique(B,10,B[0]),None) is None else None
        t=d|1<<i|1<<(n-i)
        if all(not(t&r) for j,r in enumerate(rows(n,t)) if t>>j&1):
            a=visit(i+1,t)
            if a is not None:return a
        return visit(i+1,d)
    return visit(1,0)
def main():
    best=None
    for n in range(40,48):
        d=cyclic(n);print('cyclic',n,None if d is None else [j for j in range(1,n//2+1) if d>>j&1],flush=True)
        if d is not None:best=n,d
    n,d=best;N=rows(n,d);s=[0]
    for i,r in enumerate(N):
        assert all(not(r&N[j]) for j in range(i) if r>>j&1);s += [t|1<<i for t in s if not r&t]
    alpha=max(map(int.bit_count,s));assert alpha<=10;ten=[t for t in s if t.bit_count()==10];border=next((t for t in s if all(t&u for u in ten)),None);print('verified seed',n,'alpha',alpha,'blue tens',len(ten),'unchanged legal border',border,flush=True)
    c=Circuit();Q=[[c.var() for _ in range(4)] for _ in N];R={}
    for i,j in combinations(range(n+1),2):
        if j==n:R[i,j]=c.var()
        else:
            v=c.symp(Q[i],Q[j]);R[i,j]=-v if N[i]>>j&1 else v
    for vs in combinations(range(n+1),3):c.cnf.append([-R[e] for e in combinations(vs,2)])
    def clause(s):return [R[e] for e in combinations([i for i in range(n+1) if s>>i&1],2)]
    c.cnf.extend(clause(t|1<<n) for t in ten);models=0;cuts=0;full=(1<<(n+1))-1
    with Solver(name='cadical195',bootstrap_with=c.cnf) as sol:
        limit=monotonic()+40
        while monotonic()<limit:
            sol.conf_budget(1500);ok=sol.solve_limited()
            if ok is None:continue
            if not ok:print('UNSAT');return
            m=set(sol.get_model());labels=[sum((v in m)<<b for b,v in enumerate(q)) for q in Q];A=[0]*(n+1)
            for (i,j),v in R.items():
                if j<n:assert (v in m)==bool((N[i]>>j&1)^pairing(labels[i],labels[j]))
                if v in m:A[i]|=1<<j;A[j]|=1<<i
            assert all(not(A[i]&A[j]) for i,j in combinations(range(n+1),2) if A[i]>>j&1);B=[full^r^1<<i for i,r in enumerate(A)];bad=list(islice(clique(B,11,full),64));models+=1
            if not bad:print('WITNESS',A,flush=True);return
            for t in bad:sol.add_clause(clause(t));cuts+=1
    print('two-qubit budget expired: models',models,'blue-eleven cuts',cuts)
if __name__=='__main__':main()
