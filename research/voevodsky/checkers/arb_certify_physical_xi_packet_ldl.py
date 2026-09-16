"""Arb certification of positive definiteness for three finite Xi packets.
Run with PYTHONPATH="$PWD/research/benincasa/.tmp_flint".
"""
import json
from pathlib import Path
from flint import acb, acb_series, arb, ctx
ctx.dps=180
PI=acb(arb.pi()); I=acb(0,1)
BASE_PACKETS=[[('0','1'),('5','1'),('10','1'),('15','1')],[('2','2'),('8','3'),('14','2'),('20','4')],[('5','0.25'),('12','0.5'),('20','0.75'),('28','1')]]
# The union tests cross-packet coherence, not merely positivity of separate blocks.
UNION=sum(BASE_PACKETS,[])
# Stress the kernel close to the real axis around the first four critical zeros.
NEAR_ZERO=[('14.134725','0.05'),('14.134725','0.2'),('21.022040','0.05'),('21.022040','0.2'),('25.010858','0.05'),('25.010858','0.2'),('30.424876','0.05'),('30.424876','0.2')]
PACKETS=BASE_PACKETS+[UNION,UNION+NEAR_ZERO]

def E_pair(z):
 s=acb_series([acb('0.5')+I*z,I],3)
 xi=acb('0.5')*s*(s-1)*((-s/2)*PI.log()).exp()*(s/2).gamma()*s.zeta()
 X=xi[0];Xp=xi[1]
 return X+I*Xp,X-I*Xp

def kernel(z,w):
 Ez,Esz=E_pair(z);Ew,Esw=E_pair(w)
 return (Ez*Ew.conjugate()-Esz*Esw.conjugate())/(acb(2)*PI*I*(w.conjugate()-z))

def certify(raw,radius=None):
 def ball(x): return arb(x) if radius is None else arb(f'{x} +/- {radius}')
 pts=[acb(ball(x),ball(y)) for x,y in raw];n=len(pts)
 K=[[acb(0) for _ in range(n)] for _ in range(n)]
 for i in range(n):
  for j in range(n):
   q=kernel(pts[i],pts[j]);qr=kernel(pts[j],pts[i]).conjugate();K[i][j]=(q+qr)/2
 L=[[acb(int(i==j)) for j in range(n)] for i in range(n)];D=[]
 for j in range(n):
  pivot=(K[j][j]-sum((L[j][q]*acb(D[q])*L[j][q].conjugate() for q in range(j)),acb(0))).real
  if not pivot>0: return {'points':raw,'coordinate_radius':radius,'certified_positive_definite':False,'failed_pivot':j,'pivot':str(pivot),'pivots':[str(x) for x in D]}
  D.append(pivot)
  for i in range(j+1,n):
   num=K[i][j]-sum((L[i][q]*acb(D[q])*L[j][q].conjugate() for q in range(j)),acb(0));L[i][j]=num/pivot
 # Explicit Kolmogorov/Douglas feature: K = F^* F with F = sqrt(D) L^*.
 F=[[acb(D[q].sqrt())*L[j][q].conjugate() for j in range(n)] for q in range(n)]
 residuals=[]
 for i in range(n):
  for j in range(n): residuals.append(K[i][j]-sum((F[q][i].conjugate()*F[q][j] for q in range(n)),acb(0)))
 return {'points':raw,'coordinate_radius':radius,'certified_positive_definite':True,'pivots':[str(x) for x in D],'pivot_relative_accuracy_bits':[x.rel_accuracy_bits() for x in D],'gram_feature_shape':[n,n],'gram_feature_formula':'F=sqrt(D) L^*, so K=F^*F','gram_identity_ball_certified':all(x.contains(0) for x in residuals)}

exact=[certify(p) for p in PACKETS]
# Independent complex coordinate boxes around every point of the 20-point packet.
robust=[certify(UNION+NEAR_ZERO,r) for r in ('1e-100','1e-90','1e-80','1e-70','1e-60','1e-50','1e-40')]
local_robust=[{'packet_index':i,'trials':[certify(p,r) for r in ('1e-12','1e-10','1e-8','1e-6')]} for i,p in enumerate(BASE_PACKETS,1)]
out={'packets':exact,'robustness_trials':robust,'local_packet_robustness':local_robust,'arithmetic':'Arb complex balls, 180 decimal digits','scope':'only the listed finite packets and coordinate boxes','rh_proved':False}
if __name__=='__main__':
 p=Path(__file__).parents[1]/'results'/'arb-certified-physical-xi-packet-ldl.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
