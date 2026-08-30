"""Simulate capability attestation and reconcile signed execution receipts."""
import hashlib, hmac, importlib.util, json, sys
from pathlib import Path

def canonical(value):
    return json.dumps(value,sort_keys=True,separators=(",",":")).encode()

def signature(key,value):
    return hmac.new(key.encode(),canonical(value),hashlib.sha256).hexdigest()

def load_plan(root):
    spec=importlib.util.spec_from_file_location("routes",root/"research/aspect/tools/coherent_control_route_compiler.py")
    mod=importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)
    contract=json.loads((root/"research/aspect/contracts/coherent-control-route-compiler.v1.json").read_text(encoding="utf-8"))
    return mod.compile_route(contract,{"id":"receipt-source-plan","fault":None})

def make_fixture(contract,fixture,root):
    plan=load_plan(root); inventory={k:{"device_id":k,"firmware":v,"capability_attested":True} for k,v in contract["required_firmware"].items()}
    planned=[x for x in plan["operations"] if x["op"]=="acquire"]; receipts=[]
    for index,op in enumerate(planned):
        body={"operation_id":f"op-{index:03d}","channel":op["channel"],"tick":op["tick"],
              "source":op["source"],"actuator":op["actuator"],"observer":op["observer"],
              "status":"executed","nonce":f"nonce-{index:03d}"}
        receipts.append({"body":body,"signature":signature(contract["fixture_hmac_key"],body)})
    fault=fixture["fault"]
    if fault=="device_substitution":
        receipts[0]["body"]["observer"]="heterodyne-unknown"
    elif fault=="receipt_replay":
        receipts[1]=json.loads(json.dumps(receipts[0]))
    elif fault=="receipt_omission":
        receipts.pop()
    elif fault=="firmware_drift":
        inventory["heterodyne-1"]["firmware"]="4.0.2"
    elif fault=="signature_tamper":
        receipts[0]["body"]["tick"]+=1
    return plan,inventory,receipts

def audit(contract,fixture,root):
    plan,inventory,receipts=make_fixture(contract,fixture,root)
    planned=[x for x in plan["operations"] if x["op"]=="acquire"]
    capability=all(k in inventory and inventory[k]["capability_attested"] and
                   inventory[k]["firmware"]==v for k,v in contract["required_firmware"].items())
    signed=all(hmac.compare_digest(x["signature"],signature(contract["fixture_hmac_key"],x["body"])) for x in receipts)
    unique=len({x["body"]["operation_id"] for x in receipts})==len(receipts) and len({x["body"]["nonce"] for x in receipts})==len(receipts)
    complete=len(receipts)==len(planned)
    correspondence=complete and all(
        r["body"]["channel"]==p["channel"] and r["body"]["tick"]==p["tick"] and
        r["body"]["source"]==p["source"] and r["body"]["actuator"]==p["actuator"] and
        r["body"]["observer"]==p["observer"] and r["body"]["status"]=="executed"
        for p,r in zip(planned,receipts))
    gates={"capability_attested":capability,"signatures_valid":signed,
           "receipts_unique":unique,"receipt_set_complete":complete,
           "plan_receipt_correspondence":correspondence}
    admitted=all(gates.values())
    return {"id":fixture["id"],"inventory":inventory,"receipt_count":len(receipts),
            "gates":gates,"admitted":admitted,"expected_admit":fixture["expect_admit"],
            "expectation_met":admitted==fixture["expect_admit"]}

def run(contract,root):
    fixtures=[audit(contract,f,root) for f in contract["fixtures"]]
    return {"schema":"marici.aspect.apparatus-capability-receipt-gate-result.v1",
            "fixtures":fixtures,"all_expectations_met":all(x["expectation_met"] for x in fixtures),
            "live_hardware_executed":False,"signature_authority":"fixture_only"}

def main(argv):
    if len(argv)!=3:
        print("usage: apparatus_capability_receipt_gate.py CONTRACT RESULT",file=sys.stderr); return 2
    root=Path(__file__).resolve().parents[3]; c=json.loads(Path(argv[1]).read_text(encoding="utf-8")); r=run(c,root)
    Path(argv[2]).write_text(json.dumps(r,indent=2)+"\n",encoding="utf-8")
    print(json.dumps(r,indent=2)); return 0 if r["all_expectations_met"] else 1
if __name__=="__main__": raise SystemExit(main(sys.argv))
