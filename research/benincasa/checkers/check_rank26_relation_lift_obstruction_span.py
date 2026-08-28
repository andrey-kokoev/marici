#!/usr/bin/env python3
"""Compute the span of x/y relation-lifting obstruction costalks."""
import json,os
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];P=int(os.environ.get("MARICI_FIELD_PRIME","32009"));s="" if P==32009 else f"-p{P}"
def load(a):return json.loads((ROOT/"research"/"benincasa"/"results"/f"rank26-bidual-quotient-horizontality{s}-{a}.json").read_text())
def vec(j):return {int(k):int(v)%P for k,v in j["obstruction_classes"][0].items() if int(v)%P}
def rank(vs):
 ps={}
 for src in vs:
  r=dict(src)
  while r:
   c=max(r);q=r[c]
   if c not in ps:
    iq=pow(q,-1,P);ps[c]={k:v*iq%P for k,v in r.items()};break
   for k,v in ps[c].items():
    w=(r.get(k,0)-q*v)%P
    if w:r[k]=w
    else:r.pop(k,None)
 return len(ps)
x,y=load("x"),load("y");vx,vy=vec(x),vec(y);r=rank([vx,vy]);checks={"input_packets_pass":x["passed"] and y["passed"],"one_obstruction_each":len(x["obstruction_classes"])==len(y["obstruction_classes"])==1,"joint_span_computed":r in (1,2)}
payload={"schema":"marici.rank26-relation-lift-obstruction-span.v1","prime":P,"support_sizes":{"x":len(vx),"y":len(vy)},"joint_rank":r,"common_line":r==1,"checks":checks,"passed":all(checks.values())}
out=ROOT/"research"/"benincasa"/"results"/f"rank26-relation-lift-obstruction-span{s}.json";out.write_text(json.dumps(payload,indent=2)+"\n");print(json.dumps(payload,indent=2));raise SystemExit(0 if payload["passed"] else 1)
