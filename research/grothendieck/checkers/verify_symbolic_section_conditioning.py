"""Independent exact conditioning replay; no Generator import or optimizer."""
from pathlib import Path
from fractions import Fraction as Q
from bisect import bisect_right
import json,hashlib
HERE=Path(__file__).resolve().parent;ROOT=HERE.parents[1];R=HERE.parent/'results'
def load(p):return json.loads(p.read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
r=load(R/'symbolic-section-conditioning.json');contract=load(R/'symbolic-section-conditioning-contract.json')
for p,h in r['bindings'].items():assert sha(Path(p))==h
assert r['contract_sha256']==sha(R/'symbolic-section-conditioning-contract.json')
for record in r['records']:
 m=record['m'];caps=[Q(100+2*j) for j in range(m)];slopes=[Q(1,128**j) for j in range(m)]
 C=[Q(0)];W=[Q(0)]
 for a,b in zip(caps,slopes):C.append(C[-1]+a);W.append(W[-1]+a*b)
 T=C[-1];assert T==Q(record['total_capacity'])==m*(m+99)
 def greedy(U):
  k=bisect_right(C,U)-1;p=U-C[k];value=W[k]+(p*slopes[k] if k<m else 0)
  return k,p,value
 k=sum(C[j]<=T-C[j+1] for j in range(m));assert k==record['positive_prefix']
 def ratio(U):
  gap=greedy(U)[2]-(W[-1]-greedy(T-U)[2]);assert gap>0
  norm=2*(min(U,C[k])-max(Q(0),U-(T-C[k])))
  return norm/gap
 breaks=sorted(set(C)|{T-a for a in C});assert len(breaks)==record['breakpoint_count']
 candidates=[(2/(1-slopes[-1]),Q(0))]+[(ratio(U),U) for U in breaks if 0<U<T]
 value,where=max(candidates);assert value==Q(record['R_m']) and where==Q(record['maximizing_mass_or_tip'])
 assert Q(record['global_greedy_upper'])==value+1
 assert ratio(T/2)==Q(record['midpoint_lower'])<=value<=Q(record['quadratic_upper'])==Q(128)*T/12700
 Winf=Q(100)/(1-Q(1,128))+2*Q(1,128)/(1-Q(1,128))**2
 assert Q(record['quadratic_lower'])==(T-max(caps))/Winf<=ratio(T/2)
 for case in record['lift_controls']:
  U=Q(case['U']);hk,hp,high=greedy(U);ck,cp,comp=greedy(T-U);low=W[-1]-comp
  assert low==Q(case['low']) and high==Q(case['high'])
  hi=[a if j<hk else hp if j==hk else Q(0) for j,a in enumerate(caps)]
  lo=[a-(a if j<ck else cp if j==ck else Q(0)) for j,a in enumerate(caps)]
  dist=sum(abs(a-b) for a,b in zip(hi,lo));assert dist==Q(case['profile_distance']) and dist/(high-low)<=value
  # Prefix dominance certifies W>= (r0-r1)(h0-l0), the key uniform bound.
  assert all(sum(hi[:j+1])>=sum(lo[:j+1]) for j in range(m))
  assert high-low>=(1-Q(1,128))*(hi[0]-lo[0])
  for packet in case['membership_packets']:
   V=Q(packet['V']);answer=packet['answer'];assert answer['admitted'];lift=answer['lift']
   assert lift['high_prefix']==hk and Q(lift['high_partial'])==hp and lift['complement_prefix']==ck and Q(lift['complement_partial'])==cp
   theta=Q(lift['theta']);assert theta==(V-low)/(high-low) and 0<=theta<=1
   point=[(1-theta)*a+theta*b for a,b in zip(lo,hi)]
   assert sum(point)==U and sum(a*b for a,b in zip(slopes,point))==V
   assert all(0<=a<=b for a,b in zip(point,caps))
assert [z['m'] for z in r['records']]==contract['m_values']
alpha,beta=map(Q,r['nonaffine_obstruction']['direction_relation']['g2_equals_alpha_g1_plus_beta_g0'])
assert alpha+beta==1 and alpha*Q(1,128)+beta==Q(1,128**2)
# The forced source-coordinate relation is false in its third coordinate.
assert Q(1)!=alpha*0+beta*0
print('PASS: independently summed profiles, exact vertical-optimal constants, actual section packets, quadratic bounds, and forced non-affinity certificate')
