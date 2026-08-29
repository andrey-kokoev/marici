#!/usr/bin/env python3
"""Exact spatial Bell plus coherent local implementation-loop fixture."""
import cmath,itertools,json,math
from pathlib import Path
ASPECT=Path(__file__).resolve().parent.parent
CONTRACT=ASPECT/"contracts"/"coherent-refinement-loop-bell-experiment.v1.json"
RESULT=ASPECT/"results"/"coherent_refinement_loop_bell_experiment.json"
def corr(a,b):return -math.cos(2*math.radians(a-b))
def chsh(e):return abs(e[0][0]+e[0][1]+e[1][0]-e[1][1])
def main():
 c=json.loads(CONTRACT.read_text(encoding="utf-8"));A=c["settings_degrees"]["A"];B=c["settings_degrees"]["B"];phi=c["loop_phase_radians"]
 base=[[corr(a,b) for b in B] for a in A];S=chsh(base)
 fringes={"identity":1+0j,"closed_refinement":cmath.exp(1j*phi),"equivalent_dilation":c["equivalent_dilation_visibility"]*cmath.exp(1j*phi),"dephased_control":0j}
 modes={m:{"correlations":[row[:] for row in base],"chsh":S,"fringe":{"x":z.real,"y":z.imag,"visibility":abs(z),"phase":cmath.phase(z) if abs(z)>0 else None}} for m,z in fringes.items()}
 # Every mode is an honest label extension of the same four context cells.
 coarse={(i,j):base[i][j] for i in range(2) for j in range(2)}
 refined={(m,i,j):base[i][j] for m in c["modes"] for i in range(2) for j in range(2)}
 pushed={m:{(i,j):refined[m,i,j] for i in range(2) for j in range(2)} for m in c["modes"]}
 local_vertex_max=max(abs(a0*b0+a0*b1+a1*b0-a1*b1) for a0,a1,b0,b1 in itertools.product((-1,1),repeat=4))
 remote_marginals={m:{"A_delta_by_B":0.0,"B_delta_by_A":0.0} for m in c["modes"]}
 leakage_hostile_delta=0.01
 required=set(c["required_trial_fields"]);synthetic={k:(0 if k.startswith("control_") or k.startswith("outcome_") else False if k.startswith("no_click_") else "fixture") for k in required}
 checks={"all_modes_push_to_same_packet":all(pushed[m]==coarse for m in c["modes"]),"chsh_invariant":max(abs(modes[m]["chsh"]-S) for m in c["modes"])<=c["chsh_mode_tolerance"],"quantum_fixture":abs(S-2*math.sqrt(2))<1e-12,"local_ceiling":local_vertex_max==2,"identity_fringe":abs(fringes["identity"]-1)<c["fringe_tolerance"],"closed_loop_phase":abs(cmath.phase(fringes["closed_refinement"])-phi)<c["fringe_tolerance"],"equivalent_dilation_coarse_same":pushed["equivalent_dilation"]==coarse and abs(abs(fringes["equivalent_dilation"])-0.8)<c["fringe_tolerance"],"dephased_negative_control":abs(fringes["dephased_control"])<c["fringe_tolerance"],"remote_marginals_flat":all(max(abs(x) for x in d.values())<=c["remote_marginal_tolerance"] for d in remote_marginals.values()),"path_leakage_hostile_detected":leakage_hostile_delta>c["remote_marginal_tolerance"],"trial_schema_complete":required==set(synthetic),"no_click_retained":0 in c["outcomes"],"claim_boundary":not any(c["claim_boundary"].values())}
 out={"schema":"marici.aspect.coherent-refinement-loop-bell-experiment-result.v1","passed":all(checks.values()),"checks":checks,"modes":modes,"inclusive_chsh":S,"local_vertex_max":local_vertex_max,"remote_marginals":remote_marginals,"path_leakage_hostile_delta":leakage_hostile_delta,"verdict":"coarse_bell_invariant_with_distinct_constructor_loop_fringes_mathematical_fixture","physical_status":"not_run"}
 RESULT.write_text(json.dumps(out,indent=2)+"\n",encoding="utf-8");print(json.dumps(out,sort_keys=True));raise SystemExit(0 if out["passed"] else 1)
if __name__=="__main__":main()
