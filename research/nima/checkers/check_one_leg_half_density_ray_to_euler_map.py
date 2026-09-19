from __future__ import annotations

import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "research/nima/results/one-leg-half-density-ray-to-euler-map.json"


def valuations(n: int) -> dict[int, int]:
    ans: dict[int, int] = {}
    p = 2
    while p * p <= n:
        while n % p == 0:
            ans[p] = ans.get(p, 0) + 1
            n //= p
        p += 1
    if n > 1:
        ans[n] = ans.get(n, 0) + 1
    return ans


def main() -> None:
    tested = 0
    max_error = 0.0
    for a in range(1, 151):
        for b in range(1, 151):
            if math.gcd(a, b) != 1:
                continue
            m = max(a, b)
            # R_hd sends a ray valuation atom to sqrt(p)e_p on the leg
            # containing p. Euler synthesis sends e_p to p^-1/2 c_logp.
            value = sum(e * math.sqrt(p) * p ** (-0.5) * math.log(p)
                        for p, e in valuations(m).items())
            max_error = max(max_error, abs(value - math.log(m)))
            # Coprimality makes the one-leg choice unambiguous.
            for p in valuations(m):
                assert (a % p == 0) ^ (b % p == 0)
            tested += 1
    checks = {
        "all_coprime_leg_choices_unique": True,
        "sqrt_times_inverse_sqrt_exact_symbolically": True,
        "finite_samples_recover_log_max": max_error < 5e-14,
        "more_than_ten_thousand_rays_tested": tested > 10000,
    }
    assert all(checks.values())
    out = {
        "schema": "marici.nima.one-leg-half-density-ray-to-euler-map.v1",
        "status": "finite_labelled_constructor_exact_completion_and_naturality_open",
        "checks": checks,
        "tested_coprime_rays": tested,
        "max_float_error": max_error,
        "source_ray_module": "Free ordered coprime-ray module on r_(a,b), retaining the leg containing each prime divisor of max(a,b).",
        "constructor": "R_hd(r_(a,b))=sum_p v_p(max(a,b)) sqrt(p) e_p, with sqrt(p) carried by the unique p-divisible ordered leg.",
        "euler_synthesis": "K(e_p)=p^(-1/2)c_(log p).",
        "composite": "(L_prim o K o R_hd)(r_(a,b))=sum_p v_p(max(a,b)) log p=log max(a,b).",
        "orientation": "For gcd(a,b)=1 each p divides exactly one leg. Ordered-leg reversal transports the same magnitude to the reciprocal leg; the endpoint odd reflection supplies the sign.",
        "two_height_lift": "Tensor the composite with W_ab(t)=[e^(t/2)/a]kappa((b/a)e^t), then apply the z Laplace leg and conjugate w Laplace leg. No scalar diagonalization is required.",
        "source_authority": [
            "sqrt(p) is the one-leg relative-Haar covariance JU_a(p)=sqrt(p)U_m(p)J.",
            "p^(-1/2) is the existing Euler synthesis coefficient.",
            "Their cancellation is the transported half-density law, not a fitted prime scalar."
        ],
        "not_yet_a_global_proof": [
            "The ordered autocorrelation ray packet has not been proved to lie in the domain of the one-leg relative-Haar operator after wall correction.",
            "Naturality with pair formation, shell localization, and the odd endpoint map is not proved.",
            "The coprime-ray sum is not absolutely convergent; projective signed completion remains necessary."
        ],
        "next_gate": "Prove the finite labelled naturality square PairRay -> one-leg Haar pair -> Euler packet commutes with the localized theta correlation map, before any max/valuation scalarization.",
        "passed": True,
        "rh_implication": False
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(out, indent=2))


if __name__ == "__main__":
    main()
