"""Carrier-level criterion for the C8 22/14 fold-pairing split."""

import collections
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CONTOUR = ROOT / "results" / "eight-site-canonical-contour-packet.json"
SOURCE = ROOT / "results" / "eight-site-rank4-labelled-expansion.json"
REDUCED = ROOT / "results" / "eight-site-rank4-base-reduced-walls.json"
PAIRING = ROOT / "results" / "eight-site-rank4-face-fold-pairing.json"
SEWING = ROOT / "results" / "eight-site-rank4-os-fold-sewing.json"
TARGET = ROOT / "results" / "eight-site-rank4-routing-visibility-criterion.json"


def rotate_edge(edge: int, shift: int) -> int:
    return (edge + shift - 1) % 8 + 1


def face_edge_multiplicities(labels: list[str], facets: dict, vertices: list[dict]) -> collections.Counter:
    face = sorted(set.intersection(*(set(facets[label]["zero_vertex_indices"]) for label in labels)))
    assert len(face) == 9
    return collections.Counter(vertices[index]["edge"] for index in face)


def main() -> None:
    contour = json.loads(CONTOUR.read_text())
    source = json.loads(SOURCE.read_text())
    reduced = json.loads(REDUCED.read_text())
    pairing = json.loads(PAIRING.read_text())
    sewing = json.loads(SEWING.read_text())
    facets = {item["label"]: item for item in contour["facets"]}
    reduced_by_key = {item["canonical_key"]: item for item in reduced["records"]}
    pairing_by_key = {item["source_orbit_key"]: item for item in pairing["families"]}
    sewing_by_occurrence = {item["occurrence_id"]: item for item in sewing["occurrences"]}

    audits = []
    for occurrence in source["occurrences"]:
        multiplicities = face_edge_multiplicities(occurrence["labels"], facets, contour["vertices"])
        doubled_edges = sorted(edge for edge, count in multiplicities.items() if count == 2)
        singleton_edges = sorted(edge for edge, count in multiplicities.items() if count == 1)
        assert len(doubled_edges) == 4 and len(singleton_edges) == 1
        canonical_free = reduced_by_key[occurrence["source_orbit_key"]]["free_edges"]
        transported_free = sorted(rotate_edge(edge, occurrence["cyclic_shift"]) for edge in canonical_free)
        visible = doubled_edges == transported_free
        local_nonzero = pairing_by_key[occurrence["source_orbit_key"]]["local_pairing_nonzero"]
        sewn_nonzero = sewing_by_occurrence[occurrence["occurrence_id"]]["sewn_pairing_nonzero"]
        assert visible == local_nonzero == sewn_nonzero
        audits.append({
            "occurrence_id": occurrence["occurrence_id"],
            "source_orbit_key": occurrence["source_orbit_key"],
            "cyclic_shift": occurrence["cyclic_shift"],
            "canonical_free_routing_edges": canonical_free,
            "transported_free_routing_edges": transported_free,
            "doubled_face_edges": doubled_edges,
            "singleton_face_edge": singleton_edges[0],
            "full_routing_visibility": visible,
            "local_fold_pairing_nonzero": local_nonzero,
            "os_sewn_pairing_nonzero": sewn_nonzero,
        })

    orbit_representatives = [item for item in audits if item["cyclic_shift"] == 0]
    checks = {
        "occurrence_count": len(audits),
        "orbit_count": len(orbit_representatives),
        "full_visibility_orbit_count": sum(item["full_routing_visibility"] for item in orbit_representatives),
        "failed_visibility_orbit_count": sum(not item["full_routing_visibility"] for item in orbit_representatives),
        "full_visibility_occurrence_count": sum(item["full_routing_visibility"] for item in audits),
        "failed_visibility_occurrence_count": sum(not item["full_routing_visibility"] for item in audits),
        "visibility_iff_local_pairing": all(item["full_routing_visibility"] == item["local_fold_pairing_nonzero"] for item in audits),
        "visibility_iff_os_sewn_pairing": all(item["full_routing_visibility"] == item["os_sewn_pairing_nonzero"] for item in audits),
        "criterion_is_cyclically_covariant": all(
            len({item["full_routing_visibility"] for item in audits if item["source_orbit_key"] == key}) == 1
            for key in reduced_by_key
        ),
    }
    assert checks == {
        "occurrence_count": 288,
        "orbit_count": 36,
        "full_visibility_orbit_count": 22,
        "failed_visibility_orbit_count": 14,
        "full_visibility_occurrence_count": 176,
        "failed_visibility_occurrence_count": 112,
        "visibility_iff_local_pairing": True,
        "visibility_iff_os_sewn_pairing": True,
        "criterion_is_cyclically_covariant": True,
    }
    packet = {
        "schema": "marici.eight_site_rank4_routing_visibility_criterion.v1",
        "criterion": {
            "statement": "the fold pairing is nonzero iff the four doubled edges of the source eight-simplex face equal the four free routing edges",
            "carrier_meaning": "the face retains both occurrence vertices on every routing direction needed by the companion fold",
            "negative_case": "at least one free routing direction is absent from the face, so its odd fold coefficient vanishes identically",
        },
        "checks": checks,
        "occurrences": audits,
    }
    TARGET.write_text(json.dumps(packet, indent=2) + "\n")
    print(json.dumps(checks, sort_keys=True))


if __name__ == "__main__":
    main()
