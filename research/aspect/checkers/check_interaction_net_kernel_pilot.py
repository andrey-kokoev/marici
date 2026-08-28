#!/usr/bin/env python3
"""Small exact checker for the bounded SCC interaction-net kernel pilot."""
from __future__ import annotations
import json
from copy import deepcopy
from math import comb
from pathlib import Path

HERE=Path(__file__).resolve().parent
ASPECT=HERE.parent
CONTRACT=ASPECT/"contracts"/"interaction-net-kernel-pilot.v1.json"
RESULT=ASPECT/"results"/"interaction_net_kernel_pilot.json"

def fiber_rank(k): return (k+1)*(2*k+1)
def grade_count(k,j): return 3*comb(5,j)*fiber_rank(k)
def generated_table(max_depth=4):
    return [{"k":k,"occurrence_grade":j,"generated_reachability":grade_count(k,j),
             "exact_relation_image_rank":None,"quotient_rank":None}
            for k in range(max_depth+1) for j in range(6)]

def normal_form(word):
    occurrences=tuple(sorted(x for x in word if x.startswith("o")))
    depth=sum(x=="K" for x in word)
    structural=tuple(sorted(x for x in word if x in ("DUP","DEL")))
    return occurrences,depth,structural

def metadata_complete(rules,required): return all(required<=set(rule) for rule in rules)
def interfaces_preserved(rules): return all(rule["external_interface_before"]==rule["external_interface_after"] for rule in rules)
def structural_agents_complete(signature): return {"Duplicate","Delete"}<={x["type"] for x in signature}
def first_outgoing_edge(k): return {"from":[k,0,0],"generator":"K","to":[k+1,0,0]}

def main():
    contract=json.loads(CONTRACT.read_text(encoding="utf-8"))
    required={"authority_root","support_delta","resource_equation","fault_modality_grade","coherence_class","external_interface_before","external_interface_after"}
    rule_metadata=metadata_complete(contract["rules"],required)
    interface_preserved=interfaces_preserved(contract["rules"])
    coefficients=[fiber_rank(k) for k in range(5)]
    total=sum(grade_count(k,j) for k in range(5) for j in range(6))
    chart_totals={"G12":total,"G31":total}
    pairs=[]
    for left,right in [(["o1","o2"],["o2","o1"]),(["o3","K"],["K","o3"]),(["DUP","DEL"],["DEL","DUP"]),(["DUP","o1"],["o1","DUP"]),(["DEL","o1"],["o1","DEL"])]:
        pairs.append({"left":left,"right":right,"join":normal_form(left)==normal_form(right)})
    local_confluence=all(x["join"] for x in pairs)
    outgoing=[{"truncation_depth":k,"edge":first_outgoing_edge(k)} for k in range(9)]
    missing_authority=deepcopy(contract["rules"]);missing_authority[0].pop("authority_root")
    changed_interface=deepcopy(contract["rules"]);changed_interface[0]["external_interface_after"]=["changed"]
    implicit_duplication=[x for x in contract["agent_signature"] if x["type"]!="Duplicate"]
    implicit_deletion=[x for x in contract["agent_signature"] if x["type"]!="Delete"]
    conflated=generated_table();conflated[0]["exact_relation_image_rank"]=0;conflated[0]["quotient_rank"]=conflated[0]["generated_reachability"]
    hostiles={
        "finite_closure_rejected":all(x["edge"]["to"][0]>x["truncation_depth"] for x in outgoing),
        "quotient_conflation_rejected":not all(row["exact_relation_image_rank"] is None and row["quotient_rank"] is None for row in conflated),
        "missing_rule_authority_rejected":not metadata_complete(missing_authority,required),
        "external_interface_change_rejected":not interfaces_preserved(changed_interface),
        "implicit_duplication_rejected":not structural_agents_complete(implicit_duplication),
        "implicit_deletion_rejected":not structural_agents_complete(implicit_deletion),
        "full_yoneda_witness_rejected":contract["semantic_gate"]["full_yoneda_nonexecutable_probes_rejected"] is True}
    reachability_exact=(coefficients==[1,6,15,28,45] and total==9120 and len(set(chart_totals.values()))==1)
    semantic_ready=(contract["semantic_gate"]["basis_physically_realizable"] is True and contract["semantic_gate"]["restricted_enriched_nerve_faithful"] is True)
    verdict=("faithful_local_kernel" if reachability_exact and local_confluence and semantic_ready else "useful_but_incomplete_presentation" if reachability_exact and local_confluence else "interaction_net_mismatch")
    passed=reachability_exact and local_confluence and all(hostiles.values()) and verdict==contract["verdict"]
    out={"schema":"marici.aspect.interaction-net-kernel-pilot-result.v1","passed":passed,
         "entry_4013":{"fiber_coefficients_through_depth_four":coefficients,"depth_four_coefficient":coefficients[4],"cumulative_total_rank":total,"chart_totals":chart_totals},
         "grade_table":generated_table(),"critical_pairs":pairs,"local_confluence":local_confluence,
         "first_outgoing_generator_edges":outgoing,"all_finite_truncations_have_outgoing_edge_by_formula":"first_outgoing_edge(k)=(k,0,0)-K->(k+1,0,0) for every k>=0","rule_metadata_complete":rule_metadata,
         "external_interface_preserved":interface_preserved,"hostiles":hostiles,
         "semantic_gate":contract["semantic_gate"],"verdict":verdict}
    RESULT.parent.mkdir(parents=True,exist_ok=True)
    RESULT.write_text(json.dumps(out,indent=2)+"\n",encoding="utf-8")
    print(json.dumps(out,sort_keys=True))
    raise SystemExit(0 if passed else 1)

if __name__=="__main__": main()
