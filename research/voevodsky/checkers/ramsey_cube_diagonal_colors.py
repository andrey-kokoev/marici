"""Compare complete fresh-row colorings under both identifications of the two diagonal ports."""
from ramsey_cube_diagonal_pairs import profile,joint,marked_faces,charts,path,D,independent_sets,analyze
from itertools import combinations,product
from collections import Counter
import json


def colors(pf,group):
    g,opts=pf;n=len(group);out=set()
    for ms in product(*(opts[r] for r in group)):
        red=g|{(i,17+j) for j,m in enumerate(ms) for i in range(1,17) if m>>i&1};free=[(17+i,17+j) for i,j in combinations(range(n),2) if not ms[i]&ms[j]]
        for k in range(len(free)+1):
            for links in combinations(free,k):
                if k==3:continue  # at most three fresh rows; would close a triangle
                if not independent_sets(16+n,red|set(links),7):out.add((tuple((m>>15)&3 for m in ms),links))
    return out


def audit():
    records=[];hist=Counter();table=analyze(10);upper=sorted(list(map(tuple,table['leftover']))+[tuple(r) for p in table['pieces'] for r in p['new']]);sheets={'upper':upper,'mirror':[tuple(11-i for i in reversed(r)) for r in reversed(upper)]};census={s:c for s,_,c in charts()}
    for half,start,sq,opp in marked_faces():
        corners=set(sq+opp);rows=[r for r in combinations(range(1,11),3) if r not in corners and all(e not in path for e in combinations(r,2))];diag=[p for p in combinations(opp,2) if len(set(p[0])&set(p[1]))==1];sheet=sheets[half];later=set(sheet[max(sheet.index(r) for r in corners)+1:])
        for c in census.get(sq,[]):
            pf=[profile(sq,d,c,rows) for d in diag];sing=sorted(pf[0][1]);
            if set(sing)!=set(pf[1][1]):continue
            pairs=[set(joint(*p)) for p in pf]
            if pairs[0]!=pairs[1]:continue
            assert len(pairs[0])<6
            groups=[(r,) for r in sing]+sorted(pairs[0])+[t for t in combinations(sing,3) if all(p in pairs[0] for p in combinations(t,2))];diff=[[],[]];inter=[];single=[[],[]]
            for t in groups:
                a,b=[colors(p,t) for p in pf];assert a and b
                if {l for m,l in a}!={l for m,l in b}:inter.append(t)
                for swap in (False,True):
                    other={(tuple(((m&1)<<1 | (m>>1)) if swap else m for m in masks),l) for masks,l in b}
                    if len(t)==1:
                        for j in range(2):
                            allowed=[any(ms[0]&(1<<j) for ms,l in options) for options in (a,other)]
                            if allowed[0]!=allowed[1]:single[swap].append(dict(row=t[0],to_port=j,accepts=allowed.index(True)))
                    if a!=other:diff[swap].append(dict(rows=t,only_first=sorted(a-other),only_second=sorted(other-a)))
            key=(bool(diff[0]),bool(diff[1]),bool(inter));hist[key]+=1
            records.append(dict(square=sq,half=half,start=start,cycle=sorted(c),diagonals=diag,common_rows=sing,mutual_link_differences=inter,alignment_differences=diff,one_red=single,later=[any(set(d['rows'])<=later for d in ds) for ds in diff]))
    assert len(records)==12;print(hist);print(next((r for r in records if any(r['alignment_differences'])),None));(D/'ramsey_cube_diagonal_colors.json').write_text(json.dumps(dict(hist={str(k):v for k,v in hist.items()},records=records),indent=2)+'\n')
if __name__=='__main__':audit()
