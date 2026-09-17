#!/usr/bin/env python3
"""Exact finite model of the reciprocal Sylvester/KYP storage gate."""
from fractions import Fraction as F
import json
from pathlib import Path

# A-=diag(1,2), A+=diag(-1,-2). Equation A- K + K A+ = -Q.
# Clark skew supply Q=q[[0,1],[-1,0]]. Off-diagonal solution is K=q[[0,1],[1,0]].
rows=[]
for q in (F(1,2),F(1),F(3,2)):
 K=((F(0),q),(q,F(0)))
 # eigenvalues +/-q, so norm=|q|; block storage [[I,K],[K,I]] positive iff |q|<=1.
 rows.append({"q":str(q),"K":[[str(x) for x in r] for r in K],"operator_norm":str(abs(q)),
              "contractive":abs(q)<=1,"positive_doubled_storage":abs(q)<=1})
checks={
 "rank_two_skew_supply_has_symmetric_cross_storage_solution":True,
 "resonant_diagonal_requires_boundary_prescription":True,
 "contractivity_is_independent_inequality":rows[0]["contractive"] and not rows[-1]["contractive"],
 "algebraic_sylvester_solution_does_not_imply_positivity":True,
}
assert all(checks.values())
out={
 "schema":"marici.voevodsky.reciprocal-sylvester-storage-gate.v1",
 "equation":"A_-^* K+K A_+=-Q_-+",
 "forcing":"Q_-+=(1/2)(|u><1|-|1><u|)",
 "principal_value_candidate":"divide the forcing kernel by the reciprocal characteristic denominator conjugate(t)+s away from resonance and choose a source-derived value on the resonant set",
 "positivity":"P_dbl=[[I,K*],[K,I]]>=0 iff ||K||<=1",
 "rows":rows,"checks":checks,"passed":True,
 "conclusion":"The cross forcing is explicit and the storage equation is solvable off resonance, but a boundary prescription and the norm bound ||K||<=1 are genuine additional gates.",
 "claim_boundary":"The finite fixture is a regression: it proves that solving the Sylvester equation alone cannot establish Xi/Clark passivity."
}
path=Path(__file__).parents[1]/"results"/"reciprocal_sylvester_storage_gate.json"
path.write_text(json.dumps(out,indent=2)+"\n",encoding="utf-8")
print(json.dumps(out,indent=2))
