"""WP358: exact joint-faithfulness audit for jump plus fluctuation curvature."""

import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]


def main():
    u, w = sp.symbols("u w", real=True)
    q_symbol, kappa_symbol = sp.symbols("q kappa", real=True, positive=True)

    q = -3 * u / (4 * w)
    kappa = 3 * u**2 / (4 * w)
    response = sp.Matrix([q, kappa]).jacobian([u, w])
    determinant = sp.factor(response.det())

    inverse_u = -kappa_symbol / q_symbol
    inverse_w = 3 * kappa_symbol / (4 * q_symbol**2)
    inverse_r = kappa_symbol / 4
    forward_after_inverse = (
        sp.simplify(q.subs({u: inverse_u, w: inverse_w})),
        sp.simplify(kappa.subs({u: inverse_u, w: inverse_w})),
    )

    packet_a = {u: -4, w: 3}
    packet_b = {u: -8, w: 6}
    qa, qb = sp.simplify(q.subs(packet_a)), sp.simplify(q.subs(packet_b))
    ka, kb = sp.simplify(kappa.subs(packet_a)), sp.simplify(kappa.subs(packet_b))

    checks = {
        "response_determinant_is_nonzero_on_domain": determinant == -9 * u**2 / (16 * w**3),
        "inverse_recovers_q": forward_after_inverse[0] == q_symbol,
        "inverse_recovers_curvature": forward_after_inverse[1] == kappa_symbol,
        "coexistence_r_is_curvature_over_four": (
            sp.simplify(3 * inverse_u**2 / (16 * inverse_w) - inverse_r) == 0
        ),
        "jump_only_hostile_pair_collides": qa == qb == 1,
        "curvature_separates_hostile_pair": ka == 4 and kb == 8 and ka != kb,
        "positive_readouts_reconstruct_admitted_signs": (
            inverse_u.is_negative and inverse_w.is_positive and inverse_r.is_positive
        ),
        "deliberate_missing_curvature_leaves_scale_kernel": (
            sp.simplify(q.subs({u: 2 * u, w: 2 * w}) - q) == 0
            and sp.simplify(kappa.subs({u: 2 * u, w: 2 * w}) - kappa) != 0
        ),
    }
    checks = {name: bool(value) for name, value in checks.items()}

    result = {
        "work_package": "WP358",
        "admitted_state_domain": "normalized even-sextic source packets on the coexistence surface with u<0 and w>0, conditional on a fixed canonical kinetic normalization",
        "faithful_quotient_coordinate": "the joint source readout (q,kappa), where q=t^2 and kappa is the calibrated broken-vacuum pole-curvature scale; this is not full physical16",
        "source_authorized_probe_family": "vacuum jump plus quadratic fluctuation response derived from the same sextic action",
        "contextual_partition": "jump-only classes are rays under common positive action scaling; adding calibrated curvature separates every point of the coexistence coefficient family",
        "classification": "jointly faithful source identifier on the conditional coexistence grammar; neither a numerical selector nor a full physical16 selector",
        "response_matrix": str(response),
        "response_determinant": str(determinant),
        "inverse": {"u": str(inverse_u), "w": str(inverse_w), "r": str(inverse_r)},
        "hostile_pair": {
            "packet_a": {"r": 1, "u": -4, "w": 3, "q": int(qa), "kappa": int(ka)},
            "packet_b": {"r": 2, "u": -8, "w": 6, "q": int(qb), "kappa": int(kb)},
        },
        "smallest_exact_falsifier": "jump-only readout maps the two distinct packets to q=1, while calibrated curvature separates them as kappa=4 and 8",
        "remaining_physical_instrument_gate": "fix the field kinetic normalization and realize kappa as a pole mass or calibrated response including wave-function and threshold corrections in the same frame as q",
        "checks": checks,
        "passed": all(checks.values()),
    }
    output = ROOT / "results/wp358_coexistence_fluctuation_completion.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    if not result["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
