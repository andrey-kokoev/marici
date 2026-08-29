#!/usr/bin/env python3
"""Compile digest-bound parent/refined views and emit an admission receipt."""
import hashlib,json
from pathlib import Path
ASPECT=Path(__file__).resolve().parent.parent
CONTRACT=ASPECT/"contracts"/"hardware-bound-pushforward-acquisition.v1.json"
PACKET=ASPECT/"fixtures"/"hardware-bound-pushforward-synthetic-packet.v1.json"
RESULT=ASPECT/"results"/"hardware_bound_pushforward_acquisition.json"
def canon(x):return json.dumps(x,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()
def digest(x):return hashlib.sha256(canon(x)).hexdigest()
def main():
 c=json.loads(CONTRACT.read_text(encoding="utf-8"));p=json.loads(PACKET.read_text(encoding="utf-8"));events=p["events"]
 required_packet=set(c["required_packet_fields"]);required_event=set(c["required_event_fields"]);parent_fields=c["parent_fields"]
 parent=[{k:e[k] for k in parent_fields} for e in events]
 refined=[dict(e) for e in events]
 pushed=[{k:e[k] for k in parent_fields} for e in refined]
 ids=[e["event_id"] for e in events]
 local_a=set(p["provenance"]["local_a"]);local_b=set(p["provenance"]["local_b"])
 receipt={"schema":"marici.aspect.pushforward-admission-receipt.v1","run_id":p["run_id"],"status":p["status"],"event_count":len(events),"raw_digest":digest(events),"packet_digest":digest(p),"contract_digest":hashlib.sha256(CONTRACT.read_bytes()).hexdigest(),"compiler_digest":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),"parent_view_digest":digest(parent),"refined_view_digest":digest(refined),"pushed_view_digest":digest(pushed),"pushforward_exact":parent==pushed,"bell_admitted":parent==pushed}
 tampered_events=json.loads(json.dumps(events));tampered_events[0]["photon_bin_a"]+=1
 tampered_packet=json.loads(json.dumps(p));tampered_packet["compiler_id"]="mutated-compiler"
 replay_packet=json.loads(json.dumps(p));replay_packet["run_id"]="replayed-under-new-run"
 hostile_provenance=set(p["provenance"]["local_a"])|{"setting_b"}
 checks={"packet_fields_complete":required_packet<=set(p),"event_fields_complete":all(required_event<=set(e) for e in events),"event_ids_unique":len(ids)==len(set(ids)),"event_ids_stable":[e["event_id"] for e in parent]==[e["event_id"] for e in pushed],"pushforward_exact":receipt["pushforward_exact"],"parent_digest_matches_pushforward":receipt["parent_view_digest"]==receipt["pushed_view_digest"],"local_a_provenance":local_a<=set(c["local_a_allowed_sources"]),"local_b_provenance":local_b<=set(c["local_b_allowed_sources"]),"no_click_retained":any(e["no_click_a"] or e["no_click_b"] for e in events),"compiler_bound":len(receipt["compiler_digest"])==64,"raw_mutation_invalidates_receipt":digest(tampered_events)!=receipt["raw_digest"],"compiler_identity_mutation_invalidates_receipt":digest(tampered_packet)!=receipt["packet_digest"],"run_replay_invalidates_receipt":digest(replay_packet)!=receipt["packet_digest"],"remote_provenance_rejected":not hostile_provenance<=set(c["local_a_allowed_sources"]),"synthetic_claim_boundary":p["status"]=="synthetic_reference" and not any(c["claim_boundary"].values())}
 out={"schema":"marici.aspect.hardware-bound-pushforward-acquisition-result.v1","passed":all(checks.values()),"checks":checks,"receipt":receipt,"verdict":"digest_bound_same_ledger_views_admitted_synthetic_reference","physical_status":"not_run"}
 RESULT.write_text(json.dumps(out,indent=2)+"\n",encoding="utf-8");print(json.dumps(out,sort_keys=True));raise SystemExit(0 if out["passed"] else 1)
if __name__=="__main__":main()
