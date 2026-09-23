"""Competing normalizers joined by typed surplus-sized redistribution."""
from fractions import Fraction as Q
from itertools import product
from pathlib import Path
import json
def valid(p,T):
 a,u,v,c=map(Q,p);return min(a,u,v,c)>=0 and u+v-a==1 and u+v+c==Q(T)
def n(p,T,which):
 assert valid(p,T)
 a,u,v,c=map(Q,p)
 q=(a+c,u+c,v,Q(0)) if which=='A' else (a+c,u,v+c,Q(0))
 assert valid(q,T);return q
def r(p,T,theta):
 assert valid(p,T)
 a,u,v,c=map(Q,p);theta=Q(theta)
 if not -v<=theta<=u:raise ValueError('TRANSFER_OVERDRAW')
 q=(a,u-theta,v+theta,c);assert valid(q,T);return q
checks=0;nonzero=0
for T,u,v in product((Q(2),Q(3),Q(4)),(Q(1),Q(3,2),Q(2)),(Q(0),Q(1,2),Q(1))):
 a=u+v-1;c=T-u-v
 if min(a,c)<0:continue
 p=(a,u,v,c);assert valid(p,T)
 assert r(n(p,T,'A'),T,c)==n(p,T,'B')
 for theta in (Q(0),Q(1,2),-v):
  if not -v<=theta<=u:continue
  # Each chosen normalizer commutes with redistribution on proof packets.
  for side in ('A','B'):
   assert n(r(p,T,theta),T,side)==r(n(p,T,side),T,theta)
  # Two route changes (switch normalizer, then redistribute) form
  # a commuting PACKET diagram with transfer parameter c+theta.
  assert n(r(p,T,theta),T,'B')==r(n(p,T,'A'),T,c+theta)
  checks+=1
  if c:nonzero+=1
assert checks>20 and nonzero>0
p=(Q(0),Q(1),Q(0),Q(1));assert r(n(p,2,'A'),2,1)==n(p,2,'B')
# A weakening 2->3 injects one more unit of surplus; the bridge grows to 2.
w=(p[0],p[1],p[2],p[3]+1)
assert r(n(w,3,'A'),3,2)==n(w,3,'B')
try:r(n(p,2,'A'),2,3)
except ValueError:overdraw_refused=True
else:raise AssertionError('overspent transfer')
report={'passed':True,'interchange_squares_checked':checks,'nonzero_surplus_cases':nonzero,'normalizer_bridge':'R_c N_A(p)=N_B(p) for duplicated upper rows at L=1','interchange':'N_B R_theta(p)=R_(c+theta) N_A(p); N_i R_theta=R_theta N_i on typed packets','target_weakening':'bridge parameter grows by injected surplus','overdraw_refused':overdraw_refused,'scope':'Packet-level equalities on three separately rooted primitive rows; symbolic 2-cell paths and any 3/4-cell interchange still unadmitted, no analytic or operational authority.'}
out=Path(__file__).resolve().parents[1]/'results/redistribution-normalization-interchange.json';out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
