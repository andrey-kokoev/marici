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

packet = {
    "schema": "marici.benincasa.five_cycle_ofpt_packet.v1",
    "method": "exact source-vertex/facet incidence with G plus all singleton facets fixed",
    "five_cycle": pentagon,
}
OUT.write_text(json.dumps(packet, indent=2) + "\n")
print(json.dumps({"terms": pentagon["term_count"],
                  "cyclic_orbits": len(pentagon["cyclic_orbit_sizes"]),
                  "orbit_sizes": pentagon["cyclic_orbit_sizes"]}))
