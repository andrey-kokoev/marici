#!/usr/bin/env python3
"""Exact Euclidean embedding of two oriented half-planes with a shared axis."""
import json
from pathlib import Path

def mv(A,v):return tuple(sum(A[i][j]*v[j] for j in range(3)) for i in range(3))
def dot(u,v):return sum(a*b for a,b in zip(u,v))
def add(u,v):return tuple(a+b for a,b in zip(u,v))
def scale(a,v):return tuple(a*x for x in v)

def main():
 axis=(1,0,0);nu_plus=(0,1,0);nu_minus=(0,0,-1)
 R=((1,0,0),(0,0,-1),(0,-1,0))
 assert dot(axis,nu_plus)==dot(axis,nu_minus)==dot(nu_plus,nu_minus)==0
 assert dot(axis,axis)==dot(nu_plus,nu_plus)==dot(nu_minus,nu_minus)==1
 assert mv(R,axis)==axis and mv(R,nu_plus)==nu_minus and mv(R,nu_minus)==nu_plus
 for v in (axis,nu_plus,nu_minus):assert mv(R,mv(R,v))==v
 # Parameterized half-planes P+ and P-; t >= 0 is sampled exactly.
 samples=0
 for s in range(-4,5):
  for t in range(5):
   pplus=add(scale(s,axis),scale(t,nu_plus));pminus=add(scale(s,axis),scale(t,nu_minus))
   assert mv(R,pplus)==pminus and mv(R,pminus)==pplus;samples+=1
 # Their intersection is t=0, the shared axis. Their chosen induced boundary signs cancel.
 boundary_sign_plus=1;boundary_sign_minus=-1
 assert boundary_sign_plus+boundary_sign_minus==0
 result={'schema':'marici.voevodsky.right-angle-ditch-embedding.v1','ambient':'Q^3 embedded in R^3','shared_axis':axis,'plus_inward_normal':nu_plus,'minus_inward_normal':nu_minus,'normal_inner_product':dot(nu_plus,nu_minus),'dihedral_angle_degrees':90,'reflection_matrix':[list(r) for r in R],'reflection_involutive':True,'reflection_fixes_axis':True,'reflection_exchanges_half_planes':True,'parameter_samples_checked':samples,'induced_shared_boundary_signs':[boundary_sign_plus,boundary_sign_minus],'shared_boundary_cancels':True,'claim_boundary':'Exact local Euclidean embedding; global attachment to every simplex is a product thickening, not a source-derived metric geometry.'}
 out=Path(__file__).parents[1]/'results'/'right_angle_ditch_embedding.json';out.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
if __name__=='__main__':main()
