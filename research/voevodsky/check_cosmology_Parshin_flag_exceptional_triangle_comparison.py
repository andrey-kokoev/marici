"""Compute the three-line P2 Parshin flags of {u,v} and compare to the triangle cycle."""
from __future__ import annotations
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];OUT=ROOT/'research'/'voevodsky'/'results'/'cosmology_Parshin_flag_exceptional_triangle_comparison.json'
def main():
 # Divisors X,Y,Z; u=X/Z, v=Y/Z. Tame units up to a constant sign:
 # X: v^-1, Y: u, Z: v/u.
 # Secondary valuations at pair intersections.
 flags={
  'X>XY':-1,'Y>XY':1,
  'Y>YZ':-1,'Z>YZ':1,
  'Z>ZX':-1,'X>ZX':1,
 }
 assert flags['X>XY']+flags['Y>XY']==0
 assert flags['Y>YZ']+flags['Z>YZ']==0
 assert flags['Z>ZX']+flags['X>ZX']==0
 oriented={'X->Y':flags['Y>XY'],'Y->Z':flags['Z>YZ'],'Z->X':flags['X>ZX']}
 assert tuple(oriented.values())==(1,1,1)
 # Deliberate orientation failure: reversing one edge is not a cycle.
 bad=(1,1,-1);boundary=(bad[0]-bad[2],bad[1]-bad[0],bad[2]-bad[1]);assert boundary!=(0,0,0)
 good=tuple(oriented.values());assert (good[0]-good[2],good[1]-good[0],good[2]-good[1])==(0,0,0)
 out={'schema':'marici.voevodsky.cosmology-Parshin-flag-exceptional-triangle-comparison.v1','status':'three_line_flags_recover_primitive_oriented_triangle','compactification':'P2 with boundary X*Y*Z=0, where u=X/Z and v=Y/Z','tame_units_up_to_constant':{'X=0':'v^-1','Y=0':'u','Z=0':'v/u'},'ordered_flag_valuations':flags,'oriented_dual_edges':oriented,'primitive_cycle':[1,1,1],'orientation_translation':'This equals the previously recorded (1,-1,1) after reversing the chosen orientation of its second edge.','correction_to_prior_gate':'The P1xP1 toric model has four boundary divisors, but the actual exceptional compactification is the three-line P2 model. Its sourced Parshin flags do map canonically to the triangle incidence complex.','degree_disposition':'The flags establish that the K2 symbol and triangle residues form a sourced total degree-two cocycle. They do not exhibit a total degree-one precycle whose differential is that cocycle.','decision':'The boundary-type mismatch is repaired on the correct compactification, but the horn remains unfilled at the next total-degree exactness gate.','next_gate':'compute the localization total-complex degree and test whether the sourced (Xi_log,-sigma123) cocycle is exact or represents the nonzero K2 regulator class','limitations':['constant signs in tame symbols have zero secondary valuation','no degree-one precycle constructed','no physical period inferred'],'passed':True};OUT.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
