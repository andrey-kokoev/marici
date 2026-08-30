import importlib.util, json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[3]
cp=ROOT/"research/aspect/contracts/apparatus-capability-receipt-gate.v1.json"
rp=ROOT/"research/aspect/results/apparatus_capability_receipt_gate.json"
spec=importlib.util.spec_from_file_location("gate",ROOT/"research/aspect/tools/apparatus_capability_receipt_gate.py")
mod=importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)
c=json.loads(cp.read_text(encoding="utf-8")); r=mod.run(c,ROOT); by={x["id"]:x for x in r["fixtures"]}
checks={
 "attested_candidate_admitted":by["attested_candidate"]["admitted"],
 "device_substitution_rejected":not by["device_substitution_hostile"]["admitted"],
 "receipt_replay_rejected":not by["receipt_replay_hostile"]["admitted"],
 "receipt_omission_rejected":not by["receipt_omission_hostile"]["admitted"],
 "firmware_drift_rejected":not by["firmware_drift_hostile"]["admitted"],
 "signature_tamper_rejected":not by["signature_tamper_hostile"]["admitted"],
 "all_24_receipts_required":by["attested_candidate"]["receipt_count"]==24,
 "fixture_signature_not_hardware_authority":r["signature_authority"]=="fixture_only",
 "live_execution_not_fabricated":not r["live_hardware_executed"]
}
out={"schema":"marici.aspect.apparatus-capability-receipt-gate-check.v1","passed":all(checks.values()),"checks":checks,"result":r}
rp.write_text(json.dumps(out,indent=2)+"\n",encoding="utf-8")
print(json.dumps(out,indent=2)); raise SystemExit(0 if out["passed"] else 1)
