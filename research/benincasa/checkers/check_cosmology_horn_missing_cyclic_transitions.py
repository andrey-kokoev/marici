#!/usr/bin/env python3
"""Construct the three projective horn-chart transitions and their K2 cocycle."""
import json
from pathlib import Path
P=Path(__file__).resolve();ROOT=P.parents[3];R=ROOT/'research'/'benincasa'/'results'
def mm(A,B):return [[sum(A[i][k]*B[k][j] for k in range(2)) for j in range(2)] for i in range(2)]
def det(A):return A[0][0]*A[1][1]-A[0][1]*A[1][0]
M32=[[1,-1],[0,-1]]   # (u,v)->(a=u/v,b=1/v)
M21=[[-1,0],[-1,1]]  # (a,b)->(c=1/a,d=b/a)
M13=[[0,-1],[1,-1]]  # (c,d)->(u=1/d,v=c/d)
assert mm(M13,mm(M21,M32))==[[1,0],[0,1]];assert [det(M32),det(M21),det(M13)]==[-1,-1,1]
# Corrections in basis A={-1,u}, B={-1,v}: B, A-B, -A.
corr=[[0,1],[1,-1],[-1,0]];assert [sum(x[i] for x in corr) for i in range(2)]==[0,0]
out={'schema':'marici.benincasa.cosmology-horn-missing-cyclic-transitions.v1','charts':{'C3':['u=x1/x3','v=x2/x3'],'C2':['a=x1/x2','b=x3/x2'],'C1':['c=x2/x1','d=x3/x1']},'transitions':[{'map':'C3->C2','ratios':['u/v','1/v'],'log_matrix':M32,'determinant':-1,'K2_correction':'{-1,v}'},{'map':'C2->C1','ratios':['1/a','b/a'],'log_matrix':M21,'determinant':-1,'K2_correction':'{-1,u}-{-1,v}'},{'map':'C1->C3','ratios':['1/d','c/d'],'log_matrix':M13,'determinant':1,'K2_correction':'-{-1,u}'}],'triple_log_transition_identity':True,'correction_vectors_in_basis_minus1_u_minus1_v':corr,'triple_K2_correction_sum':[0,0],'integral_K2_cocycle_trivial':True,'horn_chart_descent':'strict after retaining all three unit corrections','rank26_relation_transport_scope':'only G12-G31 has an independently replayed relation-level transport; this result concerns the universal horn projective charts','decision':'The two missing projective transitions complete the three-chart cycle. Their determinant signs multiply to +1 and the two-torsion unit corrections telescope to zero, so the universal integral horn has a trivial triple-overlap K2 cocycle.','passed':True};(R/'cosmology_horn_missing_cyclic_transitions.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
