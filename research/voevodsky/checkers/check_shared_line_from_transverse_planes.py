#!/usr/bin/env python3
"""Exact rank audit for the shared line of two transverse planes in Q^3."""
import json
from fractions import Fraction
from pathlib import Path

def rank(A):
 M=[[Fraction(x) for x in row] for row in A];r=0
 for c in range(len(M[0])):
  p=next((i for i in range(r,len(M)) if M[i][c]),None)
  if p is None:continue
  M[r],M[p]=M[p],M[r];q=M[r][c];M[r]=[x/q for x in M[r]]
  for i in range(len(M)):
   if i!=r:
    q=M[i][c];M[i]=[x-q*y for x,y in zip(M[i],M[r])]
  r+=1
 return r

def main():
 # P+ is z=0; P- is y=0. Their intersection satisfies both equations.
 transverse_normals=[[0,0,1],[0,1,0]]
 r=rank(transverse_normals);nullity=3-r
 assert r==2 and nullity==1
 shared_generator=[1,0,0]
 assert all(sum(row[i]*shared_generator[i] for i in range(3))==0 for row in transverse_normals)
 # Hostile: coincident planes have proportional normals and rank-two intersection.
 coincident_normals=[[0,0,1],[0,0,-1]]
 r_bad=rank(coincident_normals);nullity_bad=3-r_bad
 assert r_bad==1 and nullity_bad==2
 result={'schema':'marici.voevodsky.shared-line-from-transverse-planes.v1','ambient_dimension':3,'transverse_conormal_rank':r,'shared_intersection_rank':nullity,'shared_line_generator':shared_generator,'determinant_line_rank':1,'coincident_conormal_rank':r_bad,'coincident_intersection_rank':nullity_bad,'transversality_required':True,'conclusion':'The real rank-one shared line is derived from a three-dimensional carrier plus two independent plane conormals.','claim_boundary':'The 2-Segal structure alone supplies neither the carrier tangent space nor the independent conormals.'}
 out=Path(__file__).parents[1]/'results'/'shared_line_from_transverse_planes.json';out.write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
if __name__=='__main__':main()
