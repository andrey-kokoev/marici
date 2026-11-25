"""Test a necessary three-port condition in the 75-edge matching branch.
Inputs: all labeled two-edge triangle-free additions to the 62 House of Graphs
minimum (3,8;26) records. Counts of additions are not isomorphism classes.
"""
import json,hashlib
from pathlib import Path
from functools import lru_cache
from ramsey310_codegree7_test import sets
from ramsey310_cached_kernel import bits
F=(1<<26)-1

def decode(line):
    assert len(line)==56 and line[0]==89
    A=[0]*26;k=0
    for j in range(26):
        for i in range(j):
            if (line[1+k//6]-63)>>(5-k%6)&1:A[i]|=1<<j;A[j]|=1<<i
            k+=1
    return A

def side(A,both=False,accept=None,cap=False):
    S=list(sets(A,F,7));n=len(S);allrows=(1<<n)-1;inc=[sum(1<<j for j,t in enumerate(S) if t>>v&1) for v in range(26)]
    def disjoint(s):
        m=allrows
        for v in bits(s):m &= ~inc[v]
        return m
    D=[disjoint(s) for s in S];assert all(D) # else adjoining a vertex gives an 82-edge order-27 survivor
    comp=[]
    for m in D:
        p=allrows
        for j in bits(m):p &= ~D[j]
        comp.append(p)
    @lru_cache(maxsize=4096)
    def works(u):return next(sets(A,F & ~u,6),None) is None
    def stock(ids):
        if not cap:return allrows
        need=[8-a.bit_count()-sum(S[k]>>v&1 for k in ids) for v,a in enumerate(A)]
        if min(need)<0:return 0
        mask=allrows
        for v,k in enumerate(need):
            if not k:mask &= ~inc[v]
        return mask
    for i,r in enumerate(comp):
        for j in bits(r&((1<<i)-1)):
            if (S[i]&S[j]).bit_count()>5:continue # owners share one root, global codegree at most six
            for k in bits(r&comp[j]&((1<<j)-1)):
                if max((S[k]&S[i]).bit_count(),(S[k]&S[j]).bit_count())>5 or not works(S[i]|S[j]|S[k]):continue
                if not both:return True
                # Opposite matched supports must be disjoint; any two distinct
                # port owners have at most six common neighbors, hence no equal rows.
                used=(1<<i)|(1<<j)|(1<<k)
                for x in bits(D[i]&~used):
                    if not (stock((i,j,k))>>x&1):continue
                    for y in bits(D[j]&~used&comp[x]&stock((i,j,k,x))):
                        if (S[x]&S[y]).bit_count()>5:continue
                        for z in bits(D[k]&~used&comp[x]&comp[y]&stock((i,j,k,x,y))):
                            if max((S[z]&S[x]).bit_count(),(S[z]&S[y]).bit_count())<=5 and works(S[x]|S[y]|S[z]):
                                if accept is None or accept(tuple(S[q] for q in (i,j,k,x,y,z))):return True
    return False

def instances(A):
    opts=[(i,j) for i in range(26) for j in range(i) if not (A[i]>>j&1 or A[i]&A[j])]
    for h,(i,j) in enumerate(opts):
        B=A.copy();B[i]|=1<<j;B[j]|=1<<i
        for x,y in opts[:h]:
            if B[x]&B[y]:continue
            C=B.copy();C[x]|=1<<y;C[y]|=1<<x;yield C

if __name__=='__main__':
    import sys
    p=Path(__file__).resolve().parents[1]/'results/ramsey38_26_e73_hog.g6';data=p.read_bytes();assert hashlib.sha256(data).hexdigest()=='9a904566a969ef257db9b28719c35f84a86aa63e9a1c56a7691aa3807d35b214'
    for n,l in enumerate(data.splitlines(),1):
        A=decode(l);assert sum(a.bit_count() for a in A)==146;X=list(instances(A));budget=int(sys.argv[1]) if len(sys.argv)>1 else len(X);both='both' in sys.argv;print(json.dumps(dict(parent=n,additions=len(X),tested=min(budget,len(X)),both=both,passed=sum(side(g,both) for g in X[:budget]))),flush=True)
