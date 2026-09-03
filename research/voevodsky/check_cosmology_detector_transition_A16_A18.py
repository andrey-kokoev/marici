"""Compare A16-to-A18 detector transport with A14-to-A16."""
import json
from fractions import Fraction
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];RES=ROOT/'research'/'voevodsky'/'results';OUT=RES/'cosmology_detector_transition_A16_A18.json'
def q(x):return Fraction(x['numerator'],x['denominator'])
def enc(x):return {'numerator':x.numerator,'denominator':x.denominator}
def det(M):return M[0][0]*(M[1][1]*M[2][2]-M[1][2]*M[2][1])-M[0][1]*(M[1][0]*M[2][2]-M[1][2]*M[2][0])+M[0][2]*(M[1][0]*M[2][1]-M[1][1]*M[2][0])
def inv(M):
 D=det(M);return [[(M[(j+1)%3][(i+1)%3]*M[(j+2)%3][(i+2)%3]-M[(j+1)%3][(i+2)%3]*M[(j+2)%3][(i+1)%3])/D for j in range(3)] for i in range(3)]
def mm(A,B):return [[sum(A[i][k]*B[k][j] for k in range(3)) for j in range(3)] for i in range(3)]
def char(M):
 t=sum(M[i][i] for i in range(3));e=M[0][0]*M[1][1]-M[0][1]*M[1][0]+M[0][0]*M[2][2]-M[0][2]*M[2][0]+M[1][1]*M[2][2]-M[1][2]*M[2][1];return (Fraction(1),-t,e,-det(M))
def main():
 a=json.loads((RES/'cosmology_A16_raw_q_detector.json').read_text());b=json.loads((RES/'cosmology_A18_raw_q_detector.json').read_text());old=json.loads((RES/'cosmology_detector_change_A14_A16.json').read_text());assert a['target_order']==b['target_order'] and a['relation_basis']==b['relation_basis'];M16=[[q(x) for x in r] for r in a['detector_matrix']];M18=[[q(x) for x in r] for r in b['detector_matrix']];C=mm(M18,inv(M16));Cprev=[[q(x) for x in r] for r in old['change_matrix']];stationary=C==Cprev;samechar=char(C)==char(Cprev)
 out={'schema':'marici.voevodsky.cosmology-detector-transition-A16-A18.v1','status':'second_exact_transition_computed','relation_basis_identical':True,'transition_matrix':[[enc(x) for x in r] for r in C],'stationary':stationary,'same_characteristic_polynomial_as_prior':samechar,'decision':('Detector transport is stationary across both steps.' if stationary else 'Detector transport changes at the second step; equal characteristic data are reported separately.'),'claim_boundary':'Fixed 1,y,x labels and canonical echelon relation basis only.','next_gate':('derive-stationary-detector-law' if stationary else 'classify-nonstationary-detector-cocycle'),'passed':True};OUT.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items() if k!='transition_matrix'},indent=2))
if __name__=='__main__':main()
