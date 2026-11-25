"""Endpoint-first center packing. Try every compatible pair outside the center family, not saved pivots. Reuse equal restricted families and certify rational optima."""
from ramsey312_center_packing import *
import igraph as ig
from collections import Counter

def main():
 T=list(sets(F,10));out=[]
 for line in (D/'ramsey312_five_neg_domains.txt').open():
    z=line.split();d=list(map(int,z[:5]));s=list(map(int,z[7:]));h=F^sum(1<<v for v in d);ts=[t for t in T if not t&~h];ms=[sum(1<<j for j,t in enumerate(ts) if not t&x) for x in s];ok=lambda i,j:not s[i]&s[j] or not ms[i]&ms[j];trip=[(a,adj[a[0]]&adj[a[1]]&adj[a[2]]&h) for a in combinations(d,3)];ma=max(c.bit_count() for a,c in trip)
    for a,c in trip:
        if c.bit_count()!=ma:continue
        inside=[i for i,x in enumerate(s) if x&c==c];outside=set(range(len(s)))-set(inside);L={i:frozenset(j for j in inside if ok(i,j)) for i in outside};hist=Counter();cache={};cert=[]
        for i,j in combinations(sorted(outside),2):
            if not ok(i,j):continue
            v=L[i]&L[j]
            if len(v)<7:hist['small']+=1;continue
            f=tuple(i for i in sorted(v,key=s.__getitem__) if not any(i!=j and s[i]&s[j]==s[i] for j in v));
            if f not in cache:
                if len(f)<7:cache[f]=('few facets',[])
                else:
                    full=(1<<len(f))-1;cols={v:sum(1<<j for j,i in enumerate(f) if s[i]>>v&1) for v in bits(h)};rows=set()
                    for t in ts:
                        p=full
                        for v in bits(t):p&=~cols[v]
                        if p:rows.add(p)
                    M=[]
                    for p in sorted(rows,key=lambda p:(-p.bit_count(),p)):
                        if not any(r&p==p for r in M):M.append(p)
                    res=linprog([-1]*len(f),A_ub=[[r>>j&1 for j in range(len(f))] for r in M],b_ub=[1]*len(M),method='highs');assert res.success;w=[Fraction(float(x)).limit_denominator(10000) for x in res.x];u=[Fraction(float(-x)).limit_denominator(10000) for x in res.ineqlin.marginals];assert min(w)>=0 and min(u)>=0 and all(sum(w[j] for j in bits(r))<=1 for r in M) and all(sum(t for r,t in zip(M,u) if r>>j&1)>=1 for j in range(len(f))) and sum(w)==sum(u);xs=[i for i,t in zip(f,w) if t];n=len(xs);q=n//3;cycle=[]
                    if n in (7,10):
                        G=ig.Graph(n=n,edges=[(x,y) for x,y in combinations(range(n),2) if ok(xs[x],xs[y])]);H=ig.Graph(n=n,edges=[(x,y) for x,y in combinations(range(n),2) if q<=y-x<=n-q]);iso,perm,_=H.isomorphic_vf2(G,return_mapping_12=True)
                        if iso:cycle=[s[xs[k]] for k in perm]
                    cache[f]=(str(sum(w)),cycle)
            val,cycle=cache[f];hist[val]+=1
            if cycle:cert.append(dict(endpoints=[s[i],s[j]],cycle=cycle))
        out.append(dict(d=d,triple=a,hist=dict(hist),cert=cert));print(d,a,'pairs',sum(hist.values()),'domains',len(cache),'cycles',len(cert),'hist',hist,flush=True)
 (D/'ramsey312_conditioned_packing.json').write_text(json.dumps(out))
if __name__=='__main__':main()
