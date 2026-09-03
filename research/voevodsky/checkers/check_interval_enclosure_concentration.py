from __future__ import annotations
import json
from fractions import Fraction as Q

def ceilq(x): return (x.numerator+x.denominator-1)//x.denominator

def main():
    # Omega is enlarged to [-R,R], R=100, L=7/20. Then 2LR=70.
    # log 70 < 17/4 and pi^2>9.
    transition=Q(3,1)/9 + 2*Q(17,4)/9
    assert transition==Q(23,18)
    trace=Q(70,3)
    dimension=trace+130*transition
    M=ceilq(dimension)
    assert M==190
    result={"schema":"marici.voevodsky.interval-enclosure-concentration-check.v1",
      "status":"single_interval_enclosure_replaces_resonance_count",
      "R":100,"L":"7/20","two_L_R":70,"log_two_L_R_upper":"17/4",
      "transition_upper":str(transition),"trace_upper":str(trace),
      "strict_eta_lower":"1/130","dimension_upper":str(dimension),
      "sufficient_integer_M":M,"concentration_basis_materialized":False,
      "finite_form_evaluated":False,"rh_implication":False,"passed":True}
    print(json.dumps(result,indent=2,sort_keys=True))
if __name__=='__main__':main()
