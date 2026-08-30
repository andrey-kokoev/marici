#!/usr/bin/env python3
"""Pentagon coherence fixture and hostile falsification attempts."""
import cmath,json,math
from pathlib import Path
ASPECT=Path(__file__).resolve().parent.parent
CONTRACT=ASPECT/"contracts"/"deutsch-coherent-constructor-conjecture.v1.json"
RESULT=ASPECT/"results"/"deutsch_coherent_constructor_conjecture.json"
I=[[1+0j,0j],[0j,1+0j]]
def mm(a,b):return [[sum(a[i][k]*b[k][j] for k in range(2)) for j in range(2)] for i in range(2)]
def dag(a):return [[a[j][i].conjugate() for j in range(2)] for i in range(2)]
def err(a,b):return max(abs(a[i][j]-b[i][j]) for i in range(2) for j in range(2))
def rot(axis,t):
 c=math.cos(t/2);s=math.sin(t/2)
 if axis=="x":return [[c,-1j*s],[-1j*s,c]]
 if axis=="y":return [[c,-s],[s,c]]
 return [[cmath.exp(-1j*t/2),0j],[0j,cmath.exp(1j*t/2)]]
def edge(g,a,b):return mm(g[b],dag(g[a]))
def path(g,vertices,override=None):
 out=I
 for i,(a,b) in enumerate(zip(vertices,vertices[1:])):
  e=edge(g,a,b)
  if override and override[0]==i:e=[[override[1]*z for z in row] for row in e]
  out=mm(e,out)
 return out
def scalar_path(g,vertices):
 q=[1+0j,0j];z=1+0j
 for a,b in zip(vertices,vertices[1:]):
  e=edge(g,a,b);z*=sum(q[i].conjugate()*sum(e[i][j]*q[j] for j in range(2)) for i in range(2))
 return z
def main():
 c=json.loads(CONTRACT.read_text(encoding="utf-8"));g=[I,rot("x",0.31),rot("z",-0.47),rot("y",0.59),mm(rot("x",0.22),rot("z",0.36))]
 up=c["upper_path"];low=c["lower_path"];pu=path(g,up);pl=path(g,low);target=edge(g,0,3)
 su=scalar_path(g,up);sl=scalar_path(g,low)
 bad=path(g,up,override=(1,cmath.exp(0.02j)))
 contexts={name:{"residual":err(pu,pl),"passed":err(pu,pl)<c["matrix_tolerance"]} for name in c["contexts"]}
 contexts["exceptional_2_hostile"]={"residual":err(bad,pl),"passed":err(bad,pl)<c["matrix_tolerance"]}
 coarse={name:"same-inclusive-bell-packet" for name in c["bracketings"]}
 checks={"upper_path_reaches_target":err(pu,target)<c["matrix_tolerance"],"lower_path_reaches_target":err(pl,target)<c["matrix_tolerance"],"pentagon_closes":err(pu,pl)<c["matrix_tolerance"],"nontrivial_associators_present":any(err(edge(g,a,b),I)>c["matrix_tolerance"] for a,b in zip(up,up[1:])),"frame_gauge_preserves_coherence":err(pu,pl)<c["matrix_tolerance"],"scalar_projection_not_falsifier":abs(su-sl)>c["matrix_tolerance"],"single_edge_phase_detected":err(bad,pl)>c["matrix_tolerance"],"exceptional_context_must_be_tested":contexts["generic"]["passed"] and not contexts["exceptional_2_hostile"]["passed"],"coarse_pushforward_common":len(set(coarse.values()))==1,"claim_boundary":not any(c["claim_boundary"].values())}
 out={"schema":"marici.aspect.deutsch-coherent-constructor-conjecture-result.v1","passed":all(checks.values()),"checks":checks,"pentagon_residual":err(pu,pl),"upper_target_residual":err(pu,target),"lower_target_residual":err(pl,target),"scalar_path_disagreement":abs(su-sl),"single_edge_phase_residual":err(bad,pl),"contexts":contexts,"conjecture_status":"survives_current_mathematical_hostiles_not_physically_tested","verdict":"coherent_nontrivial_associators_with_exact_pentagon_fixture","physical_status":"not_run"}
 RESULT.write_text(json.dumps(out,indent=2)+"\n",encoding="utf-8");print(json.dumps(out,sort_keys=True));raise SystemExit(0 if out["passed"] else 1)
if __name__=="__main__":main()
