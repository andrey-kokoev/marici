from __future__ import annotations

import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[3]
RESULT=ROOT/"research/nima/results/six-point-nmhv-scattering-carrier-dimension.json"

n=6
m0n_dimension=n-3
amplituhedron_dimension=1*4
pullback_top_form_degree=amplituhedron_dimension
max_nonzero_form_degree_on_m0n=m0n_dimension
required_relative_fiber_dimension=m0n_dimension-amplituhedron_dimension

checks={
    "m0_6_has_dimension_3":m0n_dimension==3,
    "six_point_nmhv_k1_m4_geometry_has_dimension_4":amplituhedron_dimension==4,
    "ordinary_pullback_of_4_form_to_3_fold_is_zero":pullback_top_form_degree>max_nonzero_form_degree_on_m0n,
    "ordinary_pushforward_would_require_negative_fiber_dimension":required_relative_fiber_dimension<0
}
out={
    "schema":"marici.nima.six_point_nmhv_scattering_carrier_dimension.result.v1",
    "status":"conjecture_falsified_as_stated" if all(checks.values()) else "inconclusive",
    "checks":checks,
    "dimensions":{"M0_6":m0n_dimension,"A_6_1_m4":amplituhedron_dimension,"required_pushforward_fiber":required_relative_fiber_dimension},
    "residual":"A carrier supported only on M0,6 cannot recover the nonzero degree-4 NMHV amplituhedron canonical form by ordinary pullback or pushforward while preserving form degree and residues.",
    "claim_boundary":"Rejects the stated M0,6-only carrier. It does not reject an enlarged correspondence space with an independently defined positive-dimensional fiber or a map directly into scalar CHY residues."
}
RESULT.parent.mkdir(parents=True,exist_ok=True)
RESULT.write_text(json.dumps(out,indent=2)+"\n",encoding="utf-8")
if out["status"]!="conjecture_falsified_as_stated": raise SystemExit(1)
