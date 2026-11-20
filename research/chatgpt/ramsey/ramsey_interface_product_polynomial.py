"""Boundary-conditioned C5 join. Multiply row choices, retaining forbidden monochromatic sets. q grades free red links only."""
from itertools import combinations,product
from collections import Counter

def join(gap):
    boundary=(0,gap);left=tuple(i for i in range(5) if i not in boundary);right=(5,6,7)
    def cycle(order):return {frozenset((order[i],order[(i+1)%5])) for i in range(5)}
    cp=dict(zip(left,right));fixed=cycle(list(range(5)))|cycle([cp.get(i,i) for i in range(5)])
    def ok(V,E):
        return not any(all(frozenset(e) in E for e in combinations(t,2)) for t in combinations(V,3)) and not any(all(frozenset(e) not in E for e in combinations(t,2)) for t in combinations(V,4))
    # Start with one full cycle; insert private roles of second cycle with fixed internal and boundary data.
    states=[frozenset()];levels=[];V=list(range(5))
    for v in right:
        V.append(v);states=[s|row for s in states for mask in range(8) if ok(V,fixed|s|(row:=frozenset(frozenset((i,v)) for b,i in enumerate(left) if mask>>b&1)))];levels.append(len(states))
    result=Counter(map(len,states));assert sum(result.values())==(12 if gap==1 else 0);return levels,sorted(result.items())
if __name__=='__main__':
    for g in (1,2):print(('red','blue')[g-1],join(g))
