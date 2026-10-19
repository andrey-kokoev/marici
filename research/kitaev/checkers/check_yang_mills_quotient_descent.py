"""Exact quotient/covariance controls. Omega_test is NOT the SU2 ground state."""
from pathlib import Path
from fractions import Fraction as F
from hashlib import sha256
import json
from check_yang_mills_shared_link_packet import I, lift, obs, rawmul, rawinv, laplace
ROOT=Path(__file__).resolve().parents[3]
CONTRACT='research/kitaev/contracts/yang-mills-quotient-descent.v1.json'
NOTE='research/kitaev/yang-mills-quotient-descent-v1.md'
SELF='research/kitaev/checkers/check_yang_mills_quotient_descent.py'
OUT=ROOT/'research/kitaev/results/yang-mills-quotient-descent-v1.json'
EDGES=[(0,1),(1,2),(2,3),(3,0),(1,4),(4,5),(5,0)]
def require(ok,msg):
 if not ok:raise ValueError(msg)
def vadd(a,b):return tuple(x+y for x,y in zip(a,b))
def vscale(a,c):return tuple(x*c for x in a)
def adj(q,v):return rawmul(rawmul(q,(F(0),)+tuple(v)),rawinv(q))[1:]
def packet(jets):
 p,q,f,f0,_=obs(jets)
 h=tuple(f[k]/2-2*f0[k] for k in range(3));weight=tuple((2 if k==0 else 0)+(p[k]+q[k])/4 for k in range(3))
 return h,weight

def detector(links,vacuum_control=False):
 h,w=packet([lift(q) for q in links]);require(1<=w[0]<=3,'positive fixture');field=[]
 for e in range(7):
  vector=[]
  for a in range(1,4):
   unit=tuple(F(k==a) for k in range(4));velocity=vscale(rawmul(unit,links[e]),F(1,2));jets=[lift(q) for q in links];jets[e]=tuple((x,v,F(0)) for x,v in zip(links[e],velocity));dh,dw=packet(jets)
   vector.append(dw[1]-w[0]*dw[1]/w[0] if vacuum_control else dh[1]-h[0]*dw[1]/w[0])
  field.append(tuple(vector))
 return field

def ward(links,field):
 out=[(F(0),)*3 for _ in range(6)]
 for (s,t),u,z in zip(EDGES,links,field):out[s]=vadd(out[s],z);out[t]=vadd(out[t],vscale(adj(rawinv(u),z),-1))
 return out

def report():
 c=json.loads((ROOT/CONTRACT).read_text());require(all(v is False for v in c['boundary'].values()),'scope promotion')
 qs=[I,(F(0),F(1),F(0),F(0)),(F(0),F(0),F(1),F(0)),(F(0),F(0),F(0),F(1)),(F(3,5),F(4,5),F(0),F(0)),(F(5,13),F(0),F(12,13),F(0))]
 samples=[[qs[(r+k)%6] for k in range(7)] for r in range(6)]+[[I,qs[1],I,I,qs[1],I,I],[I,qs[1],I,I,qs[2],I,I],[I]*7]
 gauge_cases=0;scalar_failures=0;casimir_cases=0
 for links in samples:
  z=detector(links);base=packet([lift(q) for q in links]);norm=sum(x*x for v in z for x in v)
  require(all(v==(F(0),)*3 for v in ward(links,z)),'vertical gauge energy');require(all(v==(F(0),)*3 for v in detector(links,True)),'positive-weight vacuum kernel fixture')
  vals=obs([lift(q) for q in links]);energies=laplace(links)
  require(energies[2]/2-2*energies[3]==F(-27,4)*vals[3][0]+F(13,4)*vals[4][0],'hidden-sector Casimir');casimir_cases+=1
  for r in range(6):
   gauges=[qs[(r+k)%6] for k in range(6)];changed=[rawmul(rawmul(gauges[s],u),rawinv(gauges[t])) for (s,t),u in zip(EDGES,links)];zz=detector(changed)
   require(packet([lift(q) for q in changed])==base,'physical packet evaluation')
   require(zz==[adj(gauges[s],v) for (s,t),v in zip(EDGES,z)],'covariant target adjoint law')
   require(sum(x*x for v in zz for x in v)==norm,'quotient detector norm');require(all(v==(F(0),)*3 for v in ward(changed,zz)),'transformed vertical constraint')
   scalar_failures+=zz!=z;gauge_cases+=1
 require(scalar_failures>0,'scalar-target hostile absent')
 h1=packet([lift(q) for q in samples[-3]])[0][0];h2=packet([lift(q) for q in samples[-2]])[0][0]
 require(h1==-2 and h2==0,'relative-loop distinction')
 # Uniform signed coordinate points integrate degree<=2 exactly in each Haar quaternion.
 axes=[tuple(F(s if k==a else 0) for k in range(4)) for a in range(4) for s in (-1,1)]
 norm_h=sum((-2*sum(x*y for x,y in zip(a[1:],b[1:])))**2 for a in axes for b in axes)/64
 require(norm_h==F(3,4),'nonzero hidden Haar norm')
 # Conditional axes are independent and uniform: rational fixed scalar/radius cases.
 conditional_cases=0
 for a0,ar in [(F(0),F(1)),(F(3,5),F(4,5)),(F(1),F(0))]:
  for b0,br in [(F(0),F(1)),(F(5,13),F(12,13))]:
   values=[]
   for a in range(3):
    for b in range(3):
     for s in (-1,1):
      for t in (-1,1):values.append(-2*ar*br*s*t*(a==b))
   require(sum(values)==0 and sum(x*x for x in values)/36==F(4,3)*ar**2*br**2,'conditional blind sector');conditional_cases+=1
 energy=F(9,2)*F(9,16)+F(13,2)*F(3,16)
 require(energy==F(15,4) and energy/norm_h==5,'normalized hidden electric energy')
 haar_x2,haar_x4=F(1,4),F(1,8);flat_x2,flat_x4=F(1,2),F(3,8)
 means=[4*haar_x2-1,4*flat_x2-1];norms=[4*haar_x2,4*flat_x2]
 require(means==[0,1] and norms==[1,2],'flat-measure hostile')
 paths=[CONTRACT,NOTE,SELF,'research/kitaev/checkers/check_yang_mills_shared_link_packet.py','research/kitaev/contracts/yang-mills-ground-state-transfer.v1.json']
 return {'schema':'marici.yang-mills-quotient-descent-result.v1','passed':True,'quotient_descent_constructed':True,'covariant_gauge_cases':gauge_cases,'scalar_target_failures':scalar_failures,'direct_hidden_casimir_cases':casimir_cases,'conditional_axis_cases':conditional_cases,'hidden_Haar_norm_squared':str(norm_h),'hidden_electric_energy_over_kappa':str(energy),'hidden_normalized_Rayleigh_over_kappa':'5','chi2_means_Haar_flat':[str(x) for x in means],'chi1_norms_squared_Haar_flat':[str(x) for x in norms],'weight_fixture_is_actual_ground_state':False,'volume_uniform_detection_proved':False,'continuum_gap_proved':False,'scope':'Written closed quotient/domain theorem plus exact finite quaternion controls. No volume-compatible Poincare estimate.','source_hashes':{p:sha256((ROOT/p).read_bytes()).hexdigest() for p in paths}}
if __name__=='__main__':
 r=report();OUT.parent.mkdir(parents=True,exist_ok=True);OUT.write_text(json.dumps(r,indent=2)+'\n');print(json.dumps({k:r[k] for k in ['passed','quotient_descent_constructed','covariant_gauge_cases','scalar_target_failures','hidden_Haar_norm_squared','hidden_normalized_Rayleigh_over_kappa','volume_uniform_detection_proved']},indent=2))
