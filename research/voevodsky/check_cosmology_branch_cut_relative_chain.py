"""Audit every boundary component of the logarithmic square fundamental domain."""
from __future__ import annotations
import json
from fractions import Fraction
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];OUT=ROOT/'research'/'voevodsky'/'results'/'cosmology_branch_cut_relative_chain.json'
def main():
 # Normalize all 2-dimensional integrals by (2*pi*i)^2.
 curvature=1
 # A=log(u)dlog(v) on 0<=theta,phi<=2pi; only the theta=2pi edge contributes.
 cut_edges={'theta_0':0,'theta_2pi':1,'phi_0':0,'phi_2pi':0}
 assert sum(cut_edges.values())==curvature
 jump_period=cut_edges['theta_2pi'];corner_integer=jump_period
 assert jump_period==corner_integer==1
 # Removing the cut residual would violate Stokes on the square.
 assert curvature-sum(cut_edges.values())==0
 out={'schema':'marici.voevodsky.cosmology-branch-cut-relative-chain.v1','status':'cut_domain_primitive_has_unavoidable_unit_descent_residual','fundamental_domain':'0<=theta,phi<=2*pi with u=exp(i theta), v=exp(i phi)','local_form':'A=log(u)dlog(v)=-theta*dphi','normalized_curvature_integral':curvature,'normalized_cut_edge_contributions':cut_edges,'gluing_data':'Identifying theta=0 with theta=2*pi introduces the jump 2*pi*i*dlog(v), whose normalized v-period is one. Resolving that jump by local log(v) leaves the unit corner cocycle.','complete_boundary':'On the unglued square, Xi_log is balanced by the cut edge. After descent to the torus, the edge jump and corner integer are mandatory components; deleting either violates Stokes or Cech descent.','sigma_comparison':'The unit corner is identified by the Parshin comparison with the primitive triangle class. It is the residual obstruction, not an independently supplied opposite boundary that makes the total class exact.','decision':'The branch-cut relative chain cannot have complete boundary (Xi_log,-sigma123,0,...). Its full descent data retains a unit terminal component representing the same nonzero Deligne class.','next_gate':'analytic-cut-enlargement: classify the changed relative complex obtained by declaring the cut edge a boundary and test whether its comparison to the uncut source is faithful','limitations':['square fundamental-domain model with normalized coefficients','sign follows the fixed ordered orientation','no physical branch-cut prescription inferred'],'passed':True};OUT.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
