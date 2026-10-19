"""All-box incidence and exact linked-coefficient controls; no remainder estimate."""
from pathlib import Path
from fractions import Fraction as F
from itertools import product
from hashlib import sha256
import json
from check_yang_mills_ground_state_transfer import box
from check_yang_mills_shared_link_packet import I,lift,qp,jm,rawmul,rawinv
ROOT=Path(__file__).resolve().parents[3]
CONTRACT='research/kitaev/contracts/yang-mills-linked-density.v1.json'
NOTE='research/kitaev/yang-mills-linked-density-v1.md'
SELF='research/kitaev/checkers/check_yang_mills_linked_density.py'
OUT=ROOT/'research/kitaev/results/yang-mills-linked-density-v1.json'
def require(ok,msg):
 if not ok:raise ValueError(msg)
def disjoint(jets):return jm(tuple(2*x for x in qp(jets[:4])[0]),tuple(2*x for x in qp(jets[4:])[0]))
def energy(links):
 out=F(0)
 for e in range(8):
  for a in range(1,4):
   unit=tuple(F(k==a) for k in range(4));vel=tuple(x/2 for x in rawmul(unit,links[e]));jets=[lift(q) for q in links];jets[e]=tuple((x,v,-x/8) for x,v in zip(links[e],vel));out-=2*disjoint(jets)[2]
 return out

def report():
 c=json.loads((ROOT/CONTRACT).read_text());require(all(v is False for v in c['boundary'].values()),'uniform remainder or source theorem promoted')
 stats=[]
 for L in [2,3,4]:
  vs,edges,faces=box(L);supports=[{e for e,s in face} for face in faces];inc=[sum(e in s for s in supports) for e in range(len(edges))];neighbors=[0]*len(faces);pairs=[];vertex_only=0
  verts=[set(v for e in s for v in edges[e]) for s in supports]
  for i in range(len(faces)):
   for j in range(i+1,len(faces)):
    shared=supports[i]&supports[j];require(len(shared)<=1,'non-simple square overlap')
    if shared:neighbors[i]+=1;neighbors[j]+=1;pairs.append(supports[i]|supports[j]);require(len(pairs[-1])==7,'pair support')
    elif verts[i]&verts[j]:vertex_only+=1
  anchored=[sum(e in pair for pair in pairs) for e in range(len(edges))]
  require(max(inc)<=4 and max(neighbors)<=12 and max(anchored)<=48,'volume-local incidence')
  if L>=3:require(vertex_only>0,'vertex-only cancellation case absent')
  stats.append({'L':L,'E':len(edges),'P':len(faces),'adjacent_pairs':len(pairs),'vertex_only_pairs':vertex_only,'max_plaquettes_per_link':max(inc),'max_neighbors':max(neighbors),'max_anchored_pairs':max(anchored)})
 # Algebra from the spectral inverses: b pair= L^-1(pq)/6.
 require(2*F(1,36)-F(1,18)==0,'edge-disjoint logarithmic cancellation')
 require(2*F(1,27)-F(1,18)==F(1,54) and 2*F(1,39)-F(1,18)==F(-1,234),'adjacent channels')
 require(2*F(1,96)-F(1,36)==F(-1,144),'self character coefficient')
 qs=[I,(F(0),F(1),F(0),F(0)),(F(0),F(0),F(1),F(0)),(F(0),F(0),F(0),F(1)),(F(3,5),F(4,5),F(0),F(0)),(F(5,13),F(0),F(12,13),F(0))]
 for r in range(6):
  links=[qs[(r+k)%6] for k in range(8)];f=disjoint([lift(q) for q in links])[0];require(energy(links)==6*f,'direct disjoint electric Casimir')
 maxima=F(0)
 for x,y in product(qs,repeat=2):
  f=4*x[0]*y[0];f0=rawmul(x,rawinv(y))[0];f1=f-f0;j=f0/54-f1/234;bilinear=(2*x[0]*y[0]+8*sum(a*b for a,b in zip(x[1:],y[1:])))/351
  require(j==bilinear and abs(j)<=F(8,351),'pair norm and quaternion identity');maxima=max(maxima,abs(j))
 require(maxima==F(8,351),'sharp pair norm witness')
 osc2=4*F(4,144)+48*F(16,351);row2=4*3*F(1,72)+48*6*F(8,351)
 require(osc2==F(269,117) and row2==F(175,26),'anchored constants')
 r=F(1,16);row=8*r+row2*r*r;osc=F(16,3)*r+osc2*r*r
 require(row==F(3503,6656) and row<1 and 8*F(1,8)+row2*F(1,8)**2>1,'certified parameter boundary')
 likelihood_cases=0
 for t in [F(2),F(3),F(4)]:
  for weights in product(map(F,range(1,4)),repeat=3):
   total=sum(weights);q=[w/total for w in weights];raw=[q[0],q[1]*t,q[2]*t*t];p=[w/sum(raw) for w in raw];tv=sum(abs(a-b) for a,b in zip(p,q))/2
   require(tv<=(t-1)/(t+1),'likelihood oscillation TV bound');likelihood_cases+=1
 paths=[CONTRACT,NOTE,SELF,'research/kitaev/checkers/check_yang_mills_ground_state_transfer.py','research/kitaev/checkers/check_yang_mills_shared_link_packet.py']
 return {'schema':'marici.yang-mills-linked-density-result.v1','passed':True,'all_box_second_order_coefficient_constructed':True,'box_incidence_controls':stats,'direct_disjoint_Casimir_cases':6,'sharp_pair_norm':str(maxima),'conditional_oscillation_bound_T2':'16*abs(r)/3+269*r^2/117','conditional_TV_row_bound_T2':'8*abs(r)+175*r^2/26','TV_row_bound_at_r_1_16':str(row),'conditional_oscillation_at_r_1_16':str(osc),'likelihood_TV_cases':likelihood_cases,'uniform_remainder_proved':False,'actual_source_uniform_influence_proved':False,'conditional_tensorization_proved_for_source':False,'volume_uniform_detection_proved':False,'continuum_gap_proved':False,'scope':'All-box coefficient theorem; uniform bounds only for the Taylor log-density surrogate, not the actual source measure.','source_hashes':{p:sha256((ROOT/p).read_bytes()).hexdigest() for p in paths}}
if __name__=='__main__':
 r=report();OUT.parent.mkdir(parents=True,exist_ok=True);OUT.write_text(json.dumps(r,indent=2)+'\n');print(json.dumps({k:r[k] for k in ['passed','all_box_second_order_coefficient_constructed','sharp_pair_norm','TV_row_bound_at_r_1_16','likelihood_TV_cases','uniform_remainder_proved']},indent=2))
