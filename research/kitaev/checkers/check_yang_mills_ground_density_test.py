"""Exact controls for fixed-source Taylor equations, not a uniform cluster proof."""
from pathlib import Path
from fractions import Fraction as F
from itertools import product
from hashlib import sha256
import json
from check_yang_mills_shared_link_packet import I,lift,obs,jm,rawmul
ROOT=Path(__file__).resolve().parents[3]
CONTRACT='research/kitaev/contracts/yang-mills-ground-density-test.v1.json'
NOTE='research/kitaev/yang-mills-ground-density-test-v1.md'
SELF='research/kitaev/checkers/check_yang_mills_ground_density_test.py'
OUT=ROOT/'research/kitaev/results/yang-mills-ground-density-test-v1.json'
def require(ok,msg):
 if not ok:raise ValueError(msg)
def coefficients(jets):
 p,q,f,f0,f1=obs(jets);s=tuple(x+y for x,y in zip(p,q));pp=jm(p,p);qq=jm(q,q)
 a=tuple(x/6 for x in s);b=tuple((pp[k]+qq[k]-(2 if k==0 else 0))/96+f0[k]/27+f1[k]/39 for k in range(3))
 return a,b

def casimir(links):
 out=[F(0),F(0)]
 for e in range(7):
  for axis in range(1,4):
   unit=tuple(F(k==axis) for k in range(4));vel=tuple(x/2 for x in rawmul(unit,links[e]));jets=[lift(q) for q in links];jets[e]=tuple((x,v,-x/8) for x,v in zip(links[e],vel))
   for k,j in enumerate(coefficients(jets)):out[k]-=2*j[2]
 return out

def log2(links):
 jets=[lift(q) for q in links];a,b=coefficients(jets);p,q,f,f0,f1=[x[0] for x in obs(jets)];ell=2*b[0]-a[0]**2-F(1,18);target=-(p*p+q*q-2)/144-F(1,9)+f0/54-f1/234
 require(ell==target,'normalized log-density coefficient');require(2*b[0]+a[0]**2-F(1,18)==ell+2*a[0]**2,'density/exponential normalization')
 return ell

def variance(probs,vals):
 mean=sum(p*x for p,x in zip(probs,vals));return sum(p*(x-mean)**2 for p,x in zip(probs,vals))
def report():
 c=json.loads((ROOT/CONTRACT).read_text());require(all(v is False for v in c['boundary'].values()),'unproved promotion')
 qs=[I,(F(0),F(1),F(0),F(0)),(F(0),F(0),F(1),F(0)),(F(0),F(0),F(0),F(1)),(F(3,5),F(4,5),F(0),F(0)),(F(5,13),F(0),F(12,13),F(0))]
 samples=[[qs[(r+k)%6] for k in range(7)] for r in range(6)]+[[I,qs[1],I,I,qs[1],I,I],[I,qs[1],I,I,qs[2],I,I],[I]*7]
 for links in samples:
  p,q,*_=[v[0] for v in obs([lift(q) for q in links])];la,lb=casimir(links)
  require(la==(p+q)/2 and lb==(p+q)**2/12-F(1,6),'actual Casimir perturbation equations');log2(links)
 difference=log2(samples[-3])-log2(samples[-2]);require(difference==F(8,351),'equal-trace density hostile')
 axes=[tuple(F(s if k==i else 0) for k in range(4)) for i in range(4) for s in (-1,1)];mean_a2=F(0);mean_b=F(0);mean_ell=F(0)
 for x in axes:
  for y in axes:
   links=[I,x,I,I,y,I,I];a,b=coefficients([lift(q) for q in links]);mean_a2+=a[0]**2/64;mean_b+=b[0]/64;mean_ell+=log2(links)/64
 require((mean_a2,mean_b,mean_ell)==(F(1,18),F(0),F(-1,9)),'exact Haar Taylor normalization')
 require(mean_ell+2*mean_a2==0,'normalized density mass')
 # Exact product-measure Efron-Stein controls, not interacting SU2 estimates.
 px=[F(1,3),F(2,3)];py=[F(2,5),F(3,5)];joint=[px[i]*py[j] for i in range(2) for j in range(2)];tensor_cases=0
 for vals in product(map(F,range(-1,2)),repeat=4):
  cond_x=sum(py[j]*variance(px,[vals[j],vals[2+j]]) for j in range(2));cond_y=sum(px[i]*variance(py,[vals[2*i],vals[2*i+1]]) for i in range(2))
  require(variance(joint,vals)<=cond_x+cond_y,'product tensorization');tensor_cases+=1
 weighted_cases=0
 for p in [F(1,8),F(1,3),F(2,5),F(1,2)]:
  m=min(2*p,2*(1-p));M=max(2*p,2*(1-p))
  for u,v in product(map(F,range(-2,3)),repeat=2):
   require(variance([p,1-p],[u,v])<=M/m*(u-v)**2/4,'conditional density comparison');weighted_cases+=1
 require(F(3,4)!=3,'conditioned-link versus physical-loop normalization')
 radii=[{'P':P,'sufficient_projection_radius':str(F(3,2*P))} for P in [2,6,36,108]]
 paths=[CONTRACT,NOTE,SELF,'research/kitaev/checkers/check_yang_mills_shared_link_packet.py']
 return {'schema':'marici.yang-mills-ground-density-test-result.v1','passed':True,'fixed_graph_perturbation_constructed':True,'individual_plaquette_density_shortcut_rejected':True,'direct_Casimir_coefficient_cases':len(samples),'equal_trace_log_density_difference_r2':str(difference),'Haar_mean_a_squared':str(mean_a2),'Haar_mean_b':str(mean_b),'normalized_log_density_mean_r2':str(mean_ell),'product_tensorization_cases':tensor_cases,'conditional_comparison_cases':weighted_cases,'finite_projection_radius_controls':radii,'conditional_tensorization_proved_for_source':False,'volume_uniform_detection_proved':False,'continuum_gap_proved':False,'scope':'Fixed finite-source analytic Taylor theorem plus exact rational regressions; conditional uniform-gap criterion has unproved interacting-source premises.','source_hashes':{p:sha256((ROOT/p).read_bytes()).hexdigest() for p in paths}}
if __name__=='__main__':
 r=report();OUT.parent.mkdir(parents=True,exist_ok=True);OUT.write_text(json.dumps(r,indent=2)+'\n');print(json.dumps({k:r[k] for k in ['passed','direct_Casimir_coefficient_cases','equal_trace_log_density_difference_r2','product_tensorization_cases','conditional_comparison_cases','volume_uniform_detection_proved']},indent=2))
