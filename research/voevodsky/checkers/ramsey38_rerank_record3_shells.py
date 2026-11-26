"""Retrospectively rerank polygon proposals without consulting a saved filling."""
from ramsey38_record3_polygon_trial import g,rows,poly,fmt
from ramsey38_ring_budget_screen import screen
from ramsey38_alternating_boundary_paths import find
from ramsey38_release_census import first_ball
from collections import Counter
if __name__=='__main__':
    for root,d in [(4,17),(14,25),(20,22),(26,17)]:
        ss=set(rows(root).values());p=frozenset(g[root]);labels=sorted(p);mask=lambda s:sum(1<<labels.index(v) for v in s)
        _,opts=poly.predict(g,root,d);candidates=[bd for bd in sorted(opts[None],key=fmt) if poly.compatible(bd,ss)]
        survive=[bd for bd in candidates if screen(p,ss,bd)=='pass' and not find(ss|bd,bd)]
        actual=lambda bd:bool(first_ball(frozenset(map(mask,bd)),set(map(mask,ss))))
        stats=Counter((b in survive,actual(b)) for b in candidates);assert not stats[False,True]
        print(root,d,'before',len(candidates),'after',len(survive),'exact-shell checks',stats,'first fills',bool(survive) and actual(survive[0]),flush=True)
