"""Test stationary normalization by diagonal detector gauges."""
import json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];sys.path.insert(0,str(ROOT/'research'/'voevodsky'))
import check_cosmology_detector_transition_A16_A18 as t
RES=ROOT/'research'/'voevodsky'/'results';OUT=RES/'cosmology_stationary_diagonal_gauge.json'
def enc(x):return {'numerator':x.numerator,'denominator':x.denominator}
def core(M):return [[M[i][j]*M[0][0]/(M[i][0]*M[0][j]) for j in (1,2)] for i in (1,2)]
def main():
 a=json.loads((RES/'cosmology_detector_change_A14_A16.json').read_text());b=json.loads((RES/'cosmology_detector_transition_A16_A18.json').read_text());C1=[[t.q(x) for x in r] for r in a['change_matrix']];C2=[[t.q(x) for x in r] for r in b['transition_matrix']];assert all(x for M in (C1,C2) for row in M for x in row);K1,K2=core(C1),core(C2);same=K1==K2
 out={'schema':'marici.voevodsky.cosmology-stationary-diagonal-gauge.v1','status':('diagonal_stationary_normalization_possible' if same else 'diagonal_stationary_normalization_obstructed'),'A14_A16_cross_ratio_core':[[enc(x) for x in r] for r in K1],'A16_A18_cross_ratio_core':[[enc(x) for x in r] for r in K2],'cores_equal':same,'decision':('Independent row/column scalings can place both transitions in one common matrix orbit.' if same else 'Different cross-ratio cores obstruct even independent row/column scaling to a shared stationary matrix, hence also obstruct a compatible diagonal gauge sequence.'),'claim_boundary':'This does not decide compatibility under the full constant-line-preserving parabolic group.','next_gate':('construct-compatible-diagonal-gauges' if same else 'solve-full-parabolic-open-orbit-compatibility'),'passed':True};OUT.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items() if 'core' not in k},indent=2))
if __name__=='__main__':main()
