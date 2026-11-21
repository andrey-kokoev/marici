"""Address-only synthesis, no graph/census input. Labels (01)(23)(45) and fixed 6. Axis exchanges blocks 23 and 45."""
from itertools import combinations
from pathlib import Path
import json,z3
D=Path(__file__).parent
blocks=[(0,1),(2,3),(4,5)];S=[(1<<i)|(1<<j) for i,j in combinations(range(7),2) if (i,j) not in blocks]+[60];n=len(S)
E={(i,j):z3.Bool(f'e{i}_{j}') for i,j in combinations(range(n),2) if not S[i]&S[j]}
solver=z3.SolverFor('QF_FD');bad=[];banned=set()
for i,j,k in combinations(range(n),3):
    t=[E.get(e) for e in ((i,j),(i,k),(j,k))];
    if all(x is not None for x in t):solver.add(z3.Or(*[z3.Not(x) for x in t]))
# Every forbidden independent set contains an inclusion-minimal forbidden one.
for size in range(1,8):
    for J in combinations(range(n),size):
        u=0
        for i in J:u|=S[i]
        if size<7 and u.bit_count()>=size:continue
        mask=sum(1<<i for i in J)
        if any(mask^(1<<i) in banned for i in J):new=False
        else:new=True
        banned.add(mask)
        if new:bad.append(tuple(E[e] for e in combinations(J,2) if e in E))
    # banned contains all smaller forbidden sets (forbidden Hall failures need not persist under supersets).
for t in bad:solver.add(z3.Or(*t))

def invariance(swaps):
    p=list(range(7))
    for a,b in swaps:p[a],p[b]=p[b],p[a]
    m=[S.index(sum(1<<p[i] for i in range(7) if s>>i&1)) for s in S];return [x==E[tuple(sorted((m[i],m[j])))] for (i,j),x in E.items()]

def check(name,actions):
    solver.push()
    for g in actions:solver.add(*invariance(g))
    ans=solver.check();print(name,ans,flush=True);out={'status':str(ans)}
    if ans==z3.sat:
        mod=solver.model();A=[0]*(8+n)
        def link(i,j):A[i]|=1<<j;A[j]|=1<<i
        for v in range(7):link(0,1+v)
        for i,s in enumerate(S):
            for v in range(7):
                if s>>v&1:link(1+v,8+i)
        for (i,j),x in E.items():
            if z3.is_true(mod.eval(x)):link(8+i,8+j)
        from verify_ramsey_catalogue_free_chain import verify
        out.update(graph=A,verified=verify(A,8))
    solver.pop();return out
if __name__=='__main__':
    a=blocks[:2];b=blocks[::2];j=[(2,4),(3,5)];out={'addresses':S,'variables':len(E),'positive_clauses':len(bad),'tests':{}}
    for name,g in [('D8',[a,b,j]),('translations',[a,b]),('flip01_23',[a]),('flip01_45',[b]),('flip23_45',[blocks[1:]]),('row',[j]),('row_conjugate',[[(2,5),(3,4)]]),('unrestricted',[])]:
        out['tests'][name]=check(name,g);(D/'ramsey_seven_transport_synthesis.json').write_text(json.dumps(out)+'\n')
