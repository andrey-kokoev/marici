"""Deterministic TDGL-ring surrogate for the optical pair-stiffness-flux cell."""
import cmath, json, math, random, sys
from pathlib import Path

def wrap(x):
    return (x + math.pi) % (2 * math.pi) - math.pi

def evolve(cfg, fixture, winding, flux, seed_offset):
    n=cfg["nodes"]; d=cfg["dynamics"]; rng=random.Random(d["seed"]+seed_offset)
    alpha=fixture["alpha"]; beta=fixture["beta"]; coupling=fixture["coupling"]; noise=fixture["noise"]
    radius=math.sqrt(max(alpha,0.02)/beta)
    psi=[radius*cmath.exp(2j*math.pi*winding*k/n+0.03j*(rng.random()-.5)) for k in range(n)]
    gauge=flux/n; samples=[]
    for step in range(d["settling_steps"]+d["measurement_steps"]):
        nxt=[]
        for k,z in enumerate(psi):
            lap=cmath.exp(-1j*gauge)*psi[(k+1)%n]+cmath.exp(1j*gauge)*psi[(k-1)%n]-2*z
            drift=(alpha-beta*abs(z)**2)*z+coupling*lap
            kick=noise*math.sqrt(d["dt"])*complex(rng.gauss(0,1),rng.gauss(0,1))
            nxt.append(z+d["dt"]*drift+kick)
        psi=nxt
        if step>=d["settling_steps"]: samples.append(tuple(psi))
    return samples

def summarize(samples, coupling, flux):
    n=len(samples[0]); amps=[]; stiffness=[]; currents=[]; windings=[]; gauge=flux/n
    for state in samples:
        amps.append(sum(abs(z) for z in state)/n)
        bonds=[state[(k+1)%n]*state[k].conjugate()*cmath.exp(-1j*gauge) for k in range(n)]
        stiffness.append(coupling*sum(x.real for x in bonds)/n)
        currents.append(coupling*sum(x.imag for x in bonds)/n)
        phase_sum=sum(wrap(cmath.phase(state[(k+1)%n])-cmath.phase(state[k])) for k in range(n))
        windings.append(abs(phase_sum/(2*math.pi)))
    mean=lambda xs:sum(xs)/len(xs)
    return {"pair_amplitude":mean(amps),"phase_stiffness":mean(stiffness),"circulating_current":mean(currents),"persistent_winding":mean(windings)}

def run_fixture(cfg,f,i):
    ground=summarize(evolve(cfg,f,0,f["flux"],10*i),f["coupling"],f["flux"])
    persistent=summarize(evolve(cfg,f,1,0.0,10*i+1),f["coupling"],0.0)
    flux_per_bond=f["flux"]/cfg["nodes"]
    ground["screening_response"]=-ground["circulating_current"]/flux_per_bond if flux_per_bond else 0.0
    ground["persistent_winding"]=persistent["persistent_winding"]
    t=cfg["preregistered_thresholds"]
    gates={"pair_amplitude":ground["pair_amplitude"]>=t["pair_amplitude_min"],"phase_stiffness":ground["phase_stiffness"]>=t["phase_stiffness_min"],"opposing_flux_response":ground["screening_response"]>=t["screening_response_min"],"persistent_winding":ground["persistent_winding"]>=t["persistent_winding_min"]}
    return {"id":f["id"],"metrics":ground,"gates":gates,"joint_admitted":all(gates.values()),"expected_joint":f["expect_joint"],"expectation_met":all(gates.values())==f["expect_joint"]}

def run(contract):
    fixtures=[run_fixture(contract,f,i) for i,f in enumerate(contract["fixtures"])]
    return {"schema":"marici.aspect.optical-pair-stiffness-flux-result.v1","claim_boundary":contract["claim_boundary"],"fixtures":fixtures,"all_expectations_met":all(x["expectation_met"] for x in fixtures),"room_temperature_claim":False,"missing_kelvin_constructor":contract["temperature_authority"]["required_constructor"]}

def main(argv):
    if len(argv)!=3:
        print("usage: optical_pair_stiffness_flux_cell.py CONTRACT RESULT",file=sys.stderr);return 2
    contract=json.loads(Path(argv[1]).read_text(encoding="utf-8"));result=run(contract)
    Path(argv[2]).write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
    print(json.dumps(result,indent=2));return 0 if result["all_expectations_met"] else 1
if __name__=="__main__":raise SystemExit(main(sys.argv))
