"""Test whether flag-preserving ambient gauges can trivialize detector transport."""
import json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];sys.path.insert(0,str(ROOT/'research'/'voevodsky'))
import check_cosmology_detector_transition_A16_A18 as t
RES=ROOT/'research'/'voevodsky'/'results';OUT=RES/'cosmology_compatible_flag_gauge_obstruction.json'
def main():
 a=json.loads((RES/'cosmology_detector_change_A14_A16.json').read_text());b=json.loads((RES/'cosmology_detector_transition_A16_A18.json').read_text());Cs=[[[t.q(x) for x in r] for r in d[k]] for d,k in ((a,'change_matrix'),(b,'transition_matrix'))];moves=[not(C[1][0]==C[2][0]==0) for C in Cs];assert all(moves)
 out={'schema':'marici.voevodsky.cosmology-compatible-flag-gauge-obstruction.v1','status':'closed_orbit_normalization_obstructed','transitions_move_constant_line':moves,'identity_normalization_by_flag_gauges_possible':False,'flag_preserving_stationary_normal_form_possible':False,'decision':'Left/right multiplication by constant-line-preserving gauges cannot move an open-double-coset transition into the closed flag-preserving orbit. Thus no compatible gauge sequence can trivialize either step or make both steps flag-preserving.','claim_boundary':'This does not exclude a shared stationary normal form in the open flag-moving orbit.','next_gate':'solve-open-orbit-stationary-gauge-compatibility','passed':True};OUT.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
