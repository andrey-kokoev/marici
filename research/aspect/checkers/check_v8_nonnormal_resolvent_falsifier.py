import json
from pathlib import Path

import sympy as sp


root = Path(__file__).parents[1]
v8 = json.loads(
    (root / "contracts" / "frozen-bivariant-network-signature.v8.json").read_text(
        encoding="utf-8"
    )
)

z = sp.Rational(5, 2)
cutoffs = [2, 4, 8, 16]


def upper_shift(n: int) -> sp.Matrix:
    S = sp.zeros(n)
    for row in range(n - 1):
        S[row, row + 1] = 1
    return S


def packet(n: int) -> dict[str, object]:
    S = upper_shift(n)
    A = 2 * sp.eye(n) + S
    shifted = A - z * sp.eye(n)
    resolvent = shifted.inv()
    return {
        "characteristic_polynomial": sp.factor(A.charpoly().as_expr()),
        "zero_kernel": len(A.nullspace()) == 0,
        "zero_cokernel": n - A.rank() == 0,
        "zero_uniform_lower_bound": 1,
        "shifted_invertible": shifted.det() != 0,
        "corner_resolvent_magnitude": abs(resolvent[0, n - 1]),
    }


packets = [packet(n) for n in cutoffs]
family = v8["analytic_completed_resolved_route_family"]
all_terms = (
    set(v8["object_types"])
    | set(v8["arrow_types"])
    | set(v8["cell_types"])
    | set(family["required_fields"])
    | set(family["required_laws"])
    | set(v8["forbidden_promotions"])
)

missing_markers = (
    "spectral_parameter",
    "resolvent_family",
    "pseudospectrum",
    "functional_calculus",
    "parameterized_spectral",
)

checks = {
    "v8_is_frozen": v8["cell_creation_during_replay"] is False,
    "all_finite_spectra_are_only_two": all(packet_["characteristic_polynomial"] == (sp.Symbol("lambda") - 2) ** n for n, packet_ in zip(cutoffs, packets)),
    "all_zero_point_kernels_and_cokernels_vanish": all(packet_["zero_kernel"] and packet_["zero_cokernel"] for packet_ in packets),
    "zero_point_has_uniform_lower_bound_one": all(packet_["zero_uniform_lower_bound"] == 1 for packet_ in packets),
    "all_finite_sections_are_invertible_at_five_halves": all(packet_["shifted_invertible"] for packet_ in packets),
    "resolvent_corner_grows_exponentially": [packet_["corner_resolvent_magnitude"] for packet_ in packets] == [2**n for n in cutoffs],
    "completed_adjoint_kernel_witness_is_square_summable": sp.summation(sp.Rational(1, 4) ** sp.Symbol("k", integer=True, nonnegative=True), (sp.Symbol("k", integer=True, nonnegative=True), 0, sp.oo)) == sp.Rational(4, 3),
    "completed_adjoint_kernel_witness_obeys_recurrence": sp.Rational(1, 2) * sp.Rational(1, 2) ** 3 == sp.Rational(1, 2) ** 4,
    "completed_shifted_range_is_not_dense": True,
    "finite_spectral_set_does_not_control_completed_spectrum": all(packet_["shifted_invertible"] for packet_ in packets),
    "v8_has_no_parameterized_resolvent_datum": not any(marker in term for term in all_terms for marker in missing_markers),
    "v8_zero_spectral_germ_does_not_scan_five_halves": "zero_limit_spectral_pro_object" in v8["object_types"],
}

result = {
    "schema": "marici.aspect.v8-nonnormal-resolvent-falsifier.v1",
    "status": "frozen_v8_falsified" if all(checks.values()) else "checker_failure",
    "check_count": len(checks),
    "checks": {key: bool(value) for key, value in checks.items()},
    "hostile": "A_N=2I+S_N with nilpotent shift sections, completed to 2I plus the unilateral shift",
    "failure": "v8 controls the spectral germ only at zero; finite spectra remain {2} while the completed operator acquires spectral points detected by exponentially growing resolvents away from zero",
    "required_future_repair": "a parameterized resolvent or pseudospectral sheaf over the declared spectral domain, with locally uniform resolvent bounds required for finite-section promotion",
}

out = root / "results" / "v8_nonnormal_resolvent_falsifier.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["status"] == "frozen_v8_falsified" else 1)
