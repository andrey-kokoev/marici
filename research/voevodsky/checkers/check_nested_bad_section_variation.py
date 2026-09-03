from __future__ import annotations
import json
from fractions import Fraction

def main():
    # Nested connected sections [alpha_j,beta_j].
    alpha=[Fraction(-4),Fraction(-3),Fraction(-2),Fraction(-1)]
    beta=[Fraction(5),Fraction(4),Fraction(3),Fraction(2)]
    assert all(alpha[j]<=alpha[j+1] and beta[j+1]<=beta[j] for j in range(3))
    tv_alpha=sum(abs(alpha[j+1]-alpha[j]) for j in range(3))
    tv_beta=sum(abs(beta[j+1]-beta[j]) for j in range(3))
    telescoped=(alpha[-1]-alpha[0])+(beta[0]-beta[-1])
    assert tv_alpha+tv_beta==telescoped
    assert telescoped <= beta[0]-alpha[0]
    result={"schema":"marici.voevodsky.nested-bad-section-variation-check.v1",
            "status":"nested_interval_variation_telescopes","section_count":4,
            "total_variation":str(telescoped),"initial_width":str(beta[0]-alpha[0]),
            "variation_independent_of_section_count":True,
            "single_prime_sections_proved_connected":False,
            "rh_implication":False,"passed":True}
    print(json.dumps(result,indent=2,sort_keys=True))
if __name__=='__main__': main()
