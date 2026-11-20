"""Minimum certificate under the quarter-turn x -> 5x, with center 0."""
from itertools import combinations,combinations_with_replacement
R=[(0,2,4,6),(0,2,6,9),(0,3,6,9)]
Q=[frozenset((x+i)%13 for x in r) for r in R for i in range(13)]
B=set(range(13,26));perm=[Q.index(frozenset(5*x%13 for x in q)) for q in Q]
miss=[{i for i,b in enumerate(Q) if not a&b} for a in Q];bad=[]
for a,b,c in combinations_with_replacement(miss,3):bad.append(a&b|a&c|b&c)
assert {next(iter(s)) for s in bad if len(s)==1}==B
res=[s for s in bad if not s&B];assert len(res)==26
cycles=[];left=set(range(39))-B
while left:
    i=min(left);orb=set()
    while i not in orb:orb.add(i);left.remove(i);i=perm[i]
    cycles.append(orb)
solutions=[]
for mask in range(1<<len(cycles)):
    s=set().union(*(c for j,c in enumerate(cycles) if mask>>j&1))
    if all(s&v for v in res):solutions.append(s)
m=min(map(len,solutions));sol=[s for s in solutions if len(s)==m];print('extra',m,'solutions',len(sol),'first',sorted(sol[0]));assert all((sol[0]|B)&v for v in bad)
for p in (0,26):
    print('residual failed shift sets:',sorted({tuple(sorted(i-p for i in v)) for v in res if all(p<=i<p+13 for i in v)})[:1])
