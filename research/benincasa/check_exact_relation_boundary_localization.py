"""Consolidate the interior-versus-boundary GM closure audit."""

from __future__ import annotations

import json
from pathlib import Path


HERE=Path(__file__).resolve().parent
INTERIOR=(
 "exact-relation-gauss-manin-closure-interior-a8-p32003-point-2-3-m4.json",
 "exact-relation-gauss-manin-closure-interior-a10-p32003-point-2-3-m4.json",
 "exact-relation-gauss-manin-closure-interior-a8-p32009-point-3-5-m7.json",
)


def main():
    full=json.loads((HERE/"exact-relation-gauss-manin-closure-a8-p32003-point-2-3-m4.json").read_text())
    interior=[json.loads((HERE/name).read_text()) for name in INTERIOR]
    assert full["covariant_relation_extension_rank"]==4854
    assert not full["gauss_manin_stable"]
    assert all(item["safe_interior_only"] for item in interior)
    assert all(item["gauss_manin_stable"] for item in interior)
    assert all(item["covariant_relation_extension_rank"]==0 for item in interior)
    assert [item["covariant_test_count"] for item in interior]==[10,21,10]
    result={
      "schema":"marici.benincasa.exact-relation-boundary-localization.v1",
      "status":"passed","full_extension_rank_at_a8":4854,
      "interior_test_counts":[10,21,10],"interior_extension_ranks":[0,0,0],
      "replication_files":list(INTERIOR),
      "classification":"Gauss-Manin nonclosure of the finite exact image is supported on declared K-depth, q-depth, or polynomial-cutoff faces",
    }
    output=HERE/"exact-relation-boundary-localization.json"
    output.write_text(json.dumps(result,indent=2,sort_keys=True)+"\n")
    print(json.dumps(result,indent=2,sort_keys=True))


if __name__=="__main__":main()
