"""Exact cube unions on the upper half of the Excel greedy mirror completion. No Ramsey numbers as input."""
from itertools import combinations,product
from collections import Counter
from pathlib import Path
import json

def analyze(k):
    rows=[p for p in combinations(range(1,k+1),3) if min(p[1]-p[0],p[2]-p[1])>=2];lo,hi=0,len(rows)-1;upper=[];center=[]
    while lo<=hi:
        ends=rows[lo]==tuple(k+1-i for i in reversed(rows[hi]))
        if ends and lo==hi:center=[rows[lo]];break
        upper.append(rows[lo]);lo+=1;hi-=ends
    U=set(upper);assert len(U)==len(upper);seen=set();pieces=[];cubes=[]
    for a in combinations(range(1,k),3):
        corners=set(product(*[(v,v+1) for v in a]));
        if corners<=U:cubes.append((a,corners))
    for a,C in cubes:
        d=C-seen;seen|=C;pieces.append(dict(start=a,new=sorted(d),box=bool(d) and set(product(*map(set,zip(*d))))==d))
    rest=sorted(U-seen);assert Counter(x for p in pieces for x in p['new'])+Counter(rest)==Counter(upper)
    rebuilt=sorted([x for p in pieces for x in p['new']]+rest);assert rebuilt==upper
    return dict(width=k,upper=len(U),center=center,cubes=len(cubes),union=len(seen),pieces=pieces,leftover=rest,display_rows=2*len(U)+len(center))
if __name__=='__main__':
    out=[analyze(k) for k in range(6,14)]
    for r in out:print(r['width'],r['upper'],r['cubes'],r['union'],len(r['leftover']),[len(p['new']) for p in r['pieces']][:25],sum(not p['box'] for p in r['pieces']))
    (Path(__file__).resolve().parents[1]/'results/ramsey_table_cube_differences.json').write_text(json.dumps(out))
