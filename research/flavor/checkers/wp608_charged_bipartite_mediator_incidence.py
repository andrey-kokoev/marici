"""Exact WP608 audit: charged bipartite orientation is removable by relabelling."""

import json
from pathlib import Path

import sympy as sp


mass, g_a, g_b, width = sp.symbols("M g_A g_B Gamma", positive=True, real=True)

identity = sp.eye(3)
forward_shift = sp.Matrix([[0, 1, 0], [0, 0, 1], [1, 0, 0]])
reverse_shift = forward_shift.T
reflection = sp.Matrix([[1, 0, 0], [0, 0, 1], [0, 1, 0]])

g_a_matrix = g_a * identity
g_b_matrix = g_b * forward_shift
heavy_inverse = identity / mass**2
cross_kernel = sp.simplify(-g_a_matrix.T * heavy_inverse * g_b_matrix)
full_schur = sp.simplify(
    -g_a_matrix.row_join(g_b_matrix).T
    * heavy_inverse
    * g_a_matrix.row_join(g_b_matrix)
)

# Relabel B_prime=P_forward*B. Then B=P_reverse*B_prime and the directed
# cross-block becomes the identity. The corresponding shifted B reflection
# stabilizes the original cross-block together with the ordinary A reflection.
b_relabel = forward_shift
relabeled_cross_kernel = sp.simplify(cross_kernel * b_relabel.T)
b_shifted_reflection = sp.simplify(
    b_relabel.T * reflection * b_relabel
)
generalized_reflection_residual = sp.simplify(
    reflection.T * cross_kernel * b_shifted_reflection - cross_kernel
)

# Z2^3 charges. B_j carries the charge at the preceding node, so X_i can
# couple to A_i and B_(i+1), but not B_(i-1).
unit_charges = [(1, 0, 0), (0, 1, 0), (0, 0, 1)]
x_charge = unit_charges
a_charge = unit_charges
b_charge = [unit_charges[(index - 1) % 3] for index in range(3)]


def equal_mod_two(left, right):
    return all((x - y) % 2 == 0 for x, y in zip(left, right))


allowed_a = {
    (i, j)
    for i in range(3)
    for j in range(3)
    if equal_mod_two(x_charge[i], a_charge[j])
}
allowed_b = {
    (i, j)
    for i in range(3)
    for j in range(3)
    if equal_mod_two(x_charge[i], b_charge[j])
}
expected_a = {(i, i) for i in range(3)}
expected_forward_b = {(i, (i + 1) % 3) for i in range(3)}
reverse_b = {(i, (i - 1) % 3) for i in range(3)}

# Detector-facing support record for the B-family branches.
forward_width_record = width * forward_shift
reverse_width_entries = [
    forward_width_record[i, (i - 1) % 3] for i in range(3)
]
orientation_contrast = sp.simplify(
    sum(forward_width_record[i, (i + 1) % 3] for i in range(3))
    - sum(reverse_width_entries)
)

checks = {
    "cross_kernel_is_directed_forward_shift": cross_kernel
    == -g_a * g_b * forward_shift / mass**2,
    "cross_kernel_has_rank_three": cross_kernel.rank() == 3,
    "fewer_than_three_mediator_modes_cannot_factor_rank_three": all(
        number < cross_kernel.rank() for number in (1, 2)
    ),
    "full_schur_kernel_is_reciprocal": full_schur == full_schur.T,
    "common_label_reflection_reverses_cross_kernel": sp.simplify(
        reflection.T * forward_shift * reflection - reverse_shift
    )
    == sp.zeros(3),
    "forward_and_reverse_are_distinct": forward_shift != reverse_shift,
    "charge_rule_allows_exactly_diagonal_a_channels": allowed_a == expected_a,
    "charge_rule_allows_exactly_forward_b_channels": allowed_b
    == expected_forward_b,
    "charge_rule_forbids_every_reverse_b_channel": allowed_b.isdisjoint(
        reverse_b
    ),
    "independent_b_relabel_removes_shift": relabeled_cross_kernel
    == -g_a * g_b * identity / mass**2,
    "shifted_b_reflection_stabilizes_incidence": generalized_reflection_residual
    == sp.zeros(3),
    "shifted_b_reflection_is_an_involution": b_shifted_reflection**2
    == identity,
    "forward_support_has_three_nonzero_entries": sum(
        1 for value in forward_width_record if value != 0
    )
    == 3,
    "reverse_support_is_exactly_zero": reverse_width_entries == [0, 0, 0],
    "orientation_contrast_is_three_widths": orientation_contrast == 3 * width,
}

if not all(checks.values()):
    raise SystemExit(f"WP608 check failed: {checks}")

result = {
    "work_package": "WP608",
    "status": "PASS",
    "checks": {key: bool(value) for key, value in checks.items()},
    "source_domain": "three complex mediators and two cyclic channel families with independent texture-chart relabellings, equipped with the displayed Z2^3 semidirect C3 charge incidence",
    "allowed_incidence": ["X_i to A_i", "X_i to B_(i+1)"],
    "forbidden_incidence": "X_i to B_(i-1) for every i",
    "effective_cross_kernel": "K=-(g_A*g_B/M^2) P_forward",
    "minimality": "rank(P_forward)=3, so any Gaussian factorization needs at least three mediator modes; the displayed construction saturates the bound",
    "relabeling_kernel": "B_prime=P_forward*B turns K into a scalar identity cross-block",
    "generalized_reflection": "ordinary reflection on A together with P_forward^T*S*P_forward on B stabilizes K",
    "hard_to_vary_content": "none at the physical quotient level unless a source-derived common A/B label alignment is added",
    "contextual_partition": "the apparent forward/reverse support partition is chart-dependent under independent B relabelling",
    "smallest_exact_falsifier": "the explicit B_prime=P_forward*B relabelling removes the orientation without changing the source incidence",
    "experimental_record": "a family-resolved branch table tests the incidence only after an independently physical common A/B label frame has been declared",
    "temporal_gate": "the ordered-channel result must be conditioned on a derived phase-monitor or reset history; static marginal visibility is insufficient",
    "physical16_gate": "derive a common A/B alignment from weak-basis-invariant flavor operations; otherwise the shift cannot descend to physical16",
    "reference_disposition": "an added alignment port defines a relational experiment over the stabilizer of that port; it does not reveal an absolute pre-existing orientation",
    "classification": "negative: the charged incidence rigidifies a bipartite presentation but does not select physical orientation",
}

out = (
    Path(__file__).resolve().parents[1]
    / "results"
    / "wp608_charged_bipartite_mediator_incidence.json"
)
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
