from __future__ import annotations
import json
from fractions import Fraction as Q

def ceilq(x): return (x.numerator+x.denominator-1)//x.denominator

def main():
    transition=Q(5856199,21735); trace=Q(70,3)
    # eta_strict=delta/[2(delta+Cminus)] > 1/130, giving C_tail >= delta/2=1/40.
    dimension=trace+130*transition; M=ceilq(dimension)
    # Exact scalar fixture: C>=c and G=F-BB*/c>=0 imply exact Schur F-B C^-1 B*>=0.
    c=Q(1,40); C=Q(1,20); B=Q(1,100); F=Q(1,100)
    G=F-B*B/c; exact_schur=F-B*B/C
    assert G>=0 and exact_schur>=G>=0
    result={"schema":"marici.voevodsky.strict-tail-schur-form-check.v1",
      "status":"computable_finite_sufficient_form_derived","strict_eta_lower":"1/130",
      "tail_margin":"1/40","dimension_upper":str(dimension),"sufficient_integer_M":M,
      "finite_form":"G_M=PAP-40*PAQAP","scalar_fixture_G":str(G),
      "scalar_fixture_exact_schur":str(exact_schur),
      "actual_finite_form_evaluated":False,"rh_implication":False,"passed":True}
    print(json.dumps(result,indent=2,sort_keys=True))
if __name__=='__main__':main()
