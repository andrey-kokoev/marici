"""Keep pair column identities fixed. Test for a common omitted blue triple."""
from itertools import combinations,product
from functools import lru_cache
from collections import defaultdict,Counter
from pathlib import Path
import json
from ramsey_table_cube_differences import analyze
from ramsey_quartet_live_probe import independent_sets


def audit():
    P={(i,i+1) for i in range(1,9)};rows=sorted(set().union(*(set(product(*[(v,v+1) for v in p['start']])) for p in analyze(9)['pieces'])));triples=[t for t in combinations(range(1,10),3) if not P.intersection(combinations(t,2))];seen=[defaultdict(dict) for _ in range(3)];counts=Counter();examples={}
    @lru_cache(None)
    def legal(rs):
        g=P|{(v,10+j) for j,r in enumerate(rs) for v in r};return not independent_sets(9+len(rs),g,7)
    @lru_cache(None)
    def missed(a,b):return {t for t in triples if set(t).isdisjoint(a+b)}
    for rs in combinations(rows,4):
        if not all(legal(sub) for sub in combinations(rs,3)):continue
        l,r=missed(*rs[:2]),missed(*rs[2:]);ok=legal(rs);assert ok==(not l&r);counts[ok]+=1
        key=tuple(tuple(sorted(set(a)&set(b))) for a,b in combinations(rs,2));info=dict(rows=rs,side_counts=[len(l),len(r)],common=sorted(l&r));
        for level,k in enumerate((key,(key,len(l),len(r)),(len(l),len(r)))):
            d=seen[level][k];d.setdefault(ok,info)
            if len(d)==2:examples.setdefault(level,dict(intersections=key,passes=d[True],fails=d[False]))
    out=dict(rows=len(rows),verdicts={str(k):v for k,v in counts.items()},key_order=['six pair intersections','intersections and both counts','counts alone'],mixed_keys=[sum(len(v)==2 for v in x.values()) for x in seen],examples=examples);print(out);(Path(__file__).resolve().parents[1]/'results/ramsey_tet_joint_miss.json').write_text(json.dumps(out,indent=2)+'\n')
if __name__=='__main__':audit()
