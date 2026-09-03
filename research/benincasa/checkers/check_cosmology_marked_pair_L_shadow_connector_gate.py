#!/usr/bin/env python3
"""Solve the cyclic integral sign-conversion problem on the L orbit."""
import itertools,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];R=ROOT/'research/benincasa/results'
assert json.loads((R/'cosmology_three_colour_marked_occurrence_refinement.json').read_text())['passed']
l=(0,-1,-1);s=(0,-1,1)
def mat(a,b,c):return ((a,b,c),(c,a,b),(b,c,a))
def mv(M,v):return tuple(sum(M[i][j]*v[j] for j in range(3)) for i in range(3))
sol=[]
for a,b,c in itertools.product(range(-4,5),repeat=3):
 M=mat(a,b,c)
 if mv(M,l)==s:sol.append((a,b,c,M))
assert len(sol)==1 and sol[0][:3]==(0,1,-1)
A=sol[0][3];assert A==((0,1,-1),(-1,0,1),(1,-1,0)) and all(sum(r)==0 for r in A)
A2=tuple(tuple(sum(A[i][k]*A[k][j] for k in range(3)) for j in range(3)) for i in range(3))
assert A2==((-2,1,1),(1,-2,1),(1,1,-2))
out={'schema':'marici.benincasa.cosmology-marked-pair-L-shadow-connector-gate.v1','L_axis_order':['g12','g23','g31'],'literal_L_vector':list(l),'oriented_shadow':list(s),'unique_cyclic_integral_converter':[list(r) for r in A],'converter_properties':{'circulant':True,'skew_symmetric':True,'row_sums_zero':True,'rank':2,'square':[list(r) for r in A2]},'sign_conversion_exact':True,'ordered_cocycle_sum_zero':sum(mv(A,l))==0,'formal_connector_exists':True,'source_authorized':False,'source_blockers':['q_g12 is absent from the literal five-mark word','domain marked-pair axes and codomain occurrence axes are not identified','interpreting the skew circulant as an ordered incidence map requires the missing complement labelling morphism'],'conclusion':'orientation determines a unique formal cyclic converter, but not a typed source chain map','next_test':'factor the skew circulant through the ordered triangle incidence and complement maps, then test whether those maps are source-derived','passed':True};(R/'cosmology_marked_pair_L_shadow_connector_gate.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
