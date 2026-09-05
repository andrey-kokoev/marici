from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
CHAIN_RESULT = ROOT / "research/nima/results/six-point-nmhv-triangulation-fixture.json"
DICTIONARY = ROOT / "research/nima/six-point-nmhv-boundary-dictionary.json"
RESULT = ROOT / "research/nima/results/six-point-nmhv-boundary-dictionary.json"


def sorted_label(edges):
    return "".join(map(str, sorted(int(x) for edge in edges for x in edge)))


def main():
    chain = json.loads(CHAIN_RESULT.read_text(encoding="utf-8"))
    dictionary = json.loads(DICTIONARY.read_text(encoding="utf-8"))
    external = set(chain["left_boundary"])
    declared = set(dictionary["facets"])
    cyclic_edges = {"12","23","34","45","56","61"}
    classifications = {}
    for facet, entry in dictionary["facets"].items():
        edges = entry["cyclic_edges"]
        classifications[facet] = len(edges) == 2 and all(e in cyclic_edges for e in edges) and sorted_label(edges) == facet
    internal = set(dictionary["internal_left"]) | set(dictionary["internal_right"])
    physical = {entry["physical_pole"] for entry in dictionary["facets"].values()}
    expected_physical = {"s12","s23","s34","s45","s56","s61","t123","t234","t345"}
    checks = {
        "dictionary_exhausts_external_facets": declared == external,
        "each_external_facet_is_two_cyclic_edges": all(classifications.values()),
        "internal_and_external_facets_disjoint": not (internal & external),
        "nine_distinct_physical_pole_loci": len(declared) == 9,
        "physical_pole_set_matches_source": physical == expected_physical,
        "six_collinear_and_three_factorization_poles": len({p for p in physical if p.startswith("s")}) == 6 and len({p for p in physical if p.startswith("t")}) == 3
    }
    out = {
        "schema": "marici.nima.six_point_nmhv_boundary_dictionary.result.v1",
        "status": "passed" if all(checks.values()) else "failed",
        "checks": checks,
        "classifications": classifications,
        "external_facets": sorted(external),
        "claim_boundary": "Exact classification against the declared adjacent-pair rule; source authority and factorization-versus-collinear semantics remain external."
    }
    RESULT.parent.mkdir(parents=True, exist_ok=True)
    RESULT.write_text(json.dumps(out, indent=2) + "\n", encoding="utf-8")
    if out["status"] != "passed": raise SystemExit(1)


if __name__ == "__main__": main()
