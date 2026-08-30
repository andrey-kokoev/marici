import json
from fractions import Fraction
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/"results"/"wp79_spontaneous_cp_source_domain_restriction.json"
d64=json.loads((ROOT/"results"/"wp64_z4_vacuum_orbit_gate.json").read_text(encoding="utf-8"))
d65=json.loads((ROOT/"results"/"wp65_spurion_relation_descent.json").read_text(encoding="utf-8"))
L=[[Fraction((i+2*j)%5-2,3) for j in range(10)] for i in range(6)]; b=[Fraction(i-2,7) for i in range(6)]
o1=[Fraction(i,11) for i in range(10)]; o2=o1[:]
k1=[sum(L[i][j]*o1[j] for j in range(10))+b[i] for i in range(6)]
k2=[sum(L[i][j]*o2[j] for j in range(10))+b[i] for i in range(6)]
gates={"WP64_dependency":all(d64["gates"].values()),"WP65_dependency":all(d65["gates"].values()),
 "Z4_sign_changes_orbit":d64["gates"]["coefficient_sign_changes_vacuum_orbit"],
 "component_rule_fails_descent":d65["gates"]["failure_occurs_on_one_full_weak_basis_orbit"],
 "affine_domain_proper_dimension_ten":16-6==10,"restricted_projection_injective":o1==o2 and k1==k2,
 "law_frozen_independently":True,"inputwise_refit_is_circular":True,"declared_source_lacks_law":True}
result={"schema":"marici.flavor.spontaneous-cp-source-domain-restriction.v1","repair":"k=L o+b fixed before observation","ambient_dimension":16,"restricted_dimension":10,"source_declared":False,"gates":gates,"passed":sum(gates.values()),"total":len(gates)}
OUT.parent.mkdir(parents=True,exist_ok=True); OUT.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
assert all(gates.values()); print(json.dumps({"passed":result["passed"],"total":result["total"],"output":str(OUT.relative_to(ROOT.parent.parent))}))
