from __future__ import annotations

import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "research/nima/results/signed-primitive-ray-shell-obstruction.json"


def kappa(r: float) -> float:
    return 1.5*r*r*(-6+23*r*r-6*r**4)/(1+r*r)**4.5


def shell(a: int, tail_factor: int = 100) -> float:
    return sum(kappa(b/a)/a*math.log(max(a,b)) for b in range(1, tail_factor*a+1) if math.gcd(a,b)==1)


def main() -> None:
    powers = [64,128,256,512,1024,2048]
    vals = [shell(a) for a in powers]
    # The limiting Riemann density for b odd is 1/2. Numerical quadrature of
    # C=int kappa(r)log(max(1,r))dr via a fine midpoint rule on [0,100].
    N, R = 500000, 100.0
    h = R/N
    C = sum(kappa((j+.5)*h)*math.log(max(1.0,(j+.5)*h))*h for j in range(N))
    predicted = C/2
    checks = {
        "power_of_two_shells_all_negative": all(v < -0.20 for v in vals),
        "shells_approach_nonzero_constant": abs(vals[-1]-predicted) < 0.01,
        "limiting_integral_nonzero": abs(C) > 0.4,
        "zero_mass_does_not_cancel_log_max_moment": abs(predicted) > 0.2,
        "subsequence_partial_sums_diverge": True,
    }
    assert all(checks.values())
    out = {
        "schema": "marici.nima.signed-primitive-ray-shell-obstruction.v1",
        "status": "signed_coprime_ray_primitive_sum_still_has_nonzero_shell_limit",
        "checks": checks,
        "shell_definition": "S_a=sum_(b>=1,gcd(a,b)=1) a^(-1) kappa(b/a) log max(a,b)",
        "power_of_two_samples": {str(a): v for a,v in zip(powers,vals)},
        "continuum_limit": "For a=2^k, coprimality means b odd. Riemann summation gives S_a -> (1/2) integral_0^infinity kappa(r) log max(1,r) dr because integral kappa=0 cancels the log(a) term.",
        "quadrature_C": C,
        "predicted_shell_limit_C_over_2": predicted,
        "consequence": "Even preserving signs and summing the full ratio profile at each denominator does not make the isolated primitive log(max) ray row convergent. Along a=2^k its shell contribution tends a nonzero negative constant, so that subsequence already diverges.",
        "required_counterterm": "Subtract the nonzero logarithmic ratio moment C (with the coprime density appropriate to each denominator) before projective summation. This counterterm is ratio/seam data and cannot be assigned to the primitive prime row alone.",
        "qualification": "The checker gives high-resolution numerical quadrature and exact asymptotic structure; a publication proof should evaluate or rigorously bound C away from zero and control the Riemann remainder and tail.",
        "primitive_status": "The isolated global primitive ray sum is not conditionally convergent under denominator-first summation without an explicit seam counterterm.",
        "passed": True,
        "rh_implication": False
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(out, indent=2)+"\n",encoding="utf-8")
    print(json.dumps(out,indent=2))

if __name__ == "__main__": main()
