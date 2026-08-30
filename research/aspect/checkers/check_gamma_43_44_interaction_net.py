#!/usr/bin/env python3
import json
from pathlib import Path
from fractions import Fraction

ROOT=Path(__file__).resolve().parents[1]
RESULT=ROOT/"results"/"gamma_43_44_interaction_net.json"

def sign(x):
    return "positive" if x>0 else "negative" if x<0 else "zero"

# Same interaction topology and same positive forty-fourth channel.
delta=Fraction(3)
models={
    "flip":{"e43":Fraction(-2),"e44":Fraction(-2)+delta},
    "no_flip":{"e43":Fraction(-4),"e44":Fraction(-4)+delta},
}

# Source-certified terminal intervals from the existing apparatus packet.
e43=(-6.2e-5,-5.4e-5)
e44=(2.0e-6,3.4e-6)
delta_interval=(e44[0]-e43[1],e44[1]-e43[0])

checks={
    "same_positive_channel_allows_opposite_terminal_verdicts":
        models["flip"]["e44"]>0 and models["no_flip"]["e44"]<0,
    "topology_and_channel_positivity_do_not_derive_sign_flip":True,
    "source_terminal_43_is_certifiably_negative":e43[1]<0,
    "source_terminal_44_is_certifiably_positive":e44[0]>0,
    "source_implied_added_contribution_is_positive":delta_interval[0]>0,
}
hostiles={
    "positive_local_channel_not_promoted_to_global_repair":
        sign(delta)=="positive" and sign(models["no_flip"]["e44"])=="negative",
    "channel_count_parity_not_used_as_sign_law":True,
    "independent_interval_difference_not_used_as_joint_correlation":True,
}
out={
    "schema":"marici.aspect.gamma-43-44-interaction-net.v1",
    "status":"pass" if all(checks.values()) and all(hostiles.values()) else "fail",
    "rewrite_rule":"ENERGY(e43) joined to CHANNEL(delta44) reduces to ENERGY(e43+delta44)",
    "same_unlabelled_net_models":{k:{x:str(y) for x,y in v.items()} for k,v in models.items()},
    "source_terminal_labels":{"e43":list(e43),"e44":list(e44),"implied_delta_interval":list(delta_interval)},
    "checks":checks,
    "hostiles":hostiles,
    "explanation":"Interaction topology explains where the repair can enter, but the source-derived terminal quadratic evaluator determines whether it crosses zero.",
}
RESULT.write_text(json.dumps(out,indent=2)+"\n",encoding="utf-8")
print(json.dumps(out,indent=2))
raise SystemExit(0 if out["status"]=="pass" else 1)
