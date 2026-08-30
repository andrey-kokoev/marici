"""A cyclic source does not determine a terminal readout quotient."""

from __future__ import annotations

import json
from pathlib import Path

import sympy as sp


OUT = Path(__file__).resolve().parents[1] / "results" / "cyclic_source_readout_variance_gate.json"


def row_rank(rows: list[sp.Matrix]) -> int:
    return sp.Matrix.vstack(*rows).rank()


def main() -> None:
    # One fixed connection and one fixed cyclic source.
    connection = sp.Matrix(((0, 0), (1, 0)))
    source = sp.Matrix((1, 0))
    controllability = sp.Matrix.hstack(source, connection * source)
    assert controllability.rank() == 2

    readouts = {
        "zero": sp.Matrix(((0, 0),)),
        "rank_one": sp.Matrix(((1, 0),)),
        "full": sp.Matrix(((0, 1),)),
    }
    observability_ranks = {
        name: row_rank([readout, readout * connection])
        for name, readout in readouts.items()
    }
    assert observability_ranks == {"zero": 0, "rank_one": 1, "full": 2}

    packet = {
        "schema": "marici.cyclic-source-readout-variance-gate.v1",
        "state_dimension": 2,
        "source_orbit_rank": controllability.rank(),
        "same_connection_and_source": True,
        "readout_observability_ranks": observability_ranks,
        "source_cyclicity_implies_observability": False,
        "canonical_pairing_supplied": False,
        "cosmology_rank26_inference_authorized": False,
        "superseded_cutoff_plateau": 21,
        "stabilized_geometric_rank": 26,
        "required_next_datum": "source-derived physical chain covector on the rank-26 quotient",
        "passed": True,
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(packet, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(packet, indent=2))


if __name__ == "__main__":
    main()
