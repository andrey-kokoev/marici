"""Seedless binary cyclic search, followed by direct-coordinate Pauli lift and unrestricted border."""
from itertools import combinations,islice
from time import monotonic
from pysat.solvers import Solver
from ramsey_310_two_qubit_coordinates import Circuit,pairing
from ramsey_311_two_qubit_trial import clique,rows

def main():
    for n in range(17,26):
        full=(1<<n)-1;found=None
        for mask in range(1<<(n//2)):
            ds=[i for i in range(1,n//2+1) if mask>>(i-1)&1];d=sum(1<<i for i in set(ds)|{n-i for i in ds});r=rows(n,d);b=[full^v^1<<i for i,v in enumerate(r)]
            if next(clique(r,3,r[0]),None) is None and next(clique(b,4,b[0]),None) is None:found=ds;best=(n,r);break
        print('cyclic',n,found,flush=True)
    n,N=best;v=range(n+1);full=(1<<(n+1))-1;c=Circuit();Q=[[c.var() for _ in range(4)] for _ in N];R={}
    for i,j in combinations(v,2):
        if j==n:R[i,j]=c.var();continue
        k=c.symp(Q[i],Q[j]);R[i,j]=-k if N[i]>>j&1 else k
    def clauses(ms,col):return [[(-1 if col else 1)*R[e] for e in combinations([i for i in v if s>>i&1],2)] for s in ms]
    for col,k in [(True,4),(False,5)]:
        a=N if col else [((1<<n)-1)^r^1<<i for i,r in enumerate(N)];assert next(clique(a,k,(1<<n)-1),None) is None
        c.cnf.extend(clauses((s|1<<n for s in clique(a,k-1,(1<<n)-1)),col))
    with Solver(name='cadical195',bootstrap_with=c.cnf) as sol:
        print('seed',n,'unchanged border exists',sol.solve(assumptions=[-x for q in Q for x in q]),flush=True);end=monotonic()+35;models=0;counts=[0,0]
        while monotonic()<end:
            sol.conf_budget(1500);ok=sol.solve_limited()
            if ok is None:continue
            if not ok:print('UNSAT',models,counts);return
            m=set(sol.get_model());ls=[sum((x in m)<<j for j,x in enumerate(q)) for q in Q];a=[0]*(n+1)
            for (i,j),k in R.items():
                if j<n:assert (k in m)==bool((N[i]>>j&1)^pairing(ls[i],ls[j]))
                if k in m:a[i]|=1<<j;a[j]|=1<<i
            models+=1;bad=[]
            for ix,(adj,k,col) in enumerate([(a,4,True),([full^r^1<<i for i,r in enumerate(a)],5,False)]):
                cuts=clauses(islice(clique(adj,k,full),48),col);counts[ix]+=len(cuts);bad+=cuts
            if not bad:print('WITNESS',a,'labels',ls);return
            for cs in bad:sol.add_clause(cs)
        print('budget expired models',models,'red/blue cuts',counts)
if __name__=='__main__':main()
