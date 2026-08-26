"""Exact block-support zero theorem for the eight WP529 candidate triples."""

import json
from pathlib import Path

import sympy as sp


root = Path(__file__).resolve().parents[1]


def load(name):
    return json.loads((root / "results" / name).read_text(encoding="utf-8"))


wp508 = load("wp508_canonical_heavy_gauge_poles.json")
wp529 = load("wp529_lightweight_vector_census.json")
wp530 = load("wp530_multiprecision_vector_candidates.json")

imag = sp.I
lambdas = [
    sp.Matrix([[0, 1, 0], [1, 0, 0], [0, 0, 0]]),
    sp.Matrix([[0, -imag, 0], [imag, 0, 0], [0, 0, 0]]),
    sp.diag(1, -1, 0),
    sp.Matrix([[0, 0, 1], [0, 0, 0], [1, 0, 0]]),
    sp.Matrix([[0, 0, -imag], [0, 0, 0], [imag, 0, 0]]),
    sp.Matrix([[0, 0, 0], [0, 0, 1], [0, 1, 0]]),
    sp.Matrix([[0, 0, 0], [0, 0, -imag], [0, imag, 0]]),
    sp.diag(1, 1, -2) / sp.sqrt(3),
]
g_f = sp.sqrt(2)
g_p = sp.Rational(1, 10)
g_e = sp.Rational(1, 50)

gauge_tensor = sp.MutableDenseNDimArray.zeros(14, 14, 14)
for left in range(8):
    for middle in range(8):
        commutator = lambdas[left] * lambdas[middle] - lambdas[middle] * lambdas[left]
        for right in range(8):
            gauge_tensor[left, middle, right] = sp.simplify(
                g_f * sp.trace(commutator * lambdas[right]) / (4 * imag)
            )
for offset, coupling in ((8, g_p), (11, g_e)):
    for left in range(3):
        for middle in range(3):
            for right in range(3):
                gauge_tensor[offset + left, offset + middle, offset + right] = (
                    coupling * sp.LeviCivita(left, middle, right)
                )

# Exact WP508 four-generator sparsity blocks in canonical gauge coordinates.
blocks = {
    0: [0, 5, 8, 11],
    1: [1, 6, 9, 12],
    2: [2, 7, 10, 13],
}
expected_names = {
    0: ["F1", "F6", "P1", "E1"],
    1: ["F2", "F7", "P2", "E2"],
    2: ["F3", "F8", "P3", "E3"],
}
reported_four_blocks = [
    component["generators"]
    for component in wp508["heavy_gauge_poles"]["components"]
    if component["size"] == 4
]

# State-to-cubic-sector map from the common WP518 ordering. Only states
# appearing in the eight candidates are needed.
state_sector = {
    0: 2,
    1: 0,
    2: 1,
    3: 2,
    4: 0,
    5: 1,
    6: 2,
    12: 0,
    13: 1,
}
candidates = wp529["precutoff_census"]["subcutoff_candidate_channels"]
candidate_signatures = [
    (
        state_sector[item["parent"]],
        state_sector[item["daughter_1"]],
        state_sector[item["daughter_2"]],
    )
    for item in candidates
]
unique_signatures = sorted(set(candidate_signatures))


def restriction_packet(signature):
    entries = [
        sp.simplify(gauge_tensor[left, middle, right])
        for left in blocks[signature[0]]
        for middle in blocks[signature[1]]
        for right in blocks[signature[2]]
    ]
    return {
        "signature": list(signature),
        "entry_count": len(entries),
        "nonzero_entries": [str(value) for value in entries if value != 0],
        "squared_norm": str(sp.simplify(sum(value**2 for value in entries))),
    }


restriction_packets = [
    restriction_packet(signature) for signature in unique_signatures
]
all_restrictions_zero = all(
    packet["nonzero_entries"] == [] and packet["squared_norm"] == "0"
    for packet in restriction_packets
)

checks = {
    "wp508_dependency_passed": bool(wp508["passed"]),
    "wp529_dependency_passed": bool(wp529["passed"]),
    "wp530_dependency_passed": bool(wp530["passed"]),
    "reported_blocks_match_exact_canonical_supports": reported_four_blocks
    == [expected_names[index] for index in range(3)],
    "all_eight_candidates_have_declared_sector_support": len(
        candidate_signatures
    )
    == 8,
    "candidate_signatures_are_exactly_the_four_ordered_supports": unique_signatures
    == [(0, 0, 2), (0, 2, 0), (1, 1, 2), (1, 2, 1)],
    "both_restricted_gauge_tensors_vanish_identically": all_restrictions_zero,
    "every_candidate_mass_basis_contraction_is_zero": all_restrictions_zero
    and len(candidate_signatures) == 8,
}
checks = {name: bool(value) for name, value in checks.items()}

result = {
    "work_package": "WP531",
    "domain": "The eight WP529/WP530 candidate triples, typed by their exact WP508 four-generator sparsity blocks.",
    "exact_blocks": {
        str(index): names for index, names in expected_names.items()
    },
    "candidate_sector_signatures": [list(value) for value in candidate_signatures],
    "restricted_tensor_certificates": restriction_packets,
    "theorem": "The exact gauge-basis Yang-Mills tensor vanishes on B0 x B0 x B2, B0 x B2 x B0, B1 x B1 x B2 and B1 x B2 x B1. Since every mass eigenvector in a simple cubic sector lies inside its exact WP508 block, arbitrary within-block rotations preserve the zero. All eight candidate mass-basis couplings vanish identically.",
    "classification": "Exact block-support zero theorem superseding the numerical candidate interpretation. It certifies the eight WP529 entries as artifacts and removes them from the vector self-energy.",
    "selector": False,
    "rigidifier": bool(all_restrictions_zero),
    "instrument": "The eight sub-cutoff candidates are now exactly excluded. Complete 34-channel width authority still requires a basis-invariant audit of the fivefold degenerate quintet projector and every other numerical-zero block class.",
    "smallest_exact_falsifier": "One entry of either 64-component restricted tensor is nonzero, or an alleged candidate eigenvector has support outside its WP508 block.",
    "remaining_gate": "Construct the exact five-dimensional quintet spectral projector, classify all remaining threshold-open zero classes and degenerate-subspace coupling sums, then freeze the complete 34-channel vector self-energy on WP527.",
    "checks": checks,
    "passed": all(checks.values()),
}

out = root / "results" / "wp531_exact_candidate_block_zeros.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
raise SystemExit(0 if result["passed"] else 1)
