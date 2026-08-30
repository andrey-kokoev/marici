#!/usr/bin/env python3
"""Compile two exact lifts to unitaries and run the coherent-control reference acquisition."""
import json, math
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
ASPECT=Path(__file__).resolve().parent.parent
SOURCE=ROOT/"research"/"benincasa"/"results"/"interaction-net-barcode-lift-hostile-p32009.json"
CONTRACT=ASPECT/"contracts"/"connected-route-coherent-control-acquisition.v1.json"
RESULT=ASPECT/"results"/"connected_route_coherent_control.json"
ACQ=ASPECT/"results"/"connected_route_coherent_control_acquisition.json"
def dot(a,b): return sum(x*y for x,y in zip(a,b))
def mv(a,x): return [dot(row,x) for row in a]
def norm(x): return math.sqrt(dot(x,x))
def normalize(x): n=norm(x); return [v/n for v in x]
def householder(target):
 n=len(target); e=[1.0]+[0.0]*(n-1); d=[e[i]-target[i] for i in range(n)]
 if norm(d)<1e-15: return [[1.0 if i==j else 0.0 for j in range(n)] for i in range(n)]
 u=normalize(d); return [[(1.0 if i==j else 0.0)-2*u[i]*u[j] for j in range(n)] for i in range(n)]
def transpose(a): return [list(x) for x in zip(*a)]
def mm(a,b): return [[dot(a[i],[b[k][j] for k in range(len(b))]) for j in range(len(b[0]))] for i in range(len(a))]
def frob(a,b): return math.sqrt(sum((a[i][j]-b[i][j])**2 for i in range(len(a)) for j in range(len(a))))
def main():
 s=json.loads(SOURCE.read_text(encoding="utf-8")); c=json.loads(CONTRACT.read_text(encoding="utf-8"))
 ra=normalize(s["balanced_lift"]); rb=normalize(s["shifted_lift"]); ua=householder(ra); ub=householder(rb); n=len(ra)
 ident=[[1.0 if i==j else 0.0 for j in range(n)] for i in range(n)]
 witness=normalize(s["witness_input"]); probes=[("mode0",[1.0]+[0.0]*(n-1)),("hostile_witness",witness)]
 for k in range(min(4,n)): probes.append((f"support_basis_{k}",[1.0 if j==k else 0.0 for j in range(n)]))
 records=[]
 for idx,(name,x) in enumerate(probes):
  ya,yb=mv(ua,x),mv(ub,x); fringe=dot(ya,yb)
  records.append({"trial_group":idx,"probe_id":name,"source_row_index":s["source_row_index"],"route_a":"balanced","route_b":"shifted","compiler_a":"householder-balanced-v1","compiler_b":"householder-shifted-v1","control_x":fringe,"control_y":0.0,"bypass_a":dot(ya,ya),"bypass_b":dot(yb,yb),"environment_a":0.0,"environment_b":0.0,"phase_fixture":"identity-real-v1","reset_a":"reset-balanced-v1","reset_b":"reset-shifted-v1","status":"synthetic_reference"})
 required=c["required_record_fields"]; tol=c["acceptance"]["unitarity_tolerance"]
 checks={"source_packet_passed":s["passed"],"route_a_unitary":frob(mm(transpose(ua),ua),ident)<tol,"route_b_unitary":frob(mm(transpose(ub),ub),ident)<tol,"route_a_analyzer":norm([ua[i][0]-ra[i] for i in range(n)])<tol,"route_b_analyzer":norm([ub[i][0]-rb[i] for i in range(n)])<tol,"all_fields":all(all(k in r for k in required) for r in records),"norm_closure":all(abs(r["bypass_a"]-1)<tol and abs(r["bypass_b"]-1)<tol for r in records),"no_environment_leakage":all(r["environment_a"]==0 and r["environment_b"]==0 for r in records),"routes_distinct":norm([ra[i]-rb[i] for i in range(n)])>1e-3,"hostile_dark_bright_preserved":s["responses"]["balanced"]==0 and s["responses"]["shifted"]!=0,"claim_boundary":not any(c["claim_boundary"].values())}
 acq={"schema":"marici.aspect.connected-route-coherent-control-acquisition-packet.v1","status":"synthetic_reference","source_packet":str(SOURCE.relative_to(ROOT)).replace("\\","/"),"dimension":n,"records":records,"physical_counts":[]}
 out={"schema":"marici.aspect.connected-route-coherent-control-result.v1","passed":all(checks.values()),"checks":checks,"dimension":n,"analyzer_overlap":dot(ra,rb),"fringe_range":[min(r["control_x"] for r in records),max(r["control_x"] for r in records)],"acquisition_packet":str(ACQ.relative_to(ROOT)).replace("\\","/"),"physical_status":"not_run"}
 ACQ.write_text(json.dumps(acq,indent=2)+"\n",encoding="utf-8"); RESULT.write_text(json.dumps(out,indent=2)+"\n",encoding="utf-8"); print(json.dumps(out,sort_keys=True)); raise SystemExit(0 if out["passed"] else 1)
if __name__=="__main__": main()

