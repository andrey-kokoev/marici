from __future__ import annotations
import json
from fractions import Fraction as Q

def ceilq(x): return (x.numerator+x.denominator-1)//x.denominator

def main():
    L=Q(7,20); N=24; W=200
    p_upper=Q(4400,483)       # 2*pi/log2 < (44/7)/(69/100)
    inv_pi2_upper=Q(1,9)      # pi > 3
    logN_upper=Q(16,5)        # log 24 < 16/5
    H=Q(2)+Q(2,3)+Q(2,5)+Q(2,7)
    zero=Q(1)+2*logN_upper
    middle=8*L*p_upper*N*inv_pi2_upper*H
    tail=4*L*p_upper*N*inv_pi2_upper
    transition=zero+middle+tail
    trace=L*W*Q(1,3)          # 1/pi < 1/3
    cminus_upper=Q(16,5)
    eta_lower=Q(1,20)/(Q(1,20)+cminus_upper) # 1/65
    dimension=trace+transition/eta_lower
    M=ceilq(dimension)
    assert M>=15839
    result={"schema":"marici.voevodsky.rational-first-prime-dimension-check.v1",
      "status":"first_prime_tail_dimension_rationally_certified",
      "p_upper":str(p_upper),"half_harmonic_K4":str(H),"zero_upper":str(zero),
      "middle_upper":str(middle),"tail_upper":str(tail),
      "transition_upper":str(transition),"trace_upper":str(trace),
      "cminus_upper":str(cminus_upper),"eta_lower":str(eta_lower),
      "dimension_upper":str(dimension),"sufficient_integer_M":M,
      "finite_schur_positivity_verified":False,"rh_implication":False,"passed":True}
    print(json.dumps(result,indent=2,sort_keys=True))
if __name__=='__main__':main()
