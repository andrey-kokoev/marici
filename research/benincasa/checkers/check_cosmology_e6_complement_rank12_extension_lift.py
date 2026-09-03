#!/usr/bin/env python3
"""Classify cyclic shear freedom in lifting the primitive A2 complement."""
import itertools,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];R=ROOT/'research/benincasa/results'
corr=json.loads((R/'cosmology_e6_common_weight_divisibility_gate.json').read_text());gate=json.loads((R/'cosmology_e6_rank12_triangular_transport_gate.json').read_text());census=json.loads((R/'cosmology_rank12_shear_artifact_census.json').read_text())
assert corr['passed'] and gate['passed'] and census['passed']
Q=((0,-1),(1,-1))
def mm(A,B):return tuple(tuple(sum(A[i][k]*B[k][j] for k in range(2)) for j in range(2)) for i in range(2))
comm=[]
for x,y,z,w in itertools.product(range(-3,4),repeat=4):
 M=((x,y),(z,w))
 if mm(M,Q)==mm(Q,M):comm.append(M)
assert all(M[1][0]==-M[0][1] and M[1][1]==M[0][0]+M[0][1] for M in comm)
expected={((x,y),(-y,x+y)) for x,y in itertools.product(range(-3,4),repeat=2) if -3<=x+y<=3}
assert set(comm)==expected
T0=gate['underdetermination_witness']['two_lifts'][0];T1=gate['underdetermination_witness']['two_lifts'][1]
N=[[T1[i][j]-T0[i][j] for j in range(2)] for i in range(2)];assert N==[[0,1],[0,0]]
out={'schema':'marici.benincasa.cosmology-e6-complement-rank12-extension-lift.v1','associated_grade_complement_primitive':True,'A2_cyclic_matrix':[list(r) for r in Q],'equivariant_shear_centralizer':'M(x,y)=[[x,y],[-y,x+y]]','centralizer_parameter_rank':2,'bounded_centralizer_check_count':len(comm),'two_existing_formal_lifts':[T0,T1],'lift_difference':N,'lift_difference_nonzero_but_graded_invisible':True,'cyclic_equivariance_selects_unique_lift':False,'extension_lift_realized':False,'missing_selection_equations':['marked q0 action','C2 dlog(X3/X2) shear coefficients','full rank-twelve connection','connector naturality components'],'conclusion':'the primitive A2 complement admits a rank-two lattice of cyclic extension shears; current data do not select a rank-twelve lift','next_test':'determine whether the sourced dlog(X3/X2) divisor root defines a specific centralizer element M(x,y)','passed':True};(R/'cosmology_e6_complement_rank12_extension_lift.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
