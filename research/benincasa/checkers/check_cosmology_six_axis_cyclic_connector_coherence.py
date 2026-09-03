#!/usr/bin/env python3
"""Audit the Boolean-cube coherence of the six-to-three axis map."""
import itertools,json,math
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];R=ROOT/'research/benincasa/results'
assert json.loads((R/'cosmology_connector_cyclic_equivariance_gate.json').read_text())['passed']
# Axis fibers: (q_g3,q_G12)->G12, (q_g1,q_G23)->G23, (q_g2,q_G31)->G31.
fiber=(0,1,2,0,1,2)
verts=list(itertools.product((0,1),repeat=6))
def F(v): return tuple(int(any(v[i] for i,x in enumerate(fiber) if x==j)) for j in range(3))
edges=6*2**5;squares=math.comb(6,2)*2**4
same=0;different=0
for i,j in itertools.combinations(range(6),2):
 for rest in itertools.product((0,1),repeat=4):
  v=[0]*6;k=0
  for a in range(6):
   if a not in (i,j):v[a]=rest[k];k+=1
  vi=v.copy();vi[i]=1;vj=v.copy();vj[j]=1;vij=vi.copy();vij[j]=1
  assert F(vij)==F(tuple(vj[:i]+[1]+vj[i+1:]))
  if fiber[i]==fiber[j]:same+=1
  else:different+=1
assert (len(verts),edges,squares,same,different)==(64,192,240,48,192)
fibers={str(t):sum(F(v)==t for v in verts) for t in itertools.product((0,1),repeat=3)}
assert sorted(fibers.values())==[1,3,3,3,9,9,9,27]
out={'schema':'marici.benincasa.cosmology-six-axis-cyclic-connector-coherence.v1','domain':{'vertices':64,'edges':192,'squares':240},'target':{'vertices':8,'edges':12,'squares':6},'vertex_map':'Boolean OR on each two-axis fiber','target_vertex_fiber_sizes':fibers,'formal_monotone_functor':True,'square_classification':{'different_target_axis_squares':different,'same_target_axis_absorption_squares':same},'same_fiber_relation':'the first deletion maps to the target deletion and the second to identity, in either order','formal_cube_coherence':True,'source_realized':False,'source_blocker':'48 absorption squares require singleton-complement and same-pair deletions to become the same target operation, with the second operation trivial after the first; no such source quotient is defined','next_test':'construct the fiber-congruence quotient and test whether the source relation module descends without erasing labelled deletion data','passed':True};(R/'cosmology_six_axis_cyclic_connector_coherence.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
