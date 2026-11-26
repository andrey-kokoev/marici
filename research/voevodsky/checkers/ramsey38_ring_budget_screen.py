"""Necessary seven-label shell screens: tip count, then consistent edge fans/rings.
No shelling or ball search in screen(). Compare with first_ball only after classification.
"""
from itertools import combinations,permutations
from collections import Counter
from functools import lru_cache
from ramsey38_global_shell import sub

@lru_cache(None)
def pieces(p):
    return sub(p,4),sub(p,2)

def screen(p,ss,bd):
    cells,edges=pieces(p); forced={s for s in ss if len(s)==4};possible=set(cells);be=set.union(set(),*(sub(f,2) for f in bd));req=ss|bd
    # A boundary edge between two boundary faces of a single observed cell is locked.
    for t in forced:
        for f,h in combinations(bd&sub(t,3),2):
            e=f&h;possible-={u for u in cells if e<=u and u!=t}
    mandatory=set.union(set(),*(sub(s,2) for s in req));
    for e in mandatory-be:
        tips=set.union(set(),*(u-e for u in possible if e<=u))
        if len(tips)<3:return 'short-ring'
    while True:
        if not forced<=possible:return 'inconsistent'
        prior=(len(possible),len(forced));needed=req|forced
        for e in edges:
            incident={u for u in possible if e<=u};must=forced&incident
            if not incident and e not in mandatory and not must:continue
            boundary=e in be;ends=sorted(set.union(set(),*(f-e for f in bd if e<=f)));tips=p-e-set(ends)
            needed_tips=set.union(set(),*(s-e for s in needed if e<=s)); choices=[]
            for n in range(0 if boundary else 3,len(tips)+1):
                for q in permutations(tips,n):
                    if not boundary and (q[0]!=min(q) or q[1]>q[-1]):continue
                    order=(ends[0],)+q+(ends[1],) if boundary else q+(q[0],)
                    if not needed_tips<=set(order):continue
                    ts={e|{a,b} for a,b in zip(order,order[1:])}
                    if must<=ts<=incident:choices.append(ts)
            optional=e not in mandatory and not must
            if not choices and not optional:return 'inconsistent'
            possible-=incident-set.union(set(),*choices)
            if not optional:forced|=set.intersection(*choices)
        if (len(possible),len(forced))==prior:return 'pass'

if __name__=='__main__':
    import json
    from ramsey38_record3_polygon_trial import pf,rows,g
    from ramsey38_release_census import first_ball
    saved=json.loads(pf.read_text())['predictions'];counts=Counter();hits=[]
    for rk,ds in saved.items():
        root=int(rk);p=frozenset(g[root]);ss=set(rows(root).values());ls=sorted(p);mask=lambda s:sum(1<<ls.index(v) for v in s)
        for drop,a in ds.items():
            if a['class']!='original':continue
            bd=frozenset(map(frozenset,a['shell']));verdict=screen(p,ss,bd);ball=bool(first_ball(frozenset(map(mask,bd)),set(map(mask,ss))))
            assert verdict=='pass' or not ball;counts[verdict,ball]+=1
            if not ball:hits.append((root,int(drop),verdict))
    print(counts,hits)
