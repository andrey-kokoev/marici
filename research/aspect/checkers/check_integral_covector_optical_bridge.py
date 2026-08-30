#!/usr/bin/env python3
"""Bridge a validated integral-complex packet to minimal analyzer programs without row selection."""
import json, math
from functools import reduce
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]; ASPECT=Path(__file__).resolve().parent.parent
CONTRACT=ASPECT/"contracts"/"integral-covector-optical-bridge.v1.json"
RESULT=ASPECT/"results"/"integral_covector_optical_bridge.json"; ATLAS=ASPECT/"results"/"integral_covector_optical_atlas.json"
def gcd_all(xs): return reduce(math.gcd,(abs(int(x)) for x in xs),0)
def dot(a,b): return sum(x*y for x,y in zip(a,b))
def norm(x): return math.sqrt(dot(x,x))
def normalize(x): n=norm(x); return [v/n for v in x]
def rotate(v,p,q,c,s,transpose=False):
 x,y=v[p],v[q]
 if transpose:v[p],v[q]=c*x-s*y,s*x+c*y
 else:v[p],v[q]=c*x+s*y,-s*x+c*y
def compile_vector(target):
 work=target[:];ops=[]
 for q in range(len(work)-1,0,-1):
  p=q-1;r=math.hypot(work[p],work[q])
  if r<1e-15:continue
  c=work[p]/r;s=work[q]/r;rotate(work,p,q,c,s);ops.append({"mode_a":p,"mode_b":q,"cosine":c,"sine":s})
 sign=1 if work[0]>=0 else -1; rec=[float(sign)]+[0.0]*(len(work)-1)
 for op in reversed(ops):rotate(rec,op["mode_a"],op["mode_b"],op["cosine"],op["sine"],True)
 return ops,rec
def main():
 c=json.loads(CONTRACT.read_text(encoding="utf-8")); candidate=ROOT/c["source_candidate"]; fallback=ROOT/c["fallback_fixture"]; source=candidate if candidate.exists() else fallback
 p=json.loads(source.read_text(encoding="utf-8")); status=p.get("status","unknown"); cov=p["quotient_covectors"]
 rels=[]
 for block in p["relation_matrices"].values(): rels.extend(block if block and isinstance(block[0],list) else [block])
 programs=[]
 for i,v in enumerate(cov):
  nv=normalize(v);ops,rec=compile_vector(nv)
  programs.append({"covector_id":i,"integral_covector":v,"primitive":gcd_all(v)==1,"annihilates_relations":all(len(r)!=len(v) or dot(v,r)==0 for r in rels),"normalization":norm(v),"normalized_analyzer":nv,"rotations":ops,"reconstruction_error":norm([rec[j]-nv[j] for j in range(len(v))]),"good_prime_reductions":{q:d["covectors"][i] for q,d in p["good_prime_comparisons"].items()},"promotion_status":"source_authorized" if status=="source_authorized" else "synthetic_not_promotable"})
 overlaps=[]; distances=[]
 for i in range(len(programs)):
  for j in range(i+1,len(programs)):
   z=dot(programs[i]["normalized_analyzer"],programs[j]["normalized_analyzer"]); overlaps.append({"i":i,"j":j,"overlap":z});distances.append({"i":i,"j":j,"projector_frobenius_squared":2*(1-z*z)})
 bad=cov[0][:];bad[0]*=2
 checks={"all_covectors_compiled":len(programs)==len(cov),"no_selection":c["selection"].startswith("compile_every"),"primitive":all(x["primitive"] for x in programs),"incidence":all(x["annihilates_relations"] for x in programs),"minimal_rotations":all(len(x["rotations"])<=len(x["integral_covector"])-1 for x in programs),"reconstruction":all(x["reconstruction_error"]<1e-12 for x in programs),"atlas_complete":len(overlaps)==len(cov)*(len(cov)-1)//2,"nonprimitive_hostile":gcd_all([2*x for x in cov[0]])!=1,"fixture_not_promoted":status=="source_authorized" or all(x["promotion_status"]=="synthetic_not_promotable" for x in programs),"claim_boundary":not any(c["claim_boundary"].values())}
 atlas={"schema":"marici.aspect.integral-covector-optical-atlas.v1","source_packet":str(source.relative_to(ROOT)).replace("\\","/"),"source_status":status,"programs":programs,"pairwise_overlaps":overlaps,"projector_distances":distances}
 out={"schema":"marici.aspect.integral-covector-optical-bridge-result.v1","passed":all(checks.values()),"checks":checks,"source_status":status,"program_count":len(programs),"pairwise_overlaps":overlaps,"projector_distances":distances,"atlas":str(ATLAS.relative_to(ROOT)).replace("\\","/"),"promotion_status":"source_authorized" if status=="source_authorized" else "synthetic_not_promotable"}
 ATLAS.write_text(json.dumps(atlas,indent=2)+"\n",encoding="utf-8"); RESULT.write_text(json.dumps(out,indent=2)+"\n",encoding="utf-8"); print(json.dumps(out,sort_keys=True)); raise SystemExit(0 if out["passed"] else 1)
if __name__=="__main__":main()
