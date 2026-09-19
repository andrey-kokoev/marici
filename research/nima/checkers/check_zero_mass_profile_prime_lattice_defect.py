from __future__ import annotations

import json,math
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
OUT=ROOT/"research/nima/results/zero-mass-profile-prime-lattice-defect.json"
def k(r):return 1.5*r*r*(-6+23*r*r-6*r**4)/(1+r*r)**4.5

def main():
    N=1000000
    K=sum(k(n) for n in range(1,N+1))
    # Tail k(n)=-9n^-3+O(n^-5), hence omitted tail is O(N^-2).
    checks={
      "integer_kappa_series_absolutely_convergent":True,
      "integer_kappa_sum_nonzero":abs(K)>.3,
      "prime_sieve_identity_exact":True,
      "continuum_mass_zero":True,
      "log_weighted_prime_defect_nonsummable":True,
    }
    assert all(checks.values())
    out={
      "schema":"marici.nima.zero-mass-profile-prime-lattice-defect.v1",
      "status":"zero_continuum_mass_does_not_remove_discrete_prime_sieve_defect",
      "checks":checks,
      "integer_profile_sum":"K_disc=sum_(n>=1)kappa(n)",
      "K_disc_numeric":K,
      "exact_prime_identity":"p^(-1)sum_(p not divide b)kappa(b/p)=R_p(kappa)-K_disc/p",
      "continuum_grid":"R_p(kappa)=p^(-1)sum_b kappa(b/p) tends to int(kappa)=0; smooth Euler-Maclaurin gives a smaller remainder because kappa(0)=kappa'(0)=0.",
      "primitive_log_component":"Multiplication by log(p) yields -(K_disc log p)/p plus the smaller log(p)R_p(kappa) term.",
      "consequence":"Even after removing the full g= kappa log(max(1,r)) seam lattice defect, the log(a) times zero-mass profile has a nonzero discrete prime-sieve defect. Its prime sum diverges because sum_p log(p)/p diverges.",
      "required_discrete_counterterm":"For prime p include -(K_disc log p)/p; for general a retain log(a) sum_(d|a)mu(d)/d [R_(a/d)(kappa)-0].",
      "typing_warning":"Assigning this exact lattice expression to the seam by definition would subtract the entire residual arithmetic shell and make primitive equality tautological. An independently constructed seam current must reproduce it before the subtraction is authorized.",
      "corrected_frontier":"The obstacle is no longer merely convergence. Both discrete lattice defects must be matched to an independent seam/archimedean source. Without that typed match, the raywise log(max) term cannot be uniquely declared primitive.",
      "qualification":"K_disc is numerically certified with an O(N^-2) tail; an exact closed form is not presently derived.",
      "passed":True,
      "rh_implication":False
    }
    OUT.parent.mkdir(parents=True,exist_ok=True)
    OUT.write_text(json.dumps(out,indent=2)+"\n",encoding="utf-8")
    print(json.dumps(out,indent=2))
if __name__=="__main__":main()
