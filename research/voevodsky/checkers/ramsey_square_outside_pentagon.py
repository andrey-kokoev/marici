"""Construct width-ten square cores by completing only the five outside sites."""
from itertools import combinations, permutations
from collections import Counter
from pathlib import Path
import json

V=set(range(1,11));path={(i,i+1) for i in range(1,10)}

def run():
    rows={frozenset(s) for s in combinations(sorted(V),3) if min(s[1]-s[0],s[2]-s[1])>=2};squares=set()
    for r in rows:
        mv=[frozenset((i,i+1)) for i in range(1,10) if len(r&{i,i+1})==1 and r^{i,i+1} in rows]
        for a,b in combinations(mv,2):
            if not a&b and r^a^b in rows:squares.add(tuple(sorted(tuple(sorted(s)) for s in (r,r^a,r^b,r^a^b))))
    hist=Counter();cost=Counter();examples={};rejected=[]
    for sq in sorted(squares):
        U=set().union(*sq);W=sorted(V-U);embedded={e for e in path if set(e)<=set(W)};good=0
        for tail in permutations(W[1:]):
            if tail[0]>tail[-1]:continue
            p=(W[0],)+tail;cycle={tuple(sorted((p[i-1],p[i]))) for i in range(5)};extra=cycle-path
            possible=embedded<=cycle and all(y-x!=2 for x,y in extra)
            core=path|cycle;red=core|{(i,j) for j,row in enumerate(sq,11) for i in row};vertices=range(1,15)
            valid=not any(all((e in red)==color for e in combinations(q,2)) for n,color in [(3,True),(7,False)] for q in combinations(vertices,n));assert valid==possible
            if valid:
                good+=1;cost[len(extra)]+=1;examples.setdefault(len(extra),dict(rows=sq,outside_cycle=p,extra=sorted(extra)))
        hist[good]+=1
        if not good:rejected.append(sq)
    out=dict(squares=len(squares),completion_histogram=dict(hist),valid_by_added_edges=dict(cost),examples=examples,impossible_squares=rejected);print(out);(Path(__file__).resolve().parents[1]/'results/ramsey_square_outside_pentagon.json').write_text(json.dumps(out,indent=2)+'\n')
if __name__=='__main__':run()
