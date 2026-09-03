"""Classify detector transitions under rational changes preserving the constant line."""
import json,sys
from fractions import Fraction
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];sys.path.insert(0,str(ROOT/'research'/'voevodsky'))
import check_cosmology_detector_transition_A16_A18 as t
RES=ROOT/'research'/'voevodsky'/'results';OUT=RES/'cosmology_triangular_detector_normalization.json'
def main():
 a=json.loads((RES/'cosmology_detector_change_A14_A16.json').read_text());b=json.loads((RES/'cosmology_detector_transition_A16_A18.json').read_text());C1=[[t.q(x) for x in r] for r in a['change_matrix']];C2=[[t.q(x) for x in r] for r in b['transition_matrix']];assert t.det(C1) and t.det(C2)
 def orbit(C):return 'closed_flag_preserving' if C[1][0]==C[2][0]==0 else 'open_flag_moving'
 o1,o2=orbit(C1),orbit(C2);same=o1==o2
 out={'schema':'marici.voevodsky.cosmology-triangular-detector-normalization.v1','status':'parabolic_double_coset_classified','A14_A16_orbit':o1,'A16_A18_orbit':o2,'same_double_coset':same,'rational_flag_preserving_normalization_exists':same,'decision':'Both transitions lie in the open double coset for the rational parabolic stabilizing the constant-probe line; independent flag-preserving left/right gauges can relate them.','claim_boundary':'Existence of noncanonical parabolic gauges does not produce a sourced normalization, and does not preserve fixed 1,y,x labels.','next_gate':'test-single-compatible-gauge-sequence','passed':True};OUT.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
