from fractions import Fraction as F
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
OUT=ROOT/'research/nima/results/low-cumulants-do-not-select-det3-operator.json'
def invariants(xs):
 return sum(xs,F(0)),sum((x*x for x in xs),F(0)),__import__('functools').reduce(lambda a,x:a*(1+x),xs,F(1))
def main():
 a=[F(1,2),F(-1,2),F(0)]
 b=[F(4,13),F(7,26),F(-15,26)]
 ia=invariants(a);ib=invariants(b)
 checks={'same_trace':ia[0]==ib[0],'same_trace_square':ia[1]==ib[1],'different_fredholm_determinant':ia[2]!=ib[2],'all_I_plus_eigenvalues_nonzero':all(1+x for x in a+b)}
 assert all(checks.values())
 # det3 differs by the same determinant ratio because low counterterms agree.
 out={'schema':'marici.nima.low-cumulants-do-not-select-det3-operator.v1','status':'primitive_and_square_currents_insufficient_to_construct_state_indexed_det3_assignment','checks':checks,'spectrum_A':[str(x) for x in a],'spectrum_B':[str(x) for x in b],'common_trace':str(ia[0]),'common_trace_square':str(ia[1]),'det_I_plus_A':str(ia[2]),'det_I_plus_B':str(ib[2]),'det3_consequence':'Since Tr K and Tr K^2 agree, the det3 counterterm exp(-Tr K+Tr K^2/2) is identical; unequal det(I+K) therefore gives unequal det3(I+K).','architectural_consequence':'Endpoint primitive and square currents constrain only the first two cumulants. They cannot define kappa_G or its connected determinant tail. A source operator family, composition law, or independent connected spectral data is indispensable.','noncircularity':'Choosing eigenvalues to reproduce the desired det3 section would fit the missing connected channel and is not a source construction.','passed':True,'rh_implication':False}
 OUT.write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
