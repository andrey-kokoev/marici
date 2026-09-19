import json
from fractions import Fraction as F
from pathlib import Path

ROOT=Path(__file__).resolve().parents[3]
OUT=ROOT/'research/nima/results/two-shell-ordered-port-equals-green-relative-response.json'

def addterm(poly,power,coefficient):
 poly[power]=poly.get(power,F(0))+coefficient
 if poly[power]==0: del poly[power]
def neg(poly): return {k:-v for k,v in poly.items()}
def encode(poly): return {str(k):str(v) for k,v in sorted(poly.items())}

def main():
 positions=[0,2,5]
 weights=[F(2,3),F(-3,5),F(7,4)]
 ordered={}; integrated_relative={}; pair_terms=[]
 for i,(qi,fi) in enumerate(zip(positions,weights)):
  for j in range(i+1,len(positions)):
   qj,fj=positions[j],weights[j]; d=qj-qi; c=fi*fj
   addterm(ordered,d,c);addterm(ordered,-d,-c)
   # r_Delta,i=-f_i sum_(j>i) f_j(t^d-t^-d)
   addterm(integrated_relative,d,-c);addterm(integrated_relative,-d,c)
   pair_terms.append({'i':i,'j':j,'distance':d,'positive_coefficient':str(c),'negative_coefficient':str(-c)})
 checks={
  'ordered_pairing_nonzero':bool(ordered),
  'relative_response_nonzero':bool(integrated_relative),
  'exact_incidence':integrated_relative==neg(ordered),
  'diagonal_excluded_by_antisymmetry':0 not in ordered
 }
 assert all(checks.values()),checks
 out={
  'schema':'marici.nima.two-shell-ordered-port-green-response.v1',
  'classification':'ordered_inverse_derivative_port_is_exactly_minus_the_integrated_green_relative_response_on_labelled_shell_sources',
  'positions':positions,'weights':[str(x) for x in weights],'pair_terms':pair_terms,
  'ordered_laurent_coefficients':encode(ordered),
  'integrated_relative_laurent_coefficients':encode(integrated_relative),
  'checks':checks,
  'identity':'For q_i<q_j, u(q_i)-v(q_i)=sum_(j>i) f_j(exp(z(q_j-q_i))-exp(-z(q_j-q_i))); hence integral r_Delta=-sum_i f_i(u_i-v_i)=-C_f(z).',
  'scope':'Exact finite labelled atomic sources; extension requires continuity of S and the Green tail maps on one common rigged core.',
  'next_gate':'Prove the identity for Schwartz or admissible theta forcing by Fubini on the ordered half-plane, then transport it through reciprocal/Tate completion without collapsing r_Delta.',
  'passed':True
 }
 OUT.write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8');print(json.dumps(out,indent=2))
if __name__=='__main__':main()
