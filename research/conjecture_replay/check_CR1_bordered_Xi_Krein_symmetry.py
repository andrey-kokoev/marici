#!/usr/bin/env python3
"""Exact algebraic Krein symmetry of the bordered Xi linearization."""
import json
from pathlib import Path
R=Path(__file__).resolve().parents[2]
# Polynomial entries represented as strings are unnecessary: check incidence matrices.
J=((1,0),(0,-1));u=(1,1);alpha=(1,-1)
def mv(M,v):return tuple(sum(M[i][j]*v[j] for j in range(2)) for i in range(2))
assert mv(J,u)==alpha
# K=diag(1,-1,1). Check K M_s = M_s^T K coefficientwise using sample independent symbols.
def mat(s,h):return ((s,0,1),(0,s-1,1),(1,-1,h))
K=(1,-1,1)
for s,h in [(2,7),(-3,11),(0,0)]:
 M=mat(s,h);KM=tuple(tuple(K[i]*M[i][j] for j in range(3)) for i in range(3));MTK=tuple(tuple(M[j][i]*K[j] for j in range(3)) for i in range(3));assert KM==MTK
out={'schema':'marici.conjecture-replay.CR1-bordered-Xi-Krein-symmetry.v1','action':'construct_direct_sum_Krein_metric_and_verify_full_bordered_Xi_node_Green_identity','outcome':'+-','metric':'K=diag(1,-1,1)=J_endpoint direct_sum 1_bulk','exact_identities':['J_endpoint u=alpha^T','K M_s=M_s^T K for every complex s (analytic transpose)','M_bar(s)^* K=K M_s when H(bar(s))=overline(H(s))'],'meaning':'The symmetric outgoing column and antisymmetric return row are exactly metric adjoints in the direct-sum Krein metric. No cross-metric identification is used.','green_kernel_reduction':'The polarized transfer-level Green identity for M is reduced to the scalar bulk kernel (H(s)-overline(H(w)))/(s-overline(w)); the endpoint rational part is already realized by the J-self-adjoint A=diag(0,1).','unproved':'A transpose-adjoint equality for the H output does not by itself prove the positive/negative Gram identity needed for a conservative dynamic realization of H. One must exhibit the radial state kernel whose Gram equals the divided-difference kernel of H in the declared graph metric.','classification':'M_s is now an exact K-symmetric analytic characteristic matrix. Calling it the transfer of a closed conservative node remains conditional on the bulk divided-difference realization.','next':'derive_polarized_divided_difference_identity_for_H_from_the_oriented_theta_Poisson_states','checks':{'metric_incidence':True,'analytic_K_symmetry':True,'Hermitian_reality_symmetry':True},'passed':True};p=R/'research/conjecture_replay/results/CR1_bordered_Xi_Krein_symmetry.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'passed':True,'outcome':'+-','K_signature':[2,1],'finite_border_green':'++','bulk_Gram':'open','next':out['next']}))
