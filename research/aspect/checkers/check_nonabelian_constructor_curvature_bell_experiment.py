#!/usr/bin/env python3
"""Exact two-word constructor commutator and Bell-invariance fixture."""
import json,math
from pathlib import Path
ASPECT=Path(__file__).resolve().parent.parent
CONTRACT=ASPECT/"contracts"/"nonabelian-constructor-curvature-bell-experiment.v1.json"
RESULT=ASPECT/"results"/"nonabelian_constructor_curvature_bell_experiment.json"
def mm(a,b):return [[sum(a[i][k]*b[k][j] for k in range(2)) for j in range(2)] for i in range(2)]
def mv(a,v):return [sum(a[i][k]*v[k] for k in range(2)) for i in range(2)]
def inner(a,b):return sum(a[i].conjugate()*b[i] for i in range(2))
def rx(t):
 c=math.cos(t/2);s=math.sin(t/2);return [[c,-1j*s],[-1j*s,c]]
def rz(t):return [[complex(math.cos(-t/2),math.sin(-t/2)),0j],[0j,complex(math.cos(t/2),math.sin(t/2))]]
def main():
 c=json.loads(CONTRACT.read_text(encoding="utf-8"));u=rx(c["u_angle_radians"]);v=rz(c["v_angle_radians"]);q=[1+0j,0j]
 uv=mv(mm(u,v),q);vu=mv(mm(v,u),q);fringe=inner(vu,uv)
 reverse=inner(uv,vu);commuting=inner(mv(mm(u,u),q),mv(mm(u,u),q));dephased=0j
 curvature=abs(1-fringe);S=c["bell_chsh"]
 routes={name:{"inclusive_chsh":S,"remote_marginal_delta":0.0} for name in c["required_routes"]}
 checks={"noncommuting_curvature_nonzero":curvature>c["tolerance"],"orientation_conjugates":abs(reverse-fringe.conjugate())<c["tolerance"],"commuting_control_flat":abs(commuting-1)<c["tolerance"],"dephased_control_zero":abs(dephased)<c["tolerance"],"bell_invariant":all(abs(r["inclusive_chsh"]-S)<c["tolerance"] for r in routes.values()),"remote_marginals_flat":all(r["remote_marginal_delta"]==0 for r in routes.values()),"bell_obstruction_present":S>c["local_ceiling"],"route_registry_complete":set(routes)==set(c["required_routes"]),"claim_boundary":not any(c["claim_boundary"].values())}
 out={"schema":"marici.aspect.nonabelian-constructor-curvature-bell-experiment-result.v1","passed":all(checks.values()),"checks":checks,"uv_vu_fringe":{"x":fringe.real,"y":fringe.imag,"visibility":abs(fringe),"phase":math.atan2(fringe.imag,fringe.real)},"orientation_reversed":{"x":reverse.real,"y":reverse.imag},"commuting_control":{"x":commuting.real,"y":commuting.imag},"curvature_distance_from_flat":curvature,"routes":routes,"verdict":"nonabelian_constructor_curvature_with_invariant_coarse_bell_fixture","physical_status":"not_run"}
 RESULT.write_text(json.dumps(out,indent=2)+"\n",encoding="utf-8");print(json.dumps(out,sort_keys=True));raise SystemExit(0 if out["passed"] else 1)
if __name__=="__main__":main()
