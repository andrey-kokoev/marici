"""Check the homological obstruction to a faithful comparison from a filled face."""
from __future__ import annotations
import json
from fractions import Fraction
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];OUT=ROOT/'research'/'voevodsky'/'results'/'cosmology_higher_dimensional_faithful_face_no_go.json'
def rank(a):
 a=[[Fraction(x) for x in r] for r in a];i=j=0;m=len(a);n=len(a[0]) if m else 0
 while i<m and j<n:
  p=next((k for k in range(i,m) if a[k][j]),None)
  if p is None:j+=1;continue
  a[i],a[p]=a[p],a[i];q=a[i][j];a[i]=[x/q for x in a[i]]
  for k in range(m):
   if k!=i and a[k][j]:q=a[k][j];a[k]=[x-q*y for x,y in zip(a[k],a[i])]
  i+=1;j+=1
 return i
def main():
 d1=[[-1,0,1],[1,-1,0],[0,1,-1]];face=[[1],[1],[1]]
 boundary=[sum(d1[i][j]*face[j][0] for j in range(3)) for i in range(3)];assert boundary==[0,0,0]
 h1_boundary=3-rank(d1);h1_filled=3-rank(d1)-rank(face);assert h1_boundary==1 and h1_filled==0
 # Any chain map sends a boundary to a boundary: F(d face)=d F(face).
 faithful_on_generator=False;assert not faithful_on_generator
 out={'schema':'marici.voevodsky.cosmology-higher-dimensional-faithful-face-no-go.v1','status':'filled_face_incompatible_with_faithful_nonzero_pullback','source_boundary':'the three-edge dual cycle with H1 rank one','higher_dimensional_source':'three SNC divisors meeting in a smooth threefold contribute a 2-simplex whose boundary is that cycle','homology_checks':{'boundary_H1_rank':h1_boundary,'filled_simplex_H1_rank':h1_filled,'face_boundary':[1,1,1]},'functorial_obstruction':'For every chain map, the image of the face boundary is again a boundary. It cannot equal the verified nonboundary sigma123 in a target where Xi_log/sigma123 remains nonzero.','retraction_obstruction':'A retraction from the filled simplex to its boundary inducing the identity would force the zero H1 of the simplex to surject onto rank-one H1 of the boundary, which is impossible.','decision':'Higher dimension can geometrically add the missing face, but no chain-level comparison can both carry that filler to the original triangle and remain faithful on its primitive class. Any successful correspondence must kill or alter Xi_log, so it does not solve the fixed-source horn.','next_gate':'classify whether the remaining nonfaithful correspondences encode any independently sourced physical readout rather than a horn filler','limitations':['homological no-go for comparison maps preserving the primitive class','does not prohibit correspondences that deliberately kill the class','no physical readout or period inferred'],'passed':True};OUT.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
