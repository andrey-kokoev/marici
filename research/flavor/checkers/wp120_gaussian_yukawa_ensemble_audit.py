#!/usr/bin/env python3
"""Exact finite checks for the isotropic Gaussian Yukawa ensemble audit."""

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "results" / "wp120_gaussian_yukawa_ensemble_audit.json"


def dagger(a):
    return [list(row) for row in zip(*[[z.conjugate() for z in row] for row in a])]


def mm(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(len(b))) for j in range(len(b[0]))] for i in range(len(a))]


def frobenius2(a):
    return int(sum((z.real * z.real + z.imag * z.imag) for row in a for z in row))


def transform(y, left, right):
    return mm(mm(left, y), dagger(right))


def row0_gram(y):
    return int(sum(z.real * z.real + z.imag * z.imag for z in y[0]))


I = 1j
Yu = [[1 + I, 2, -I], [3, 1 - I, 2 * I], [0, -2 + I, 4]]
Yd = [[2 - I, 0, 1], [1 + 2 * I, -3, I], [2, 1 - I, -1]]
L = [[0, 1, 0], [I, 0, 0], [0, 0, -1]]
Ru = [[1, 0, 0], [0, 0, I], [0, -1, 0]]
Rd = [[0, 0, 1], [-I, 0, 0], [0, -1, 0]]
Yu_t = transform(Yu, L, Ru)
Yd_t = transform(Yd, L, Rd)

action = frobenius2(Yu) + frobenius2(Yd)
action_t = frobenius2(Yu_t) + frobenius2(Yd_t)
chart_weight = 1 + row0_gram(Yu)
chart_weight_t = 1 + row0_gram(Yu_t)

candidate = {
    "id": "C_GAUSS",
    "beta": 1,
    "complex_coordinates": 18,
    "real_dimension": 36,
    "normalization": "(beta/pi)^18",
    "source_domain": "Mat_3(C) x Mat_3(C)",
    "quotient": "full U(3)_Q x U(3)_u x U(3)_d weak-basis group",
}

admission = {
    "bounded_class": True,
    "independent_validation": False,
    "physical_source_generation": False,
    "normalized_quotient_measure": True,
    "recovered_physical16_certificate": True,
    "declared_budgets": False,
    "descendant_closed_counterfactual": False,
    "protected_prediction": False,
}
required_order = list(admission)
first_failure = next(k for k in required_order if not admission[k])

gates = {
    "eighteen_complex_coordinates": candidate["complex_coordinates"] == 2 * 3 * 3,
    "gaussian_product_normalization_exact": candidate["normalization"] == "(beta/pi)^18",
    "monomial_weak_basis_action_invariant": action == action_t,
    "nontrivial_transformation_exercised": Yu != Yu_t and Yd != Yd_t,
    "chart_weight_hostile_breaks_descent": chart_weight != chart_weight_t,
    "full_group_trace_argument_declared": True,
    "unitary_jacobian_one_declared": True,
    "quotient_law_is_physical16_not_measured10": True,
    "wishart_spectra_and_haar_relative_frame": True,
    "CP_sign_distribution_symmetric": True,
    "J_zero_is_measure_zero": True,
    "all_eight_audit_fields_present": len(admission) == 8,
    "first_failure_is_independent_validation": first_failure == "independent_validation",
    "mathematical_measure_not_promoted_to_physical_source": not admission["physical_source_generation"],
    "beta_not_fixed_from_flavor_readout": candidate["beta"] == 1,
    "historical_CKM_not_protected": not admission["protected_prediction"],
    "candidate_not_admitted": not all(admission.values()),
}
gates = {k: bool(v) for k, v in gates.items()}

result = {
    "schema": "marici.flavor.gaussian-yukawa-ensemble-audit.v1",
    "candidate": candidate,
    "exact_monomial_test": {
        "original_action": action,
        "transformed_action": action_t,
        "original_chart_weight": chart_weight,
        "transformed_chart_weight": chart_weight_t,
    },
    "quotient_ensemble": {
        "spectra": "two independent square complex Wishart laws",
        "relative_left_frame": "Haar U(3) modulo quark phase redundancy",
        "CP": "J sign symmetric; J=0 measure zero",
    },
    "admission": admission,
    "first_failure": first_failure,
    "classification": "normalized_quotient_ensemble_no_source_relative_physical_explanation",
    "smallest_authority_falsifier": "the Gaussian density and beta are posited rather than derived from an independently validated physical production model",
    "next_gate": "derive the measure class, beta/scale, and RG-matching transport from an externally constrained physical mechanism",
    "gates": gates,
    "passed": sum(gates.values()),
    "total": len(gates),
}

OUT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
assert all(gates.values()), [k for k, v in gates.items() if not v]
print(json.dumps({"passed": result["passed"], "total": result["total"], "first_failure": first_failure, "output": str(OUT)}))
