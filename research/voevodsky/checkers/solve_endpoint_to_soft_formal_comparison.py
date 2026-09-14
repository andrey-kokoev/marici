#!/usr/bin/env python3
"""Solve the integral linear constraints on an endpoint-port to base-soft comparison."""
import json
from pathlib import Path
R=Path(__file__).resolve().parents[3]
census=json.loads((R/'research/voevodsky/results/valg_relative_chain_candidate_census.json').read_text())
# A label-exchange equivariant map has M=[[a,b],[b,a]]. Preserve the oriented
# boundary iff a-b=1; preserve augmentation/degree iff a+b=1.
solutions=[]
for a in range(-8,9):
 for b in range(-8,9):
  M=[[a,b],[b,a]]
  if a-b==1 and a+b==1:solutions.append(M)
M=solutions[0];gamma=[1,-1];aug=[1,1]
def mv(A,v):return [sum(A[i][j]*v[j] for j in range(2)) for i in range(2)]
checks={'prior_census_passed':census['passed'],'unique_bounded_solution':len(solutions)==1,'solution_identity':M==[[1,0],[0,1]],'boundary_preserved':mv(M,gamma)==gamma,'augmentation_preserved':mv(M,aug)==aug,'determinant_unit':M[0][0]*M[1][1]-M[0][1]*M[1][0]==1}
assert all(checks.values()),checks
out={'schema':'marici.voevodsky.endpoint-to-base-soft-formal-comparison.v1','domain_basis':['xi=+1 unmarked CM port','xi=-1 marked residue-CM port (cone-shifted)'],'codomain_basis':['v=0 soft divisor','v=2 soft divisor'],'constraints':['commute with exchange of the two ordered labels','send the Stokes boundary (1,-1) to the soft divisor generator (1,-1)','preserve the augmentation (1,1)'],'general_exchange_equivariant_matrix':'[[a,b],[b,a]]','equations':['a-b=1','a+b=1'],'unique_integral_solution':M,'smith_invariants':[1,1],'formal_status':'unique unimodular chain-level candidate','geometric_status':'not source-authorized','remaining_obstruction':'No source specialization identifies xi=+1 with v=0 and the cone-shifted xi=-1 residue port with v=2. The identity matrix is forced after assuming that label assignment; it does not prove the assignment.','useful_consequence':'There is no normalization or finite-index ambiguity left. Any source-derived comparison satisfying the three constraints must be the identity (up to simultaneous reversal if both ordered bases are reversed).','next_falsifier':'derive or refute the labelled endpoint-to-soft assignment from the explicit homogeneous coordinate maps, comparing divisor pullbacks and normal Jacobians.','checks':checks,'passed':True}
d=R/'research/voevodsky/results/endpoint_to_base_soft_formal_comparison.json';d.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'passed':True,'matrix':M,'formal':out['formal_status'],'geometric':out['geometric_status']}))
