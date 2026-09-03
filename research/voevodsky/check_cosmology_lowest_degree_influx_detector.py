"""Compute the exact matrix of the unique lowest-degree influx detector."""
import json
from fractions import Fraction
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];RES=ROOT/'research'/'voevodsky'/'results';OUT=RES/'cosmology_lowest_degree_influx_detector.json'
def q(x):return Fraction(x['numerator'],x['denominator'])
def enc(x):return {'numerator':x.numerator,'denominator':x.denominator}
def det(M):return M[0][0]*(M[1][1]*M[2][2]-M[1][2]*M[2][1])-M[0][1]*(M[1][0]*M[2][2]-M[1][2]*M[2][0])+M[0][2]*(M[1][0]*M[2][1]-M[1][1]*M[2][0])
def inverse(M):
 D=det(M);return [[(M[(j+1)%3][(i+1)%3]*M[(j+2)%3][(i+2)%3]-M[(j+1)%3][(i+2)%3]*M[(j+2)%3][(i+1)%3])/D for j in range(3)] for i in range(3)]
def main():
 d=json.loads((RES/'cosmology_raw_q_collapse_certificates.json').read_text());cs=d['groups'][1]['certificates'];pairs=[(0,0),(0,1),(1,0)];M=[]
 for pair in pairs:
  row=[]
  for c in cs:
   hits=[q(t['coefficient']) for t in c['raw_q_terms'] if t['descriptor'][1:4]==[0,0,[1,1,2,1,1]] and tuple(t['descriptor'][4])==pair];assert len(hits)==1;row.append(hits[0])
  M.append(row)
 D=det(M);assert D;I=inverse(M);assert all(sum(I[i][k]*M[k][j] for k in range(3))==Fraction(i==j) for i in range(3) for j in range(3))
 out={'schema':'marici.voevodsky.cosmology-lowest-degree-influx-detector.v1','status':'exact_invertible_affine_monomial_detector','exponent_pairs':[list(x) for x in pairs],'detector_matrix':[[enc(x) for x in row] for row in M],'determinant':enc(D),'inverse_matrix':[[enc(x) for x in row] for row in I],'decision':'The coefficient probes at monomials 1,y,x give an exact invertible coordinate system on the collapse space.','claim_boundary':'These are raw-q monomial-coefficient probes, not point-evaluation interpolation and not a geometric readout.','next_gate':'transport-lowest-degree-detector-across-ambient-steps','passed':True};OUT.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'status':out['status'],'determinant':out['determinant'],'passed':True},indent=2))
if __name__=='__main__':main()
