"""Type the literal physical-chain map on the strict principal cone."""
from __future__ import annotations

import argparse
import json
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("cone", type=Path)
    parser.add_argument("support", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()

    cone = json.loads(args.cone.read_text(encoding="utf-8"))
    support = json.loads(args.support.read_text(encoding="utf-8"))
    cohomology = cone["cone_cohomology"]
    maps = support["literal_chain_maps"]

    assert cohomology["H_minus_1_dimension"] == 1
    assert cohomology["H_0_dimension"] == 1
    for point in ("Z12", "Z13", "Z23"):
        assert maps[f"to_{point}"] == "zero by support disjointness"
    assert support["entry_740_line_image_from_literal_chain"] == "zero"

    result = {
        "schema": "marici.nima.literal_chain_on_strict_cone.v1",
        "sources": [str(args.cone).replace("\\", "/"), str(args.support).replace("\\", "/")],
        "cone_lines": {"H_minus_1": 1, "H_0": 1},
        "literal_point_supported_map": "zero",
        "induced_pairing": {"H_minus_1": "zero", "H_0": "zero"},
        "selection": "neither",
        "reason": "The literal normalized physical chamber is disjoint from Z12, Z13, and Z23, so its point-supported chain map vanishes before cone cohomology is taken.",
        "not_tested": "An analytically continued weighted relative-cycle specialization at Z23 is not present in the source packet.",
        "allocator_claim": "seqclaim-d78aa77fdcbceddeb9a156bf",
    }
    args.output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"selection": "neither", "H_minus_1_pairing": "zero", "H_0_pairing": "zero"}))


if __name__ == "__main__":
    main()
