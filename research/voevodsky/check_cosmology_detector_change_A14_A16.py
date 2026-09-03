"""Compare exact 1,y,x detector matrices at A14 and A16."""
import json
from fractions import Fraction
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];RES=ROOT/'research'/'voevodsky'/'results';OUT=RES/'cosmology_detector_change_A14_A16.json'
def q(x):return Fraction(x['numerator'],x['denominator'])
def enc(x):return {'numerator':x.numerator,'denominator':x.denominator}
def mm(A,B):return [[sum(A[i][k]*B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]
def main():
 a=json.loads((RES/'cosmology_lowest_degree_influx_detector.json').read_text());b=json.loads((RES/'cosmology_A16_raw_q_detector.json').read_text());raw=json.loads((RES/'cosmology_raw_q_collapse_certificates.json').read_text());ids=b['target_order'];rb=[]
 for c in raw['groups'][1]['certificates']:
  m={x['target_id']:q(x['coefficient']) for x in c['target_coefficients']};rb.append([m.get(i,Fraction()) for i in ids])
 r16=[[q(x) for x in row] for row in b['relation_basis']];assert rb==r16;M14=[[q(x) for x in row] for row in a['detector_matrix']];M16=[[q(x) for x in row] for row in b['detector_matrix']];I14=[[q(x) for x in row] for row in a['inverse_matrix']];C=mm(M16,I14);diag=all(not C[i][j] for i in range(3) for j in range(3) if i!=j);scalar=diag and C[0][0]==C[1][1]==C[2][2]
 out={'schema':'marici.voevodsky.cosmology-detector-change-A14-A16.v1','status':'exact_detector_change_computed','relation_basis_identical':True,'change_matrix':[[enc(x) for x in row] for row in C],'diagonal':diag,'scalar':scalar,'decision':('Detector transport is scalar.' if scalar else 'Detector transport is diagonal but non-scalar.' if diag else 'Detector transport genuinely mixes the 1,y,x probes.'),'claim_boundary':'Matrix uses the canonical echelon relation basis and raw-q coefficient normalization.','next_gate':'classify-mixed-detector-transport','passed':True};OUT.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
