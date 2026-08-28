#!/usr/bin/env python3
"""Test the joint span of the Bockstein line and its x,y mixed images."""
import json,os
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];P=int(os.environ.get("MARICI_FIELD_PRIME","32009"));s="" if P==32009 else f"-p{P}"
POINT=tuple(int(os.environ.get(n,d)) for n,d in (("MARICI_SOURCE_X","2"),("MARICI_SOURCE_Y","3"),("MARICI_SOURCE_Z","4")))
ps="" if POINT==(2,3,4) else "-at-"+"-".join(map(str,POINT))
def load(axis):return json.loads((ROOT/"research"/"benincasa"/"results"/f"rank26-bidual-quotient-horizontality{s}-{axis}{ps}.json").read_text())
def sparse(v):return {int(k):int(x)%P for k,x in v.items() if int(x)%P}
def rank(vs):
 ps={}
 for src in vs:
  r=dict(src)
  while r:
   c=max(r);q=r[c]
   if c not in ps:
    iq=pow(q,-1,P);ps[c]={k:x*iq%P for k,x in r.items()};break
   for k,x in ps[c].items():
    y=(r.get(k,0)-q*x)%P
    if y:r[k]=y
    else:r.pop(k,None)
 return len(ps)
x,y=load("x"),load("y"); beta=[sparse(v) for v in x["bockstein_vectors"] if v]; mx=[sparse(v) for v in x["mixed_vectors"] if v]; my=[sparse(v) for v in y["mixed_vectors"] if v]
r1=rank(beta);rx=rank(beta+mx);ry=rank(beta+my);rxy=rank(beta+mx+my)
checks={"input_packets_pass":x["passed"] and y["passed"],"common_bockstein_rank_one":r1==1,"each_direction_adds_one":rx==2 and ry==2,"joint_first_saturation_computed":rxy>=2}
payload={"schema":"marici.rank26-bockstein-first-saturation.v1","prime":P,"ranks":{"line":r1,"line_plus_x":rx,"line_plus_y":ry,"line_plus_x_plus_y":rxy},"rank_two_first_saturation":rxy==2,"checks":checks,"passed":all(checks.values())}
out=ROOT/"research"/"benincasa"/"results"/f"rank26-bockstein-first-saturation{s}{ps}.json";out.write_text(json.dumps(payload,indent=2)+"\n");print(json.dumps(payload,indent=2));raise SystemExit(0 if payload["passed"] else 1)
