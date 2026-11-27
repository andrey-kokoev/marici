"""Construct one fixed probe per outside pair from square support alone; replay graph test."""
from itertools import combinations,permutations
from collections import Counter
from pathlib import Path
import json

V=set(range(1,11));path={(i,i+1) for i in range(1,10)};ind=lambda s:all(v+1 not in s for v in s)

def run():
    rows={frozenset(s) for s in combinations(V,3) if ind(s)};squares=set()
    for c in rows:
        ops=[{i,i+1} for i in range(1,10) if len(c&{i,i+1})==1 and c^{i,i+1} in rows]
        for a,b in combinations(ops,2):
            if a&b or c^a^b not in rows:continue
            squares.add(tuple(sorted(tuple(sorted(s)) for s in (c,c^a,c^b,c^a^b))))
    count=Counter();example=None
    for sq in sorted(squares):
        U=set().union(*sq);fixed=set.intersection(*map(set,sq));W=sorted(V-U);queries={}
        for a,b in combinations(W,2):
            if (a,b) in path:continue
            z=min(v for v in U-fixed if ind({a,b,v}));queries[a,b]={a,b,z}
        predictions=[]
        for perm in permutations(W[1:]):
            if perm[0]>perm[-1]:continue
            ring=(W[0],)+perm;cyc={tuple(sorted((ring[i-1],ring[i]))) for i in range(5)};core=path|cyc
            if any(set(e)<=set(W) and e not in cyc for e in path) or any(j-i==2 for i,j in cyc):continue
            read=set(path)&set(combinations(W,2));count['completions']+=1
            for pair,s in queries.items():
                red=core|{(i,11+j) for j,r in enumerate(sq) for i in r}|{(i,15) for i in s}|{(11+j,15) for j,r in enumerate(sq) if s.isdisjoint(r)}
                tri=any(all(e in red for e in combinations(q,2)) for q in combinations(range(1,16),3));seven=any(all(e not in red for e in combinations(q,2)) for q in combinations(range(1,16),7)) if not tri else False
                assert (not tri and not seven)==(pair not in cyc);count['direct_checks']+=1
                if tri or seven:read.add(pair)
            assert read==cyc;predictions.append(cyc)
        for a,b in combinations(predictions,2):
            e=min(a-b);assert e in queries;count['distinguished_pairs']+=1
            if example is None:example=dict(square=sq,edge=e,probe=sorted(queries[e]),reject_cycle=sorted(a),accept_cycle=sorted(b))
    assert count['completions']==122 and count['distinguished_pairs']==108;out=dict(counts=count,example=example);print(out);(Path(__file__).resolve().parents[1]/'results/ramsey_pentagon_edge_probe.json').write_text(json.dumps(out,indent=2)+'\n')
if __name__=='__main__':run()
