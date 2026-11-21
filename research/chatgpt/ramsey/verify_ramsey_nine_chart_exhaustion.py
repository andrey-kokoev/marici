"""Rooted embedding count. External premise: uniqueness up to isomorphism of the (3,9;35) graph. Enumerate all labeled fits of that graph to the fixed signature table, without assuming a modular relabeling on the chart."""
from itertools import permutations,combinations
from collections import Counter
from ramsey_address_to_cube import S,probes,D,json

def verify_charts():
    labels=sorted({d%35 for x in [1,7,11,16] for d in (x,-x)});steps=set(labels);V=set(range(1,35))-steps;cat={sum(1<<j for j,b in enumerate(labels) if (a-b)%35 in steps):a for a in V};assert len(cat)==len(set(S))==26
    E=[e for e in combinations(range(26),2) if not S[e[0]]&S[e[1]]];pos=[E.index(e) for e in probes];mult=Counter();examined=0
    for p in permutations(range(8)):
        examined+=1;coords=[]
        for s in S:
            mask=sum(1<<p[j] for j in range(8) if s>>j&1)
            if mask not in cat:break
            coords.append(cat[mask])
        else:
            assert len(set(coords))==26
            w=sum(1<<i for i,(a,b) in enumerate(E) if (coords[a]-coords[b])%35 in steps);mult[w]+=1
    by_code={tuple(w>>i&1 for i in pos):w for w in mult};assert len(mult)==len(by_code)==8 and set(mult.values())=={6};known=json.loads((D/'ramsey_nine_frame_readout.json').read_text())['coordinate_ordered_wirings'];assert all(by_code[tuple(k>>i&1 for i in range(3))]==w for k,w in enumerate(known));return dict(examined=examined,full_fits=sum(mult.values()),wiring_count=len(mult),multiplicities=sorted(mult.values()),outside_previously_known=len(set(mult)-set(known)))
if __name__=='__main__':
    result=verify_charts();print(result);(D/'ramsey_nine_chart_exhaustion.json').write_text(json.dumps(result)+'\n')
