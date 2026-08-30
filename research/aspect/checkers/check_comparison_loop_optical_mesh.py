#!/usr/bin/env python3
"""Lower the connected route unitaries to explicit two-mode optical meshes."""
import json, math
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]; ASPECT=Path(__file__).resolve().parent.parent
SOURCE=ROOT/"research"/"benincasa"/"results"/"interaction-net-barcode-lift-hostile-p32009.json"
CONTRACT=ASPECT/"contracts"/"comparison-loop-optical-mesh.v1.json"
RESULT=ASPECT/"results"/"comparison_loop_optical_mesh.json"; MESH=ASPECT/"results"/"comparison_loop_optical_mesh_program.json"
def dot(a,b): return sum(x*y for x,y in zip(a,b))
def norm(x): return math.sqrt(dot(x,x))
def normalize(x): n=norm(x); return [v/n for v in x]
def ident(n): return [[1.0 if i==j else 0.0 for j in range(n)] for i in range(n)]
def mm(a,b): return [[sum(a[i][k]*b[k][j] for k in range(len(b))) for j in range(len(b[0]))] for i in range(len(a))]
def transpose(a): return [list(x) for x in zip(*a)]
def frob(a,b): return math.sqrt(sum((a[i][j]-b[i][j])**2 for i in range(len(a)) for j in range(len(a))))
def householder(target):
 n=len(target); e=[1.0]+[0.0]*(n-1); d=[e[i]-target[i] for i in range(n)]
 if norm(d)<1e-15:return ident(n)
 u=normalize(d); return [[(1 if i==j else 0)-2*u[i]*u[j] for j in range(n)] for i in range(n)]
def left_rotate(a,p,q,c,s,transpose_rotation=False):
 x=a[p][:]; y=a[q][:]
 if transpose_rotation: a[p]=[c*x[j]-s*y[j] for j in range(len(x))]; a[q]=[s*x[j]+c*y[j] for j in range(len(x))]
 else: a[p]=[c*x[j]+s*y[j] for j in range(len(x))]; a[q]=[-s*x[j]+c*y[j] for j in range(len(x))]
def decompose(u):
 a=[r[:] for r in u]; ops=[]; n=len(a)
 for j in range(n):
  for q in range(n-1,j,-1):
   p=q-1; x=a[p][j]; y=a[q][j]; r=math.hypot(x,y)
   if r<1e-15: continue
   c=x/r; s=y/r; left_rotate(a,p,q,c,s); ops.append({"mode_a":p,"mode_b":q,"cosine":c,"sine":s})
 d=[1.0 if a[i][i]>=0 else -1.0 for i in range(n)]
 rec=[[d[i] if i==j else 0.0 for j in range(n)] for i in range(n)]
 for op in reversed(ops): left_rotate(rec,op["mode_a"],op["mode_b"],op["cosine"],op["sine"],True)
 return ops,d,rec,a
def main():
 s=json.loads(SOURCE.read_text(encoding="utf-8")); c=json.loads(CONTRACT.read_text(encoding="utf-8")); routes={}
 for arm,key in (("A","balanced_lift"),("B","shifted_lift")):
  u=householder(normalize(s[key])); ops,d,rec,tri=decompose(u)
  routes[arm]={"source_lift":key,"dimension":len(u),"rotation_count":len(ops),"rotations":[dict(rotation_index=i,control_arm=arm,mesh_id=f"route-{arm}-mesh-v1",phase_fixture="identity-real-v1",reset_id=f"reset-{arm}-v1",**op) for i,op in enumerate(ops)],"terminal_phases":[0.0 if x>0 else math.pi for x in d],"reconstruction_frobenius":frob(rec,u),"orthogonality_frobenius":frob(mm(transpose(rec),rec),ident(len(u)))}
 tol=c["tolerances"]; checks={"both_routes_compiled":set(routes)=={"A","B"},"nonempty_meshes":all(v["rotation_count"]>0 for v in routes.values()),"reconstruction":all(v["reconstruction_frobenius"]<tol["reconstruction_frobenius"] for v in routes.values()),"orthogonality":all(v["orthogonality_frobenius"]<tol["orthogonality_frobenius"] for v in routes.values()),"shot_total":c["shot_plan"]["total_primary_trials"]+c["shot_plan"]["total_bypass_trials"]==1320000,"claim_boundary":not any(c["claim_boundary"].values())}
 packet={"schema":"marici.aspect.comparison-loop-optical-mesh-program.v1","routes":routes,"coherent_control":{"arms":{"A":"route-A-mesh-v1","B":"route-B-mesh-v1"},"input_control":"plus","readout":["X","Y"]},"shot_plan":c["shot_plan"],"status":"compiled_not_programmed"}
 out={"schema":"marici.aspect.comparison-loop-optical-mesh-result.v1","passed":all(checks.values()),"checks":checks,"rotation_counts":{k:v["rotation_count"] for k,v in routes.items()},"reconstruction":{k:v["reconstruction_frobenius"] for k,v in routes.items()},"mesh_program":str(MESH.relative_to(ROOT)).replace("\\","/"),"physical_status":"not_run"}
 MESH.write_text(json.dumps(packet,indent=2)+"\n",encoding="utf-8"); RESULT.write_text(json.dumps(out,indent=2)+"\n",encoding="utf-8"); print(json.dumps(out,sort_keys=True)); raise SystemExit(0 if out["passed"] else 1)
if __name__=="__main__": main()
