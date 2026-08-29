import json
from pathlib import Path
import sympy as sp

ROOT=Path(__file__).parents[1]
wp1022=json.loads((ROOT/"results"/"wp1022_cyclic_incidence_cancellation_no_go.json").read_text())
ensemble=json.loads((ROOT/"results"/"wp20_valley_audit.json").read_text())
assert wp1022["status"]=="PASS"

x=sp.symbols("x",real=True)
g=sp.expand(x*(1-x)**2)
dg=sp.factor(sp.diff(g,x))
assert dg==(x-1)*(3*x-1)
assert g.subs(x,sp.Rational(1,3))==sp.Rational(4,27)
assert g.subs(x,0)==0 and g.subs(x,1)==0

# J^2=(s12*c12)^2(s23*c23)^2*s13^2*c13^4*sin(delta)^2.
factor12=sp.Rational(1,4)
factor23=sp.Rational(1,4)
factor13=sp.Rational(4,27)
phase=sp.Integer(1)
J2max=sp.factor(factor12*factor23*factor13*phase)
assert J2max==sp.Rational(1,108)

Js=[abs(sp.Rational(str(row["J"]))) for row in ensemble["records"]]
assert len(Js)==1210
max_J=max(Js)
max_J2=max(j*j for j in Js)
assert max_J<sp.Rational(1,1000)
assert max_J2<sp.Rational(1,1000000)<J2max
assert sum(j*j==J2max for j in Js)==0

# Deliberate contrasting obstruction: the exact maximum is nonzero and
# isolated in the invariant mixing variables up to CP sign and permutations.
assert J2max!=0

result={
 "schema":"marici.flavor.wp1023.v1","status":"PASS",
 "admissible_domain":"unitary three-generation mixing quotient with nondegenerate quark spectra",
 "candidate_operation":"maximize the weak-basis-invariant normalized CP measure J^2",
 "exact_maximum_J_squared":str(J2max),
 "equality_conditions":["s12^2=1/2","s23^2=1/2","s13^2=1/3","sin(delta)^2=1"],
 "weak_basis_descent":"J^2 is invariant under the full weak-basis group and insensitive to CP sign",
 "contextual_partition":"maximal-CP orbit versus all submaximal physical16 points",
 "classification":"coefficient-free mathematical selector and presentation-independent rigidifier; no declared source action realizes the extremization",
 "ensemble_sheets_tested":len(Js),
 "ensemble_sheets_surviving":sum(j*j==J2max for j in Js),
 "ensemble_max_abs_J":str(max_J),
 "smallest_exact_falsifier":"all fitted sheets have |J|<1/1000 while maximal CP requires J^2=1/108",
 "deliberate_failure_nonzero_obstruction":str(J2max),
 "instrument":"signed CKM/Jarlskog readout measures J and falsifies the selected orbit",
 "claim_boundary":"does not claim a source potential proportional to J^2 exists or is local, renormalizable, executable, or radiatively closed",
 "remaining_gate":"derive a source-local invariant action whose stationary locus predicts the observed small nonzero J without inserting its scale",
}
out=ROOT/"results"/"wp1023_maximal_cp_selector_no_go.json"
out.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
print("WP1023 PASS: J^2 max =",J2max,"survivors",0)
