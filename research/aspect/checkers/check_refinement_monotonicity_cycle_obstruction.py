#!/usr/bin/env python3
"""Finite exact witness for local-refinement monotonicity and CHSH cycle persistence."""
import itertools, json, math
from pathlib import Path

ASPECT=Path(__file__).resolve().parent.parent
CONTRACT=ASPECT/"contracts"/"refinement-monotonicity-cycle-obstruction.v1.json"
RESULT=ASPECT/"results"/"refinement_monotonicity_cycle_obstruction.json"

def corr(a,b): return -math.cos(2*math.radians(a-b))
def chsh(e): return abs(e[0][0]+e[0][1]+e[1][0]-e[1][1])

def main():
 c=json.loads(CONTRACT.read_text(encoding="utf-8")); A=c["settings_degrees"]["A"];B=c["settings_degrees"]["B"]
 coarse={(i,j,x,y):(1+x*y*corr(a,b))/4 for i,a in enumerate(A) for j,b in enumerate(B) for x in (-1,1) for y in (-1,1)}
 # Setting- and outcome-local stochastic label kernels; deliberately nonuniform.
 qa=lambda i,x,l: (0.7 if l==(i+(x+1)//2)%2 else 0.3)
 qb=lambda j,y,l: (0.6 if l==(j+(y+1)//2)%2 else 0.4)
 refined={(i,j,x,y,la,lb):p*qa(i,x,la)*qb(j,y,lb) for (i,j,x,y),p in coarse.items() for la in (0,1) for lb in (0,1)}
 pushed={(i,j,x,y):sum(refined[i,j,x,y,la,lb] for la in (0,1) for lb in (0,1)) for i,j,x,y in coarse}
 push_error=max(abs(pushed[k]-coarse[k]) for k in coarse)
 ecoarse=[[sum(x*y*coarse[i,j,x,y] for x in (-1,1) for y in (-1,1)) for j in range(2)] for i in range(2)]
 epushed=[[sum(x*y*pushed[i,j,x,y] for x in (-1,1) for y in (-1,1)) for j in range(2)] for i in range(2)]
 # Exhaust every deterministic refined local assignment: outcome and label at each setting.
 refined_vertices=[]
 choices=list(itertools.product((-1,1),(0,1)))
 for a0,a1,b0,b1 in itertools.product(choices,repeat=4):
  e=[[a0[0]*b0[0],a0[0]*b1[0]],[a1[0]*b0[0],a1[0]*b1[0]]]
  refined_vertices.append(chsh(e))
 S=chsh(ecoarse); excess=S-c["local_ceiling"]
 # Hostile: context-dependent selection replaces the inclusive packet; its pushforward is detectably different.
 selected={k:(p if k[2]*k[3]==(1 if (k[0],k[1])!=(1,1) else -1) else 0.0) for k,p in coarse.items()}
 for i in range(2):
  for j in range(2):
   z=sum(selected[i,j,x,y] for x in (-1,1) for y in (-1,1))
   for x in (-1,1):
    for y in (-1,1): selected[i,j,x,y]/=z
 selection_push_error=max(abs(selected[k]-coarse[k]) for k in coarse)
 checks={
  "local_kernels_normalized":all(abs(sum(qa(i,x,l) for l in (0,1))-1)<1e-15 for i in range(2) for x in (-1,1)) and all(abs(sum(qb(j,y,l) for l in (0,1))-1)<1e-15 for j in range(2) for y in (-1,1)),
  "honest_pushforward_commutes":push_error<c["pushforward_tolerance"],
  "cycle_witness_natural":max(abs(ecoarse[i][j]-epushed[i][j]) for i in range(2) for j in range(2))<c["pushforward_tolerance"],
  "all_refined_local_vertices_project_local":len(refined_vertices)==256 and max(refined_vertices)<=c["local_ceiling"],
  "coarse_packet_nonlocal":S>c["local_ceiling"],
  "witness_distance_positive":excess/4>0,
  "selection_is_not_refinement":selection_push_error>c["pushforward_tolerance"],
  "claim_boundary_preserved":not any(c["claim_boundary"].values())
 }
 out={"schema":"marici.aspect.refinement-monotonicity-cycle-obstruction-result.v1","passed":all(checks.values()),"checks":checks,"coarse_chsh":S,"pushed_chsh":chsh(epushed),"pushforward_max_error":push_error,"refined_local_vertex_count":len(refined_vertices),"refined_local_vertex_max":max(refined_vertices),"witness_distance_lower_bound":excess/4,"selection_pushforward_error":selection_push_error,"verdict":"honest_local_refinement_preserves_coarse_nonfactorization_finite_fixture","physical_status":"not_run"}
 RESULT.write_text(json.dumps(out,indent=2)+"\n",encoding="utf-8");print(json.dumps(out,sort_keys=True));raise SystemExit(0 if out["passed"] else 1)
if __name__=="__main__":main()
