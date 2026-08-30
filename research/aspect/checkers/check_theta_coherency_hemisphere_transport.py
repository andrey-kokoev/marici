from __future__ import annotations

import json
from pathlib import Path

import sympy as sp


def main() -> None:
    K = sp.diag(1, -1)
    u, v = sp.symbols("u v", complex=True)
    psi = sp.Matrix([u, sp.conjugate(v)])
    s3 = sp.expand((sp.conjugate(psi).T * K * psi)[0])
    assert sp.simplify(s3 - (u * sp.conjugate(u) - v * sp.conjugate(v))) == 0

    # Ordinary unitary Jones transport preserves purity but not hemisphere.
    rotation = sp.Matrix([[sp.Rational(3, 5), -sp.Rational(4, 5)],
                          [sp.Rational(4, 5), sp.Rational(3, 5)]])
    assert rotation.T * rotation == sp.eye(2)
    north = sp.Matrix([1, 0])
    rotated = rotation * north
    north_s3 = (north.T * K * north)[0]
    rotated_s3 = (rotated.T * K * rotated)[0]
    assert north_s3 == 1
    assert rotated_s3 == sp.Rational(-7, 25)

    # A K-conformal transport preserves the sheet globally.
    boost = sp.Matrix([[sp.Rational(5, 3), sp.Rational(4, 3)],
                       [sp.Rational(4, 3), sp.Rational(5, 3)]])
    assert boost.T * K * boost == K
    transported_s3 = sp.simplify((sp.conjugate(boost * psi).T * K * (boost * psi))[0])
    assert sp.simplify(transported_s3 - s3) == 0

    # Unequal diagonal gain preserves rank one and positivity but can reverse
    # S3 for a state sufficiently close to the seam.
    gain = sp.diag(sp.Rational(1, 2), 1)
    assert gain.T * K * gain != K
    near_seam = sp.Matrix([sp.Rational(6, 5), 1])
    before_gain = (near_seam.T * K * near_seam)[0]
    after_gain = ((gain * near_seam).T * K * (gain * near_seam))[0]
    assert before_gain == sp.Rational(11, 25) > 0
    assert after_gain == sp.Rational(-16, 25) < 0

    # Reciprocal exchange is an orientation-reversing transport.
    exchange = sp.Matrix([[0, 1], [1, 0]])
    assert exchange.T * K * exchange == -K

    result = {
        "schema": "marici.aspect.theta-coherency-hemisphere-transport.v1",
        "status": "pass",
        "physical_interpretation": "H is a pure two-mode Jones coherency matrix if and only if (U,conjugate(V)) is admitted as a physical mode amplitude vector",
        "ordinary_unitary_preserves_rank_one": True,
        "ordinary_unitary_preserves_S3_sheet": False,
        "unitary_counterexample_S3_before": str(north_s3),
        "unitary_counterexample_S3_after": str(rotated_s3),
        "global_sheet_preservation_law": "J^dagger K J = lambda K with lambda>0",
        "K_unitary_boost_verified": True,
        "unequal_gain_counterexample_S3_before": str(before_gain),
        "unequal_gain_counterexample_S3_after": str(after_gain),
        "reciprocal_exchange_law": "P^dagger K P = -K",
        "verdict": "Rank-one positivity supplies pure coherency but no hemisphere dynamics; sheet preservation requires a source-derived positive K-conformal transport law.",
        "claim_boundary": "finite two-mode coherency/Jones audit; does not establish that theta transforms are laboratory optical modes or that completed Clark transport is K-conformal",
    }
    output = Path(__file__).parents[1] / "results" / "theta_coherency_hemisphere_transport.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
