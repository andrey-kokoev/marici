"""Derive link colors from interactions confined to at most L distinct labels; measure exactly what is forced given the frame, without reading completed graphs."""
from itertools import combinations
from functools import reduce
from operator import or_
from pathlib import Path
import json,z3
D=Path(__file__).parent;S=[(1<<i)|(1<<j) for i,j in combinations(range(7),2) if (i,j) not in [(0,1),(2,3),(4,5)]]+[60];E=[(i,j) for i,j in combinations(range(19),2) if not S[i]&S[j]];X=z3.Bools(' '.join('e'+str(i) for i in range(80)));ix=dict(zip(E,X));clauses=[[] for _ in range(8)];forbid=set()
for n in range(1,8):
    for J in combinations(range(19),n):
        mask=sum(1<<i for i in J);u=reduce(or_,(S[i] for i in J));L=u.bit_count();links=[ix[e] for e in combinations(J,2) if e in ix]
        if n==3 and len(links)==3:clauses[L].append(z3.Or(*[z3.Not(x) for x in links]))
        if any(mask^(1<<i) in forbid for i in J):forbid.add(mask);continue
        if n==7 or L<n:forbid.add(mask);clauses[L].append(z3.Or(*links))

def backbone(s,code):
    s.push();s.add(*[X[i]==bool(code>>j&1) for j,i in enumerate([0,4,6])]);assert s.check()==z3.sat;m=s.model();vals=[z3.is_true(m.eval(x,model_completion=True)) for x in X];fixed=set(range(80));example=None
    while fixed:
        s.push();s.add(z3.Or(*[X[i]!=vals[i] for i in fixed]));r=s.check();assert r in (z3.sat,z3.unsat)
        if r==z3.unsat:s.pop();break
        a=s.model();alt=[z3.is_true(a.eval(x,model_completion=True)) for x in X];fixed={i for i in fixed if vals[i]==alt[i]};s.pop()
    s.pop();return {i:int(vals[i]) for i in sorted(fixed)}
if __name__=='__main__':
    s=z3.SolverFor('QF_FD');out={}
    for L,c in enumerate(clauses):
        s.add(*c)
        if L<4:continue
        rows=[backbone(s,k) for k in range(8)];out[L]=rows;print(L,len(c),[len(row) for row in rows],flush=True)
    (D/'ramsey_seven_incidence_radius.json').write_text(json.dumps(out)+'\n')
    # Structural compression: saturate both sides of the special 2345 address. Choose the f=0 frame and transport the other four.
    q=S[-1];motif=[i for i,(a,b) in enumerate(E) if q in (S[a],S[b]) or (S[a]|S[b])==q];s=z3.SolverFor('QF_FD');s.add(*(c for cs in clauses[:7] for c in cs));s.add(*[X[i] for i in motif]);tab=[backbone(s,k) for k in range(8)];print('motif',motif,'determined',list(map(len,tab)))
    p=[0,1,4,5,2,3,6];m=[S.index(sum(1<<p[i] for i in range(7) if sm>>i&1)) for sm in S];em=[E.index(tuple(sorted((m[a],m[b])))) for a,b in E];W={}
    for k,row in enumerate(tab):
        if (k&1)!=(k>>2):continue
        assert len(row)==80;w=sum(b<<i for i,b in row.items());v=sum((w>>i&1)<<j for i,j in enumerate(em));c=sum((v>>j&1)<<i for i,j in enumerate((0,4,6)));assert (c&1)!=(c>>2);W[k]=w;W[c]=v
    from verify_ramsey_catalogue_free_chain import verify
    for k,w in W.items():
        A=[0]*27
        def link(i,j):A[i]|=1<<j;A[j]|=1<<i
        for i in range(7):link(0,1+i)
        for i,sm in enumerate(S):
            for j in range(7):
                if sm>>j&1:link(1+j,8+i)
        for i,(a,b) in enumerate(E):
            if w>>i&1:link(8+a,8+b)
        verify(A,8)
    assert len(W)==8;print('verified outputs',len(W));(D/'ramsey_seven_incidence_motif.json').write_text(json.dumps(dict(motif=motif,determined=list(map(len,tab)),wirings=W))+'\n')
