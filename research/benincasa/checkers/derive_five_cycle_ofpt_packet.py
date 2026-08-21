"""Derive the five-cycle OFPT denominator packet from source incidence."""
import json
from pathlib import Path

from derive_polygon_ofpt_packet import polygon

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "research/benincasa/results/five-cycle-ofpt-packet.json"

pentagon = polygon(5)
assert pentagon["projective_dimension"] == 9
assert pentagon["source_vertex_count"] == 15
assert pentagon["facet_count"] == 26
assert pentagon["additional_denominators_per_term"] == 4
assert all(len(term) == 4 for term in pentagon["terms"])
assert sum(pentagon["cyclic_orbit_sizes"]) == pentagon["term_count"]
assert len(pentagon["cyclic_term_orbits"]) == 36
assert all(len(orbit) == 5 for orbit in pentagon["cyclic_term_orbits"])

packet = {
    "schema": "marici.benincasa.five_cycle_ofpt_packet.v1",
    "method": "exact source-vertex/facet incidence with G plus all singleton facets fixed",
    "source_representation": {
        "reference": "arXiv:2112.09028, Eq. (33)",
        "fixed_G_circle": ["G", "g_1", "g_2", "g_3", "g_4", "g_5"],
        "compatible_Gc_size": 4,
        "predicate": "nonempty projective codimension-four intersection on the source polytope",
        "orientation_normalized_common_weight": 1,
        "status": "source-authorized OFPT canonical-function representation",
    },
    "five_cycle": pentagon,
}
OUT.write_text(json.dumps(packet, indent=2) + "\n")
print(json.dumps({"terms": pentagon["term_count"],
                  "cyclic_orbits": len(pentagon["cyclic_orbit_sizes"]),
                  "orbit_sizes": pentagon["cyclic_orbit_sizes"]}))
