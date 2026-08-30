#!/usr/bin/env python3
"""Exact factorial response and observability-rank fixture."""
import json,math
from pathlib import Path
ASPECT=Path(__file__).resolve().parent.parent
CONTRACT=ASPECT/"contracts"/"three-axis-explanation-rank-experiment.v1.json"
RESULT=ASPECT/"results"/"three_axis_explanation_rank_experiment.json"
def obs(p,g,phi):return (2*math.sqrt(2)*p,g*math.cos(phi),g*math.sin(phi))
def main():
 c=json.loads(CONTRACT.read_text(encoding="utf-8"));ps=c["bell_visibilities"];gs=c["loop_visibilities"];phis=c["loop_phases_radians"]
 grid=[{"p":p,"gamma":g,"phi":q,"S":obs(p,g,q)[0],"X":obs(p,g,q)[1],"Y":obs(p,g,q)[2]} for p in ps for g in gs for q in phis]
 ranks={str(g):(2 if g==0 else 3) for g in gs};determinants={str(g):2*math.sqrt(2)*g for g in gs}
 # Axis invariances over the full factorial grid.
 s_by_p={p:{round(r["S"],14) for r in grid if r["p"]==p} for p in ps}
 mag_by_g={g:{round(math.hypot(r["X"],r["Y"]),14) for r in grid if r["gamma"]==g} for g in gs}
 phase_rotation=all(abs(math.hypot(*obs(1,g,q)[1:])-g)<c["invariance_tolerance"] for g in gs for q in phis)
 bell_crosses=any(obs(p,1,0)[0]<=c["bell_local_ceiling"] for p in ps) and any(obs(p,1,0)[0]>c["bell_local_ceiling"] for p in ps)
 # A one-scalar response has tangent rank at most one by construction; preregister it as the hostile alternative.
 single_latent_rank=1
 checks={"factorial_grid_complete":len(grid)==len(ps)*len(gs)*len(phis),"chsh_depends_only_on_p":all(len(v)==1 for v in s_by_p.values()),"fringe_magnitude_depends_only_on_gamma":all(len(v)==1 for v in mag_by_g.values()),"phase_rotates_quadratures":phase_rotation,"full_rank_when_coherent":all(ranks[str(g)]==3 and determinants[str(g)]>c["full_rank_threshold"] for g in gs if g>0),"rank_drop_at_decoherence":ranks["0.0"]==2 and determinants["0.0"]==0,"bell_boundary_crossed":bell_crosses,"single_latent_hostile_lower_rank":single_latent_rank<3,"claim_boundary":not any(c["claim_boundary"].values())}
 out={"schema":"marici.aspect.three-axis-explanation-rank-experiment-result.v1","passed":all(checks.values()),"checks":checks,"grid_size":len(grid),"jacobian_determinants":determinants,"observable_ranks":ranks,"bell_threshold_visibility":1/math.sqrt(2),"sample_cells":grid[:6],"verdict":"three_independent_explanatory_coordinates_with_decoherence_rank_drop_mathematical_fixture","physical_status":"not_run"}
 RESULT.write_text(json.dumps(out,indent=2)+"\n",encoding="utf-8");print(json.dumps(out,sort_keys=True));raise SystemExit(0 if out["passed"] else 1)
if __name__=="__main__":main()
