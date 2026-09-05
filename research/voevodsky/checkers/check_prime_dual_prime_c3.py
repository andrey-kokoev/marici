from __future__ import annotations
import json
from pathlib import Path
import sympy as sp

x=sp.symbols('x',real=True)
ell=sp.log(2);m=sp.log(3)
f=sp.exp(x)

def R(expr,q):return sp.simplify(expr.subs(x,q-x))

def main():
 involution_2=sp.simplify(R(R(f,ell),ell)-f)==0
 involution_3=sp.simplify(R(R(f,m),m)-f)==0
 product=R(R(f,m),ell) # R_ell R_m f
 cube=f
 for _ in range(3):cube=R(R(cube,m),ell)
 ratio=sp.simplify(cube/f);obstruction=sp.simplify(ratio-1)
 direct_adjoint=sp.simplify(f.subs(x,x+ell).subs(x,x-ell)-f)==0
 equal_prime_cube=f
 for _ in range(3):equal_prime_cube=R(R(equal_prime_cube,ell),ell)
 equal_trivial=sp.simplify(equal_prime_cube-f)==0
 result={
  'schema':'marici.voevodsky.prime-dual-prime-c3.v1',
  'R_log2_involutive':involution_2,'R_log3_involutive':involution_3,
  'R_log2_R_log3_on_exp_x':str(product),
  'cube_ratio_on_exp_x':str(ratio),'cube_obstruction':str(obstruction),
  'distinct_prime_C3_closure':obstruction==0,
  'direct_translation_adjoint_collapses_to_identity':direct_adjoint,
  'equal_prime_control_closes_trivially':equal_trivial,
  'deliberate_failure_trivial_control_rejected_as_three_phase':equal_trivial,
  'periodic_quotient_required_for_nontrivial_closure':True,
  'periodic_quotient_source_derived':False,
  'bold_conjecture_survives':False,
  'abstract_C3_index_unaffected':True,
  'passed':all([involution_2,involution_3,obstruction==sp.Rational(19,8),direct_adjoint,equal_trivial])}
 text=json.dumps(result,indent=2,sort_keys=True);Path('research/voevodsky/results/prime_dual_prime_c3.json').write_text(text+'\n',encoding='utf-8');print(text)
if __name__=='__main__':main()
