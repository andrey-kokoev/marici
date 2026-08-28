#!/usr/bin/env python3
"""Finite hostile checker for the interaction-net executable context gate."""
from __future__ import annotations
import json
from pathlib import Path

HERE=Path(__file__).resolve().parent
ASPECT=HERE.parent
CONTRACT=ASPECT/"contracts"/"interaction-net-semantic-context-gate.v1.json"
RESULT=ASPECT/"results"/"interaction_net_semantic_context_gate.json"

def states(N):
    for chart in range(3):
        for mask in range(32):
            support=mask.bit_count()
            for k in range(N-support+1):
                for u in range(k+1):
                    for v in range(2*k+1):
                        yield chart,mask,k,u,v

def algebraic_record(state):
    chart,mask,k,u,v=state
    return (chart,)+tuple((mask>>i)&1 for i in range(5))+(k,u,v)

def bounded_record(state,R):
    chart,mask,k,u,v=state
    return (chart,)+tuple((mask>>i)&1 for i in range(5))+(min(k,R),min(u,R),min(v,2*R))

def injective(records):
    seen={}
    for state,record in records:
        if record in seen and seen[record]!=state: return False,{"left":seen[record],"right":state,"record":record}
        seen[record]=state
    return True,None

def main():
    contract=json.loads(CONTRACT.read_text(encoding="utf-8"))
    finite=[]
    for N in range(5):
        algebraic_ok,_=injective((state,algebraic_record(state)) for state in states(N))
        bounded_ok,_=injective((state,bounded_record(state,N)) for state in states(N))
        finite.append({"N":N,"algebraic_injective":algebraic_ok,"range_N_optical_injective":bounded_ok})
    hostiles=[]
    for R in range(5):
        ok,witness=injective((state,bounded_record(state,R)) for state in states(R+2))
        hostiles.append({"fixed_range":R,"unbounded_extension_injective":ok,"collision":witness})
    algebraic_all=all(row["algebraic_injective"] for row in finite)
    finite_optical_all=all(row["range_N_optical_injective"] for row in finite)
    every_fixed_range_fails=all(not row["unbounded_extension_injective"] for row in hostiles)
    full_yoneda_rejected=contract["full_yoneda"]["arbitrary_probe_separation"]=="rejected"
    passed=algebraic_all and finite_optical_all and every_fixed_range_fails and full_yoneda_rejected
    out={"schema":"marici.aspect.interaction-net-semantic-context-gate-result.v1","passed":passed,
         "finite_truncations":finite,"fixed_range_hostiles":hostiles,
         "algebraic_basis":{"object_separating":algebraic_all,"physical_realizability":"not_certified"},
         "bounded_optical_basis":{"each_matched_truncation_separating":finite_optical_all,"fixed_basis_on_unbounded_category_faithful":not every_fixed_range_fails},
         "full_yoneda_rejected":full_yoneda_rejected,
         "semantic_verdict":contract["semantic_verdict"],"pilot_verdict":contract["pilot_verdict"],
         "scope":"object separation is a necessary gate; morphism-level enriched-nerve faithfulness is not claimed"}
    RESULT.parent.mkdir(parents=True,exist_ok=True)
    RESULT.write_text(json.dumps(out,indent=2)+"\n",encoding="utf-8")
    print(json.dumps(out,sort_keys=True))
    raise SystemExit(0 if passed else 1)

if __name__=="__main__": main()
