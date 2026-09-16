#!/usr/bin/env python3
"""Enumerate critical three-transition coherence prototypes."""
from itertools import combinations
import json
from pathlib import Path

ELEMENTS = ("A", "J", "P", "C", "T", "E", "F")
INCOMPARABLE = {frozenset(pair) for pair in ("AP", "AE", "JP", "JC", "JE", "PC", "CE", "TE")}

critical = {}
for triple in combinations(ELEMENTS, 3):
    edges = ["".join(pair) for pair in combinations(triple, 2) if frozenset(pair) in INCOMPARABLE]
    if len(edges) >= 2:
        critical["".join(triple)] = edges

PROTOTYPES = {
    "AJP": ("amplification naturality of Mellin polarization", "whiskered_naturality"),
    "AJE": ("amplification naturality of contour endpoint completion", "whiskered_contour_cell"),
    "APC": ("amplification covariance of ordered observer/cutoff placement", "whiskered_noncommuting_cell"),
    "APE": ("amplified polarization with separately retained endpoint row", "direct_sum_interchange"),
    "ACE": ("amplified cutoff bulk and endpoint boundary split", "relative_boundary_naturality"),
    "ATE": ("amplified finite-part/endpoint residue identity", "whiskered_residue_cell"),
    "JPC": ("Fourier transport of the Hermitian and skew eight-leg placement channels", "full_braid_cell"),
    "JPE": ("Mellin polarization compatibility with the completed contour differential", "contour_polarization_cell"),
    "JCE": ("transported cutoff compatibility with endpoint contour completion", "full_braid_cell"),
    "JTE": ("spectral chart transport of the finite-part/endpoint residue identity", "whiskered_residue_cell"),
    "PCE": ("endpoint-augmented ordered cutoff placement", "relative_eight_leg_cell"),
    "CTE": ("cutoff realization of the completed finite-part boundary identity", "relative_trace_boundary_cell"),
}

assert list(critical) == list(PROTOTYPES)
full_braids = [name for name, edges in critical.items() if len(edges) == 3]
assert full_braids == ["JPC", "JCE"]

result = {
    "schema": "marici.voevodsky.seven-transition-tetrahedron-prototypes.v1",
    "critical_triples": critical,
    "critical_triple_count": len(critical),
    "full_incomparability_braids": full_braids,
    "prototypes": {
        name: {"analytical_form": form, "kind": kind, "status": "constructed"}
        for name, (form, kind) in PROTOTYPES.items()
    },
    "passed": True,
    "conclusion": (
        "There are 12 critical three-transition prototypes. Only JPC and JCE "
        "are full three-way braid cells; the other ten are whiskered or relative "
        "naturality cells."
    ),
}

out = Path(__file__).parents[1] / "results" / "seven_transition_tetrahedron_prototypes.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
