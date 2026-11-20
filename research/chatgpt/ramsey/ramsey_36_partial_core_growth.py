"""Can the partially doubled reservation reach 17? No catalogue input.
0,1=endpoints; 2..5=witnesses; 6+2i,7+2i=private neighbors of witness i.
"""
from itertools import combinations,permutations,product
from collections import Counter
from pysat.solvers import Solver

def shape(t,arcs):
    return min(tuple(int((p[i],p[j]) in arcs) for i in range(t) for j in range(t) if i!=j) for p in permutations(range(t)))

def main():
    n=17;v=range(n);var={e:j+1 for j,e in enumerate(combinations(v,2))}
    clauses=[[-var[e] for e in combinations(s,2)] for s in combinations(v,3)]+[[var[e] for e in combinations(s,2)] for s in combinations(v,6)]
    for t in (1,2,3,4):
        counts=Counter();cached={};pairs=list(combinations(range(t),2))
        with Solver(name='cadical195',bootstrap_with=clauses) as sol:
            for choices in product((1,2,3),repeat=len(pairs)):
                arcs=set()
                for (i,j),c in zip(pairs,choices):
                    if c&1:arcs.add((i,j))
                    if c&2:arcs.add((j,i))
                key=shape(t,arcs)
                if key not in cached:
                    pos={(0,1)}
                    for i in range(t):pos.update(((0,6+2*i),(1,7+2*i),(2+i,6+2*i),(2+i,7+2*i)))
                    pos.update(tuple(sorted((6+2*i,7+2*j))) for i,j in arcs)
                    fixed=[var[e] if e in pos else -var[e] for e in combinations(range(6+2*t),2)]
                    cached[key]=sol.solve(assumptions=fixed)
                cycle=any((i,j) in arcs and (j,k) in arcs and (k,i) in arcs for i,j,k in permutations(range(t),3))
                counts[(choices.count(3),cycle,cached[key])]+=1
        print(t,'labelled patterns grouped by (# reciprocal pairs, has directed triangle, completes):',sorted(counts.items()),flush=True)
if __name__=='__main__':main()
