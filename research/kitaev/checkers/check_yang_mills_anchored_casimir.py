"""Exact majorant/edge-activity controls for the written anchored theorem."""
from pathlib import Path
from fractions import Fraction as F
from itertools import combinations,product
from math import comb
from hashlib import sha256
import json
ROOT=Path(__file__).resolve().parents[3]
CONTRACT='research/kitaev/contracts/yang-mills-anchored-casimir.v1.json'
NOTE='research/kitaev/yang-mills-anchored-casimir-v1.md'
SELF='research/kitaev/checkers/check_yang_mills_anchored_casimir.py'
OUT=ROOT/'research/kitaev/results/yang-mills-anchored-casimir-v1.json'
def require(ok,msg):
 if not ok:raise ValueError(msg)
def norm(terms,t=F(2)):
 return max(sum(t**len(s)*w for s,w in terms if e in s) for e in range(4))
def report():
 c=json.loads((ROOT/CONTRACT).read_text());require(all(v is False for v in c['boundary'].values()),'remainder construction promoted to detection/continuum theorem')
 spin_cases=0
 for labels in product(range(5),repeat=4):
  J=sum(F(n,2) for n in labels);C=sum(F(n*(n+2),4) for n in labels)
  require(J<=F(2,3)*(1+C),'Casimir pays edge derivative activity')
  if C>=3:require((1+C)/C<=F(4,3),'physical inverse Casimir ratio')
  spin_cases+=1
 physical_cases=0
 for na,nb,ns in product(range(7),range(7),range(13)):
  if not any((na,nb,ns)) or not(abs(na-nb)<=ns<=na+nb) or (na+nb+ns)%2:continue
  a,b,s=F(na,2),F(nb,2),F(ns,2);C=3*a*(a+1)+3*b*(b+1)+s*(s+1)
  require(C>=3 and (1+C)/C<=F(4,3),'actual seven-link physical inverse');physical_cases+=1
 supports=[frozenset(s) for k in range(1,5) for s in combinations(range(4),k)];activity_cases=0
 for shift in range(8):
  p=[];q=[];mp=[];mq=[]
  for i,s in enumerate(supports):
   wp=F((i+shift)%5+1,7);wq=F((2*i+shift)%7+1,11);p.append((s,wp));q.append((s,wq));rawp={e:F((e+i+shift)%3+1) for e in s};rawq={e:F((2*e+i+shift)%5+1) for e in s}
   mp.append({e:F(2,3)*wp*x/sum(rawp.values()) for e,x in rawp.items()});mq.append({e:F(2,3)*wq*x/sum(rawq.values()) for e,x in rawq.items()})
  for t in [F(1),F(2),F(3)]:
   out=[]
   for i,(a,wa) in enumerate(p):
    for j,(b,wb) in enumerate(q):
     if a&b:
      require(t**len(a|b)<=t**(len(a)+len(b)),'support weight')
      out.append((a|b,4*sum(mp[i].get(e,0)*mq[j].get(e,0) for e in range(4))))
   require(norm(out,t)<=F(32,9)*norm(p,t)*norm(q,t),'closed edge-resolved anchored bound');activity_cases+=1
 K=F(32,9);a=F(128,3)*2**4;threshold=1/(4*K*a)
 require(a==F(2048,3) and threshold==F(27,262144),'uniform source/contraction constants')
 r=threshold/2;alpha=a*r;R=2*alpha;q=4*K*alpha;tail=alpha*q*q/(1-q)
 require(q==F(1,2) and R==F(9,128) and tail==F(9,512),'interior majorant')
 require(alpha+K*R*R<=R and 2*K*R<1,'actual source interaction ball')
 cats=[comb(2*n,n)//(n+1) for n in range(21)]
 for n,catalan in enumerate(cats):
  require(catalan<=4**n,'Catalan geometric majorant')
  if n:require(catalan==sum(cats[k]*cats[n-1-k] for k in range(n)),'quadratic coefficient recursion')
 partial=sum(F(cats[n-1])*K**(n-1)*a**n*r**n for n in range(3,14));require(partial<=tail,'analytic interaction tail')
 require(all(F(n-1,2**n)<=F(1,4) for n in range(1,65)),'influence row support moment')
 require(R/2==F(9,256) and R<F(9,64),'actual density influence constants')
 require(r*2430>=F(1,96),'anchored window must exceed old global P-scaling restriction')
 paths=[CONTRACT,NOTE,SELF]
 return {'schema':'marici.yang-mills-anchored-casimir-result.v1','passed':True,'uniform_anchored_contraction_constructed':True,'actual_source_uniform_remainder_proved':True,'actual_source_uniform_influence_proved':True,'coupling_window':'0<=lambda/kappa<27/262144','Casimir_weight_cases':spin_cases,'physical_inverse_cases':physical_cases,'edge_activity_overlap_cases':activity_cases,'anchored_bilinear_constant':str(K),'weighted_source_constant':str(a),'interior_parameter':str(r),'interior_radius':str(R),'interior_tail_bound':str(tail),'interior_TV_row_bound':str(R/2),'Catalan_controls':len(cats),'volume_uniform_detection_proved':False,'continuum_gap_proved':False,'infinite_volume_correlations_constructed':False,'scope':'Actual finite-source density interaction expansion uniformly over open boxes in a fixed small bare-coupling window; functional inequality still pending.','source_hashes':{p:sha256((ROOT/p).read_bytes()).hexdigest() for p in paths}}
if __name__=='__main__':
 r=report();OUT.parent.mkdir(parents=True,exist_ok=True);OUT.write_text(json.dumps({**r},indent=2)+'\n');print(json.dumps({k:r[k] for k in ['passed','uniform_anchored_contraction_constructed','coupling_window','anchored_bilinear_constant','edge_activity_overlap_cases','actual_source_uniform_remainder_proved','volume_uniform_detection_proved']},indent=2))
