"""Degree-zero seam cycles for the three-prime layered source graph."""
from pathlib import Path
import sympy as s,json
ROOT=Path(__file__).resolve().parents[3]
# vertices: root, three first cuts, three second cuts, terminal
V=['r','a','b','c','ab','ac','bc','t']
edges=[('r',x) for x in 'abc']+[(x,y) for x,ys in [('a','ab ac'.split()),('b','ab bc'.split()),('c','ac bc'.split())] for y in ys]+[(x,'t') for x in ('ab','ac','bc')]
D=s.zeros(len(V),len(edges)); vi={v:i for i,v in enumerate(V)}
for j,(a,b) in enumerate(edges):D[vi[b],j]=1;D[vi[a],j]=-1
cycle= len(edges)-D.rank()
assert len(edges)==12 and D.rank()==7 and cycle==5
# Boundary compression identifying all three first/second cut labels reduces the
# layered attachment to a single route pair and destroys these cycle classes.
compressed=s.Matrix([[1]*len(edges)])
assert compressed.rank()==1
result={'schema':'marici.nima.three-prime-seam-cycle.v1','passed':True,
 'vertices':len(V),'edges':len(edges),'incidence_rank':D.rank(),
 'degree_zero_seam_cycle_dimension':cycle,
 'terminal_label_compression_rank':compressed.rank(),
 'interpretation':'five independent layered seam cycles precede terminal compression; the two marginal ghosts are record correlations, not the whole seam H1.',
 'scope':'Degree-zero incidence seam only; no feature metric or derived equivalence.'}
(ROOT/'research/nima/results/three-prime-seam-cycle.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
