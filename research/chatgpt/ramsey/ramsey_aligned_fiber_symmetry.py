"""Catalogue audit. A layout consists of a fixed-point-free color automorphism t, one seed orbit, a three-orbit R subset, and a transversal of the eleven orbits giving one global side. Seven remaining pairs are B. Layout symmetries commute with t and preserve side or exchange both sides globally. Any such symmetry is uniquely t^e h where h fixes the upper seed and preserves the upper transversal. Enumerate all these tests; quotient out the irrelevant choice of which side is called upper."""
from itertools import combinations
from pathlib import Path
from collections import Counter
import json
H=Path(__file__).parent;V=tuple(range(22));I=V

def autom(N):
    sig=[len(a) for a in N]
    for _ in V:
        desc=[(sig[i],tuple(sorted(sig[j] for j in N[i]))) for i in V];d={v:i for i,v in enumerate(sorted(set(desc)))};s=[d[v] for v in desc]
        if len(set(s))==len(set(sig)):break
        sig=s
    def gen(p,L,U):
        if not L:yield tuple(p[i] for i in V);return
        opts=[([v for v in U if sig[u]==sig[v] and all((x in N[u])==(y in N[v]) for x,y in p.items())],u) for u in L];vs,u=min(opts,key=lambda z:len(z[0]));
        for v in vs:yield from gen(p|{u:v},L-{u},U-{v})
    return list(gen({},set(V),set(V)))

def audit(G):
    best=0;w=None;ts=[t for t in G if all(t[i]!=i and t[t[i]]==i for i in V)]
    for t in ts:
        O=[(i,t[i]) for i in V if i<t[i]];C=[h for h in G if all(h[t[i]]==t[h[i]] for i in V)]
        for seed,(z,_) in enumerate(O):
            F=[h for h in C if h[z]==z];others=[j for j in range(11) if j!=seed]
            if len(F)*2<=best:continue
            for mask in range(1024):
                if len(F)*2<=best:break
                A=[O[j][0] for j in range(11)]
                for b,j in enumerate(others):A[j]=O[j][mask>>b&1]
                U=set(A);K=[h for h in F if all(h[i] in U for i in U)];
                if 2*len(K)<=best:continue
                for J in combinations(others,3):
                    R={A[j] for j in J};T=[h for h in K if all(h[i] in R for i in R)];n=2*len(T)
                    if n>best:
                        best=n;w=dict(swap=t,seed=(z,t[z]),upper_R=sorted(R),upper_B=sorted(U-R-{z}),upper_preserving=T)
                    if best==2*len(K):break
    return best,len(ts),w
rows=[]
for i,g in enumerate((H/'pauli-realization-catalogues/r37_22.g6').read_text().splitlines(),1):
    bits=''.join(f'{ord(c)-63:06b}' for c in g[1:]);N=[set() for _ in V]
    for a,b in combinations(V,2):
        if bits[b*(b-1)//2+a]=='1':N[a].add(b);N[b].add(a)
    G=autom(N);best,n,w=audit(G);rows.append(dict(record=i,aut=len(G),swaps=n,maximum=best,example=w))
print(Counter(r['maximum'] for r in rows));mx=max(r['maximum'] for r in rows);print([(r['record'],r['aut']) for r in rows if r['maximum']==mx]);print(next(r['example'] for r in rows if r['maximum']==mx));(H/'ramsey_aligned_fiber_symmetry.json').write_text(json.dumps(rows,indent=2)+'\n')
