"""Test whether the ordinary corner blow-up contains a cell filling the boundary triangle."""
from __future__ import annotations
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]; OUT=ROOT/'research'/'voevodsky'/'results'/'cosmology_exceptional_triangle_total_lift.json'
def rank_q(A):
 from fractions import Fraction
 M=[[Fraction(x) for x in row] for row in A]; r=0
 if not M:return 0
 for c in range(len(M[0])):
  p=next((i for i in range(r,len(M)) if M[i][c]),None)
  if p is None:continue
  M[r],M[p]=M[p],M[r];q=M[r][c];M[r]=[x/q for x in M[r]]
  for i in range(len(M)):
   if i!=r and M[i][c]:q=M[i][c];M[i]=[M[i][j]-q*M[r][j] for j in range(len(M[0]))]
  r+=1
 return r
def main():
 # E=P2; D_i are U=0, V=0, U+V+P=0.
 triple_solution_projective=False # U=V=P=0 is not a projective point.
 d1=[[-1,0,1],[1,-1,0],[0,1,-1]]
 rank_d1=rank_q(d1); c1_rank=3; c2_rank=0
 h1_rank=(c1_rank-rank_d1)-0
 cycle=[1,1,1]; assert rank_d1==2 and h1_rank==1 and not triple_solution_projective
 assert [sum(row[j]*cycle[j] for j in range(3)) for row in d1]==[0,0,0]
 out={'schema':'marici.voevodsky.cosmology-exceptional-triangle-total-lift.v1','status':'ordinary_corner_blowup_has_no_total_lift_cell_triangle_cycle_is_primitive_nonboundary','exceptional_divisor':'P2','boundary_lines':['U=0','V=0','U+V+P=0'],'triple_intersection_exists':False,'dual_complex':{'vertices':3,'edges':3,'faces':0,'edge_boundary_rank':rank_d1,'H1_rank':h1_rank,'primitive_cycle':cycle},'decision':'The ordinary oriented blow-up contains no geometric 2-cell whose boundary is the primitive triangle cycle. Its dual complex is S1, so the relative Xi-minusSigma class remains nonboundary integrally.','required_enlargement':'a sourced modification or external relative-face/Cayley-Menger cone that adds a genuine face over the cycle together with a chain map; declaring an abstract cone repeats tau_p','limitations':['no-go for the ordinary blow-up SNC incidence complex','does not exclude an enlarged semistable or Cayley-Menger source geometry','no Bockstein or physical period'],'passed':True}
 OUT.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
