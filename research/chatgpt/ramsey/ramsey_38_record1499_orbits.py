"""Audit a symmetry-only copier and replay record 1499 from its edge orbit seeds."""
from itertools import combinations
from collections import Counter
import igraph as ig
from ramsey_38_cube_inversion import sign

edges=set(combinations(range(27),2));positive={e for e in edges if sign(*e)}
g=ig.Graph(27,list(positive));group=g.get_automorphisms_vf2()
def orbit(e):return {tuple(sorted((p[e[0]],p[e[1]]))) for p in group}
reps=[e for e in sorted(edges) if e==min(orbit(e))];seeds=[e for e in reps if e in positive]
replayed={s for e in seeds for s in orbit(e)};assert replayed==positive
print('group size, all pair orbits, positive orbits, positive links:',len(group),len(reps),len(seeds),len(positive))
outer=set(range(27))-{4,13,22};print('pair orbits outside old block:',sum(not any(i in outer and j in outer for i,j in orbit(e)) for e in reps))
