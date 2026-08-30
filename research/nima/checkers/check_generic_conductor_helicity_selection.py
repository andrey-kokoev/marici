"""Helicity selection on the two generic chiral conductor lifts."""

import itertools
import json
from pathlib import Path


words = [(0, 1, 0, 1, 0, 1), (1, 0, 1, 0, 1, 0)]
f_plus_edges = (0, 2, 4)
f_minus_edges = (1, 3, 5)

rows = []
for w in words:
    hp = tuple(w[i] for i in f_plus_edges)
    hm = tuple(w[i] for i in f_minus_edges)
    assert len(set(hp)) == 1 and len(set(hm)) == 1
    assert hp[0] != hm[0]
    rows.append({"word": list(w), "f_plus_helicities": list(hp), "f_minus_helicities": list(hm)})

# Color-ordered 4D YM at three points is supported only on the 2+1 and 1+2
# helicity sectors (MHV and anti-MHV), not homogeneous triples.
all_helicity_words = list(itertools.product((0, 1), repeat=3))
ym_supported = [h for h in all_helicity_words if sum(h) in (1, 2)]
strict_triples = [tuple(r[k]) for r in rows for k in ("f_plus_helicities", "f_minus_helicities")]
assert all(h not in ym_supported for h in strict_triples)

result = {
    "status": "PASS",
    "rows": rows,
    "three_point_YM_supported_helicity_words": [list(h) for h in ym_supported],
    "strict_conductor_YM_section": "zero",
    "conclusion": (
        "The generic diagonal conductor line exists, but each alternating "
        "scaffold pairing produces an all-equal helicity triple. Its ordinary "
        "4D three-gluon YM restriction vanishes; any activation must live in "
        "a derived first-normal or Bockstein grade."
    ),
}
out = Path(__file__).parents[1] / "results" / "generic_conductor_helicity_selection.json"
out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
print(json.dumps(result, indent=2))
