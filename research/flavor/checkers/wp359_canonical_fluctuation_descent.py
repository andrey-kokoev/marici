"""WP359: exact field-reparameterization descent of the fluctuation probe."""

import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]


def main():
    a, Z = sp.symbols("a Z", positive=True)
    r, u, w = sp.symbols("r u w", real=True)
    q, kappa = sp.symbols("q kappa", positive=True)

    transformed = {
        Z: Z / a**2,
        r: r / a**2,
        u: u / a**4,
        w: w / a**6,
        q: a**2 * q,
        kappa: kappa / a**2,
    }
    Q = Z * q
    mass2 = kappa / Z
    R = r / Z
    U = u / Z**2
    W = w / Z**3

    def transform(expression):
        return sp.simplify(expression.xreplace(transformed))

    Qs, Ms = sp.symbols("Q M2", positive=True)
    inverse_R = Ms / 4
    inverse_U = -Ms / Qs
    inverse_W = 3 * Ms / (4 * Qs**2)
    coexist_q_canonical = -3 * inverse_U / (4 * inverse_W)
    coexist_mass = 3 * inverse_U**2 / (4 * inverse_W)

    representative_a = {Z: 1, r: 1, u: -4, w: 3, q: 1, kappa: 4}
    representative_b = {
        Z: sp.Rational(1, 4), r: sp.Rational(1, 4),
        u: sp.Rational(-1, 4), w: sp.Rational(3, 64), q: 4, kappa: 1,
    }

    checks = {
        "canonical_jump_descends": transform(Q) == Q,
        "pole_curvature_descends": transform(mass2) == mass2,
        "quadratic_coefficient_descends": transform(R) == R,
        "quartic_coefficient_descends": transform(U) == U,
        "sextic_coefficient_descends": transform(W) == W,
        "inverse_recovers_canonical_jump": sp.simplify(coexist_q_canonical - Qs) == 0,
        "inverse_recovers_pole_curvature": sp.simplify(coexist_mass - Ms) == 0,
        "hostile_representatives_have_different_raw_readouts": (
            representative_a[q] != representative_b[q]
            and representative_a[kappa] != representative_b[kappa]
        ),
        "hostile_representatives_have_equal_physical_readouts": (
            sp.simplify(Q.subs(representative_a) - Q.subs(representative_b)) == 0
            and sp.simplify(mass2.subs(representative_a) - mass2.subs(representative_b)) == 0
        ),
        "deliberate_raw_hessian_fails_descent": transform(kappa) != kappa,
    }
    checks = {name: bool(value) for name, value in checks.items()}

    result = {
        "work_package": "WP359",
        "admitted_state_domain": "classical WP357 coexistence packets augmented by Z>0, modulo positive effective-field rescalings t'=a*t",
        "faithful_quotient_coordinate": "(Q,M2)=(Z*q,kappa/Z), faithful on the two-dimensional coexistence coefficient quotient (R,U,W)=(r/Z,u/Z^2,w/Z^3)",
        "source_authorized_probe_family": "canonically normalized vacuum displacement and quadratic pole-curvature response from one effective action",
        "contextual_partition": "literal packets lie in positive field-rescaling orbits; (Q,M2) is constant on each orbit and reconstructs the coexistence quotient",
        "classification": "reparameterization-invariant source identifier on the conditional effective coexistence quotient; neither a numerical selector nor a full weak-basis descent theorem",
        "transformation": {name: str(expr) for name, expr in {
            "Z_prime": transformed[Z], "r_prime": transformed[r],
            "u_prime": transformed[u], "w_prime": transformed[w],
            "q_prime": transformed[q], "kappa_prime": transformed[kappa],
        }.items()},
        "invariant_readouts": {"Q": str(Q), "M2": str(mass2)},
        "inverse_quotient": {"R": str(inverse_R), "U": str(inverse_U), "W": str(inverse_W)},
        "smallest_exact_falsifier": "raw kappa transforms as kappa/a^2 and therefore cannot be treated as an instrument readout before kinetic normalization",
        "remaining_physical_instrument_gate": "derive the effective field and its coupling to flavor observables, measure a renormalized pole and canonical response in one scheme, and separately prove descent into physical16 under the full weak-basis groupoid",
        "checks": checks,
        "passed": all(checks.values()),
    }
    output = ROOT / "results/wp359_canonical_fluctuation_descent.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    if not result["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
