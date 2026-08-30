#!/usr/bin/env python3
"""Exact finite checks for the preregistered pro-context tower."""
from __future__ import annotations
import json
from pathlib import Path

HERE=Path(__file__).resolve().parent
ASPECT=HERE.parent
CONTRACT=ASPECT/"contracts"/"interaction-net-pro-context-tower.v1.json"
RESULT=ASPECT/"results"/"interaction_net_pro_context_tower.json"

def states(N):
    for chart in range(3):
        for mask in range(32):
            support=mask.bit_count()
            for k in range(N-support+1):
                for u in range(k+1):
                    for v in range(2*k+1):
                        yield chart,mask,k,u,v

def record(state,R):
    chart,mask,k,u,v=state
    return (chart,mask,min(k,R),min(u,R),min(v,2*R))

def restrict(record_at_higher,R):
    chart,mask,k,u,v=record_at_higher
    return chart,mask,min(k,R),min(u,R),min(v,2*R)

def injective_at(states_list,R):
    seen={}
    for state in states_list:
        value=record(state,R)
        if value in seen and seen[value]!=state: return False,{"left":seen[value],"right":state,"record":value}
        seen[value]=state
    return True,None

def main():
    contract=json.loads(CONTRACT.read_text(encoding="utf-8"))
    levels=[]
    for R in range(6):
        matched=list(states(R))
        extended=list(states(R+2))
        matched_ok,_=injective_at(matched,R)
        global_ok,collision=injective_at(extended,R)
        naturality=all(restrict(record(state,R+1),R)==record(state,R) for state in extended)
        levels.append({"R":R,"matched_truncation_injective":matched_ok,
                       "extension_injective":global_ok,"extension_collision":collision,
                       "restriction_square_closed":naturality})
    finite_universe=list(states(5))
    pro_records={state:tuple(record(state,R) for R in range(6)) for state in finite_universe}
    pro_injective=len(set(pro_records.values()))==len(finite_universe)
    # Deliberately wrong restriction caps v at R rather than 2R.
    wrong_transition_witness=None
    for state in states(4):
        high=record(state,4)
        wrong=(high[0],high[1],min(high[2],3),min(high[3],3),min(high[4],3))
        if wrong!=record(state,3):
            wrong_transition_witness={"state":state,"wrong":wrong,"direct":record(state,3)}
            break
    hostiles={
        "fixed_level_global_claim_rejected":all(not x["extension_injective"] for x in levels),
        "adaptive_probe_creation_rejected":contract["tower"]["target_adaptive_level_creation"] is False,
        "wrong_restriction_rejected":wrong_transition_witness is not None,
        "resource_growth_visible":contract["tower"]["resource_growth_declared"] is True,
        "morphism_promotion_rejected":contract["claims"]["morphism_faithful_enriched_nerve"]=="not_yet_certified"}
    passed=all(x["matched_truncation_injective"] and x["restriction_square_closed"] for x in levels) and pro_injective and all(hostiles.values())
    out={"schema":"marici.aspect.interaction-net-pro-context-tower-result.v1","passed":passed,
         "levels":levels,"pro_object_faithful_through_grade_five":pro_injective,
         "separation_law":"for distinct finite states x,y choose any preregistered R at least max(resource_grade(x),resource_grade(y))",
         "wrong_transition_witness":wrong_transition_witness,"hostiles":hostiles,
         "physical_gate":contract["physical_gate"],"verdict":contract["verdict"]}
    RESULT.parent.mkdir(parents=True,exist_ok=True)
    RESULT.write_text(json.dumps(out,indent=2)+"\n",encoding="utf-8")
    print(json.dumps(out,sort_keys=True))
    raise SystemExit(0 if passed else 1)

if __name__=="__main__": main()
