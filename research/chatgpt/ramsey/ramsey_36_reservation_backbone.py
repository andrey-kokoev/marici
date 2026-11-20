"""Test which single signs, other than the 14 stipulated signs, hold in all completions."""
from itertools import combinations
from pysat.solvers import Solver
v=range(1,18);es=list(combinations(v,2));x={e:i+1 for i,e in enumerate(es)}
R=set(range(11,15));ends={9,10}
def role(i):return 0 if i in R else 1 if i in ends else 2
classes={}
for e in es:classes.setdefault(tuple(sorted(map(role,e))),[]).append(e)
clauses=[[-x[e] for e in combinations(t,2)] for t in combinations(v,3)]+[[x[e] for e in combinations(t,2)] for t in combinations(v,6)]
for cls in ((0,0),(0,1)):
    for e in classes[cls]:clauses.append([-x[e]])
with Solver(name='cadical195',bootstrap_with=clauses) as sol:
    for cls,group in sorted(classes.items()):
        e=group[0];print(cls,len(group),[s for s in (-1,1) if sol.solve(assumptions=[s*x[e]])])
