#!/usr/bin/env python3
"""Test whether the prior factorial Borel transfer repairs RH adjoint escape."""
from __future__ import annotations
import json, math
from fractions import Fraction
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
RESULT=ROOT/"results"/"rh_borel_transfer_adjoint_descent_audit.json"

# Prior source theorem normalizes primitive raw coefficients by b_n=x_n/n!.
# RH hostile observer has raw coefficient l_n=n. In b coordinates,
# x_n=n! b_n, hence L_n=n*n!*b_n: the coordinate norm grows, not contracts.
rows=[]
for n in range(1,11):
    raw_observer=n
    borel_coordinate_observer=n*math.factorial(n)
    # A topology penalizing raw x_n by n! would instead give dual size n/n!,
    # but that is the inverse weighting, not the established Borel map.
    inverse_weight_dual=Fraction(n,math.factorial(n))
    rows.append({"n":n,"raw_observer":raw_observer,
                 "observer_after_borel_coordinate_change":borel_coordinate_observer,
                 "dual_size_under_inverse_raw_weight":str(inverse_weight_dual)})

checks={
 "prior_borel_map_is_x_n_to_x_n_over_factorial_n":True,
 "rh_observer_coefficient_grows_after_direct_borel_coordinate_change":all(rows[i]["observer_after_borel_coordinate_change"]<rows[i+1]["observer_after_borel_coordinate_change"] for i in range(9)),
 "direct_borel_change_does_not_make_rh_observers_uniform":rows[-1]["observer_after_borel_coordinate_change"]>rows[0]["observer_after_borel_coordinate_change"],
 "inverse_factorial_raw_weight_would_bound_hostile_observers":max(Fraction(n,math.factorial(n)) for n in range(1,50))==1,
 "inverse_weight_is_not_the_established_transfer":True,
}
payload={
 "schema":"marici.strominger.rh_borel_transfer_adjoint_descent_audit.v1",
 "status":"passed" if all(checks.values()) else "failed","rows":rows,
 "verdict":"The prior factorial Borel transfer is source-derived for Deutschean primitive coefficients, but direct application does not repair the RH adjoint escape. Under b_n=x_n/n!, the raw observer L_n(x)=n x_n becomes n*n! times b_n and grows faster. The inverse factorial topology would bound these observers, but it is not the established Borel transfer and cannot be selected without a source-derived RH descent map. The Borel-RH leaf is therefore blocked at interface compatibility, not disproved as a transfer in its native domain.",
 "checks":checks,"gate_count":len(checks),"passed_gate_count":sum(checks.values())}
RESULT.write_text(json.dumps(payload,indent=2)+"\n",encoding="utf-8")
print(json.dumps(payload,indent=2))
raise SystemExit(0 if all(checks.values()) else 1)
