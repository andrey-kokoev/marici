"""Gate ungraded marked-wall augmentation against unit-ideal collapse."""
from __future__ import annotations
import json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]; sys.path.insert(0,str(ROOT/'research'/'benincasa'))
import physical_four_mark_residue_twisted_derham as base
RES=ROOT/'research'/'voevodsky'/'results'; OUT=RES/'cosmology_rank26_p_normal_marked_wall_ideal_gate.json'
def sub(a,b):
 out=dict(a)
 for e,v in b.items():
  x=(out.get(e,0)-v)%base.PRIME
  if x:out[e]=x
  else:out.pop(e,None)
 return out
def scale(a,c):return {e:v*c%base.PRIME for e,v in a.items() if v*c%base.PRIME}
def main():
 protocol=json.loads((RES/'cosmology_rank26_p_normal_protocol_gate.json').read_text()); point=tuple(protocol['test_point_xyz']); _,q=base.fiber_data(*point)
 difference=sub(q['g31'],q['g2']); assert difference=={(0,0):base.PRIME-6}; inverse=pow(base.PRIME-6,base.PRIME-2,base.PRIME); unit=scale(difference,inverse); assert unit=={(0,0):1}
 out={'schema':'marici.voevodsky.cosmology-rank26-p-normal-marked-wall-ideal-gate.v1','status':'ungraded_wall_augmentation_rejected_as_unit_ideal','field':base.PRIME,'point_xyz':list(point),'identity':'(-6)^(-1) * (q_g31 - q_g2) = 1','difference_polynomial':{str(e):v for e,v in difference.items()},'inverse_coefficient':inverse,'unit_verified':True,'decision':'Adjoining all wall polynomials to an ungraded polynomial ideal makes the ideal equal to the whole ring at the test point. Any directional K membership would therefore be tautological and cannot explain source-complex absorption.','required_refinement':'retain q-level grading and level-lowering source maps; do not identify wall generators across distinct marked-level blocks','passed':True}
 OUT.write_text(json.dumps(out,indent=2)+'\n'); print(json.dumps(out,indent=2))
if __name__=='__main__':main()
