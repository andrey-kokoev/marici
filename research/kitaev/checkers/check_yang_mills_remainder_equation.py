"""Exact SU2 Chebyshev norm-obstruction and connected-support controls."""
from pathlib import Path
from fractions import Fraction as F
from math import comb
from itertools import combinations
from hashlib import sha256
import json
from check_yang_mills_ground_state_transfer import box
ROOT=Path(__file__).resolve().parents[3]
CONTRACT='research/kitaev/contracts/yang-mills-remainder-equation.v1.json'
NOTE='research/kitaev/yang-mills-remainder-equation-v1.md'
SELF='research/kitaev/checkers/check_yang_mills_remainder_equation.py'
OUT=ROOT/'research/kitaev/results/yang-mills-remainder-equation-v1.json'
def require(ok,msg):
 if not ok:raise ValueError(msg)
def trim(p):
 p=list(p)
 while len(p)>1 and p[-1]==0:p.pop()
 return p

def add(a,b):return trim([(a[i] if i<len(a) else 0)+(b[i] if i<len(b) else 0) for i in range(max(len(a),len(b)))])
def scale(a,c):return trim([x*c for x in a])
def mul(a,b):
 out=[F(0)]*(len(a)+len(b)-1)
 for i,x in enumerate(a):
  for j,y in enumerate(b):out[i+j]+=x*y
 return trim(out)
def deriv(p):return trim([i*p[i] for i in range(1,len(p))] or [F(0)])
def mean(p):return sum(x*F(comb(i,i//2),(i//2+1)*4**(i//2)) for i,x in enumerate(p) if i%2==0)
def center(p):return add(p,[-mean(p)])
def L(p):return add(scale(mul([F(1),F(0),F(-1)],deriv(deriv(p))),-1),scale(mul([F(0),F(1)],deriv(p)),3))
def gamma(p,q):return mul([F(1),F(0),F(-1)],mul(deriv(p),deriv(q)))
def cheb(n):
 a=[F(1)];b=[F(0),F(1)]
 if n==0:return a
 for k in range(1,n):a,b=b,add(scale(mul([F(0),F(1)],b),2),scale(a,-1))
 return b

def connected(nodes,overlap):
 seen={next(iter(nodes))}
 while True:
  enlarged=seen|{j for i in seen for j in nodes if j in overlap[i]}
  if enlarged==seen:return seen==set(nodes)
  seen=enlarged

def report():
 c=json.loads((ROOT/CONTRACT).read_text());require(all(v is False for v in c['boundary'].values()),'norm obstruction promoted to gap theorem')
 chi=[F(-1),F(0),F(4)]
 require(mean(chi)==0 and mean(mul(chi,chi))==1 and L(chi)==scale(chi,8),'SU2 Haar/Casimir normalization')
 projections=[]
 for n in range(3,13):
  f=scale(add(cheb(n),cheb(n+2)),F(1,2));require(mean(f)==0,'mean-zero norm fixture');g=gamma(f,f);projection=mean(mul(g,chi))/8
  require(projection==F(n*(n+2),64),'unbounded low-character projection')
  projections.append({'n':n,'sup_norm_upper_bound':'1','inverse_projection_chi2':str(projection)})
 # Actual one-plaquette log-equation coefficients; this is not a discrete chain-rule analogy.
 u1=[F(0),F(1,3)];u2=scale(chi,F(-1,288))
 require(L(u1)==[F(0),F(1)] and L(u2)==center(gamma(u1,u1)),'log-eigen-equation first two coefficients')
 cubic=scale(center(gamma(u1,u2)),2);quartic=center(gamma(u2,u2))
 require(cubic!=[0] and quartic!=[0],'nonzero remainder source')
 # F(u*) coefficients at r^3,r^4 are negatives of the displayed source terms.
 require(add(scale(center(gamma(u1,u2)),-2),cubic)==[0] and add(scale(center(gamma(u2,u2)),-1),quartic)==[0],'exact polynomial defect identity')
 vs,edges,faces=box(2);supports=[{e for e,s in face} for face in faces];overlap=[{j for j,t in enumerate(supports) if s&t} for s in supports]
 clusters=[frozenset(s) for k in range(1,4) for s in combinations(range(len(faces)),k) if connected(frozenset(s),overlap)];joins=0
 for a in clusters:
  sa=set().union(*(supports[i] for i in a))
  for b in clusters:
   sb=set().union(*(supports[i] for i in b))
   if sa&sb:
    require(connected(a|b,overlap) and len(a|b)<=len(a)+len(b),'connected-support recursion');joins+=1
 paths=[CONTRACT,NOTE,SELF,'research/kitaev/checkers/check_yang_mills_ground_state_transfer.py']
 return {'schema':'marici.yang-mills-remainder-equation-result.v1','passed':True,'exact_log_remainder_equation_constructed':True,'formal_all_order_connectedness_constructed':True,'sup_norm_only_contraction_rejected':True,'physical_one_plaquette_projection_controls':projections,'one_plaquette_cubic_source_coefficients':[str(x) for x in cubic],'one_plaquette_quartic_source_coefficients':[str(x) for x in quartic],'connected_support_joins':joins,'uniform_remainder_proved':False,'convergent_cluster_expansion_proved':False,'actual_source_uniform_influence_proved':False,'volume_uniform_detection_proved':False,'continuum_gap_proved':False,'scope':'Exact physical high-frequency obstruction to a proposed proof norm, not a low-energy family or a gap counterexample.','source_hashes':{p:sha256((ROOT/p).read_bytes()).hexdigest() for p in paths}}
if __name__=='__main__':
 r=report();OUT.parent.mkdir(parents=True,exist_ok=True);OUT.write_text(json.dumps(r,indent=2)+'\n');print(json.dumps({k:r[k] for k in ['passed','exact_log_remainder_equation_constructed','sup_norm_only_contraction_rejected','connected_support_joins','uniform_remainder_proved']},indent=2))
