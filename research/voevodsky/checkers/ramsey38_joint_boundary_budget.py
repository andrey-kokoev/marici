"""Test rows 6 and 17 on the boundary simultaneously, for a fixed added-cell budget."""
from itertools import combinations
from math import comb
from ramsey38_support_ball_completion import N,P,rows,forced,pool,shelling,fmt
from ramsey38_compare_support_fillings import boundary

def scan(k):
    tri=frozenset(N[1]&N[6]);edge=frozenset(N[1]&N[17]);universe=sorted(forced,key=sorted)+pool
    def carriers(f):return sum(1<<i for i,t in enumerate(universe) if f<=t)
    must=[carriers(r) for r in rows if not any(r<=t for t in forced)]
    tri_mask=carriers(tri);faces=[carriers(edge|{v}) for v in P if v not in edge]
    f0=(1<<len(forced))-1; wins=0; example=None; hidden_profiles={}; nested=0
    short={v:frozenset(N[1]&N[v]) for v in N if v!=1 and v not in N[1] and len(N[1]&N[v])<4}
    for opts in combinations(range(len(forced),len(universe)),k):
        m=f0+sum(1<<i for i in opts)
        if (m&tri_mask).bit_count()!=1 or not all(m&h for h in must):continue
        if sum((m&f).bit_count()==1 for f in faces)!=2:continue
        ts=forced.union(universe[i] for i in opts); order=shelling(ts)
        if order:
            bd=boundary(ts);assert tri in bd and any(edge<=f for f in bd)
            hidden=tuple(v for v,r in short.items() if not any(r<=f for f in bd));hidden_profiles[hidden]=hidden_profiles.get(hidden,0)+1
            if any(all(any(r<=t for t in ts-{x}) for r in rows) and shelling(ts-{x}) for x in ts-forced):nested+=1
            wins+=1
            if example is None:example=order
    print(k,'added;',comb(len(pool),k),'choices;',wins,'joint-boundary balls')
    print('hidden short-row profiles:',hidden_profiles,'contain a five-addition shellable completion:',nested)
    if example:print('shelling:',fmt(example),'boundary:',fmt(sorted(boundary(example),key=sorted)))
    return wins
if __name__=='__main__':scan(6)
