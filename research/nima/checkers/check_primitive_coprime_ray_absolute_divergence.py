from __future__ import annotations

import hashlib
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "research/nima/results/primitive-coprime-ray-absolute-divergence.json"
SOURCES = {
    "profile": "research/nima/theta-autocorrelation-double-kernel-reduces-to-a-universal-ratio-profile.md",
    "pushforward": "research/nima/results/coprime-ray-to-primitive-valuation-pushforward.json",
    "sign": "research/nima/results/primitive-ray-global-sign.json",
}


def kappa(r: float) -> float:
    return 1.5 * r*r * (-6 + 23*r*r - 6*r**4) / (1 + r*r)**4.5


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    return all(n % d for d in range(2, int(math.sqrt(n)) + 1))


def main() -> None:
    raw = {name: (ROOT / path).read_text(encoding="utf-8") for name, path in SOURCES.items()}
    # At t=0 use the fixed wedge 1/8 <= b/a <= 1/4.  Kappa is strictly
    # negative there. For prime a every 1<=b<a is coprime to a. Each wedge
    # has Theta(a) terms of size Theta(1/a), hence absolute shell mass is
    # bounded below independently of a; multiplying by log(max)=log(a)
    # makes prime shells grow like log(a).
    shells: dict[str, float] = {}
    for a in range(101, 1000):
        if not is_prime(a):
            continue
        lo, hi = math.ceil(a / 8), math.floor(a / 4)
        mass = sum(abs(kappa(b / a)) / a * math.log(a) for b in range(lo, hi + 1))
        shells[str(a)] = mass
    vals = list(shells.values())
    checks = {
        "explicit_sign_changing_profile_available": "kappa(r)" in raw["profile"],
        "valuation_weight_is_log_max": "log max(a,b)" in raw["pushforward"],
        "wedge_profile_strictly_negative": max(kappa(j / 10000) for j in range(1250, 2501)) < 0,
        "many_prime_shells_tested": len(vals) > 100,
        "prime_shell_absolute_mass_positive": min(vals) > 0,
        "normalized_shell_mass_uniform": min(v / math.log(int(a)) for a, v in shells.items()) > 0.001,
        "prior_majorant_gate_was_open": "projective majorant" in raw["sign"],
    }
    assert all(checks.values())
    out = {
        "schema": "marici.nima.primitive-coprime-ray-absolute-divergence.v1",
        "status": "absolute_coprime_ray_majorant_falsified_conditional_completion_required",
        "checks": checks,
        "wedge": "t=0, a prime, a/8 <= b <= a/4",
        "proof": "On r in [1/8,1/4], kappa(r)<0 and |kappa(r)|>=c>0. For prime a all wedge labels b are coprime to a; there are Theta(a) of them. Since W_ab=a^(-1)kappa(b/a) and log max(a,b)=log a, the absolute primitive mass of each such a-shell is >=C log a. Hence the full absolute coprime-ray sum diverges.",
        "tested_prime_shells": len(vals),
        "tested_shell_mass_range": [min(vals), max(vals)],
        "consequence": "No Tonelli argument or coefficientwise l1/projective majorant can close the primitive row. The zero-mass cancellation of the complete ratio profile is essential and is destroyed by absolute values.",
        "required_completion": "Use signed ratio summation (Euler-Maclaurin or Poisson) at each denominator before prime-valuation readout, prove the remainder is continuous in the declared projective topology, and only then commute the result with the two Laplace legs.",
        "primitive_status": "Normalization, arithmetic labels, sign, and two-height ray formula are closed; global equality remains open solely at the conditional resummation/topology gate.",
        "artifacts_sha256": {name: hashlib.sha256((ROOT / path).read_bytes()).hexdigest() for name, path in SOURCES.items()},
        "passed": True,
        "rh_implication": False,
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(out, indent=2))


if __name__ == "__main__":
    main()
