"""Test whether the 180 compatible five-cycle bases form a simplicial chain."""
import json
from collections import Counter
from itertools import combinations
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
SOURCE = ROOT / "research/benincasa/results/five-cycle-ofpt-packet.json"
OUTPUT = ROOT / "research/benincasa/results/five-cycle-candidate-ridge-audit.json"

packet = json.loads(SOURCE.read_text())["five_cycle"]
terms = [tuple(term) for term in packet["terms"]]
assert len(terms) == 180
assert all(len(term) == 4 for term in terms)

ridge_multiplicity = Counter(
    tuple(sorted(ridge))
    for term in terms
    for ridge in combinations(term, 3)
)
census = Counter(ridge_multiplicity.values())
assert census == Counter({3: 130, 4: 65, 2: 35})

# This is a census in the nerve of denominator labels.  It is not the boundary
# complex of the adjoint-locus signed triangulation of arXiv:2112.09028, Eq. (33).
odd_internal_ridges = sorted(
    "|".join(ridge)
    for ridge, multiplicity in ridge_multiplicity.items()
    if multiplicity > 1 and multiplicity % 2 == 1
)
assert len(odd_internal_ridges) == 130

result = {
    "schema": "marici.benincasa.five_cycle_candidate_ridge_audit.v1",
    "term_count": len(terms),
    "ridge_count": len(ridge_multiplicity),
    "multiplicity_census": {str(k): census[k] for k in sorted(census)},
    "odd_internal_ridge_count": len(odd_internal_ridges),
    "ordinary_nerve_boundary_test_applicable": False,
    "conclusion": (
        "The raw denominator-label nerve has odd ridge multiplicities, but this "
        "does not test the adjoint-locus signed triangulation of the source."
    ),
}
OUTPUT.write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps(result, sort_keys=True))
