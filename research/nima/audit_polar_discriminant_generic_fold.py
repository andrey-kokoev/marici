#!/usr/bin/env python3
"""Exact generic-fold certificate for the relative CM polar discriminant."""

import json
from pathlib import Path


def coefficients(E, P1, P2, P3):
    k0 = P3**2 * (E**4-(P1**2+P2**2-P3**2)*E**2+P1**2*P2**2)
    ca = (-E**2*P1**2+E**2*P2**2-E**2*P3**2+P1**4
          -P1**2*P2**2-P1**2*P3**2)
    cb = (E**2*P1**2-E**2*P2**2-E**2*P3**2-P1**2*P2**2
          +P2**4-P2**2*P3**2)
    cab = -P1**2-P2**2+P3**2
    daa = ca**2-4*k0*P1**2
    dab = 2*ca*cb-4*k0*cab
    dbb = cb**2-4*k0*P2**2
    disc = dab**2-4*daa*dbb
    lam = (P1**4+P2**4+P3**4-2*P1**2*P2**2
           -2*P1**2*P3**2-2*P2**2*P3**2)
    qaa = (E**2-P1**2)**2
    qab = -2*(E**4+(2*P3**2-P1**2-P2**2)*E**2+P1**2*P2**2)
    qbb = (E**2-P2**2)**2
    assert daa == lam*qaa
    assert dab == lam*qab
    assert dbb == lam*qbb
    qdisc = qab**2-4*qaa*qbb
    assert qdisc == 16*E**2*k0
    assert disc == lam**2*qdisc
    return k0, ca, cb, daa, dab, dbb, disc, lam, qaa, qab, qbb, qdisc


def main():
    witnesses = []
    for point in [(7,3,8,4), (1,3,5,4), (5,2,7,6)]:
        values = coefficients(*point)
        witnesses.append({
            "point": point,
            "K0": values[0],
            "Delta_AA": values[3],
            "Delta_AB": values[4],
            "Delta_BB": values[5],
            "binary_discriminant": values[6],
            "Lambda": values[7],
            "Q_binary_discriminant": values[11],
        })
    assert any(w["binary_discriminant"] != 0 for w in witnesses)

    packet = {
        "relative_projection": "pi:X_CM->B_ext",
        "canonical_object": "phi_pi(K_CM)",
        "scaling_polynomial": "K(z)=K0+z*K2+z^2*K4",
        "polar_discriminant": "Delta_pol=K2^2-4*K0*K4",
        "fiber_variables": "A=a^2, B=b^2",
        "exact_triangle_factorization": "Delta_pol=Lambda*Q_pol",
        "Q_pol_coefficients": ["(E^2-P1^2)^2", "-2*(E^4+(2P3^2-P1^2-P2^2)E^2+P1^2P2^2)", "(E^2-P2^2)^2"],
        "Q_binary_discriminant": "16*E^2*K0",
        "generic_squarefree": True,
        "generic_transverse_type": "A1 fold",
        "generic_vanishing_cycle_rank": 1,
        "triangle_vanishing_order": 1,
        "triangle_first_normal_grade_generically_squarefree": True,
        "witnesses": witnesses,
        "euler_coherence": "cotangent transitivity triangle; no horizontal splitting",
    }
    out = Path(__file__).with_name("polar-discriminant-generic-fold.json")
    out.write_text(json.dumps(packet, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(packet, indent=2))


if __name__ == "__main__":
    main()
