"""Materialize the exact six-cycle OFPT incidence packet."""

import importlib.util
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = HERE / "derive_polygon_ofpt_packet.py"
OUT = HERE.parent / "results" / "six-cycle-ofpt-packet.json"


def main():
    spec = importlib.util.spec_from_file_location("polygon_source", SOURCE)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(module)

    six_cycle = module.polygon(6)
    assert six_cycle["facet_count"] == 37
    assert six_cycle["term_count"] == 1476
    assert six_cycle["cyclic_orbit_sizes"] == [6] * 246
    assert all(abs(x) == 64 for x in six_cycle["ordered_denominator_determinants"])

    packet = {
        "schema": "marici.benincasa.six_cycle_ofpt_packet.v1",
        "method": "exact source-vertex/facet incidence with G plus all singleton facets fixed",
        "six_cycle": six_cycle,
    }
    OUT.write_text(json.dumps(packet, indent=2) + "\n")
    print(json.dumps({
        "facets": six_cycle["facet_count"],
        "terms": six_cycle["term_count"],
        "cyclic_orbits": len(six_cycle["cyclic_term_orbits"]),
        "determinant": 64,
    }))


if __name__ == "__main__":
    main()
