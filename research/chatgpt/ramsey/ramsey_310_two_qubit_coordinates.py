"""Unrestricted two-qubit Exoo lift, direct (x1,z1,x2,z2) SAT variables. uv run --with python-sat python <file> [seconds]."""
from itertools import combinations, islice
from time import monotonic
import sys
from pysat.solvers import Solver
from exoo39_symbolic_relations import edges
from ramsey_310_two_qubit_lift import tens

class Circuit:
    def __init__(self): self.n=0;self.cnf=[]
    def var(self):self.n+=1;return self.n
    def binary(self,a,b,xor):
        c=self.var();self.cnf.extend(([a,b,-c],[-a,-b,-c],[a,-b,c],[-a,b,c]) if xor else ([-a,-b,c],[a,-c],[b,-c]));return c
    def symp(self,u,v):
        t=[self.binary(u[i],v[i^1],False) for i in range(4)]
        return self.binary(self.binary(t[0],t[1],True),self.binary(t[2],t[3],True),True)

def pairing(u,v):return sum(((u>>i)&1)*((v>>(i^1))&1) for i in range(4))%2

def main(seconds):
    c=Circuit();Q=[[c.var() for _ in range(4)] for _ in range(39)];E=edges();red={};N=[0]*39
    for i,j in combinations(range(40),2):
        if j==39:red[i,j]=c.var();continue
        t=c.symp(Q[i],Q[j]);red[i,j]=-t if (i,j) in E else t
        if (i,j) in E:N[i]|=1<<j;N[j]|=1<<i
    for vs in combinations(range(40),3):c.cnf.append([-red[e] for e in combinations(vs,2)])
    sets=[0]
    for i,row in enumerate(N):sets.extend([s|1<<i for s in sets if not s&row]);
    nine=[s for s in sets if s.bit_count()==9];assert max(map(int.bit_count,sets))==9
    clause=lambda vs:[red[e] for e in combinations(vs,2)]
    for s in nine:c.cnf.append(clause([i for i in range(39) if s>>i&1]+[39]))
    # Check all 256 Pauli-pair truth-table entries independently of graph clauses.
    g=Circuit();uv=[g.var() for _ in range(8)];t=g.symp(uv[:4],uv[4:]);
    with Solver(name='cadical195',bootstrap_with=g.cnf) as check:
        for u in range(16):
            for v in range(16):
                a=[q if (u+(v<<4))>>i&1 else -q for i,q in enumerate(uv)];lit=t if pairing(u,v) else -t;assert check.solve(assumptions=a+[lit]) and not check.solve(assumptions=a+[-lit])
    print('vars',c.n,'clauses',len(c.cnf),'seed blue-ten clauses',len(nine),'truth table OK',flush=True)
    with Solver(name='cadical195',bootstrap_with=c.cnf) as sol:
        assert not sol.solve(assumptions=[-q for row in Q for q in row]);print('identity lift UNSAT (control)',flush=True)
        end=monotonic()+seconds;models=cuts=0
        while monotonic()<end:
            sol.conf_budget(2000);sat=sol.solve_limited()
            if sat is None:continue
            if not sat:print('UNSAT',models,cuts);return
            model=set(sol.get_model());labels=[sum((q in model)<<i for i,q in enumerate(row)) for row in Q];adj=[0]*40
            for (i,j),r in red.items():
                on=r in model
                if j<39:assert on==(((i,j) in E)^pairing(labels[i],labels[j]))
                if on:adj[i]|=1<<j;adj[j]|=1<<i
            assert all(not(adj[i]&adj[j]) for i,j in combinations(range(40),2) if adj[i]>>j&1);bad=list(islice(tens(adj),64));models+=1
            if not bad:print('WITNESS labels',labels,'border',adj[39]);return
            for s in bad:sol.add_clause(clause([i for i in range(40) if s>>i&1]));cuts+=1
        print('budget expired',seconds,'seconds;',models,'triangle-free candidate models;',cuts,'additional blue-ten clauses')
if __name__=='__main__':main(int(sys.argv[1]) if len(sys.argv)>1 else 60)
