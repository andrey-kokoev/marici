"""WP351: exact radial-independent normalized CP selector on WP350 rays."""

import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]


def main():
    x, y = sp.symbols("x y", real=True, nonzero=True)
    spectral = sp.symbols("lambda")
    identity = sp.eye(3)
    p = sp.diag(1, 0, 0)
    q = sp.Matrix([[sp.Rational(1, 2), sp.Rational(1, 2), 0],
                   [sp.Rational(1, 2), sp.Rational(1, 2), 0],
                   [0, 0, 0]])
    vector_r = sp.Matrix([1, sp.I, 1])
    r = sp.simplify(vector_r * vector_r.conjugate().T / 3)
    democratic = sp.simplify(p + q + r)
    odd = sp.simplify(p - q)
    yukawa_up = identity + x * democratic
    yukawa_down = 2 * identity + y * odd
    hu = sp.simplify(yukawa_up * yukawa_up.conjugate().T)
    hd = sp.simplify(yukawa_down * yukawa_down.conjugate().T)
    commutator = sp.simplify(hu * hd - hd * hu)
    cp_trace = sp.factor(sp.trace(commutator**3))
    up_discriminant = sp.factor(sp.discriminant(hu.charpoly(spectral).as_expr(), spectral))
    down_discriminant = sp.factor(sp.discriminant(hd.charpoly(spectral).as_expr(), spectral))
    normalized_commutator_ratio = sp.factor(cp_trace**2 / (up_discriminant * down_discriminant))
    jarlskog_squared = sp.factor(-normalized_commutator_ratio / 36)
    checks = {
        "up_discriminant_is_nonzero_polynomial_generically": up_discriminant != 0,
        "down_discriminant_is_nonzero_polynomial_generically": down_discriminant != 0,
        "normalized_commutator_ratio_is_radial_independent": normalized_commutator_ratio == -sp.Rational(12, 181),
        "jarlskog_squared_is_exact": jarlskog_squared == sp.Rational(1, 543),
        "x_response_of_normalized_cp_is_zero": sp.diff(jarlskog_squared, x) == 0,
        "y_response_of_normalized_cp_is_zero": sp.diff(jarlskog_squared, y) == 0,
        "raw_cp_still_depends_on_radii": sp.diff(cp_trace, x) != 0 and sp.diff(cp_trace, y) != 0,
        "benchmark_matches_wp350_raw_cp": cp_trace.subs({x: 1, y: 1}) == -sp.Rational(3658, 3) * sp.I,
    }
    checks = {name: bool(value) for name, value in checks.items()}
    result = {
        "work_package": "WP351",
        "admitted_state_domain": "the nondegenerate strata of the WP350 sector-character ray family, excluding radial values where either Hermitian discriminant vanishes",
        "faithful_quotient_coordinate": "the normalized CP invariant after spectral Vandermonde factors are divided out",
        "source_operation": "WP350 symmetry characters select the Hermitian directions K=P+Q+R and L=P-Q while radial amplitudes x,y remain free",
        "raw_cp_trace": str(cp_trace),
        "up_discriminant": str(up_discriminant),
        "down_discriminant": str(down_discriminant),
        "normalized_commutator_ratio": str(normalized_commutator_ratio),
        "jarlskog_squared": str(jarlskog_squared),
        "jarlskog_magnitude": "1/sqrt(543)",
        "contextual_partition": "all nondegenerate radial points on the two selected rays share the same normalized CP magnitude while retaining different spectral invariants",
        "classification": "a genuine conditional numerical selector of one normalized mixing invariant, but not of spectra or a full physical16 point; projector geometry and sector characters remain stipulated source data",
        "smallest_exact_falsifier": "any admitted fitted flavor point with J^2 different from 1/543 falsifies the selected ray geometry independently of radial normalization",
        "remaining_physical_instrument_gate": "derive P,Q,R and the unequal sector characters from a source action, state eigenvalue-ordering conventions across discriminant strata, and compare the exact normalized prediction with the complete fitted ensemble",
        "checks": checks,
        "passed": all(checks.values()),
    }
    output = ROOT / "results/wp351_radial_independent_cp_selector.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    if not result["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
