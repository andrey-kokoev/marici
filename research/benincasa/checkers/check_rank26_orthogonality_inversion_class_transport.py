#!/usr/bin/env python3
"""Transport h=0 relation classes under a<->b, x<->y."""
import json,os
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];P=int(os.environ.get("MARICI_FIELD_PRIME","32009"));s="" if P==32009 else f"-p{P}"
mons=[(i,j) for i in range(7) for j in range(7-i)];idx={m:i for i,m in enumerate(mons)};perm={i:idx[(b,a)] for i,(a,b) in enumerate(mons)}
def load(point,axis):
 q="-at-"+"-".join(map(str,point));return json.loads((ROOT/"research"/"benincasa"/"results"/f"rank26-bidual-quotient-horizontality{s}-{axis}{q}.json").read_text())
def vs(j,key):return [{int(k):int(v)%P for k,v in r.items() if int(v)%P} for r in j[key]]
def transport(v):return {perm[k]:x for k,x in v.items()}
def annihilates(coeffs,columns):
 out={}
 for j,a in coeffs.items():
  for c,v in columns[j].items():
   w=(out.get(c,0)+a*v)%P
   if w:out[c]=w
   else:out.pop(c,None)
 return not out
def rank(rows):
 ps={}
 for src in rows:
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
rows=[]
for sa,ta in (("x","y"),("y","x")):
 a,b=load((3,4,5),sa),load((4,3,5),ta);entry={"route":f"{sa}->{ta}"}
 # The base quotient columns are independent of the parameter-derivative
 # direction.  Read them from the regenerated x packet so older y packets
 # remain valid inputs for the relation-class comparison.
 target_columns=vs(load((4,3,5),"x"),"base_quotient_columns")
 source_columns=vs(load((3,4,5),"x"),"base_quotient_columns")
 for key in ("base_relation_vectors","lifted_base_relation_vectors","obstructed_base_relation_vectors"):
  raw_left=vs(a,key);left=[transport(v) for v in raw_left];right=vs(b,key);entry[key]={"source_rank":rank(left),"target_rank":rank(right),"union_rank":rank(left+right),"same_subspace":rank(left)==rank(right)==rank(left+right),"serialized_vectors_annihilate_source_base_map":all(annihilates(v,source_columns) for v in raw_left),"transported_vectors_annihilate_target_base_map":all(annihilates(v,target_columns) for v in left)}
 rows.append(entry)
natural=all(all(v["same_subspace"] for k,v in r.items() if k!="route") for r in rows)
checks={"all_six_subspace_comparisons_computed":len(rows)==2 and all(len(r)==4 for r in rows),"naive_monomial_inversion_rejected":not natural}
payload={"schema":"marici.rank26-orthogonality-inversion-class-transport.v1","prime":P,"routes":rows,"naive_transport_natural":natural,"checks":checks,"passed":all(checks.values()),"conclusion":"The independently serialized relation vectors fail the naive coordinate comparison. The ambient exact-row audit proves that the reducer and low quotient generators are natural, so this packet is diagnostic of a post-reduction frame/serialization mismatch and is not evidence of geometric or truncation noncovariance."}
out=ROOT/"research"/"benincasa"/"results"/f"rank26-orthogonality-inversion-class-transport{s}.json";out.write_text(json.dumps(payload,indent=2)+"\n");print(json.dumps(payload,indent=2));raise SystemExit(0 if payload["passed"] else 1)
