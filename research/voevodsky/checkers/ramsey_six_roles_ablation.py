"""Six-role pilot: fixed five-role source, first six colex edges give the colored K4. Four star edges remain.
Customer = two-bit proposal for edges 04,14; product = proposal for 24,34. Offer tests red; response tests blue.
Polarity is explicit and exhaustive in this binary workload. Fold the endpoint axis by quotienting by simultaneous transpose.
Compare to an independent direct-color oracle. Exclude already forbidden prefixes. No fitted partitions."""
from itertools import combinations
from collections import defaultdict
from pathlib import Path
import json

def test(k):
    old=list(combinations(range(4),2));rows=[];full=(1<<16)-1
    for x in range(64):
        red={e for i,e in enumerate(old) if x>>i&1};blue=set(old)-red
        def clique(S,r,edges):return any(set(combinations(t,2))<=edges for t in combinations(sorted(S),r))
        if clique(range(4),3,red) or clique(range(4),k,blue):continue
        offer=response=oracle=0
        for a in range(4):
            for b in range(4):
                v=a+4*b;R={i for i in range(4) if v>>i&1};B=set(range(4))-R
                if not clique(R,2,red):offer|=1<<v
                if not clique(B,k-1,blue):response|=1<<v
                extended=red|{(i,4) for i in R};edges=set(combinations(range(5),2));
                if not clique(range(5),3,extended) and not clique(range(5),k,edges-extended):oracle|=1<<v
        assert offer&response==oracle
        rows.append((x,offer,response,oracle))
    def tr(m):return sum(1<<(i//4+4*(i%4)) for i in range(16) if m>>i&1)
    result={}
    for name,key in [('all',lambda o,r:(o,r)),('forget_offer',lambda o,r:r),('forget_response',lambda o,r:o),('forget_endpoint_orientation',lambda o,r:min((o,r),(tr(o),tr(r)))),('success_pairs_only',lambda o,r:o&r)]:
        g=defaultdict(list)
        for x,o,r,f in rows:g[key(o,r)].append((x,f))
        mixed=[v for v in g.values() if len({f for _,f in v})>1];example=None
        if mixed:
            v=mixed[0];(x,fx),(y,fy)=next((a,b) for a,b in combinations(v,2) if a[1]!=b[1]);s=((fx^fy)&-(fx^fy)).bit_length()-1;example={'prefix_red_edges':[[e for i,e in enumerate(old) if h>>i&1] for h in (x,y)],'suffix_red_neighbors':[i for i in range(4) if s>>i&1],'legal_in':[bool(z>>s&1) for z in (fx,fy)]}
        result[name]=dict(keys=len(g),ambiguous_keys=len(mixed),example=example)
    return dict(k=k,prefix_count=len(rows),results=result)
if __name__=='__main__':
    out=[test(k) for k in (3,4)];print(json.dumps(out,indent=1));(Path(__file__).resolve().parents[1]/'results/ramsey_six_roles_ablation.json').write_text(json.dumps(out,indent=1)+'\n')
