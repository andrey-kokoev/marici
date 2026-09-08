"""Planar phi^3+phi^4 source and noncanonical cubic refinements."""
import json
from pathlib import Path
from itertools import combinations
from collections import Counter
from sympy import symbols,prod,expand,factor,simplify,Rational

def tris(V):
    if len(V)<=3:return [frozenset()]
    out=[]
    for j in range(1,len(V)-1):
        L=V[:j+1];R=V[j:];E=set()
        if len(L)>2:E.add((V[0],V[j]))
        if len(R)>2:E.add((V[j],V[-1]))
        out += [a|b|E for a in tris(L) for b in tris(R)]
    return out

def faces(D):
    F=[list(range(6))]
    for a,b in sorted(D):
        k=next(k for k,P in enumerate(F) if a in P and b in P)
        P=F.pop(k);i,j=sorted((P.index(a),P.index(b)))
        F.extend([P[i:j+1],P[j:]+P[:i+1]])
    return F
T=tris(tuple(range(6)));edges=sorted(set().union(*T));s=dict(zip(edges,symbols(' '.join('s%d%d'%e for e in edges))))
g,h=symbols('g lambda');D=set()
for t in T:
    for k in range(4):
        for E in combinations(sorted(t),k):
            d=frozenset(E)
            if all(len(f) in (3,4) for f in faces(d)):D.add(d)
weights={};counts=Counter()
for d in D:
    f=faces(d);v3=sum(len(x)==3 for x in f);v4=sum(len(x)==4 for x in f)
    weights[d]=g**v3*h**v4;counts[v3,v4]+=1
    assert sum(d<=t for t in T)==2**v4
W=[]
for t in T:
    W.append(expand(sum(weights[d]*prod(s[e] for e in t-d)/sum(d<=u for u in T) for d in D if d<=t)))
# Each original diagram's total coefficient is preserved exactly by refinement.
for d in D:assert sum(Rational(1,sum(d<=u for u in T)) for t in T if d<=t)==1
residuals=[]
for e in edges:
    inside=set(range(e[0],e[1]+1));cells={}
    for k,t in enumerate(T):
        if e in t:
            a=frozenset(x for x in t-{e} if set(x)<=inside);cells[a,(t-{e})-a]=k
    L=sorted({a for a,b in cells},key=repr);R=sorted({b for a,b in cells},key=repr)
    for a,b in combinations(L,2):
        for c,d in combinations(R,2):
            ids=[cells[a,c],cells[b,d],cells[a,d],cells[b,c]]
            res=factor(W[ids[0]]*W[ids[1]]-W[ids[2]]*W[ids[3]])
            assert res.subs(h,0)==0
            assert simplify(res.subs(s[e],0))==0
            residuals.append({'channel':e,'indices':ids,'residual':str(res),'nonzero':res!=0})
# Central channel separates two four-point amplitudes.
e=(0,3)
residue=sum(w/prod(s[x] for x in d-{e}) for d,w in weights.items() if e in d)
expected=(g**2*(1/s[0,2]+1/s[1,3])+h)*(g**2*(1/s[0,4]+1/s[3,5])+h)
assert simplify(residue-expected)==0
x,y,alpha=symbols('x y alpha');A4=g**2/x+g**2/y+h
assert simplify((g**2+alpha*h*x)/x+(g**2+(1-alpha)*h*y)/y-A4)==0
assert any(r['nonzero'] for r in residuals)
out={'status':'passed','diagram_counts':{str(k):v for k,v in sorted(counts.items())},'triangulations':[sorted(t) for t in T],'refined_weights':[str(w) for w in W],'quadrics':residuals,'central_residue_factorization':True,'A4':'g^2/s+g^2/t+lambda','scope':'Equal distribution across 2^v4 cubic refinements is declared presentation, not a source vertex rule. Nonzero off-pole weight quadrics coexist with correct channel residues.'}
Path('research/nima/results/quartic_contact_source.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items() if k not in ('triangulations','refined_weights')}))
