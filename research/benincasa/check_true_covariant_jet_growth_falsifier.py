"""Consolidate the replicated true covariant-jet growth law."""

from __future__ import annotations

import json
import math
from pathlib import Path


HERE=Path(__file__).resolve().parent
FILES=(
 "true-covariant-source-jet-closure-d5-a12-p32003-point-2-3-m4.json",
 "true-covariant-source-jet-closure-d5-a14-p32003-point-2-3-m4.json",
 "true-covariant-source-jet-closure-d5-a12-p32009-point-3-5-m7.json",
)


def predicted(depth): return 1 if depth==0 else math.comb(depth+3,3)-1


def main():
    packets=[json.loads((HERE/name).read_text()) for name in FILES]
    expected=[predicted(depth) for depth in range(6)]
    assert expected==[1,3,9,19,34,55]
    assert all(item["cumulative_covariant_ranks"]==expected for item in packets)
    assert all(item["parameter_derivative_checks"]==18 for item in packets)
    assert len({item["field"] for item in packets})==2
    assert len({item["ambient_relation_degree"] for item in packets})==2
    assert len({tuple(item["point"]) for item in packets})==2
    result={
      "schema":"marici.benincasa.true-covariant-jet-growth-falsifier.v1",
      "status":"passed","depths":list(range(6)),"ranks":expected,
      "rank_law":"r_0=1; r_d=binomial(d+3,3)-1 for 1<=d<=5",
      "increments":[expected[i]-expected[i-1] for i in range(1,len(expected))],
      "replication_files":list(FILES),
      "classification":"no finite differential closure is visible through depth five; rank26 static closure is falsified as the observer module",
    }
    output=HERE/"true-covariant-jet-growth-falsifier.json"
    output.write_text(json.dumps(result,indent=2,sort_keys=True)+"\n")
    print(json.dumps(result,indent=2,sort_keys=True))


if __name__=="__main__":main()
