"""WP350: exact sector-character coefficient rays and residual amplitude authority."""

import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]


def main():
    x, y = sp.symbols("x y", real=True)
    coefficient_vector = sp.Matrix(sp.symbols("c1:4"))
    swap_12 = sp.Matrix([[0, 1, 0], [1, 0, 0], [0, 0, 1]])
    swap_23 = sp.Matrix([[1, 0, 0], [0, 0, 1], [0, 1, 0]])
    up_ray = sp.linsolve(
        list((swap_12 - sp.eye(3)) * coefficient_vector) + list((swap_23 - sp.eye(3)) * coefficient_vector),
        list(coefficient_vector),
    )
    down_ray = sp.linsolve(list((swap_12 + sp.eye(3)) * coefficient_vector), list(coefficient_vector))
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
    cp_odd = sp.factor(sp.trace(commutator**3))
    benchmark = {x: 1, y: 1}
    up_discriminant = sp.factor(sp.discriminant(yukawa_up.subs(benchmark).charpoly().as_expr()))
    down_discriminant = sp.factor(sp.discriminant(yukawa_down.subs(benchmark).charpoly().as_expr()))
    responses = [sp.factor(sp.diff(cp_odd, parameter).subs(benchmark)) for parameter in (x, y)]
    checks = {
        "up_symmetry_selects_democratic_ray": up_ray == {(coefficient_vector[2], coefficient_vector[2], coefficient_vector[2])},
        "down_odd_character_selects_antisymmetric_ray": down_ray == {(-coefficient_vector[1], coefficient_vector[1], 0)},
        "benchmark_up_spectrum_is_nondegenerate": up_discriminant == sp.Rational(181, 54),
        "benchmark_down_spectrum_is_nondegenerate": down_discriminant == sp.Rational(1, 2),
        "benchmark_commutator_is_nonsingular": commutator.subs(benchmark).det() == -sp.Rational(3658, 9) * sp.I,
        "benchmark_cp_invariant_is_nonzero": cp_odd.subs(benchmark) == -sp.Rational(3658, 3) * sp.I,
        "cp_responds_to_both_radial_amplitudes": responses == [-sp.Rational(48422, 9) * sp.I, -sp.Rational(10738, 3) * sp.I],
    }
    checks = {name: bool(value) for name, value in checks.items()}
    result = {
        "work_package": "WP350",
        "admitted_state_domain": "WP326 projector geometry with the up coefficient vector in the trivial permutation character and the down vector odd under P-Q transposition",
        "faithful_quotient_coordinate": "nondegenerate spectra and cubic CP-odd invariant on physical16",
        "source_operation": "sector character assignments select coefficient rays (1,1,1) and (1,-1,0), leaving radial amplitudes x and y",
        "up_invariant_ray": str(up_ray),
        "down_odd_ray": str(down_ray),
        "cp_odd_invariant": str(cp_odd),
        "benchmark_discriminants": [str(up_discriminant), str(down_discriminant)],
        "benchmark_cp_odd": str(cp_odd.subs(benchmark)),
        "radial_cp_responses": [str(value) for value in responses],
        "contextual_partition": "sector characters select two nonparallel coefficient directions and restore generic mixing, while every radial pair (x,y) remains a distinct physical packet generically",
        "classification": "a progressive structural selector of coefficient rays with generic CP capability, but not a numerical physical16 selector because both radial amplitudes retain physical response",
        "smallest_exact_falsifier": "at x=y=1 the CP invariant has nonzero derivatives with respect to both amplitudes, so symmetry-selected directions do not fix the physical packet",
        "remaining_physical_instrument_gate": "derive the unequal sector character assignments, select or normalize x and y upstream, prove stable matching, and test the predicted invariants on the fitted ensemble",
        "checks": checks,
        "passed": all(checks.values()),
    }
    output = ROOT / "results/wp350_sector_character_rays.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
    if not result["passed"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
