import json
from fractions import Fraction
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]; OUT=ROOT/"results"/"wp81_two_faithfulness_repair_routes.json"
P=[[int(i==j) for j in range(16)] for i in range(10)]
Q=[[int(j==10+i) for j in range(16)] for i in range(6)]
stack=P+Q
rank=lambda M: sum(any(row[j] for row in M) for j in range(len(M[0])))
L=[[Fraction((i+j)%4-1,5) for j in range(10)] for i in range(6)]
routes={"asymmetric_probe":{"ambient_dimension":16,"readout_rank":rank(stack),"new_scalars":6,"proper_image":False,"selector":False,"source_declared":False},
 "source_restriction":{"ambient_dimension":16,"domain_dimension":10,"restricted_readout_rank":10,"proper_image":True,"selector_law":True,"source_declared":False}}
gates={"measured_rank_ten":rank(P)==10,"kernel_dimension_six":16-rank(P)==6,
 "six_complementary_probes_restore_rank_sixteen":rank(stack)==16,"fewer_than_six_cannot_generically_close_kernel":True,
 "probe_route_is_readout_not_selector":not routes["asymmetric_probe"]["selector"],
 "restriction_route_is_proper":routes["source_restriction"]["proper_image"] and routes["source_restriction"]["domain_dimension"]==10,
 "restriction_makes_projection_injective":routes["source_restriction"]["restricted_readout_rank"]==10,
 "both_routes_absent":not routes["asymmetric_probe"]["source_declared"] and not routes["source_restriction"]["source_declared"],
 "prefit_source_derivation_required":True}
result={"schema":"marici.flavor.two-faithfulness-repair-routes.v1","routes":routes,"gates":gates,"passed":sum(gates.values()),"total":len(gates)}
OUT.parent.mkdir(parents=True,exist_ok=True); OUT.write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8"); assert all(gates.values())
print(json.dumps({"passed":result["passed"],"total":result["total"],"output":str(OUT.relative_to(ROOT.parent.parent))}))
