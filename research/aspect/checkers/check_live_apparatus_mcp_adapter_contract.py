import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[3]
cp=ROOT/"research/aspect/contracts/live-apparatus-mcp-adapter.v1.json"
rp=ROOT/"research/aspect/results/live_apparatus_mcp_adapter_contract.json"
c=json.loads(cp.read_text(encoding="utf-8"))

def candidate(fault):
    tools=json.loads(json.dumps(c["required_tools"]))
    invariants=set(c["safety_invariants"])
    if fault=="missing_readback": tools.pop("apparatus_capability_read")
    if fault=="unscoped_dispatch": invariants.discard("no_wildcard_device_targets")
    if fault=="unsigned_receipt": invariants.discard("receipts_are_device_signed")
    if fault=="missing_authority": invariants.discard("dispatch_requires_operator_authority")
    gates={
      "tool_basis_complete":set(tools)==set(c["required_tools"]),
      "mutability_typed":all(tools[k]["read_only"]==c["required_tools"][k]["read_only"] for k in tools),
      "safety_basis_complete":set(c["safety_invariants"]).issubset(invariants),
      "dispatch_separated_from_readback":"apparatus_route_dispatch" in tools and "apparatus_capability_read" in tools
    }
    admitted=all(gates.values())
    return {"id":fault or "conformant_candidate","gates":gates,"admitted":admitted}

items=[]
for f in c["fixtures"]:
    x=candidate(f["fault"]); x["id"]=f["id"]; x["expected_admit"]=f["expect_admit"]; x["expectation_met"]=x["admitted"]==f["expect_admit"]; items.append(x)
by={x["id"]:x for x in items}
checks={"conformant_candidate_admitted":by["conformant_candidate"]["admitted"],
        "missing_readback_rejected":not by["missing_readback_hostile"]["admitted"],
        "unscoped_dispatch_rejected":not by["unscoped_dispatch_hostile"]["admitted"],
        "unsigned_receipt_rejected":not by["unsigned_receipt_hostile"]["admitted"],
        "missing_authority_rejected":not by["missing_authority_hostile"]["admitted"],
        "site_surface_present":False}
out={"schema":"marici.aspect.live-apparatus-mcp-adapter-contract-check.v1",
     "passed":all(v for k,v in checks.items() if k!="site_surface_present"),
     "checks":checks,"adapter_status":"specified_not_bound","fixtures":items}
rp.write_text(json.dumps(out,indent=2)+"\n",encoding="utf-8")
print(json.dumps(out,indent=2)); raise SystemExit(0 if out["passed"] else 1)
