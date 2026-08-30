"""Measure the full source-cyclic rank at a declared total-energy slice point."""

from __future__ import annotations

import json
import os
from pathlib import Path

import check_rank26_unsplit_source_cyclicity as cyclic


def main():
    energy = int(os.environ.get("MARICI_E_VALUE", "1"))
    ambient = int(os.environ.get("MARICI_AMBIENT", "12"))
    original = cyclic.charts.SOURCE_POINT
    point = (2, 3, -5 + energy)
    cyclic.charts.SOURCE_POINT = point
    try:
        record = cyclic.census(ambient)
    finally:
        cyclic.charts.SOURCE_POINT = original
    result = {
        "schema":"marici.benincasa.rank26-normal-slice-cyclic-rank.v1",
        "field":cyclic.base.PRIME,"point":list(point),"E_T":energy,
        "record":record,
    }
    output=Path(__file__).with_name(f"rank26-normal-slice-cyclic-rank-e{energy}-a{ambient}-p{cyclic.base.PRIME}.json")
    output.write_text(json.dumps(result,indent=2,sort_keys=True)+"\n")
    print(json.dumps(result,indent=2,sort_keys=True))


if __name__ == "__main__": main()
