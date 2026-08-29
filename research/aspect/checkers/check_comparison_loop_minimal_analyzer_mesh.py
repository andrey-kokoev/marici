#!/usr/bin/env python3
"""Compile each normalized analyzer with the minimal adjacent-rotation ladder."""
import json, math
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]; ASPECT=Path(__file__).resolve().parent.parent
SOURCE=ROOT/"research"/"benincasa"/"results"/"interaction-net-barcode-lift-hostile-p32009.json"
CONTRACT=ASPECT/"contracts"/"comparison-loop-minimal-analyzer-mesh.v1.json"
RESULT=ASPECT/"results"/"comparison_loop_minimal_analyzer_mesh.json"
PROGRAM=ASPECT/"results"/"comparison_loop_minimal_analyzer_mesh_program.json"
def dot(a,b): return sum(x*y for x,y in zip(a,b))
def norm(x): return math.sqrt(dot(x,x))
def normalize(x): n=norm(x); return [v/n for v in x]
def rotate_vec(v,p,q,c,s,transpose=False):
 x,y=v[p],v[q]
 if transpose: v[p],v[q]=c*x-s*y,s*x+c*y
 else: v[p],v[q]=c*x+s*y,-s*x+c*y
def compile_vector(target):
 work=target[:]; ops=[]; n=len(work)
 for q in range(n-1,0,-1):
  p=q-1; r=math.hypot(work[p],work[q])
  if r<1e-15: continue
  c=work[p]/r; s=work[q]/r; rotate_vec(work,p,q,c,s); ops.append({"mode_a":p,"mode_b":q,"cosine":c,"sine":s})
 sign=1.0 if work[0]>=0 else -1.0; rec=[sign]+[0.0]*(n-1)
 for op in reversed(ops): rotate_vec(rec,op["mode_a"],op["mode_b"],op["cosine"],op["sine"],True)
 return ops,sign,rec,work
def main():
 s=json.loads(SOURCE.read_text(encoding="utf-8")); c=json.loads(CONTRACT.read_text(encoding="utf-8")); routes={}
 for arm,key in (("A","balanced_lift"),("B","shifted_lift")):
  target=normalize(s[key]); ops,sign,rec,reduced=compile_vector(target)
  routes[arm]={"source_lift":key,"rotations":[dict(rotation_index=i,control_arm=arm,**op) for i,op in enumerate(ops)],"input_phase":0.0 if sign>0 else math.pi,"reconstruction_error":norm([rec[i]-target[i] for i in range(len(target))]),"inverse_dark_port_error":norm(reduced[1:])}
 total=sum(len(v["rotations"]) for v in routes.values()); baseline=2*c["full_unitary_baseline_per_route"]; eps=c["rotation_systematic_budget"]/total
 checks={"nineteen_each":all(len(v["rotations"])==c["expected_rotations_per_route"] for v in routes.values()),"exact_reconstruction":all(v["reconstruction_error"]<1e-12 for v in routes.values()),"inverse_readout":all(v["inverse_dark_port_error"]<1e-12 for v in routes.values()),"component_reduction":total==38 and total<baseline,"tolerance_relaxed":eps>0.00026,"claim_boundary":not any(c["claim_boundary"].values())}
 packet={"schema":"marici.aspect.comparison-loop-minimal-analyzer-mesh-program.v1","routes":routes,"total_rotations":total,"per_rotation_angle_bound_radians":eps,"status":"compiled_not_programmed"}
 out={"schema":"marici.aspect.comparison-loop-minimal-analyzer-mesh-result.v1","passed":all(checks.values()),"checks":checks,"rotations_per_route":{k:len(v["rotations"]) for k,v in routes.items()},"total_rotations":total,"baseline_rotations":baseline,"component_reduction_fraction":1-total/baseline,"per_rotation_angle_bound_radians":eps,"tolerance_relaxation_factor":baseline/total,"program":str(PROGRAM.relative_to(ROOT)).replace("\\","/"),"physical_status":"not_run"}
 PROGRAM.write_text(json.dumps(packet,indent=2)+"\n",encoding="utf-8"); RESULT.write_text(json.dumps(out,indent=2)+"\n",encoding="utf-8"); print(json.dumps(out,sort_keys=True)); raise SystemExit(0 if out["passed"] else 1)
if __name__=="__main__": main()
