"""Consolidate stabilization of the labelled cutoff-adapter cone."""

from __future__ import annotations

import json
from pathlib import Path


HERE=Path(__file__).resolve().parent
FILES=(
 "cutoff-inclusion-gauss-manin-adapter-a8-to-a10-p32003-point-2-3-m4.json",
 "cutoff-inclusion-gauss-manin-adapter-a8-to-a12-p32003-point-2-3-m4.json",
 "cutoff-inclusion-gauss-manin-adapter-a8-to-a14-p32003-point-2-3-m4.json",
 "cutoff-inclusion-gauss-manin-adapter-a8-to-a16-p32003-point-2-3-m4.json",
 "cutoff-inclusion-gauss-manin-adapter-a8-to-a14-p32009-point-3-5-m7.json",
)


def main():
    packets=[json.loads((HERE/name).read_text()) for name in FILES]
    ranks=[item["adapter_cone_rank"] for item in packets]
    assert ranks==[3980,2348,2349,2349,2349]
    assert all(not item["gauss_manin_compatible"] for item in packets)
    assert len({item["field"] for item in packets})==2
    result={
      "schema":"marici.benincasa.cutoff-adapter-stabilization.v1",
      "status":"passed","big_ambient_values":[10,12,14,16,14],
      "adapter_cone_ranks":ranks,"stable_rank":2349,
      "classification":"literal polynomial-cutoff inclusion leaves a stable nonzero GM cone; boundary coherence cannot be supplied by ordinary inclusion alone",
      "inputs":list(FILES),
    }
    output=HERE/"cutoff-adapter-stabilization.json"
    output.write_text(json.dumps(result,indent=2,sort_keys=True)+"\n")
    print(json.dumps(result,indent=2,sort_keys=True))


if __name__=="__main__":main()
