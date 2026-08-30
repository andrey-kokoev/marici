"""Simulation-only reference MCP adapter. Dispatch is structurally refused."""
import hashlib, json, sys

INVENTORY={
 "laser-A":{"firmware":"1.4.2","capabilities":["continuous_source"]},
 "pulse-A":{"firmware":"2.1.0","capabilities":["pulsed_source"]},
 "mesh-pair-port":{"firmware":"3.2.1","capabilities":["complex_coupling"]},
 "phase-twist-eom":{"firmware":"1.9.0","capabilities":["phase_twist"]},
 "loop-flux-eom":{"firmware":"1.9.0","capabilities":["synthetic_flux"]},
 "heterodyne-1":{"firmware":"4.0.3","capabilities":["complex_spectrum"]},
 "homodyne-1":{"firmware":"4.0.3","capabilities":["quadrature"]},
 "balanced-homodyne":{"firmware":"4.0.3","capabilities":["differential_quadrature"]},
 "fast-detector":{"firmware":"2.8.4","capabilities":["transient_readout"]}
}

def digest(value):
    return hashlib.sha256(json.dumps(value,sort_keys=True,separators=(",",":")).encode()).hexdigest()

def capability_read(_):
    return {"mode":"simulation_only","inventory":INVENTORY,"inventory_digest":digest(INVENTORY),
            "attestation":{"kind":"fixture","hardware_backed":False}}

def route_dry_run(args):
    expected=args.get("expected_inventory_digest"); plan=args.get("route_plan",{})
    current=digest(INVENTORY); resolved=[]; errors=[]
    if expected!=current: errors.append("inventory_digest_mismatch")
    for op in plan.get("operations",[]):
        if op.get("op")!="acquire": continue
        devices=[op.get("source"),op.get("actuator"),op.get("observer")]
        missing=[x for x in devices if x not in INVENTORY]
        if missing: errors.append({"operation":op.get("channel"),"missing_devices":missing})
        else: resolved.append({"channel":op["channel"],"tick":op["tick"],"devices":devices})
    return {"admitted":not errors,"resolved_routes":resolved,"inventory_digest":current,
            "errors":errors,"dry_run_ref":"sim-dry-"+digest({"plan":plan,"inventory":current})[:20]}

def route_dispatch(_):
    return {"status":"refused","reason":"simulation_only_adapter_has_no_dispatch_authority","execution_ref":None}

def receipts_read(_):
    return {"device_receipts":[],"completion_state":"no_live_execution"}

TOOLS={"apparatus_capability_read":capability_read,"apparatus_route_dry_run":route_dry_run,
       "apparatus_route_dispatch":route_dispatch,"apparatus_receipts_read":receipts_read}

def tool_contracts():
    return [{"name":name,"description":"Reference optical apparatus adapter tool.",
             "inputSchema":{"type":"object","additionalProperties":True}} for name in TOOLS]

def handle(request):
    method=request.get("method"); rid=request.get("id")
    if method=="initialize":
        result={"protocolVersion":"2025-06-18","capabilities":{"tools":{}},
                "serverInfo":{"name":"reference-optical-apparatus","version":"0.1.0"}}
    elif method=="tools/list": result={"tools":tool_contracts()}
    elif method=="tools/call":
        params=request.get("params",{}); name=params.get("name")
        if name not in TOOLS: return {"jsonrpc":"2.0","id":rid,"error":{"code":-32601,"message":"tool not found"}}
        value=TOOLS[name](params.get("arguments",{}))
        result={"content":[{"type":"text","text":json.dumps(value)}],"structuredContent":value}
    else: return {"jsonrpc":"2.0","id":rid,"error":{"code":-32601,"message":"method not found"}}
    return {"jsonrpc":"2.0","id":rid,"result":result}

def main():
    for line in sys.stdin:
        try: response=handle(json.loads(line))
        except Exception as exc: response={"jsonrpc":"2.0","id":None,"error":{"code":-32603,"message":str(exc)}}
        print(json.dumps(response),flush=True)
if __name__=="__main__": main()
