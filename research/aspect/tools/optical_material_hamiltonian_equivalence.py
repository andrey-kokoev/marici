"""Shared-transport comparison across four reduced observable families."""
import json, math, sys
from pathlib import Path

def observable(channel, x):
    x=min(x,0.999)
    if channel=="gap": return math.sqrt(1.0-x*x)
    if channel=="stiffness": return 1.0-x*x
    if channel=="screening": return (1.0-x*x)/(1.0+0.4*x*x)
    if channel=="relaxation": return 0.15+0.6*x*x
    raise ValueError(channel)

def rmse(a,b):
    return math.sqrt(sum((x-y)**2 for x,y in zip(a,b))/len(a))

def scale_grid(cfg):
    lo=cfg["minimum"]; hi=cfg["maximum"]; step=cfg["step"]
    return [round(lo+i*step,10) for i in range(round((hi-lo)/step)+1)]

def run_fixture(contract, fixture):
    xs=contract["reduced_coordinates"]; channels=contract["channels"]
    target={c:[observable(c,x) for x in xs] for c in channels}
    measured={c:[observable(c,fixture["channel_scales"][c]*x) for x in xs] for c in channels}
    grid=scale_grid(contract["scale_search"]); independent={}; independent_errors={}
    for c in channels:
        scores=[(rmse([observable(c,s*x) for x in xs],measured[c]),s) for s in grid]
        independent_errors[c],independent[c]=min(scores)
    shared_scores=[]
    for s in grid:
        errors=[rmse([observable(c,s*x) for x in xs],measured[c]) for c in channels]
        shared_scores.append((math.sqrt(sum(e*e for e in errors)/len(errors)),s,errors))
    shared_error,shared_scale,channel_errors=min(shared_scores)
    spread=max(independent.values())-min(independent.values())
    t=contract["preregistered_thresholds"]
    gates={"each_channel_identifiable":max(independent_errors.values())<=t["independent_fit_rmse_max"],
           "one_shared_transport":shared_error<=t["shared_fit_rmse_max"],
           "transport_coherence":spread<=t["transport_spread_max"]}
    return {"id":fixture["id"],"target_packet":target,"measured_packet":measured,
            "independent_best_scales":independent,"independent_fit_rmse":independent_errors,
            "shared_best_scale":shared_scale,"shared_fit_rmse":shared_error,
            "shared_channel_rmse":dict(zip(channels,channel_errors)),
            "transport_spread":spread,"gates":gates,"admitted":all(gates.values()),
            "expected_admit":fixture["expect_admit"],"expectation_met":all(gates.values())==fixture["expect_admit"]}

def run(contract):
    fixtures=[run_fixture(contract,f) for f in contract["fixtures"]]
    return {"schema":"marici.aspect.optical-material-hamiltonian-equivalence-result.v1",
            "claim_boundary":contract["claim_boundary"],"fixtures":fixtures,
            "all_expectations_met":all(x["expectation_met"] for x in fixtures),
            "material_superconductivity_established":False}

def main(argv):
    if len(argv)!=3:
        print("usage: optical_material_hamiltonian_equivalence.py CONTRACT RESULT",file=sys.stderr); return 2
    contract=json.loads(Path(argv[1]).read_text(encoding="utf-8")); result=run(contract)
    Path(argv[2]).write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
    print(json.dumps(result,indent=2)); return 0 if result["all_expectations_met"] else 1
if __name__=="__main__": raise SystemExit(main(sys.argv))
