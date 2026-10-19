"""Exact controls for the written ground-transform / temporal-transfer theorem.
The rational three-site control is NOT an SU2 vacuum computation.
"""
from pathlib import Path
from fractions import Fraction as F
from itertools import combinations, product
from hashlib import sha256
import json
from check_yang_mills_shared_link_packet import rawmul, rawinv, I as QI
ROOT=Path(__file__).resolve().parents[3]
CONTRACT='research/kitaev/contracts/yang-mills-ground-state-transfer.v1.json'
NOTE='research/kitaev/yang-mills-ground-state-transfer-v1.md'
SELF='research/kitaev/checkers/check_yang_mills_ground_state_transfer.py'
OUT=ROOT/'research/kitaev/results/yang-mills-ground-state-transfer-v1.json'
def require(ok,msg):
 if not ok:raise ValueError(msg)
def matrix(a):return [[F(x) for x in row] for row in a]
def eye(n):return [[F(i==j) for j in range(n)] for i in range(n)]
def add(a,b):return [[x+y for x,y in zip(r,s)] for r,s in zip(a,b)]
def scale(a,c):return [[x*c for x in r] for r in a]
def mv(a,v):return [sum(x*y for x,y in zip(r,v)) for r in a]
def dot(u,v):return sum(x*y for x,y in zip(u,v))
def mm(a,b):return [mv(list(map(list,zip(*b))),r) for r in a]
def determinant(a):
 if not a:return F(1)
 return sum((-1)**j*a[0][j]*determinant([r[:j]+r[j+1:] for r in a[1:]]) for j in range(len(a)))
def psd(a):
 require(a==list(map(list,zip(*a))),'nonsymmetric positivity claim')
 return all(determinant([[a[i][j] for j in s] for i in s])>=0 for k in range(1,len(a)+1) for s in combinations(range(len(a)),k))
def inverse(a):
 d=determinant(a);require(d!=0,'singular inverse');n=len(a)
 return [[(-1)**(i+j)*determinant([[a[r][c] for c in range(n) if c!=i] for r in range(n) if r!=j])/d for j in range(n)] for i in range(n)]
def box(L):
 vs=list(product(range(L),repeat=3));edges=[];idx={}
 def step(v,a):return tuple(x+(k==a) for k,x in enumerate(v))
 for v in vs:
  for a in range(3):
   if v[a]+1<L:idx[(v,a)]=len(edges);edges.append((v,step(v,a)))
 faces=[]
 for v in vs:
  for a,b in combinations(range(3),2):
   if v[a]+1<L and v[b]+1<L:faces.append([(idx[(v,a)],1),(idx[(step(v,a),b)],1),(idx[(step(v,b),a)],-1),(idx[(v,b)],-1)])
 return vs,edges,faces
def girth(vs,edges):
 best=len(edges)+1
 for omit,(start,end) in enumerate(edges):
  seen={start};front=[start];d=0
  while front:
   if end in front:best=min(best,d+1);break
   new=[]
   for v in front:
    for i,(a,b) in enumerate(edges):
     if i==omit:continue
     w=b if a==v else a if b==v else None
     if w is not None and w not in seen:seen.add(w);new.append(w)
   front=new;d+=1
 return best
def traces(links,faces):
 out=[]
 for face in faces:
  q=QI
  for e,s in face:q=rawmul(q,links[e] if s==1 else rawinv(links[e]))
  out.append(2*q[0])
 return out
def report():
 c=json.loads((ROOT/CONTRACT).read_text());require(all(v is False for v in c['boundary'].values()),'scope promotion')
 r=F(1,64);tail=(1+r)/(1-r)**3-1
 require(tail==F(16193,250047) and tail<F(1,8),'heat tail normalization')
 require(all(n*(n+2)>=3*n for n in range(1,65)),'heat exponent regression')
 K=matrix(c['exact_control']['kinetic']);V=c['exact_control']['potential'];H=add(K,[[F(V[i] if i==j else 0) for j in range(3)] for i in range(3)]);A=add(H,scale(eye(3),-1));omega=[F(1),F(2),F(1)]
 require(mv(H,omega)==omega,'independently supplied ground equation')
 vectors=[omega,[F(1),F(0),F(-1)],[F(1),F(-1),F(1)]]
 for v,e in zip(vectors,[0,2,3]):require(mv(A,v)==[e*x for x in v],'shifted spectrum')
 require(determinant(vectors)!=0,'incomplete eigenbasis')
 P=[[omega[i]*omega[j]/6 for j in range(3)] for i in range(3)];Q=add(eye(3),scale(P,-1));comparison=add(A,scale(Q,F(-1,4)))
 require(psd(comparison),'weighted comparison full-matrix inequality')
 constant_projection=[[F(1,3)]*3 for _ in range(3)]
 require(psd(add(K,scale(add(eye(3),scale(constant_projection,-1)),-1))),'kinetic Poincare constant')
 count=0
 for v in product(map(F,range(-2,3)),repeat=3):
  q=dot(v,mv(A,v));weighted=2*(v[0]-v[1]/2)**2+2*(v[1]/2-v[2])**2
  require(q==weighted,'ground transform form identity');require(q>=F(1,4)*dot(v,mv(Q,v)),'weighted detector comparison');count+=1
 require(dot(omega,mv(A,omega))==0 and (omega[0]-omega[1])**2+(omega[1]-omega[2])**2==2,'raw detector mismatch')
 transfer_cases=0
 for delta in [F(1,8),F(1,2),F(1),F(4)]:
  R=inverse(add(eye(3),scale(K,delta)));M=[[F(1,i+1) if i==j else F(0) for j in range(3)] for i in range(3)];S=mm(mm(M,R),M)
  require(psd(S),'symmetric positive transfer step');transfer_cases+=1
 swap=matrix([[0,1,0],[1,0,0],[0,0,1]]);w=[F(1),F(-1),F(0)]
 require(all(x>=0 for row in swap for x in row) and dot(w,mv(swap,w))==-2,'entrywise-positive transfer hostile')
 qs=[QI,(F(0),F(1),F(0),F(0)),(F(0),F(0),F(1),F(0)),(F(0),F(0),F(0),F(1)),(F(3,5),F(4,5),F(0),F(0)),(F(5,13),F(0),F(12,13),F(0))]
 boxes=[];gauge_cases=0
 for L in [2,3]:
  vs,edges,faces=box(L);E=len(edges);Pfaces=len(faces)
  require(E==3*L**2*(L-1) and Pfaces==3*L*(L-1)**2 and girth(vs,edges)==4,'open cubic source counts/girth')
  links=[qs[i%6] for i in range(E)];original=traces(links,faces)
  for shift in range(6):
   gs={v:qs[(i+shift)%6] for i,v in enumerate(vs)};changed=[rawmul(rawmul(gs[a],u),rawinv(gs[b])) for u,(a,b) in zip(links,edges)]
   require(traces(changed,faces)==original,'oriented box plaquette gauge action');gauge_cases+=len(faces)
  bound=3*F(7,9)**(2*E)*F(1,2)**(32*Pfaces)
  boxes.append({'L':L,'E':E,'P':Pfaces,'girth':4,'unit_coupling_bound_positive':bound>0,'bound_denominator_bits':bound.denominator.bit_length(),'electric_actual_gap_over_kappa':'3'})
 # All exponents are integral for these ratios, so these are exact source bounds.
 fixed=[]
 for coupling in [F(0),F(1,64),F(1,4),F(1,2),F(1),F(2)]:
  exponent=64*coupling;require(exponent.denominator==1,'test exponent');bound=3*F(7,9)**14*F(1,2)**int(exponent)
  require(bound>0,'all-coupling bound');fixed.append({'lambda_over_kappa':str(coupling),'bound_over_kappa':str(bound),'old_minmax_over_kappa':str(3-2*coupling)})
 require(F(fixed[-1]['old_minmax_over_kappa'])<0,'new bound must exceed old certificate scope')
 require(boxes[1]['bound_denominator_bits']>boxes[0]['bound_denominator_bits'],'volume deterioration control')
 paths=[CONTRACT,NOTE,SELF,'research/kitaev/checkers/check_yang_mills_shared_link_packet.py']
 return {'schema':'marici.yang-mills-ground-state-transfer-result.v1','passed':True,'finite_gauge_source_constructed':True,'ground_state_relative_detector_constructed':True,'scope':'Written finite-graph SU2 theorem with exact rational matrix/heat-majorant/box-gauge controls; no SU2 vacuum numerics or continuum theorem.','heat_tail_majorant':str(tail),'toy_form_cases':count,'toy_shifted_spectrum':[0,2,3],'toy_comparison_constant':'1/4','positive_transfer_cases':transfer_cases,'entrywise_positive_transfer_hostile':True,'box_plaquette_gauge_cases':gauge_cases,'boxes':boxes,'two_plaquette_bounds':fixed,'explicit_gap':'3*kappa*(7/9)^(2E)*2^(-32*P*lambda/kappa)','volume_uniform_gap_proved':False,'continuum_gap_proved':False,'source_hashes':{p:sha256((ROOT/p).read_bytes()).hexdigest() for p in paths}}
if __name__=='__main__':
 r=report();OUT.parent.mkdir(parents=True,exist_ok=True);OUT.write_text(json.dumps(r,indent=2)+'\n');print(json.dumps({k:r[k] for k in ['passed','finite_gauge_source_constructed','heat_tail_majorant','toy_form_cases','positive_transfer_cases','box_plaquette_gauge_cases','explicit_gap','volume_uniform_gap_proved']},indent=2))
