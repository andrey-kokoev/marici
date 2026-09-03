from __future__ import annotations
import json
from fractions import Fraction

def main():
    numerator_lower=Fraction(17,2)-Fraction(23,20)-Fraction(1,30000)-Fraction(1,200000000)
    gamma_lower=numerator_lower/Fraction(88,7)
    required_upper=Fraction(547,1000)
    margin=gamma_lower-required_upper
    assert margin>0
    result={"schema":"marici.voevodsky.binet-digamma-cutoff-check.v1",
            "status":"safe_cutoff_certified_by_rational_bounds",
            "log_abs_z_lower":"17/2","log_pi_upper":"23/20",
            "binet_remainder_upper":"1/30000","half_inverse_real_upper":"1/200000000",
            "four_pi_upper":"88/7","m_gamma_lower":str(gamma_lower),
            "required_level_upper":str(required_upper),"certified_margin":str(margin),
            "safe_R":10000,"directed_interval_required":False,
            "rh_implication":False,"passed":True}
    print(json.dumps(result,indent=2,sort_keys=True))
if __name__=='__main__':main()
