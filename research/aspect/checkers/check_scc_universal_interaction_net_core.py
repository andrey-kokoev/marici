#!/usr/bin/env python3
import copy,json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT/"research/aspect/scc"))
from universal_net_certifier import compile_universal_core
CP=ROOT/"research/aspect/contracts/scc-universal-interaction-net-core.v1.json";RP=ROOT/"research/aspect/results/scc_universal_interaction_net_core.json"
base=json.loads(CP.read_text(encoding="utf-8"));positive=compile_universal_core(base)
def hostile(name,mutate,expected):
 c=copy.deepcopy(base);mutate(c);r=compile_universal_core(c);return {"id":name,"expected":expected,"actual":r.get("first_failed_gate"),"passed":r.get("first_failed_gate")==expected}
hostiles=[
 hostile("nondecreasing_rule",lambda c:c["rules"][0].update(rhs_measure=c["rules"][0]["lhs_measure"]),"termination"),
 hostile("duplicate_active_pair",lambda c:c["rules"].append({**c["rules"][0],"id":"competing"}),"orthogonality"),
 hostile("unjoined_critical_pair",lambda c:c["critical_pairs"][0].update(join=None),"local_confluence"),
 hostile("nonassociative_quotient",lambda c:c["quotient_category"]["composition"].update({"p,p":"p"}),"category_associativity"),
 hostile("partial_sector_observer",lambda c:c["sector_representations"]["coherent_loop"].pop("d"),"sector_totality"),
]
checks={
 "universal_termination_on_closed_schema":positive.get("termination",{}).get("universal_over_admitted_rules") is True,
 "universal_confluence_on_closed_schema":positive.get("confluence",{}).get("universal_over_admitted_rules") is True,
 "yoneda_faithful_on_quotient":positive.get("faithfulness",{}).get("universal_over_finite_quotient_category") is True,
 "coarse_kernel_exposed":positive.get("sector_kernels",{}).get("coarse_optics")==[["d","e","p"]],
 "coherent_loop_separates":positive.get("sector_kernels",{}).get("coherent_loop")==[],
 "all_hostiles_rejected":all(x["passed"] for x in hostiles),
}
out={"schema":"marici.aspect.scc-universal-interaction-net-core-check.v1","passed":all(checks.values()),"checks":checks,"hostiles":hostiles,"report":positive}
RP.write_text(json.dumps(out,indent=2)+"\n",encoding="utf-8");print(json.dumps(out,indent=2));raise SystemExit(0 if out["passed"] else 1)
