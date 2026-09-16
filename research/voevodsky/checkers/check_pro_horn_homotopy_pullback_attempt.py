#!/usr/bin/env python3
"""Audit the minimal homotopy-pullback repair of the terminal pro-horn."""
import json
from fractions import Fraction
from pathlib import Path

# Finite observer scout: coordinates 0 and 2 represent +/-gamma; coordinate 1
# is bulk away from the crossing. A is atomic evaluation and B is Plancherel
# volume. No scalar multiple of B equals A on this source.
def A(m): return m[0]*m[0] + m[2]*m[2]
def B(m): return sum(x*x for x in m)
observers={"crossing":(Fraction(1),Fraction(0),Fraction(1)),
           "off_crossing":(Fraction(0),Fraction(1),Fraction(0))}
values={k:{"atomic":str(A(v)),"bulk":str(B(v))} for k,v in observers.items()}
# If A=cB, crossing forces c=1 while off-crossing forces c=0.
not_proportional=A(observers["crossing"])==B(observers["crossing"]) and A(observers["off_crossing"])==0 and B(observers["off_crossing"])!=0

# Mapping-fibre coordinate v has differential equal to the obstruction omega.
# The formal tautological lift v=omega closes the boundary, but has no
# independent source/geometric construction and is therefore not admitted.
checks={
 "bulk_and_atomic_functionals_independent":not_proportional,
 "ordinary_bulk_pullback_cannot_cancel_all_observers":not_proportional,
 "formal_mapping_fibre_is_algebraically_closed":True,
 "tautological_counterrow_is_circular":True,
 "source_derived_geometric_lift_present":False,
}
assert all(v for k,v in checks.items() if k!="source_derived_geometric_lift_present")
assert not checks["source_derived_geometric_lift_present"]
out={
 "schema":"marici.voevodsky.pro-horn-homotopy-pullback-attempt.v1",
 "observer_scout":values,
 "pullback_object":"(H234_L, V_gamma,L, eta_L) with eta_L: boundary(V_gamma,L) ~= P_gamma,L",
 "required_estimate":"sup_L ||P_gamma,L-V_gamma,L||_1 < infinity",
 "checks":checks,
 "status":"formal_pullback_constructed_analytic_lift_open",
 "admitted":False,
 "reason":"The only currently available exact lift is V_gamma,L=P_gamma,L, which copies the spectral obstruction onto the geometric face and is not source-derived.",
 "next_source_target":"construct V_gamma,L from C24 geometric/index data with the atomic observer functional and prove face, dagger, successor, and regulator compatibility"
}
path=Path(__file__).parents[1]/"results"/"pro_horn_homotopy_pullback_attempt.json"
path.write_text(json.dumps(out,indent=2)+"\n",encoding="utf-8")
print(json.dumps(out,indent=2))
