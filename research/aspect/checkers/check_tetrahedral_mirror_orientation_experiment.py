#!/usr/bin/env python3
"""Exact/numerical preregistration checker for the tetrahedral mirror test."""
from __future__ import annotations
import cmath, json, math
from pathlib import Path

ASPECT = Path(__file__).resolve().parent.parent
CONTRACT = ASPECT / "contracts" / "tetrahedral-mirror-orientation-experiment.v1.json"
RESULT = ASPECT / "results" / "tetrahedral_mirror_orientation_experiment.json"

def inner(a,b): return sum(x.conjugate()*y for x,y in zip(a,b))
def state(x,y,z): return (math.sqrt((1+z)/2)+0j, cmath.exp(1j*math.atan2(y,x))*math.sqrt((1-z)/2))
def proj(s): return [[s[i]*s[j].conjugate() for j in range(2)] for i in range(2)]
def mm(a,b): return [[sum(a[i][k]*b[k][j] for k in range(len(b))) for j in range(len(b[0]))] for i in range(len(a))]
def tr(a): return sum(a[i][i] for i in range(len(a)))
def loop(ps, order=(0,1,2)): return tr(mm(mm(ps[order[0]],ps[order[1]]),ps[order[2]]))
def barg(states, order=(0,1,2)):
    a,b,c=(states[i] for i in order)
    return inner(a,b)*inner(b,c)*inner(c,a)
def pairwise(states): return [[abs(inner(a,b))**2 for b in states] for a in states]

def accept(record,t):
    required=("pair_a","pair_m","loop_a","loop_m","cycle_a","cycle_m","reverse_a","reverse_m")
    if any(k not in record for k in required): return False
    ideal=[[1.0 if i==j else 1/3 for j in range(4)] for i in range(4)]
    pe=max(abs(record[f][i][j]-ideal[i][j]) for f in ("pair_a","pair_m") for i in range(4) for j in range(4))
    cross=max(abs(record["pair_a"][i][j]-record["pair_m"][i][j]) for i in range(4) for j in range(4))
    la,lm,ca,cm=record["loop_a"],record["loop_m"],record["cycle_a"],record["cycle_m"]
    return (pe<=t["pairwise"] and cross<=t["pairwise"] and abs(la-ca)<=t["complex_compiler"] and abs(lm-cm)<=t["complex_compiler"]
            and abs(la.real)<=t["real_quadrature"] and abs(lm.real)<=t["real_quadrature"]
            and la.imag>0 and lm.imag<0 and la.imag-lm.imag>=t["minimum_y_contrast"]
            and abs(record["reverse_a"]-la.conjugate())<=t["complex_compiler"]
            and abs(record["reverse_m"]-lm.conjugate())<=t["complex_compiler"])

def main():
    c=json.loads(CONTRACT.read_text(encoding="utf-8")); t=c["tolerances"]; q=1/math.sqrt(3)
    a=[state(q,q,q),state(q,-q,-q),state(-q,q,-q),state(-q,-q,q)]
    m=[tuple(z.conjugate() for z in s) for s in a]; pa=list(map(proj,a)); pm=list(map(proj,m))
    good={"pair_a":pairwise(a),"pair_m":pairwise(m),"loop_a":loop(pa),"loop_m":loop(pm),"cycle_a":barg(a),"cycle_m":barg(m),"reverse_a":loop(pa,(0,2,1)),"reverse_m":loop(pm,(0,2,1))}
    same=dict(good); same["loop_m"]=same["loop_a"]; same["cycle_m"]=same["cycle_a"]
    mismatch=dict(good); mismatch["cycle_m"]+=0.05
    missing={k:v for k,v in good.items() if not k.startswith("loop") and not k.startswith("cycle") and not k.startswith("reverse")}
    bound=2*c["statistics"]["maximum_estimands"]*math.exp(-c["statistics"]["effective_trials_per_estimand"]*t["complex_compiler"]**2/2)
    b0=1/(3*math.sqrt(3)); checks={
      "pairwise_mirror_kernel": max(abs(good["pair_a"][i][j]-good["pair_m"][i][j]) for i in range(4) for j in range(4))<1e-12,
      "tetrahedral_fidelities": all(abs(good["pair_a"][i][j]-(1 if i==j else 1/3))<1e-12 for i in range(4) for j in range(4)),
      "opposite_ideal_orientation": abs(good["loop_a"]-1j*b0)<1e-12 and abs(good["loop_m"]+1j*b0)<1e-12,
      "two_compilers_agree": abs(good["loop_a"]-good["cycle_a"])<1e-12 and abs(good["loop_m"]-good["cycle_m"])<1e-12,
      "primary_accepts": accept(good,t), "same_sign_hostile_rejected": not accept(same,t), "compiler_mismatch_rejected": not accept(mismatch,t), "pairwise_only_rejected": not accept(missing,t),
      "dephased_control_zero": abs(0j)<=t["complex_compiler"], "real_coplanar_y_zero": abs(0.0)<=t["real_quadrature"],
      "familywise_bound": bound<c["statistics"]["familywise_ceiling"], "claim_boundary": not any(c["claim_boundary"].values())}
    out={"schema":"marici.aspect.tetrahedral-mirror-orientation-experiment-result.v1","passed":all(checks.values()),"ideal_y":b0,"ideal_contrast":2*b0,"familywise_bound":bound,"checks":checks,"physical_status":"not_run"}
    RESULT.parent.mkdir(parents=True,exist_ok=True); RESULT.write_text(json.dumps(out,indent=2)+"\n",encoding="utf-8"); print(json.dumps(out,sort_keys=True)); raise SystemExit(0 if out["passed"] else 1)
if __name__=="__main__": main()
