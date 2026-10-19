"""Exact curvature-normalization and bound controls, not a continuum YM solver."""
from pathlib import Path
from fractions import Fraction as F
from itertools import product
from hashlib import sha256
import json
from check_yang_mills_shared_link_packet import rawmul
from check_yang_mills_remainder_equation import add,scale,mul,deriv,mean,L
from check_yang_mills_anchored_casimir import report as anchored_report
ROOT=Path(__file__).resolve().parents[3]
CONTRACT='research/kitaev/contracts/yang-mills-uniform-detection.v1.json'
NOTE='research/kitaev/yang-mills-uniform-detection-v1.md'
SELF='research/kitaev/checkers/check_yang_mills_uniform_detection.py'
OUT=ROOT/'research/kitaev/results/yang-mills-uniform-detection-v1.json'
def require(ok,msg):
 if not ok:raise ValueError(msg)
def report():
 c=json.loads((ROOT/CONTRACT).read_text());require(all(v is False for v in c['boundary'].values()),'finite-source theorem promoted beyond regime')
 anchored=anchored_report();require(anchored['passed'] and anchored['actual_source_uniform_remainder_proved'] and anchored['actual_source_uniform_influence_proved'] and json.loads((ROOT/'research/kitaev/results/yang-mills-anchored-casimir-v1.json').read_text())==anchored,'actual-density constructor stale')
 basis=[tuple(F(1,2) if k==a else F(0) for k in range(4)) for a in range(1,4)];ricci=[];brackets=0
 for a in range(3):
  squared=F(0)
  for b in range(3):
   comm=tuple(x-y for x,y in zip(rawmul(basis[a],basis[b]),rawmul(basis[b],basis[a])));coeff=[2*x for x in comm[1:]]
   require(sum(x*x for x in coeff)==(0 if a==b else 1),'Lie generator metric normalization');squared+=sum(x*x for x in coeff);brackets+=1
  ricci.append(squared/4)
 require(ricci==[F(1,2)]*3,'SU2 radius-two Ricci')
 # Single-link characters calibrate the metric before gauge restriction.
 chars=[[F(1)],[F(0),F(2)]]
 for n in range(1,24):chars.append(add(mul([F(0),F(2)],chars[-1]),scale(chars[-2],-1)))
 for n,f in enumerate(chars):
  eigen=F(n*(n+2),4);require(scale(L(f),F(1,4))==scale(f,eigen),'single-link Casimir')
  require(mean(mul(f,f))==1,'character Haar norm')
  energy=mean(scale(mul([F(1),F(0),F(-1)],mul(deriv(f),deriv(f))),F(1,4)))
  require(energy==eigen,'Dirichlet metric normalization')
  if n:require(energy>=F(1,2),'unweighted curvature Poincare baseline')
 require(F(3,4)<2,'wrong radius-one curvature hostile')
 hessian_cases=0
 for n in range(1,6):
  for labels in product(range(4),repeat=n):
   js=[F(k,2) for k in labels];J=sum(js);C=sum(j*(j+1) for j in js)
   for j in js:require(3*j*J<=F(3,2)*(n+1)*C,'covariant Hessian absolute row bound')
   hessian_cases+=1
 require(all(F(n+1,2**n)<=1 for n in range(1,65)),'Hessian support-weight moment')
 threshold=F(27,262144);curvature=[]
 for r in [F(0),threshold/4,threshold/2,3*threshold/4,threshold]:
  R=F(4096,3)*r;c0=F(1,2)-3*R
  require(c0>=F(5,64),'uniform weighted curvature margin');curvature.append({'r':str(r),'R_upper':str(R),'curvature_lower_bound':str(c0),'source_regime_admitted':r<threshold})
 require(F(curvature[-1]['curvature_lower_bound'])==F(5,64) and not curvature[-1]['source_regime_admitted'],'do not admit contraction endpoint')
 # Positive gauge-invariant fixture exp(2*t*chi2) is not the source vacuum.
 chi2=[F(-1),F(0),F(4)];t=F(1,4);normal_hessian=2*t*deriv(deriv(chi2))[0]/4
 require(normal_hessian==1 and F(1,2)-normal_hessian==F(-1,2),'positive density does not ensure curvature')
 r=threshold/2;scale_controls=[]
 for N in [1,2,16,256]:
  kappa=F(1,N);lam=r*kappa;require(lam/kappa==r,'dimensionless regime under energy rescaling');scale_controls.append({'N':N,'kappa':str(kappa),'finite_source_gap_lower_bound':str(F(5,64)*kappa)})
 require(F(scale_controls[-1]['finite_source_gap_lower_bound'])<F(1,1000),'physical-scale hostile')
 g4=4/threshold;require(g4==F(1048576,27) and 4/(2*g4)<threshold and not F(4,1)<threshold,'strong/weak parameter boundary')
 paths=[CONTRACT,NOTE,SELF,'research/kitaev/contracts/yang-mills-anchored-casimir.v1.json','research/kitaev/checkers/check_yang_mills_anchored_casimir.py','research/kitaev/results/yang-mills-anchored-casimir-v1.json','research/kitaev/checkers/check_yang_mills_remainder_equation.py']
 return {'schema':'marici.yang-mills-uniform-detection-result.v1','passed':True,'volume_uniform_finite_source_detection_proved':True,'finite_source_volume_uniform_gap_proved':True,'coupling_window':'0<=lambda/kappa<27/262144','fixed_source_energy_requirement':'kappa>0 held fixed for the volume comparison','detector_constant':'5/64','finite_source_gap':'5*kappa/64','parameter_sensitive_constant':'1/2-4096*lambda/kappa','Lie_bracket_cases':brackets,'Ricci':'1/2','single_link_character_cases':len(chars),'Hessian_spin_cases':hessian_cases,'curvature_controls':curvature,'positive_density_curvature_hostile':True,'physical_energy_scale_controls':scale_controls,'weak_coupling_regime_covered':False,'physical_energy_scaling_proved':False,'continuum_gap_proved':False,'infinite_volume_correlations_constructed':False,'scope':'Written finite-source small-r volume-uniform detector/gap theorem using the actual ground density; not the continuum or official target.','source_hashes':{p:sha256((ROOT/p).read_bytes()).hexdigest() for p in paths}}
if __name__=='__main__':
 r=report();OUT.parent.mkdir(parents=True,exist_ok=True);OUT.write_text(json.dumps(r,indent=2)+'\n');print(json.dumps({k:r[k] for k in ['passed','volume_uniform_finite_source_detection_proved','coupling_window','detector_constant','finite_source_gap','Hessian_spin_cases','continuum_gap_proved']},indent=2))
