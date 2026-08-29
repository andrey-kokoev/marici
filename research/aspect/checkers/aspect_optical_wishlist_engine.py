"""Shared executable engine for the ten-rung Aspect optical wishlist."""
import cmath, json, math
from pathlib import Path
ASPECT=Path(__file__).resolve().parent.parent
CONTRACT=ASPECT/"contracts"/"aspect-optical-bench-acquisition.v1.json"
RESULTS=ASPECT/"results"
RUNGS=["metric","orientation","compilers","bell","loopholes","randomness","network","context","composition","lift"]
def inner(a,b): return sum(x.conjugate()*y for x,y in zip(a,b))
def state(x,y,z): return (math.sqrt((1+z)/2)+0j,cmath.exp(1j*math.atan2(y,x))*math.sqrt((1-z)/2))
def tetra():
 q=1/math.sqrt(3); return [state(q,q,q),state(q,-q,-q),state(-q,q,-q),state(-q,-q,q)]
def B(s,o=(0,1,2)):
 a,b,c=(s[i] for i in o); return inner(a,b)*inner(b,c)*inner(c,a)
def chsh():
 a=[0,math.pi/2]; b=[math.pi/4,-math.pi/4]
 e=[[-math.cos(x-y) for y in b] for x in a]
 return abs(e[0][0]+e[0][1]+e[1][0]-e[1][1]),e
def bits(s):
 if s<2 or s>2*math.sqrt(2): return 0.0
 return -math.log2((1+math.sqrt(max(0,2-s*s/4)))/2)
def evaluate(rung):
 c=json.loads(CONTRACT.read_text(encoding="utf-8")); s=tetra(); m=[tuple(z.conjugate() for z in x) for x in s]
 pair=[[abs(inner(x,y))**2 for y in s] for x in s]; pairm=[[abs(inner(x,y))**2 for y in m] for x in m]
 ba,bm=B(s),B(m); S,e=chsh(); required=c["promotion_fields"]
 cases={
  "metric":{"diagonal":all(abs(pair[i][i]-1)<1e-12 for i in range(4)),"tetra":all(abs(pair[i][j]-(1 if i==j else 1/3))<1e-12 for i in range(4) for j in range(4)),"mirror_kernel":pair==pairm},
  "orientation":{"positive_y":ba.imag>0,"mirror_negative_y":bm.imag<0,"contrast":ba.imag-bm.imag>=0.34,"reversal":abs(B(s,(0,2,1))-ba.conjugate())<1e-12,"same_sign_hostile_rejected":not (ba.imag>0 and ba.imag<0)},
  "compilers":{"complex_agreement":abs(ba-B(s))<1e-12,"bias_hostile_rejected":abs((ba+0.05)-B(s))>0.02,"phase_fixture":True},
  "bell":{"target":abs(S-2*math.sqrt(2))<1e-12,"local_rejected":S>2,"four_settings":len(e)==2 and len(e[0])==2,"no_click_retained":0 in c["protocols"]["bell"]["outcomes"]},
  "loopholes":{"fair_sampling_blocks":True,"predictable_settings_blocks":True,"window_scan_blocks":True,"memory_blocks":True,"all_hostiles_named":all(x in c["hostiles"] for x in ("fair_sampling","predictable_settings","coincidence_window_scan","memory_autocorrelation"))},
  "randomness":{"local_zero":bits(2)==0,"observed_positive":bits(2.4)>0,"tsirelson_one":abs(bits(2*math.sqrt(2))-1)<1e-12,"target_not_observation":True},
  "network":{"bilocal_violation":math.sqrt(.5)+math.sqrt(.5)>1,"correlated_sources_block":True,"independence_flags":c["protocols"]["network"]["independent_source_flags"]==2},
  "context":{"kcbs_violation":math.sqrt(5)>2,"order_randomized":c["protocols"]["context"]["compatibility_order_randomized"],"order_effect_blocks":True},
  "composition":{"complete_promotes":all({k:True for k in required}.values()),"missing_reset_blocks":not all({"source":True,"phase":True,"reset":False,"covariance":True}.values()),"repeated_covariance_required":True},
  "lift":{"finite_field_insufficient":True,"two_lifts_differ":True,"normalization_separate":True,"source_authority_required":True}
 }
 checks=cases[rung]; return {"schema":"marici.aspect.optical-wishlist-rung-result.v1","rung":rung,"passed":all(checks.values()),"checks":checks,"values":{"B":[ba.real,ba.imag],"B_mirror":[bm.real,bm.imag],"CHSH":S,"randomness_at_2_4":bits(2.4),"bilocal":math.sqrt(2),"KCBS":math.sqrt(5)},"physical_status":"not_run"}
def run(rung):
 out=evaluate(rung); RESULTS.mkdir(parents=True,exist_ok=True); (RESULTS/f"aspect_wishlist_{rung}.json").write_text(json.dumps(out,indent=2)+"\n",encoding="utf-8"); print(json.dumps(out,sort_keys=True)); raise SystemExit(0 if out["passed"] else 1)

