"""Can a witnessed full Excel square be realized as four simultaneous ports?"""
from itertools import combinations
from collections import Counter
from pathlib import Path
import json


def audit(k):
    V=set(range(1,k+1));rows={frozenset(t) for t in combinations(sorted(V),3) if all(y-x>=2 for x,y in zip(t,t[1:]))};squares=set()
    for r in rows:
        ops=[frozenset((i,i+1)) for i in range(1,k) if len(r&{i,i+1})==1 and r^{i,i+1} in rows]
        for a,b in combinations(ops,2):
            if a&b or r^a^b not in rows:continue
            squares.add(tuple(sorted(tuple(sorted(s)) for s in (r,r^a,r^b,r^a^b))))
    path={(i,i+1) for i in range(1,k)};counts=Counter();example=None
    for sq in sorted(squares):
        outside=V-set().union(*sq);assert len(outside)==k-5
        for chord in [None,*[e for e in combinations(sorted(V),2) if e not in path]]:
            core=path|({chord} if chord else set());vs=range(1,k+5);red=core|{(i,k+j) for j,s in enumerate(sq,1) for i in s}
            if any(all(e in red for e in combinations(q,2)) for q in combinations(vs,3)):continue
            counts['triangle_free']+=1
            if any(all(e not in core for e in combinations(q,2)) for q in combinations(sorted(outside),3)):continue
            counts['outside_test_pass']+=1
            if any(all(e not in red for e in combinations(q,2)) for q in combinations(vs,7)):continue
            counts['full_pass']+=1
            if example is None:example=dict(rows=sq,chord=chord,outside=sorted(outside))
    return dict(width=k,squares=len(squares),counts=counts,example=example)
if __name__=='__main__':
    out=[audit(k) for k in (9,10,11)];print(out);(Path(__file__).resolve().parents[1]/'results/ramsey_joint_square_boundary.json').write_text(json.dumps(out,indent=2)+'\n')
