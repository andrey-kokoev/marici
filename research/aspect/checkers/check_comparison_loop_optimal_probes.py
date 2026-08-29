#!/usr/bin/env python3
"""Compute the globally extremal coherent-control probes by Jacobi diagonalization."""
import json, math
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]; ASPECT=Path(__file__).resolve().parent.parent
PROGRAM=ASPECT/"results"/"comparison_loop_minimal_analyzer_mesh_program.json"
CONTRACT=ASPECT/"contracts"/"comparison-loop-optimal-probes.v1.json"
RESULT=ASPECT/"results"/"comparison_loop_optimal_probes.json"; PROBES=ASPECT/"results"/"comparison_loop_optimal_probe_packet.json"
def ident(n): return [[1.0 if i==j else 0.0 for j in range(n)] for i in range(n)]
def mm(a,b): return [[sum(a[i][k]*b[k][j] for k in range(len(b))) for j in range(len(b[0]))] for i in range(len(a))]
def tr(a): return [list(x) for x in zip(*a)]
def dot(a,b): return sum(x*y for x,y in zip(a,b))
def left_t(a,p,q,c,s):
 x=a[p][:]; y=a[q][:]; a[p]=[c*x[j]-s*y[j] for j in range(len(x))]; a[q]=[s*x[j]+c*y[j] for j in range(len(x))]
def route_matrix(route):
 n=20; a=ident(n)
 for op in reversed(route["rotations"]): left_t(a,op["mode_a"],op["mode_b"],op["cosine"],op["sine"])
 if abs(route["input_phase"]-math.pi)<1e-12:
  for i in range(n): a[i][0]*=-1
 return a
def jacobi(a,tol=1e-14,max_iter=20000):
 n=len(a); v=ident(n); a=[r[:] for r in a]
 for _ in range(max_iter):
  p,q=max(((i,j) for i in range(n) for j in range(i+1,n)),key=lambda z:abs(a[z[0]][z[1]]))
  if abs(a[p][q])<tol: break
  phi=.5*math.atan2(2*a[p][q],a[q][q]-a[p][p]); c=math.cos(phi); s=math.sin(phi)
  for k in range(n):
   if k not in (p,q):
    x,y=a[k][p],a[k][q]; a[k][p]=a[p][k]=c*x-s*y; a[k][q]=a[q][k]=s*x+c*y
  app,aqq,apq=a[p][p],a[q][q],a[p][q]
  a[p][p]=c*c*app-2*s*c*apq+s*s*aqq; a[q][q]=s*s*app+2*s*c*apq+c*c*aqq; a[p][q]=a[q][p]=0.0
  for k in range(n):
   x,y=v[k][p],v[k][q]; v[k][p]=c*x-s*y; v[k][q]=s*x+c*y
 return [a[i][i] for i in range(n)],v
def main():
 p=json.loads(PROGRAM.read_text(encoding="utf-8")); c=json.loads(CONTRACT.read_text(encoding="utf-8"))
 ua=route_matrix(p["routes"]["A"]); ub=route_matrix(p["routes"]["B"]); r=mm(tr(ua),ub); n=len(r)
 sym=[[(r[i][j]+r[j][i])/2 for j in range(n)] for i in range(n)]; vals,vecs=jacobi(sym)
 order=sorted(range(n),key=lambda i:vals[i]); lo,hi=order[0],order[-1]; vlo=[vecs[k][lo] for k in range(n)]; vhi=[vecs[k][hi] for k in range(n)]
 flo=dot(vlo,[sum(r[i][j]*vlo[j] for j in range(n)) for i in range(n)]); fhi=dot(vhi,[sum(r[i][j]*vhi[j] for j in range(n)) for i in range(n)])
 spread=fhi-flo; err=c["acceptance"]["two_sided_total_error"]; generic=0.22577955713951414
 checks={"two_probes":c["probe_count"]==2,"eigen_residuals":abs(flo-vals[lo])<1e-10 and abs(fhi-vals[hi])<1e-10,"global_order":vals[lo]<=min(vals)+1e-12 and vals[hi]>=max(vals)-1e-12,"beats_generic":spread>=generic-1e-12,"margin":spread-err>c["acceptance"]["minimum_margin"],"shot_reduction":c["acquisition"]["total_primary_trials"]==400000 and c["acquisition"]["total_bypass_trials"]==40000,"claim_boundary":not any(c["claim_boundary"].values())}
 packet={"schema":"marici.aspect.comparison-loop-optimal-probe-packet.v1","status":"compiled_not_prepared","probes":[{"id":"minimum_fringe","vector":vlo,"predicted_x":flo,"predicted_y":0.0},{"id":"maximum_fringe","vector":vhi,"predicted_x":fhi,"predicted_y":0.0}],"acquisition":c["acquisition"]}
 out={"schema":"marici.aspect.comparison-loop-optimal-probes-result.v1","passed":all(checks.values()),"checks":checks,"minimum_fringe":flo,"maximum_fringe":fhi,"optimal_spread":spread,"generic_spread":generic,"remaining_margin":spread-err,"primary_shot_reduction_fraction":1-400000/1200000,"probe_packet":str(PROBES.relative_to(ROOT)).replace("\\","/"),"physical_status":"not_run"}
 PROBES.write_text(json.dumps(packet,indent=2)+"\n",encoding="utf-8"); RESULT.write_text(json.dumps(out,indent=2)+"\n",encoding="utf-8"); print(json.dumps(out,sort_keys=True)); raise SystemExit(0 if out["passed"] else 1)
if __name__=="__main__": main()
