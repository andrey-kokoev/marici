#!/usr/bin/env python3
"""Test whether labelled deletion masks descend through the OR congruence."""
import itertools,json,math
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];R=ROOT/'research/benincasa/results'
assert json.loads((R/'cosmology_six_axis_cyclic_connector_coherence.json').read_text())['passed']
axes=('q_g3','q_G12','q_g1','q_G23','q_g2','q_G31');fiber=(0,0,1,1,2,2)
verts=list(itertools.product((0,1),repeat=6))
def F(v):return tuple(int(any(v[i] for i,x in enumerate(fiber) if x==j)) for j in range(3))
def labels(v):return tuple(axes[i] for i,b in enumerate(v) if b)
groups={t:[] for t in itertools.product((0,1),repeat=3)}
for v in verts:groups[F(v)].append(v)
sizes=sorted(map(len,groups.values()));assert sizes==[1,3,3,3,9,9,9,27]
collisions=sum(math.comb(len(g),2) for g in groups.values());assert collisions==468
nonconstant=sum(len({labels(v) for v in g})>1 for g in groups.values());assert nonconstant==7
witness=[]
for j in range(3):
 ids=[i for i,x in enumerate(fiber) if x==j]
 states=[]
 for bits in ((1,0),(0,1),(1,1)):
  v=[0]*6;v[ids[0]],v[ids[1]]=bits;states.append({'mask':labels(v),'target':F(v)})
 witness.append(states)
out={'schema':'marici.benincasa.cosmology-six-axis-fiber-congruence-source-descent.v1','domain_objects':64,'quotient_objects':8,'collapsed_object_excess':56,'identified_distinct_mask_pairs':collisions,'nonconstant_label_fibers':nonconstant,'three_state_fiber_witnesses':witness,'label_functor_factors_through_quotient':False,'reason':'singleton-only, pair-only, and both-deleted masks have the same occurrence image but distinct immutable source labels','unlabelled_descent_exists':True,'provenance_preserving_descent_exists':False,'conclusion':'the OR quotient realizes absorption only by erasing labelled deletion provenance, so it cannot authorize the connector','next_test':'construct a two-coloured occurrence refinement retaining singleton-complement versus same-pair provenance before any forgetful occurrence projection','passed':True};(R/'cosmology_six_axis_fiber_congruence_source_descent.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
