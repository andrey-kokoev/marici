"""Full-link pivot eligibility and residual list coloring on the twelve known six-chromatic cores. Certificates use indices into five_neg_domains rows, charges are deleted vertex labels."""
from ramsey312_google_two_step import *
import gzip

def color(V,N,B,skip=-1):
    with Solver(name='g4') as sl:
        for i in V:
            sl.add_clause([1+5*i+k for k in B[i] if k!=skip]);
            for j in N[i]&V:
                if j<i:
                    for k in B[i]&B[j]:
                        if k!=skip:sl.add_clause([-1-5*i-k,-1-5*j-k])
        if not sl.solve():return None
        m=set(sl.get_model());r={i:next(k for k in B[i] if k!=skip and 1+5*i+k in m) for i in V};assert all(r[i]!=r[j] for i in V for j in N[i]&V);return r

def run(row):
 d=list(map(int,row[:5]));s=list(map(int,row[7:]));h=F^sum(1<<v for v in d);A=[s.index(adj[i]&h) for i in d];ts=list(sets(h,10));miss=[sum(1<<j for j,t in enumerate(ts) if not t&x) for x in s];assert all(miss) and all(s);N=[{j for j,y in enumerate(s) if not x&y or not miss[i]&miss[j]} for i,x in enumerate(s)];B=[{k for k,a in enumerate(A) if a not in n} for n in N];V=set(range(len(s)));steps=[];summary=[]
 while True:
    leaf=color(V,N,B)
    if leaf is not None:break
    piv=[];rem=set();edges=sum(len(V&N[i]) for i in V)//2
    for i in sorted(V):
        for k in sorted(B[i]):
            c=color(V&N[i],N,B,k)
            if c is not None:piv.append([i,d[k],{j:d[z] for j,z in c.items()}]);break
        else:rem.add(i)
    steps.append(piv);summary.append([len(V),edges,len(piv)]);assert rem!=V,'stalled peeling';V=rem
 from itertools import combinations
 deg=sorted(len(V&N[i]) for i in V if V&N[i]);assert deg in ([1,1,2],[2,2,2,2]);pairs=[]
 for k,l in combinations(range(5),2):
    c=color(V,N,[b&{k,l} for b in B]);
    if c is not None:pairs.append([d[k],d[l]]);leaf=c
 print(d,summary,'residual',len(V),deg,'palettes',pairs,flush=True);return dict(d=d,steps=steps,summary=summary,leaf={i:d[k] for i,k in leaf.items()},leaf_edges=sum(deg)//2,leaf_pairs=pairs)
if __name__=='__main__':
 wanted={tuple(x['d']) for x in json.loads((D/'ramsey312_failed_cover_colorings.json').read_text()) if x['color'] is None};out=[run(row) for l in (D/'ramsey312_five_neg_domains.txt').open() if tuple(map(int,(row:=l.split())[:5])) in wanted];assert len(out)==12
 with gzip.open(D/'ramsey312_exchange_atlas.json.gz','wt') as f:json.dump(out,f,separators=(',',':'))
 (D/'ramsey312_exchange_atlas_summary.json').write_text(json.dumps([{k:r[k] for k in ('d','summary','leaf_edges','leaf_pairs')}|{'leaf_size':len(r['leaf'])} for r in out],indent=1))
