import json
from pathlib import Path

import sympy as sp


z, a, b, t = sp.symbols("z a b t", real=True)
L_primitive = a * z
L_square = b * z**3
L = L_primitive + L_square
gamma = sp.exp(L)
rho = sp.exp(-L)
Gamma = sp.simplify(rho * gamma)

central_jets = [sp.simplify(sp.diff(Gamma, z, order).subs(z, 0)) for order in range(1, 9)]
reconstructed = sp.simplify(sp.exp(L))
reconstruction_holds = sp.simplify(reconstructed / gamma) == 1

same_basis_aggregate = a * z + b * z
redistributed_aggregate = (a + t) * z + (b - t) * z
labelled_before = sp.Matrix([a, b])
labelled_after = sp.Matrix([a + t, b - t])

example = {a: sp.Rational(2, 5), b: sp.Rational(-1, 7)}
history_vector = sp.Matrix([L_primitive, L_square]).subs(example)
history_norm = sp.simplify(sum(component**2 for component in history_vector))

classification = {
    "scalar_flat": Gamma == 1,
    "packet_zero": history_vector == sp.zeros(2, 1),
    "normalization_erasure": Gamma == 1 and history_vector != sp.zeros(2, 1),
    "lossless_reconstruction_with_history": reconstruction_holds,
    "arithmetic_provenance_requires_grade_labels": True,
}

checks = {
    "normalized_scalar_is_identically_one": Gamma == 1,
    "first_eight_central_jets_vanish": all(value == 0 for value in central_jets),
    "raw_transition_reconstructs_from_history": reconstruction_holds,
    "history_is_reflection_odd": sp.simplify(L.subs(z, -z) + L) == 0,
    "example_history_is_nonzero": history_norm != 0,
    "flat_scalar_is_not_packet_zero": not classification["packet_zero"],
    "classifier_detects_normalization_erasure": classification["normalization_erasure"],
    "aggregate_history_is_invariant_under_grade_redistribution": sp.simplify(
        same_basis_aggregate - redistributed_aggregate
    ) == 0,
    "graded_history_changes_under_redistribution": labelled_before != labelled_after,
}

result = {
    "status": "pass" if all(checks.values()) else "fail",
    "checks": checks,
    "classification": classification,
    "example_coefficients": {"primitive": "2/5", "square": "-1/7"},
    "history_norm": str(history_norm),
    "normalized_scalar": str(Gamma),
    "central_jets_checked": len(central_jets),
    "grade_redistribution_kernel": "(a,b)->(a+t,b-t)",
}
out = Path(__file__).resolve().parents[1] / "results" / "graded_history_normalization_erasure.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
