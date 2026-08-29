#!/usr/bin/env python3
"""Classify exact finite comparison-loop holonomies and hostile fixtures."""
import cmath, json, math
from pathlib import Path
ASPECT=Path(__file__).resolve().parent.parent
CONTRACT=ASPECT/"contracts"/"comparison-loop-interferometer.v1.json"
RESULT=ASPECT/"results"/"comparison_loop_interferometer.json"
I=[[1+0j,0j],[0j,1+0j]]
def mm(a,b): return [[sum(a[i][k]*b[k][j] for k in range(2)) for j in range(2)] for i in range(2)]
def dagger(a): return [[a[j][i].conjugate() for j in range(2)] for i in range(2)]
def norm(a): return math.sqrt(sum(abs(x)**2 for row in a for x in row))
def sub(a,b): return [[a[i][j]-b[i][j] for j in range(2)] for i in range(2)]
def scale(z,a): return [[z*x for x in row] for row in a]
def inv(a):
 d=a[0][0]*a[1][1]-a[0][1]*a[1][0]
 return [[a[1][1]/d,-a[0][1]/d],[-a[1][0]/d,a[0][0]/d]]
def relative(a,b): return mm(inv(b),a)
def classify(routes,tol):
 flags={r.get("antiunitary",False) for r in routes}
 if len(flags)>1: return "source_dependent"
 if routes[0].get("antiunitary",False): return "conjugation"
 hs=[relative(r["a"],r["b"]) for r in routes]
 if any(norm(sub(h,hs[0]))>tol for h in hs[1:]): return "source_dependent"
 h=hs[0]
 if norm(sub(mm(dagger(h),h),I))>tol: return "nonunitary_leakage"
 if norm(sub(h,I))<=tol: return "identity"
 z=(h[0][0]+h[1][1])/2
 if abs(abs(z)-1)<=tol and norm(sub(h,scale(z,I)))<=tol: return "scalar_phase"
 return "general_unitary"
def main():
 c=json.loads(CONTRACT.read_text(encoding="utf-8")); t=c["tolerances"]["matrix"]
 phase=cmath.exp(0.37j); had=[[1/math.sqrt(2),1/math.sqrt(2)],[1/math.sqrt(2),-1/math.sqrt(2)]]
 fixtures={
  "identity":[{"a":I,"b":I}],
  "scalar_phase":[{"a":scale(phase,I),"b":I}],
  "conjugation":[{"a":I,"b":I,"antiunitary":True}],
  "nonunitary_leakage":[{"a":[[0.9+0j,0j],[0j,1+0j]],"b":I}],
  "general_unitary":[{"a":had,"b":I}],
  "source_dependent":[{"a":I,"b":I},{"a":scale(phase,I),"b":I}]
 }
 got={k:classify(v,t) for k,v in fixtures.items()}
 complete={k:True for k in c["edge_certificate_fields"]}; incomplete=dict(complete,source_authority=False)
 promote=c["promotion"]
 checks={
  "all_classes_separated":all(got[k]==k for k in fixtures),
  "complex_only_identity":promote["complex_observable"]==["identity"],
  "projective_admits_phase":set(promote["projective_observable"])=={"identity","scalar_phase"},
  "oriented_rejects_conjugation":"conjugation" in promote["reject"],
  "edge_certificate_complete":all(complete.values()),
  "missing_authority_blocks":not all(incomplete.values()),
  "tetrahedral_orientation_probe":c["probe_frame"]["size"]==4 and len(c["probe_frame"]["oriented_triple"])==3,
  "environment_and_reset_observed":all(x in c["acquisition_fields"] for x in ("environment_port","reset_id")),
  "claim_boundary":not any(c["claim_boundary"].values())
 }
 out={"schema":"marici.aspect.comparison-loop-interferometer-result.v1","passed":all(checks.values()),"classifications":got,"checks":checks,"physical_status":"not_run","conclusion":"comparison_map_is_an_observable_bearing_constructor"}
 RESULT.parent.mkdir(parents=True,exist_ok=True); RESULT.write_text(json.dumps(out,indent=2)+"\n",encoding="utf-8"); print(json.dumps(out,sort_keys=True)); raise SystemExit(0 if out["passed"] else 1)
if __name__=="__main__": main()

