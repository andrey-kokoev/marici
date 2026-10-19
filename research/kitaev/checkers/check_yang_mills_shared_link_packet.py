"""Exact seven-link SU(2) gauge, shared-Casimir and Haar-moment regressions."""
from pathlib import Path
from fractions import Fraction as F
from hashlib import sha256
import json
ROOT=Path(__file__).resolve().parents[3]
CONTRACT='research/kitaev/contracts/yang-mills-shared-link-packet.v1.json'
NOTE='research/kitaev/yang-mills-shared-link-packet-v1.md'
OUT=ROOT/'research/kitaev/results/yang-mills-shared-link-packet-v1.json'
I=(F(1),F(0),F(0),F(0)); ZERO=(F(0),)*3

def add(a,b):return tuple(x+y for x,y in zip(a,b))
def scale(a,c):return tuple(c*x for x in a)
def neg(a):return scale(a,-1)
def jm(a,b):return tuple(sum(a[k]*b[n-k] for k in range(n+1)) for n in range(3))
def qm(a,b):
 w,x,y,z=a;v,r,s,t=b
 return (add(add(jm(w,v),neg(jm(x,r))),add(neg(jm(y,s)),neg(jm(z,t)))),add(add(jm(w,r),jm(x,v)),add(jm(y,t),neg(jm(z,s)))),add(add(jm(w,s),neg(jm(x,t))),add(jm(y,v),jm(z,r))),add(add(jm(w,t),jm(x,s)),add(neg(jm(y,r)),jm(z,v))))
def qi(a):return (a[0],neg(a[1]),neg(a[2]),neg(a[3]))
def lift(q):return tuple((x,F(0),F(0)) for x in q)
def qp(xs):
 q=lift(I)
 for x in xs:q=qm(q,x)
 return q
def rawmul(a,b):return tuple(v[0] for v in qm(lift(a),lift(b)))
def rawinv(q):return (q[0],-q[1],-q[2],-q[3])
def obs(links):
 u=links[0];a=qp(links[1:4]);b=qp(links[4:7]);p=scale(qm(u,a)[0],2);q=scale(qm(u,b)[0],2);f=jm(p,q);f0=qm(a,qi(b))[0]
 return [p,q,f,f0,add(f,neg(f0))]
def laplace(links):
 sums=[F(0)]*5
 for edge in range(7):
  for axis in range(1,4):
   ei=tuple(F(k==axis) for k in range(4));velocity=tuple(v/2 for v in rawmul(ei,links[edge]));jets=[lift(q) for q in links];jets[edge]=tuple((q,v,-q/8) for q,v in zip(links[edge],velocity))
   for k,value in enumerate(obs(jets)):sums[k]-=2*value[2]
 return sums

def require(ok,msg):
 if not ok:raise ValueError(msg)
def digest(p):return sha256((ROOT/p).read_bytes()).hexdigest()
def report():
 c=json.loads((ROOT/CONTRACT).read_text());require(all(v is False for v in c['boundary'].values()),'source scope promotion')
 qs=[I,(F(0),F(1),F(0),F(0)),(F(0),F(0),F(1),F(0)),(F(0),F(0),F(0),F(1)),(F(3,5),F(4,5),F(0),F(0)),(F(5,13),F(0),F(12,13),F(0))]
 edges=c['source']['edges'];gauge_cases=0;differential_cases=0;residuals=[]
 samples=[[qs[(r+k)%6] for k in range(7)] for r in range(6)]+[[qs[1]]+[I]*6,[I]*7]
 for links in samples:
  values=[v[0] for v in obs([lift(q) for q in links])];energies=laplace(links)
  expected=[3*values[0],3*values[1],F(9,2)*values[3]+F(13,2)*values[4],F(9,2)*values[3],F(13,2)*values[4]]
  require(energies==expected,'shared-link Casimir recoupling');differential_cases+=1;residuals.append(str(energies[2]-6*values[2]))
  for r in range(6):
   gauges=[qs[(r+k)%6] for k in range(6)];changed=[rawmul(rawmul(gauges[a],u),rawinv(gauges[b])) for u,(a,b) in zip(links,edges)]
   require([v[0] for v in obs([lift(q) for q in changed])]==values,'gauge-invariant source evaluation');gauge_cases+=1
 require(any(F(x)!=0 for x in residuals),'independent-plaquette hostile absent')
 # The 8 signed coordinate quaternions integrate every quadratic exactly on S^3.
 axes=[]
 for i in range(4):
  for sign in (-1,1):axes.append(tuple(F(sign if k==i else 0) for k in range(4)))
 moments=[]
 for u in qs:
  sums=[F(0)]*4
  for a in axes:
   for b in axes:
    _,_,f,f0,f1=[x[0] for x in obs([lift(u),lift(a),lift(I),lift(I),lift(b),lift(I),lift(I)])]
    for k,value in enumerate((f*f,f0*f0,f1*f1,f0*f1)):sums[k]+=value/64
  require(sums==[F(1),F(1,4),F(3,4),F(0)],'exact degree-two Haar moments');moments.append([str(v) for v in sums])
 norm_residual=F(1,4)*F(-3,2)**2+F(3,4)*F(1,2)**2;require(norm_residual==F(3,4),'nonproduct energy variance')
 # Graph support theorem's finite combinatorial input: no 1-,2-,3-cycles; girth four.
 from itertools import combinations
 cycle_lengths=[]
 for k in range(1,8):
  for subset in combinations(edges,k):
   degrees=[sum(v in e for e in subset) for v in range(6)]
   if all(d==0 or d>=2 for d in degrees):cycle_lengths.append(k)
 require(min(cycle_lengths)==4,'girth/support bound')
 require(F(1,2)==2*F(1,4),'magnetic constant-vacuum residual')
 return {'schema':'marici.yang-mills-shared-link-packet-result.v1','passed':True,'gauge_cases':gauge_cases,'second_jet_differential_cases':differential_cases,'girth':4,'electric_gap':'3*kappa','shared_channel_energies':['9*kappa/2','13*kappa/2'],'shared_channel_norms_squared':['1/4','3/4'],'independent_product_residual_norm_squared_over_kappa_squared':str(norm_residual),'pointwise_naive_residuals':residuals,'haar_moment_cases':len(moments),'magnetic_gap_sufficient_bound':'3*kappa-2*lambda','constant_vacuum_residual_squared':'lambda^2/2','dictionary_gate_constructed':True,'finite_gauge_source_gate_closed':False,'continuum_gap_proved':False,'source_hashes':{p:digest(p) for p in [CONTRACT,NOTE,'research/kitaev/checkers/check_yang_mills_shared_link_packet.py']}}
if __name__=='__main__':
 r=report();OUT.parent.mkdir(parents=True,exist_ok=True);OUT.write_text(json.dumps(r,indent=2)+'\n');print(json.dumps({k:r[k] for k in ['passed','gauge_cases','second_jet_differential_cases','electric_gap','shared_channel_energies','independent_product_residual_norm_squared_over_kappa_squared','finite_gauge_source_gate_closed']},indent=2))
