#!/usr/bin/env python3
import json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT/"research/aspect/scc"))
from observer_set_compiler import compile_observer_set
c=json.loads((ROOT/"research/aspect/contracts/theta-primitive-square-observer-set.v1.json").read_text(encoding="utf-8"));r=compile_observer_set(c)
checks={"set_compiles":r["passed"],"two_members":len(r["members"])==2,"arity_domains_distinct":[x["domain"] for x in r["members"]]==["A","Sym^2(A)"],"arity_transport_natural":all(x["transport_natural"] for x in r["members"]),"polarization_retained":len(r["polarization"])==3 and all(x["passed"] for x in r["polarization"]),"one_copy_joint_faithful":r["joint_faithfulness_by_arity"]["1"]["faithful"],"two_copy_not_falsely_faithful":not r["joint_faithfulness_by_arity"]["2"]["faithful"],"a7_comparison_blocked":not r["realization_comparisons"][0]["verified_equivalent"],"unsupported_higher_not_promoted":all(not x["admitted"] for x in r["higher_coherence"] if x["state"]=="unsupported")}
out={"schema":"marici.aspect.theta-observer-set-check.v1","checks":checks,"compilation":r,"passed":all(checks.values()),"disposition":"observer set is first-class; finite arity transport passes; completed Fourier realization comparison remains blocked"};(ROOT/"research/aspect/results/theta_observer_set.json").write_text(json.dumps(out,indent=2)+"\n",encoding="utf-8");print(json.dumps({"schema":out["schema"],"checks":checks,"disposition":out["disposition"],"passed":out["passed"]},indent=2));raise SystemExit(0 if out["passed"] else 1)
