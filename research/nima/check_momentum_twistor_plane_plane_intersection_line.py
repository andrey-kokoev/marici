#!/usr/bin/env python3
"""Exact check of the plane-plane intersection-line contraction."""
import json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT/'research/benincasa/.tmp_sympy'))
import sympy as s
from momentum_twistor_constructors import (four_bracket as det4,
 plane_covector, plane_plane_line_basis, plane_plane_line_contraction,
 plane_plane_line_dual_plucker)
xs=map(s.Integer,(1,2,4,7,11,16,22,29));Z={i:s.Matrix([1,x,x*x,x**3]) for i,x in enumerate(xs,1)}
def br(a,b,c,d): return det4(Z[a],Z[b],Z[c],Z[d])
def contraction_raw(A,B,p,q):
 return plane_plane_line_contraction(*p,*q,A,B)
def contraction(A,B,p=(1,2,3),q=(4,5,6)):
 return contraction_raw(A,B,tuple(Z[i] for i in p),tuple(Z[i] for i in q))
# Plane covectors obtained directly from their determinant equations.
e=s.eye(4)
def reference_plane_covector(p): return s.Matrix([[det4(e[:,i],*(Z[j] for j in p)) for i in range(4)]])
P=reference_plane_covector((1,2,3));Q=reference_plane_covector((4,5,6));U,V=s.Matrix.vstack(P,Q).nullspace()
public_P=plane_covector(*(Z[i] for i in (1,2,3)))
public_Q=plane_covector(*(Z[i] for i in (4,5,6)))
L=plane_plane_line_dual_plucker(*(Z[i] for i in (1,2,3,4,5,6)))
public_U,public_V=plane_plane_line_basis(*(Z[i] for i in (1,2,3,4,5,6)))
try:
 plane_plane_line_basis(Z[1],Z[2],Z[3],Z[1],Z[2],Z[3])
 degeneracy_rejected=False
except ValueError:
 degeneracy_rejected=True
pairs=[(Z[7],Z[8]),(s.Matrix([2,3,5,7]),s.Matrix([11,13,17,19])),(Z[2]+Z[7],Z[3]-2*Z[8])]
ratios=[]
for A,B in pairs:
 direct=contraction(A,B); geometric=det4(A,B,U,V);ratios.append(s.factor(direct/geometric))
base=contraction(Z[7],Z[8]);swapped_planes=s.expand(det4(Z[7],Z[4],Z[5],Z[6])*det4(Z[8],Z[1],Z[2],Z[3])-det4(Z[8],Z[4],Z[5],Z[6])*det4(Z[7],Z[1],Z[2],Z[3]))
# Multihomogeneity and ambient GL(4) covariance.
columns=[Z[7],Z[8],Z[1],Z[2],Z[3],Z[4],Z[5],Z[6]]
rescaling_checks=[]
for i in range(8):
 scaled=list(columns);scaled[i]=s.Integer(3)*scaled[i]
 rescaling_checks.append(contraction_raw(scaled[0],scaled[1],tuple(scaled[2:5]),tuple(scaled[5:8]))==3*base)
G=s.Matrix([[1,2,0,1],[0,1,1,0],[2,0,1,1],[1,0,0,1]])
gl_value=contraction_raw(G*Z[7],G*Z[8],tuple(G*Z[i] for i in (1,2,3)),tuple(G*Z[i] for i in (4,5,6)))
plucker_quadric=s.expand(L[0,1]*L[2,3]-L[0,2]*L[1,3]+L[0,3]*L[1,2])
checks={'public_plane_covectors_match_determinant_equations':public_P==P and public_Q==Q,'dual_plucker_has_wedge_factorization':L==public_P.T*public_Q-public_Q.T*public_P,'public_basis_spans_kernel':L*public_U==s.zeros(4,1) and L*public_V==s.zeros(4,1) and s.Matrix.hstack(public_U,public_V).rank()==2,'coincident_plane_degeneracy_rejected':degeneracy_rejected,'intersection_basis_in_first_plane':P*U==s.zeros(1,1) and P*V==s.zeros(1,1),'intersection_basis_in_second_plane':Q*U==s.zeros(1,1) and Q*V==s.zeros(1,1),'source_contraction_matches_geometric_line':all(r==ratios[0] for r in ratios),'dual_plucker_is_antisymmetric':L.T==-L,'dual_plucker_is_decomposable_rank_two':L.rank()==2,'dual_plucker_satisfies_quadratic_relation':plucker_quadric==0,'geometric_line_is_dual_plucker_kernel':L*U==s.zeros(4,1) and L*V==s.zeros(4,1),'dual_plucker_reconstructs_contraction':all((A.T*L*B)[0]==contraction(A,B) for A,B in pairs),'contraction_vanishes_for_incident_test_line':(U.T*L*Z[7])[0]==0 and (Z[8].T*L*V)[0]==0,'contraction_vanishes_for_the_line_itself':(U.T*L*V)[0]==0,'antisymmetric_in_AB':contraction(Z[8],Z[7])==-base,'antisymmetric_under_plane_exchange':swapped_planes==-base,'degree_one_in_all_eight_twistors':all(rescaling_checks),'gl4_weight_two':gl_value==s.det(G)**2*base,'generic_nonzero':base!=0}
out={'schema':'marici.nima.momentum-twistor-plane-plane-intersection-line.v1','source':'research/sources/nima/papers/six-point-nmhv/1008.2958/all_loop__v2_penult.tex:492-493,654','object':'(123) intersect (456)','definition':'<AB|(abc) intersect (xyz)> = <Aabc><Bxyz> - <Babc><Axyz>','intersection_basis':[[str(x) for x in U],[str(x) for x in V]],'geometric_proportionality_ratios':[str(x) for x in ratios],'sample_value':str(base),'checks':checks,'passed':all(checks.values()),'scope':'Exact rational verification of the source contraction against an independently solved intersection-line basis.'}
p=ROOT/'research/nima/results/momentum-twistor-plane-plane-intersection-line.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2));raise SystemExit(0 if out['passed'] else 1)
