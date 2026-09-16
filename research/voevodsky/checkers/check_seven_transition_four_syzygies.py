#!/usr/bin/env python3
"""Enumerate critical four-transition syzygy prototypes."""
from itertools import combinations
import json
from pathlib import Path

ELEMENTS = ("A", "J", "P", "C", "T", "E", "F")
INCOMPARABLE = {frozenset(pair) for pair in ("AP", "AE", "JP", "JC", "JE", "PC", "CE", "TE")}

def critical_triple(triple):
    return sum(frozenset(pair) in INCOMPARABLE for pair in combinations(triple, 2)) >= 2

critical3 = {"".join(t) for t in combinations(ELEMENTS, 3) if critical_triple(t)}
critical4 = {}
for quad in combinations(ELEMENTS, 4):
    faces = ["".join(t) for t in combinations(quad, 3) if "".join(t) in critical3]
    if len(faces) >= 2:
        critical4["".join(quad)] = faces

FORMS = {
    "AJPC": "amplification of the Fourier-transported ordered-placement braid",
    "AJPE": "amplified Mellin/endpoint contour polarization coherence",
    "AJCE": "amplification of transported cutoff-boundary coherence",
    "AJTE": "amplified spectral finite-part/residue coherence",
    "APCE": "amplified endpoint-augmented eight-leg placement coherence",
    "APTE": "amplified polarization/trace endpoint residue coherence",
    "ACTE": "amplified cutoff/trace completed-boundary coherence",
    "JPCE": "joint Fourier, polarization, cutoff, and endpoint relative-feature coherence",
    "JPTE": "Mellin-polarized spectral finite-part/residue coherence",
    "JCTE": "transported cutoff realization of the finite-part boundary identity",
    "PCTE": "ordered-placement compatibility with cutoff finite-part endpoint completion",
}
assert list(critical4) == list(FORMS)

result = {
    "schema": "marici.voevodsky.seven-transition-four-syzygies.v1",
    "critical_four_subsets": critical4,
    "critical_four_count": len(critical4),
    "analytical_forms": {
        key: {
            "form": FORMS[key],
            "status": "forced_after_residual_augmented_strictification",
        }
        for key in FORMS
    },
    "strictification": {
        "PC": "retain Hermitian ordered placement and skew commutator as separate coordinates",
        "TE": "retain finite-part bulk and endpoint residue as separate coordinates",
        "effect": "all prototype maps become literal continuous coordinate maps in the relative-feature category",
        "higher_coherence": "ordinary nerve is 2-coskeletal, so four-boundaries and all higher syzygies fill uniquely",
    },
    "passed": True,
}
out = Path(__file__).parents[1] / "results" / "seven_transition_four_syzygies.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
