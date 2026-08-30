import importlib.util, json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
rp=ROOT/"research/aspect/results/reference_optical_apparatus_mcp.json"
spec=importlib.util.spec_from_file_location("adapter",ROOT/"research/aspect/tools/reference_optical_apparatus_mcp.py")
m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
init=m.handle({"jsonrpc":"2.0","id":1,"method":"initialize","params":{}})
listed=m.handle({"jsonrpc":"2.0","id":2,"method":"tools/list","params":{}}); cap=m.capability_read({})
plan={"operations":[{"op":"acquire","channel":"gap","tick":10,"source":"laser-A","actuator":"mesh-pair-port","observer":"heterodyne-1"}]}
dry=m.route_dry_run({"route_plan":plan,"expected_inventory_digest":cap["inventory_digest"]})
stale=m.route_dry_run({"route_plan":plan,"expected_inventory_digest":"stale"})
missing=m.route_dry_run({"route_plan":{"operations":[dict(plan["operations"][0],observer="unknown")]},"expected_inventory_digest":cap["inventory_digest"]})
dispatch=m.route_dispatch({"dry_run_ref":dry["dry_run_ref"],"operator_authority_ref":"fixture"})
checks={"mcp_initializes":init["result"]["serverInfo"]["name"]=="reference-optical-apparatus",
 "four_tools_exposed":len(listed["result"]["tools"])==4,
 "capability_is_explicitly_fixture":not cap["attestation"]["hardware_backed"],
 "valid_dry_run_admitted":dry["admitted"],"stale_inventory_rejected":not stale["admitted"],
 "unknown_device_rejected":not missing["admitted"],
 "dispatch_structurally_refused":dispatch["status"]=="refused" and dispatch["execution_ref"] is None,
 "receipts_empty":m.receipts_read({})["completion_state"]=="no_live_execution"}
out={"schema":"marici.aspect.reference-optical-apparatus-mcp-check.v1","passed":all(checks.values()),"checks":checks}
rp.write_text(json.dumps(out,indent=2)+"\n",encoding="utf-8")
print(json.dumps(out,indent=2)); raise SystemExit(0 if out["passed"] else 1)
