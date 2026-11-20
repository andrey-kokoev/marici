"""Role-aware direct transport comparators: keep each local seed-agreement bit attached to its role. Learn blue-clique clauses lazily; branch on a still-unhit positive clause while checking triangle conflicts. Starting with only forced-red variables is complete by monotonicity of the triangle prohibition."""
from itertools import permutations,combinations,product
from functools import lru_cache
from pathlib import Path
import json,sys
edge_pair_incidence='--edge-pair-incidence' in sys.argv
port_edge_incidence=edge_pair_incidence or '--port-edge-incidence' in sys.argv
endpoint_incidence=port_edge_incidence or '--endpoint-incidence' in sys.argv
corner_incidence=endpoint_incidence or '--corner-incidence' in sys.argv
incidence=corner_incidence or '--port-incidence' in sys.argv
V=range(4);X=[('c',i) for i in V]+[('p',*e) for e in permutations(V,2)]+[('e',*e) for e in combinations(V,2)]
def run(flat,roles,root_profiles=False):
    xs=[x for x in X if x[0] in roles];n=len(xs)
    def carry(a,b,i):return i if a==b else a if i==b else 6-a-b-i if flat else i
    seed=[carry(0,a,1) for a in V]
    def emits(x):
        t,a,*bs=x
        if not bs:return [(a,seed[a])]
        b,=bs;return [(a,b)] if t=='p' else [(a,b),(b,a)]
    keys={};E={}
    for i,j in combinations(range(n),2):
        x,y=xs[i],xs[j];sig=tuple(sorted((tuple(sorted(((x[0],s==seed[a]),(y[0],t==seed[b])))),carry(a,b,s)==t) for (a,s),(b,t) in product(emits(x),emits(y))))
        if incidence and x[0]==y[0]=='p':
            _,a,b=x;_,c,d=y
            relation='reverse' if (a,b)==(d,c) else 'source' if a==c else 'target' if b==d else 'chain' if a==d or b==c else 'disjoint'
            sig=(sig,relation)
        if corner_incidence and (x[0],y[0])==('c','p'):
            sig=(sig,'source' if x[1]==y[1] else 'target' if x[1]==y[2] else 'neither')
        if endpoint_incidence and (x[0],y[0])==('c','e'):
            sig=(sig,x[1] in y[1:])
        if port_edge_incidence and (x[0],y[0])==('p','e'):
            sig=(sig,(x[1] in y[1:],x[2] in y[1:]))
        if edge_pair_incidence and x[0]==y[0]=='e':
            sig=(sig,not set(x[1:]).isdisjoint(y[1:]))
        if root_profiles:
            def profile(z):
                entries=tuple(min(t,2) for t in z[1:]);return (z[0],tuple(sorted(entries)) if z[0]=='e' else entries)
            sig=(sig,tuple(sorted((profile(x),profile(y)))))
        E[i,j]=1<<keys.setdefault(sig,len(keys))
    if root_profiles:return E
    neg=sorted({E[i,j]|E[i,k]|E[j,k] for i,j,k in combinations(range(n),3)},key=int.bit_count);pos=[];full=(1<<len(keys))-1
    def visit(r,b):
        for c in neg:
            u=c&~r
            if not u:return None
            if not u&(u-1):b|=u
        clause=full+1;size=1000
        for c in pos:
            if not r&c:
                u=c&~b
                if not u:return None
                if u.bit_count()<size:clause=u;size=u.bit_count()
        if size==1000:return r
        while clause:
            v=clause&-clause;res=visit(r|v,b)
            if res is not None:return res
            b|=v;clause-=v
        return None
    for k in range(4 if incidence else 7,n+2):
        pos=[]
        while True:
            m=visit(0,0)
            if m is None:break
            adj=[0]*n
            for (i,j),v in E.items():
                if v&m:adj[i]|=1<<j;adj[j]|=1<<i
            @lru_cache(None)
            def independent(w):
                if not w:return 0
                b=w&-w;return max(independent(w^b),b|independent(w&~(b|adj[b.bit_length()-1])),key=int.bit_count)
            s=independent((1<<n)-1);independent.cache_clear()
            if s.bit_count()<k:return dict(classes=len(keys),alpha=k-1 if k>7 else s.bit_count(),red_edges=[ij for ij,b in E.items() if b&m])
            # All k-subsets of this independent set yield valid clauses; cap batch size.
            for idx,ss in enumerate(combinations([i for i in range(n) if s>>i&1],k)):
                c=0
                for e in combinations(ss,2):c|=E[e]
                pos.append(c)
                if idx>=63:break
out={}
for flat in ((True,False) if __name__=='__main__' else ()):
    for roles in ('p','cp','pe','cpe'):
        r=run(flat,roles);out[str((flat,roles))]=r;print(flat,roles,r['classes'],r['alpha'],flush=True)
if __name__=='__main__':(Path(__file__).with_name('ramsey_marked_edge_pair_incidence.json' if edge_pair_incidence else 'ramsey_marked_port_edge_incidence.json' if port_edge_incidence else 'ramsey_marked_endpoint_incidence.json' if endpoint_incidence else 'ramsey_marked_corner_incidence.json' if corner_incidence else 'ramsey_marked_port_incidence.json') if incidence else Path(__file__).with_suffix('.json')).write_text(json.dumps(out,indent=2)+'\n')
