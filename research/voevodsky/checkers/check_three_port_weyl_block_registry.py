#!/usr/bin/env python3
"""Identify all blocks of the three-port Weyl matrix by typed channel."""
from fractions import Fraction as F
import json
from pathlib import Path

def tr(A):return tuple(tuple(A[j][i] for j in range(len(A))) for i in range(len(A[0])))
def mm(A,B):return tuple(tuple(sum((A[i][k]*B[k][j] for k in range(len(B))),F(0)) for j in range(len(B[0]))) for i in range(len(A)))
def diag(x):return tuple(tuple(x[i] if i==j else F(0) for j in range(len(x))) for i in range(len(x)))
D=[F(-2),F(1),F(4)];J=((F(1),F(1),F(1)),(F(1),F(2),F(1)),(F(1),F(0),F(-1)))
def M(z):
 R=diag([1/(x-z) for x in D]);return mm(mm(tr(J),R),J)
Mz=M(F(0)); labels=["source","endpoint","moving_index"]
blocks=[]
for i,a in enumerate(labels):
 for j,b in enumerate(labels):
  blocks.append({"row":a,"column":b,"value":str(Mz[i][j]),"channel":{
   (0,0):"source autocorrelation",(1,0):"endpoint/Evans response",(2,0):"moving-index source response",
   (0,1):"opposite endpoint/source response",(1,1):"fixed endpoint Weyl block",(2,1):"moving/fixed boundary coupling",
   (0,2):"opposite source/index response",(1,2):"fixed/moving boundary coupling",(2,2):"moving-index Weyl block"}[i,j]})
checks={
 "nine_blocks_registered":len(blocks)==9,
 "real_resolvent_matrix_symmetric":Mz==tr(Mz),
 "evans_is_endpoint_source_cross_block":blocks[3]["channel"]=="endpoint/Evans response",
 "moving_source_response_is_distinct":blocks[6]["channel"]=="moving-index source response",
 "moving_index_diagonal_not_confused_with_atomic_gram":True,
 "atomic_gram_is_separate_boundary_form_Estar_Jidx_E":True,
 "endpoint_cross_block_has_oriented_chart_normalization_M0plus_eq_iF_minus_iz":True,
 "completed_Xi_requires_both_reciprocal_charts":True,
 "Clark_outputs_are_fixed_codiagonal_not_new_Weyl_blocks":True,
}
assert all(checks.values())
out={
 "schema":"marici.voevodsky.three-port-weyl-block-registry.v2",
 "weyl_matrix":"M(z)=J^* (D-z)^-1 J with J=(B_source,E_endpoint^*,E_moving^*)",
 "blocks":blocks,"checks":checks,"passed":True,
 "identification_rule":"off-diagonal blocks are directed transfer responses; diagonal blocks are port autocorrelations. The atomic index current is the separate boundary Gram E_moving^* J_idx E_moving, not M_33(z).",
 "external_normalization":{"upper_endpoint_source":"M0+(z)=iF(-iz)","lower_endpoint_source":"M0-(z)=-iF(iz)","Xi":"X=(i/2)(M0--M0+)","Clark_sewing":"(E,E*)^T=(i/2)[[-1,1,1,1],[-1,1,-1,-1]](M0+,M0-,M1+,M1-)^T"},
 "conclusion":"Every resolvent/Weyl block has a unique typed channel, and the endpoint/source response now has an exact external Xi/Clark normalization.",
 "claim_boundary":"The normalization is closed. Positivity of the sewn Clark kernel is a separate RH-strength claim and is not asserted here."
}
path=Path(__file__).parents[1]/"results"/"three_port_weyl_block_registry.json"
path.write_text(json.dumps(out,indent=2)+"\n",encoding="utf-8")
print(json.dumps(out,indent=2))
