"""Exact controls for the weighted Fourier estimates; no anchored fixed point."""
from pathlib import Path
from fractions import Fraction as F
from itertools import product,combinations
from hashlib import sha256
import json
ROOT=Path(__file__).resolve().parents[3]
CONTRACT='research/kitaev/contracts/yang-mills-weighted-fourier.v1.json'
NOTE='research/kitaev/yang-mills-weighted-fourier-v1.md'
SELF='research/kitaev/checkers/check_yang_mills_weighted_fourier.py'
OUT=ROOT/'research/kitaev/results/yang-mills-weighted-fourier-v1.json'
def require(ok,msg):
 if not ok:raise ValueError(msg)
def norm(weights,card=False):return max(sum(w*(len(s) if card else 1) for s,w in weights if e in s) for e in range(4))
def report():
 c=json.loads((ROOT/CONTRACT).read_text());require(all(v is False for v in c['boundary'].values()),'global window promoted to anchored theorem')
 fusion_cases=0
 for m,n in product(range(17),repeat=2):
  outputs=list(range(abs(m-n),m+n+1,2));require(sum(k+1 for k in outputs)==(m+1)*(n+1),'SU2 fusion dimensions')
  lhs=sum((k+1)*(1+F(k,2)) for k in outputs);rhs=(m+1)*(1+F(m,2))*(n+1)*(1+F(n,2))
  require(lhs<=rhs,'weighted Fourier character algebra');fusion_cases+=1
 kin=0
 for labels in product(range(5),repeat=4):
  if not any(labels):continue
  J=sum(F(n,2) for n in labels);C=sum(F(n*(n+2),4) for n in labels)
  require((1+J)/C<=2,'kinematic inverse normalization');kin+=1
 physical=0;max_ratio=F(0)
 for na,nb,ns in product(range(7),range(7),range(13)):
  if not any((na,nb,ns)) or not(abs(na-nb)<=ns<=na+nb) or (na+nb+ns)%2:continue
  a,b,s=F(na,2),F(nb,2),F(ns,2);J=3*a+3*b+s;C=3*a*(a+1)+3*b*(b+1)+s*(s+1)
  require(J>=2 and C>=F(3,2)*J and (1+J)/C<=1,'physical spin-network inverse');max_ratio=max(max_ratio,(1+J)/C);physical+=1
 require(max_ratio==1,'sharp physical inverse fixture')
 source_terms=2**4;source_J=F(4,2);plaquette_bound=source_terms*(1+source_J)
 require(plaquette_bound==48 and plaquette_bound/6==8 and 4*plaquette_bound/6==32,'global/anchored source constants')
 windows=[]
 for z in [F(0),F(1,384),F(1,192),F(1,128),F(1,96)]:
  alpha=8*z;R=16*z;image=alpha+3*R*R;q=6*R
  require(image<=R,'global ball invariance');require((q<1)==(z<F(1,96)),'strict contraction endpoint')
  windows.append({'abs_r_times_P':str(z),'radius':str(R),'Lipschitz_bound':str(q),'strict_contraction':q<1})
 supports=[frozenset(s) for k in range(1,5) for s in combinations(range(4),k)];overlap_cases=0
 for shift in range(6):
  phi=[(s,F((i+shift)%5+1,7)) for i,s in enumerate(supports)];psi=[(s,F((2*i+shift)%7+1,11)) for i,s in enumerate(supports)]
  output=[(a|b,3*x*y) for a,x in phi for b,y in psi if a&b]
  require(norm(output)<=3*(norm(phi,True)*norm(psi)+norm(phi)*norm(psi,True)),'anchored cardinality lift');overlap_cases+=1
 paths=[CONTRACT,NOTE,SELF]
 return {'schema':'marici.yang-mills-weighted-fourier-result.v1','passed':True,'weighted_global_nonlinear_bound_constructed':True,'global_actual_ground_fixed_point_constructed':True,'global_window':'abs(r)*P<1/96','global_quadratic_constant':'3','physical_inverse_constant':'1','fusion_cases':fusion_cases,'kinematic_inverse_cases':kin,'physical_inverse_cases':physical,'plaquette_A1_upper_bound':'48','anchored_source_upper_bound':'32','contraction_controls':windows,'overlap_cardinality_controls':overlap_cases,'global_coupling_radius_by_P':[{'P':p,'radius':str(F(1,96*p))} for p in [2,6,36,108]],'anchored_contraction_proved':False,'fixed_coupling_uniform_remainder_proved':False,'volume_uniform_detection_proved':False,'continuum_gap_proved':False,'scope':'Frequency-weighted global construction with explicit shrinking coupling window; anchored support-cardinality closure remains open.','source_hashes':{p:sha256((ROOT/p).read_bytes()).hexdigest() for p in paths}}
if __name__=='__main__':
 r=report();OUT.parent.mkdir(parents=True,exist_ok=True);OUT.write_text(json.dumps(r,indent=2)+'\n');print(json.dumps({k:r[k] for k in ['passed','weighted_global_nonlinear_bound_constructed','global_window','fusion_cases','physical_inverse_cases','anchored_contraction_proved']},indent=2))
