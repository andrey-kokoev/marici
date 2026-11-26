"""Root 7, global wheel/link obstruction. No enumeration of candidate repairs."""
from ramsey38_support_ball_completion import N

root=7
rows={v:frozenset(N[root]&N[v]) for v in N if v not in N[root]|{root}}
# Boundary cycle and four spokes, with row witnesses for each edge.
cycle=(3,11,27,9,21); witnesses=(2,1,8,17,20)
hub=6; tips=(3,11,9,21); spokes=(15,19,5,18)
assert len(set(cycle))==5 and hub not in cycle
assert tuple(v for v in cycle if v in tips)==tips
for i,v in enumerate(cycle):assert {v,cycle[(i+1)%5]}<=rows[witnesses[i]] and len(rows[witnesses[i]])<=3
for v,r in zip(tips,spokes):assert {hub,v}==rows[r]
# In a sphere, disjoint spokes on one side of a simple cycle preserve rim
# order (up to reversal) at their hub. Thus tips alternate in the link disk.
a,b,c,d=tips
assert {hub,a,c}<=rows[23] and {hub,b,d}<=rows[4]
assert len(rows[23])==len(rows[4])==4
print('boundary cycle:',cycle,'hub:',hub,'tip order:',tips)
print('link chords forced by rows 23 and 4:',(a,c),(b,d))
