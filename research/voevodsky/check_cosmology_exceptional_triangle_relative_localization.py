"""Compute the relative localization class for the triangle boundary on E=P2."""
from __future__ import annotations
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]; OUT=ROOT/'research'/'voevodsky'/'results'/'cosmology_exceptional_triangle_relative_localization.json'
def rank_q(A):
 from fractions import Fraction
 M=[[Fraction(x) for x in row] for row in A]; r=0
 for c in range(len(M[0])):
  p=next((i for i in range(r,len(M)) if M[i][c]),None)
  if p is None: continue
  M[r],M[p]=M[p],M[r]; q=M[r][c]; M[r]=[x/q for x in M[r]]
  for i in range(len(M)):
   if i!=r and M[i][c]: q=M[i][c]; M[i]=[M[i][j]-q*M[r][j] for j in range(len(M[0]))]
  r+=1
 return r
def main():
 # columns are oriented edges 12,23,31; rows are boundary components 1,2,3.
 boundary=[[-1,0,1],[1,-1,0],[0,1,-1]]
 assert rank_q(boundary)==2
 cycle=[1,1,1]; assert [sum(row[j]*cycle[j] for j in range(3)) for row in boundary]==[0,0,0]
 # Sign-change the middle edge to the programme pair-face convention.
 xi_residue=[1,-1,1]; sigma_residue=[-1,1,-1]
 assert [xi_residue[i]+sigma_residue[i] for i in range(3)]==[0,0,0]
 out={'schema':'marici.voevodsky.cosmology-exceptional-triangle-relative-localization.v1','status':'relative_localization_identifies_Xi_as_boundary_cycle_but_supplies_no_lower_filler','boundary_divisor':'three strict-transform lines forming a triangle on E=P2','dual_graph':'3-cycle','edge_boundary_rank':2,'primitive_cycle_standard_basis':cycle,'programme_residue_convention':xi_residue,'exceptional_face_boundary':sigma_residue,'relative_closed_pair':'Xi_log + minus_sigma123','ordinary_H_contribution':'zero on the complement; Xi is the boundary/dual-graph weight class, not the restriction of H','decision':'Relative localization canonically explains the nonzero Xi class as the primitive triangle cycle and its cancellation with the exceptional face. It does not create a degree-one primitive for that closed pair.','next_gate':'construct a sourced total cone cell over the primitive triangle cycle, with differential Xi_log+minus_sigma123, or prove the resolved carrier has no such cell','limitations':['cohomological localization classification, not an incoming chain-level filler','no relative Bockstein or physical period'],'passed':True}
 OUT.write_text(json.dumps(out,indent=2)+'\n'); print(json.dumps(out,indent=2))
if __name__=='__main__':main()
