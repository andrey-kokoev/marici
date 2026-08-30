#!/usr/bin/env python3
"""Reject synthetic promotion and verify conservative spacelike-margin arithmetic."""
import json
from pathlib import Path
ASPECT=Path(__file__).resolve().parent.parent
CONTRACT=ASPECT/"contracts"/"physical-promotion-spacelike-gate.v1.json"
PACKET=ASPECT/"fixtures"/"hardware-bound-pushforward-synthetic-packet.v1.json"
RECEIPT=ASPECT/"results"/"hardware_bound_pushforward_acquisition.json"
RESULT=ASPECT/"results"/"physical_promotion_spacelike_gate.json"
def margin(c,d,dt,ut,ux):return d-ux-c*(abs(dt)+ut)
def main():
 c=json.loads(CONTRACT.read_text(encoding="utf-8"));p=json.loads(PACKET.read_text(encoding="utf-8"));r=json.loads(RECEIPT.read_text(encoding="utf-8"));light=c["speed_of_light_m_per_s"]
 # Arithmetic fixture only: no authority and therefore never promotable.
 intervals={name:{"distance_m":1200.0,"delta_t_s":1e-7,"timing_uncertainty_s":2e-8,"position_uncertainty_m":0.5} for name in c["required_intervals"]}
 margins={k:margin(light,v["distance_m"],v["delta_t_s"],v["timing_uncertainty_s"],v["position_uncertainty_m"]) for k,v in intervals.items()}
 authorities={name:None for name in c["required_authorities"]}
 gates={"physical_raw_status":p["status"]=="physical_raw","receipt_passed":bool(r.get("passed")) and r.get("receipt",{}).get("pushforward_exact",False),"fixed_coincidence_policy":bool(p.get("coincidence_window_id")),"no_synthetic_fields":p["status"]!="synthetic_reference","all_intervals_spacelike":all(x>c["minimum_spacelike_margin_m"] for x in margins.values()),"all_authorities_bound":all(authorities.values())}
 promoted=all(gates.values())
 rejection_reasons=sorted(k for k,v in gates.items() if not v)
 # A hostile timelike interval must be rejected by the same arithmetic.
 hostile_margin=margin(light,10.0,1e-6,1e-7,0.1)
 checks={"geometry_fixture_spacelike":gates["all_intervals_spacelike"],"timelike_hostile_rejected":hostile_margin<=c["minimum_spacelike_margin_m"],"synthetic_packet_not_promoted":not promoted,"synthetic_status_named":"physical_raw_status" in rejection_reasons,"missing_authority_named":"all_authorities_bound" in rejection_reasons,"receipt_identity_preserved":gates["receipt_passed"]}
 out={"schema":"marici.aspect.physical-promotion-spacelike-gate-result.v1","passed":all(checks.values()),"checks":checks,"promoted":promoted,"gates":gates,"rejection_reasons":rejection_reasons,"geometry_fixture_margins_m":margins,"timelike_hostile_margin_m":hostile_margin,"verdict":"synthetic_packet_correctly_refused_physical_promotion","physical_status":"not_run"}
 RESULT.write_text(json.dumps(out,indent=2)+"\n",encoding="utf-8");print(json.dumps(out,sort_keys=True));raise SystemExit(0 if out["passed"] else 1)
if __name__=="__main__":main()
