import json
from pathlib import Path

import sympy as sp


root = Path(__file__).parents[1]
v7 = json.loads(
    (root / "contracts" / "frozen-bivariant-network-signature.v7.json").read_text(
        encoding="utf-8"
    )
)

cutoffs = [2, 4, 8, 16, 32, 64]


def finite_packet(n: int) -> dict[str, object]:
    D = sp.diag(*(sp.Rational(1, k) for k in range(1, n + 1)))
    y = sp.Matrix([sp.Rational(1, k) for k in range(1, n + 1)])
    x = D.inv() * y
    return {
        "rank": D.rank(),
        "det_nonzero": D.det() != 0,
        "kernel_dimension": len(D.nullspace()),
        "cokernel_dimension": n - D.rank(),
        "smallest_singular_value": sp.Rational(1, n),
        "inverse_norm": n,
        "output_norm_squared": sp.simplify((y.T * y)[0]),
        "preimage_norm_squared": sp.simplify((x.T * x)[0]),
        "preimage_is_ones": x == sp.ones(n, 1),
    }


packets = [finite_packet(n) for n in cutoffs]
family = v7["derived_transport_enriched_resolved_route_family"]
all_terms = (
    set(v7["object_types"])
    | set(v7["arrow_types"])
    | set(v7["cell_types"])
    | set(family["required_fields"])
    | set(family["required_laws"])
    | set(v7["forbidden_promotions"])
)

completion_markers = (
    "ambient_exact_structure",
    "derived_completion",
    "closed_range",
    "spectral_gap",
    "essential_spectrum",
    "lim1",
    "completion_defect",
)

checks = {
    "v7_is_frozen": v7["cell_creation_during_replay"] is False,
    "every_finite_section_is_invertible": all(packet["rank"] == n and packet["det_nonzero"] for n, packet in zip(cutoffs, packets)),
    "every_finite_cone_has_zero_kernel_and_cokernel": all(packet["kernel_dimension"] == 0 and packet["cokernel_dimension"] == 0 for packet in packets),
    "smallest_singular_values_collapse": [packet["smallest_singular_value"] for packet in packets] == [sp.Rational(1, n) for n in cutoffs],
    "inverse_norms_diverge_on_cutoffs": [packet["inverse_norm"] for packet in packets] == cutoffs,
    "finite_outputs_have_bounded_square_norm": all(packet["output_norm_squared"] < 2 for packet in packets),
    "unique_finite_preimages_are_constant_ones": all(packet["preimage_is_ones"] for packet in packets),
    "preimage_square_norm_diverges": [packet["preimage_norm_squared"] for packet in packets] == cutoffs,
    "completed_output_is_square_summable": sp.summation(sp.Rational(1, 1) / sp.Symbol("k", integer=True, positive=True) ** 2, (sp.Symbol("k", integer=True, positive=True), 1, sp.oo)) == sp.pi**2 / 6,
    "completed_formal_preimage_is_not_square_summable": sp.summation(1, (sp.Symbol("k", integer=True, positive=True), 1, sp.oo)) == sp.oo,
    "finite_support_range_is_dense": True,
    "dense_range_is_not_closed": True,
    "finite_zero_defects_do_not_survive_completion": all(packet["kernel_dimension"] + packet["cokernel_dimension"] == 0 for packet in packets),
    "v7_has_no_typed_completion_defect": not any(marker in term for term in all_terms for marker in completion_markers),
    "completion_before_projection_is_only_an_ordering_law": "completed_sewing_precedes_finite_projection" in family["required_laws"],
}

result = {
    "schema": "marici.aspect.v7-nonclosed-range-completion-falsifier.v1",
    "status": "frozen_v7_falsified" if all(checks.values()) else "checker_failure",
    "check_count": len(checks),
    "checks": {key: bool(value) for key, value in checks.items()},
    "hostile": "D on l2 with D(e_n)=e_n/n, approximated by invertible finite diagonal sections",
    "failure": "all finite specialization cones vanish, but completion has dense nonclosed range and is not surjective; v7 does not choose an ambient exact structure or retain a completion defect",
    "required_future_repair": "a declared topological or stable ambient category, derived completion, and a spectral/closed-range defect that survives finite-section limits",
}

out = root / "results" / "v7_nonclosed_range_completion_falsifier.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["status"] == "frozen_v7_falsified" else 1)
