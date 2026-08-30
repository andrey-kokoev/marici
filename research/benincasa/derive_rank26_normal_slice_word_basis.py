"""Derive primitive source words on the nonzero total-energy normal slice."""

from __future__ import annotations

import json
from pathlib import Path

import derive_rank26_source_word_basis as basis


REFERENCE_POINT = (2, 3, -4)  # E_T=1
CONTROL_POINTS = ((2, 3, -3), (3, 5, -7))


def main():
    descriptors, supports = basis.derive_descriptors(REFERENCE_POINT)
    controls = [
        {"point":list(point),"E_T":sum(point),"rank":basis.descriptor_rank(point,descriptors)}
        for point in CONTROL_POINTS
    ]
    assert all(item["rank"] == 26 for item in controls)
    result = {
        "schema":"marici.benincasa.rank26-normal-slice-word-basis.v1",
        "field":basis.base.PRIME,"reference_point":list(REFERENCE_POINT),
        "reference_E_T":sum(REFERENCE_POINT),"control_ranks":controls,
        "ambient_relation_degree":basis.AMBIENT,"low_cutoff":basis.CUTOFF,
        "descriptors":descriptors,"raw_support_sizes":supports,
        "maximum_connection_depth":max(item["depth"] for item in descriptors),
        "selection":"breadth-first unreduced source words selected at E_T=1",
        "warning":"rank agreement is not equality of transported submodules; connection closure is tested separately",
    }
    output=Path(__file__).with_name("rank26-normal-slice-word-basis.json")
    output.write_text(json.dumps(result,indent=2,sort_keys=True)+"\n")
    print(json.dumps({key:value for key,value in result.items() if key != "descriptors"},indent=2,sort_keys=True))


if __name__ == "__main__": main()
