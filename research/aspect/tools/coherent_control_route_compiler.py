"""Compile typed coherent-control routes and audit their schedule."""
import json, sys
from pathlib import Path

def compile_route(contract,fixture):
    operations=[]; tick=0; calibration_tick=0
    operations.append({"op":"dark_calibration","tick":tick,"resource":"detectors","calibration_id":"cal-route-1"}); tick+=5
    operations.append({"op":"reference_calibration","tick":tick,"resource":"laser-A","calibration_id":"cal-route-1"}); tick+=5
    for point_index,x in enumerate(contract["control_coordinates"]):
        cycle_start=tick
        for channel_index,(channel,route) in enumerate(contract["routes"].items()):
            op_tick=cycle_start+channel_index*8
            operations.append({"op":"acquire","channel":channel,"control_coordinate":x,
                               "tick":op_tick,"cycle":point_index,
                               "source":route["source"],"actuator":route["actuator"],
                               "observer":route["observer"],"calibration_id":"cal-route-1"})
        tick=cycle_start+40
    fault=fixture["fault"]
    if fault=="resource_collision":
        operations[3]["tick"]=operations[2]["tick"]
        operations[3]["observer"]=operations[2]["observer"]
    elif fault=="stale_calibration":
        calibration_tick=-1000
    elif fault=="unbound_port":
        operations[4]["observer"]=None
    elif fault=="trigger_skew":
        operations[5]["tick"]=operations[2]["tick"]+100
    return {"route_id":fixture["id"],"clock_hz":contract["clock_hz"],
            "calibration_tick":calibration_tick,"operations":operations}

def audit(contract,fixture):
    packet=compile_route(contract,fixture); acquisitions=[x for x in packet["operations"] if x["op"]=="acquire"]
    typed=all(x.get("source") and x.get("actuator") and x.get("observer") for x in acquisitions)
    calibrations={x["calibration_id"] for x in acquisitions}
    lineage=len(calibrations)==1 and all(x["calibration_id"]=="cal-route-1" for x in acquisitions)
    collision_free=True
    seen=set()
    for x in acquisitions:
        key=(x["tick"],x["observer"])
        if key in seen: collision_free=False
        seen.add(key)
    fresh=all(x["tick"]-packet["calibration_tick"]<=contract["maximum_calibration_age_ticks"]+
              x["cycle"]*40 for x in acquisitions)
    skew=True
    for cycle in range(len(contract["control_coordinates"])):
        ticks=[x["tick"] for x in acquisitions if x["cycle"]==cycle]
        if max(ticks)-min(ticks)>contract["maximum_channel_skew_ticks"]: skew=False
    complete=all(len([x for x in acquisitions if x["cycle"]==c])==len(contract["routes"]) for c in range(len(contract["control_coordinates"])))
    gates={"ports_typed":typed,"calibration_lineage":lineage,"resource_collision_free":collision_free,
           "calibration_fresh":fresh,"channel_skew_bounded":skew,"cycle_complete":complete}
    admitted=all(gates.values())
    return {"id":fixture["id"],"compiled_packet":packet,"gates":gates,"admitted":admitted,
            "expected_admit":fixture["expect_admit"],"expectation_met":admitted==fixture["expect_admit"]}

def run(contract):
    fixtures=[audit(contract,f) for f in contract["fixtures"]]
    return {"schema":"marici.aspect.coherent-control-route-compiler-result.v1",
            "fixtures":fixtures,"all_expectations_met":all(x["expectation_met"] for x in fixtures),
            "hardware_commands_dispatched":False}

def main(argv):
    if len(argv)!=3:
        print("usage: coherent_control_route_compiler.py CONTRACT RESULT",file=sys.stderr); return 2
    c=json.loads(Path(argv[1]).read_text(encoding="utf-8")); r=run(c)
    Path(argv[2]).write_text(json.dumps(r,indent=2)+"\n",encoding="utf-8")
    print(json.dumps(r,indent=2)); return 0 if r["all_expectations_met"] else 1
if __name__=="__main__": raise SystemExit(main(sys.argv))
