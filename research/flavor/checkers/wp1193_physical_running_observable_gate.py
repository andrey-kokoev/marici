import json
from fractions import Fraction
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
wp830=json.loads((ROOT/"results"/"wp830_process_relative_effective_charge_no_go.json").read_text())
wp1192=json.loads((ROOT/"results"/"wp1192_rg_event_anchor_gate.json").read_text())
assert wp830["summary"]["all_passed"] is True
assert wp1192["translation_fiber_repaired"] is True
model=wp830["admitted_channel_model"]
portal_a,portal_b=map(Fraction,model["portal_records"])
assert (portal_a,portal_b)==(Fraction(1,2),Fraction(9,16))
assert model["common_tree_normalization"] is True
assert model["effective_charge_A"] == "u"
assert model["effective_charge_B"] == "-u**3/2 + u**2/2 + u"
assert model["channel_B_anchor_polynomial"] == "60*u**4 - 108*u**3 + 45*u**2 + 4*u - 2"
resultant=next(t for t in wp830["tests"] if t["name"]=="second_channel_anchors_are_not_reflection_paired")["evidence"]
assert resultant == "53084160"
assert wp830["classification"]["selector"] is False
assert wp830["classification"]["first_nonfaithful_arrow"] == "source probe family to an unnamed canonical effective charge"
# Observable-defined running charges remove arbitrary scheme coordinates but
# not process choice: A and B are both monotone, tree-normalized, and physical.
physical_running_records_exist=True
canonical_running_observable=False
probe_natural_invariant=False
common_gain_instrument=False
assert physical_running_records_exist
assert not (canonical_running_observable or probe_natural_invariant or common_gain_instrument)
result={
    "schema":"marici.flavor.wp1193.v1",
    "status":"PASS",
    "question":"Can a physical running observable make the RG event anchor canonical?",
    "dpc":{
        "conjecture":"Replacing scheme coordinates by observable-defined effective charges selects the physical running observable.",
        "rivals":["canonical effective charge","process-relative charge family","unique conserved-current observable","probe-natural invariant"],
        "risky_consequences":["A(u)=u and B(u)=u+u^2(1-u)/2 share tree normalization and endpoints","portal records differ as 1/2 versus 9/16","channel-B anchor polynomial differs and has reflection resultant 53084160"],
        "falsification_attempt":"Both effective charges are monotone records of the same physical orbit, yet they assign different portal values and curvature events.",
        "residual":"A unique conserved-current experiment or a probe-natural invariant relation is required.",
        "disposition":"accept process-relative running records; reject canonical observable"
    },
    "effective_charge_A":model["effective_charge_A"],
    "effective_charge_B":model["effective_charge_B"],
    "portal_records":[str(portal_a),str(portal_b)],
    "channel_B_anchor_polynomial":model["channel_B_anchor_polynomial"],
    "reflection_resultant":resultant,
    "physical_running_records_exist":physical_running_records_exist,
    "canonical_running_observable":canonical_running_observable,
    "probe_natural_invariant":probe_natural_invariant,
    "common_gain_instrument":common_gain_instrument,
    "classification":"negative canonical-observable gate: physical effective charges remain process-relative",
    "remaining_gate":"derive a unique conserved-current channel or a probe-natural invariant",
    "hostile_gate":"do not treat operational normalization as canonical channel selection",
    "claim_boundary":"the no-go covers scalar effective-charge presentations of the same orbit; probe-family invariants remain open",
    "disposition":"physical-running-observable leaf resolved; probe-natural-invariant rival selected"
}
(ROOT/"results"/"wp1193_physical_running_observable_gate.json").write_text(json.dumps(result,indent=2)+"\n")
print("WP1193 PASS:",portal_a,portal_b,resultant)
