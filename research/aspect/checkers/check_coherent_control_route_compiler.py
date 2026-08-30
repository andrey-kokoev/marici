import importlib.util, json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[3]
cp=ROOT/"research/aspect/contracts/coherent-control-route-compiler.v1.json"
rp=ROOT/"research/aspect/results/coherent_control_route_compiler.json"
spec=importlib.util.spec_from_file_location("routes",ROOT/"research/aspect/tools/coherent_control_route_compiler.py")
mod=importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)
c=json.loads(cp.read_text(encoding="utf-8")); r=mod.run(c); by={x["id"]:x for x in r["fixtures"]}
checks={
 "valid_route_admitted":by["valid_route"]["admitted"],
 "resource_collision_rejected":not by["resource_collision_hostile"]["admitted"],
 "stale_calibration_rejected":not by["stale_calibration_hostile"]["admitted"],
 "unbound_port_rejected":not by["unbound_port_hostile"]["admitted"],
 "trigger_skew_rejected":not by["trigger_skew_hostile"]["admitted"],
 "all_coordinates_compile":len([x for x in by["valid_route"]["compiled_packet"]["operations"] if x["op"]=="acquire"])==24,
 "hardware_dispatch_not_fabricated":not r["hardware_commands_dispatched"]
}
out={"schema":"marici.aspect.coherent-control-route-compiler-check.v1","passed":all(checks.values()),"checks":checks,"result":r}
rp.write_text(json.dumps(out,indent=2)+"\n",encoding="utf-8")
print(json.dumps(out,indent=2)); raise SystemExit(0 if out["passed"] else 1)
