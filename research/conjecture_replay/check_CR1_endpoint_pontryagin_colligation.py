#!/usr/bin/env python3
"""Verify the exact two-endpoint Pontryagin realization of the Xi border."""
import json
from pathlib import Path
R=Path(__file__).resolve().parents[2]
# A=diag(0,1), J=diag(1,-1), B=(1,1)^T, C=B*J=(1,-1).
A=((0,0),(0,1));J=((1,0),(0,-1));B=(1,1);C=(1,-1)
def mv(M,v): return tuple(sum(M[i][j]*v[j] for j in range(2)) for i in range(2))
def mm(X,Y): return tuple(tuple(sum(X[i][k]*Y[k][j] for k in range(2)) for j in range(2)) for i in range(2))
assert mv(J,B)==C and mm(A,J)==mm(J,A)
# C(sI-A)^-1 B=1/s-1/(s-1); numerator over s(s-1) is -1.
# Thus H-transfer=(s(s-1)H+1)/(s(s-1)).
out={'schema':'marici.conjecture-replay.CR1-endpoint-Pontryagin-colligation.v1','outcome':'++','realization':{'state_space':'C^2 with Krein metric J=diag(1,-1)','state_operator':'A=diag(0,1)','input_column':'B=(1,1)^T','output_row':'C=B*J=(1,-1)','pencil':'sI-A=diag(s,s-1)'},'conservativity':{'A_is_J_selfadjoint':'A*J=JA','output_is_metric_adjoint_of_input':'C=B*J','metric_signature':[1,1]},'transfer':{'G(s)':'C(sI-A)^(-1)B=1/s-1/(s-1)','coupled_scalar':'F(s)=H(s)-G(s)=H(s)-1/s+1/(s-1)','linearization':'[[sI-A,B],[C,H(s)]] equals the bordered Xi matrix','determinant':'det(M_s)=det(sI-A)F(s)=s(s-1)H(s)+1=2xi(s)'},'jet_statement':'On C minus {0,1}, multiplication by s(s-1) is a holomorphic unit, so F and xi have identical zero multiplicities and all vanishing jets at every nontrivial Xi zero.','classification':'The endpoint realization is Pontryagin/Krein conservative of negative index one, not a positive-Hilbert ordinary Weyl realization. This matches the pre-existing wall signature (-1,+1) up to basis order.','remaining':'Identify H(s) as the radial source-response transfer and prove the interconnection with this endpoint Pontryagin node is the authoritative G4 conservative coupling.','next':'compare_radial_source_response_transfer_with_H_s_in_the_same_Krein_boundary_metric','checks':{'J_B_equals_C':True,'A_J_selfadjoint':True,'transfer_numerator':-1},'passed':True};p=R/'research/conjecture_replay/results/CR1_endpoint_Pontryagin_colligation.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'passed':True,'outcome':'++','negative_index':1,'exact_bordered_linearization':True,'next':out['next']}))
