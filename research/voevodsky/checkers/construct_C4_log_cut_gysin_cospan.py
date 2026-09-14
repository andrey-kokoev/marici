#!/usr/bin/env python3
"""Construct the integral common-line cospan for logarithmic and Cut-nearby maps."""
import json,itertools,math
from fractions import Fraction
from pathlib import Path
R=Path(__file__).resolve().parents[3]
cert=json.loads((R/'research/benincasa/full-rank12-cut-nearby-layers-certificate.json').read_text())
# Exact fiber x=2,y=3; ambient rows (e2,e3,e4,e5,e6,v0), source columns ordered 101,110,111.
L=[[0,-180,0],[0,0,0],[180,0,0],[0,0,0],[0,0,1],[1,1,0]]
C=[[0,0,0],[6,0,3],[0,0,0],[0,4,2],[0,0,1],[0,0,0]]
log_leg=[0,0,2];cut_leg=[-1,-1,2]
def mv(A,v):return [sum(A[i][j]*v[j] for j in range(len(v))) for i in range(len(A))]
def rank(A):
 A=[[Fraction(x) for x in r] for r in A];m=len(A);n=len(A[0]);q=0
 for j in range(n):
  p=next((i for i in range(q,m) if A[i][j]),None)
  if p is None:continue
  A[q],A[p]=A[p],A[q];z=A[q][j];A[q]=[x/z for x in A[q]]
  for i in range(m):
   if i!=q and A[i][j]:z=A[i][j];A[i]=[A[i][k]-z*A[q][k] for k in range(n)]
  q+=1
 return q
left=mv(L,log_leg);right=mv(C,cut_leg)
# Direct diophantine condition in Cut lattice: 6a+3c=0 and 4b+2c=0 force c even.
checks={'certificate_intersection_e6':cert['intersection_generator']=='e6','distinct_images':cert['strict_equality_of_algebraic_images'] is False,'ranks_3_3_union5_intersection1':(rank(L),rank(C),rank([L[i]+C[i] for i in range(6)]))==(3,3,5),'square_commutes':left==right==[0,0,0,0,2,0],'cut_leg_primitive':math.gcd(*map(abs,cut_leg))==1,'log_leg_has_index_two':math.gcd(*map(abs,log_leg))==2,'cut_e3_equation_forces_even_c':all(c%2==0 for c in range(-9,10) for a in range(-9,10) if 6*a+3*c==0),'cut_e5_equation_forces_even_c':all(c%2==0 for c in range(-9,10) for b in range(-9,10) if 4*b+2*c==0),'minimal_positive_common_e6_coefficient':all(mv(C,[a,b,c])!=[0,0,0,0,1,0] for a in range(-4,5) for b in range(-4,5) for c in range(-4,5))}
assert all(checks.values()),checks
out={'schema':'marici.voevodsky.C4-log-Cut-Gysin-cospan.v1','ambient_basis':['e2','e3','e4','e5','e6','v0'],'log_source_basis':['Theta101','Theta110','Theta111_filt'],'cut_source_basis':['g101','g110','g111_tilde'],'log_matrix':L,'cut_matrix':C,'common_generator':'2*e6 in the raw integral source frames','log_leg':log_leg,'cut_leg':cut_leg,'commuting_value':left,'identity':'2*Theta111_filt <-> 2*g111_tilde-g101-g110, both mapping to 2*e6','raw_indices':{'common_line_inside_log_top_line':2,'cut_relation_vector_primitive':True},'rational_form':'Theta111_filt <-> g111_tilde-(g101+g110)/2 maps to e6','Betti_completion':'The occurrence-resolved sheet/forgetting composition supplies the complementary factor four and identifies the physical Cut pair with primitive eta=4*rho_e6.','C4_status':'confirmed as an integral filtered cospan; the full rank-twelve operations remain layer-distinct','checks':checks,'passed':True}
(R/'research/voevodsky/results/C4_log_Cut_Gysin_cospan.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'passed':True,'C4':out['C4_status'],'identity':out['identity'],'raw_indices':out['raw_indices'],'ranks':[rank(L),rank(C),rank([L[i]+C[i] for i in range(6)])]}))
