"""WP357: exact authority audit for a finite first-order flavor jump."""

import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]


def main():
    t = sp.symbols("t", real=True)
    q = sp.symbols("q", real=True, positive=True)
    r, u, w = sp.symbols("r u w", real=True)

    potential = r * t**2 / 2 + u * t**4 / 4 + w * t**6 / 6
    potential_q = r * q / 2 + u * q**2 / 4 + w * q**3 / 6
    stationary_q = r + u * q + w * q**2
    coexist_q = -3 * u / (4 * w)
    coexist_r = 3 * u**2 / (16 * w)

    stationarity_residual = sp.factor(
        stationary_q.subs({q: coexist_q, r: coexist_r})
    )
    degeneracy_residual = sp.factor(
        potential_q.subs({q: coexist_q, r: coexist_r})
    )
    broken_curvature = sp.factor(
        sp.diff(potential, t, 2)
        .subs(t**2, coexist_q)
        .subs(r, coexist_r)
    )
    response_u = sp.diff(coexist_q, u)
    response_w = sp.diff(coexist_q, w)

    packet_a = {r: 1, u: -4, w: 3}
    packet_b = {r: 2, u: -8, w: 6}
    qa = sp.simplify(coexist_q.subs(packet_a))
    qb = sp.simplify(coexist_q.subs(packet_b))
    ra_residual = sp.simplify((r - coexist_r).subs(packet_a))
    rb_residual = sp.simplify((r - coexist_r).subs(packet_b))

    checks = {
        "coexistence_stationarity_residual_zero": stationarity_residual == 0,
        "coexistence_degeneracy_residual_zero": degeneracy_residual == 0,
        "broken_curvature_is_minus_u_times_q": broken_curvature == -u * coexist_q,
        "jump_responds_to_quartic_coefficient": response_u == -sp.Rational(3, 4) / w,
        "jump_responds_to_sextic_coefficient": response_w == 3 * u / (4 * w**2),
        "hostile_packet_a_is_on_coexistence_surface": ra_residual == 0,
        "hostile_packet_b_is_on_coexistence_surface": rb_residual == 0,
        "distinct_hostile_packets_have_equal_jump": packet_a != packet_b and qa == qb == 1,
        "deliberate_off_surface_perturbation_is_detected": (
            sp.simplify(stationary_q.subs({q: 1, r: 2, u: -4, w: 3})) != 0
        ),
    }
    checks = {name: bool(value) for name, value in checks.items()}

    result = {
        "work_package": "WP357",
        "admitted_state_domain": "classical stationary vacua of the normalized even sextic V=r*t^2/2+u*t^4/4+w*t^6/6 with u<0 and w>0, restricted to symmetric/broken coexistence",
        "faithful_quotient_coordinate": "the CP-geometry magnitude q=t^2, not the full physical16 coordinate",
        "source_authorized_probe_family": "stationarity, vacuum degeneracy, stability, and coefficient interventions inside the declared sextic grammar",
        "contextual_partition": "the coexistence surface r=3*u^2/(16*w) has a symmetric vacuum q=0 and a broken sign pair with q=-3*u/(4*w)",
        "classification": "conditional first-order phase selector and sign-pair rigidifier; not a numerical jump selector and not a full physical16 selector",
        "potential": str(potential),
        "coexistence_q": str(coexist_q),
        "coexistence_r": str(coexist_r),
        "stationarity_residual": str(stationarity_residual),
        "degeneracy_residual": str(degeneracy_residual),
        "broken_curvature": str(broken_curvature),
        "response_u": str(response_u),
        "response_w": str(response_w),
        "hostile_pair": {
            "packet_a": {"r": 1, "u": -4, "w": 3},
            "packet_b": {"r": 2, "u": -8, "w": 6},
            "common_q": int(qa),
        },
        "smallest_exact_falsifier": "d q_star/d u=-3/(4*w) is nonzero, so coexistence leaves the quartic-to-sextic source ratio authoritative",
        "remaining_physical_instrument_gate": "derive a normalized flavor sextic action, independently fix u/w, and calibrate the threshold jump in physical16; classical equality does not license quotienting action scale for fluctuation-sensitive instruments",
        "checks": checks,
        "passed": all(checks.values()),
    }
    output = ROOT / "results/wp357_first_order_jump_authority.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    if not result["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
