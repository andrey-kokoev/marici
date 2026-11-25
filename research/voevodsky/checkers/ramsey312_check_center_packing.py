"""Test (do not assume) whether selected packing supports form a circular clique and have a compatible pair of endpoints."""
from ramsey312_google_two_step import *
from fractions import Fraction
import igraph as ig

def main():
 rows={tuple(map(int,(r:=l.split())[:5])):list(map(int,r[7:])) for l in (D/'ramsey312_five_neg_domains.txt').open()};T=list(sets(F,10));out=[]
 for r in json.loads((D/'ramsey312_center_packing.json').read_text()):
    w={Fraction(w) for x,w in r['packing']};xs=[x for x,w in r['packing']];n=len(xs);q=next(iter(w)).denominator if len(w)==1 else 0
    if n!=3*q+1:continue
    d=tuple(r['d']);h=F^sum(1<<v for v in d);ts=[t for t in T if not t&~h];s=rows[d];ms={x:sum(1<<i for i,t in enumerate(ts) if not t&x) for x in s};ok=lambda x,y:not x&y or not ms[x]&ms[y];G=ig.Graph(n=n,edges=[(i,j) for i,x in enumerate(xs) for j in range(i) if ok(x,xs[j])]);template=ig.Graph(n=n,edges=[(i,j) for i in range(n) for j in range(i) if q<=i-j<=n-q]);iso,perm,_=template.isomorphic_vf2(G,return_mapping_12=True);cand=[x for x in s if all(ok(x,y) for y in xs)];pairs=[(x,y) for j,x in enumerate(cand) for y in cand[:j] if ok(x,y)];out.append(dict(d=d,triple=r['triple'],iso=iso,cycle=[xs[i] for i in perm] if iso else None,pairs=pairs));print(d,iso,len(cand),len(pairs))
 (D/'ramsey312_center_packing_lifts.json').write_text(json.dumps(out))
if __name__=='__main__':main()
