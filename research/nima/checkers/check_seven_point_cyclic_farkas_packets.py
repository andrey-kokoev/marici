"""Construct sparse exact noncyclic-minor certificates over admitted cyclic fibres."""
from pathlib import Path
from fractions import Fraction as Q
from itertools import combinations
import json,random
from check_seven_point_fibre_polygon_stress import N,pairs,line
from check_seven_point_multichamber_stress import build
cyclic=[(i,i+1) for i in range(6)]+[(0,6)]
def certificate(L,P,T):
 c,a,b=L;p,d,e=P;q,f,g=T;det=d*g-e*f
 if not det:return None
 alpha=(a*g-b*f)/det;beta=(d*b-e*a)/det;gamma=c-alpha*p-beta*q
 return (alpha,beta,gamma) if min(alpha,beta,gamma)>=0 else None
def packet(x,y,require_positive_source=True):
 L={p:line(x,y,*p) for p in pairs}
 if require_positive_source:assert all(t[0]>0 for t in L.values())
 cert=[]
 for i,j in pairs:
  if (i,j) in cyclic:continue
  option=next(((p,q,coeff) for p,q in combinations(cyclic,2) if (coeff:=certificate(L[(i,j)],L[p],L[q])) is not None),None)
  if option is None:return None
  p,q,(alpha,beta,gamma)=option
  cert.append({'minor':[i+1,j+1],'cyclic_edges':[[a+1,b+1] for a,b in (p,q)],
    'coefficients':[str(alpha),str(beta)],'constant':str(gamma)})
 return cert
def main():
 rng=random.Random(20260829);cases=[]
 for neg in range(7):
  if neg==0:
   w=[rng.randint(1,9) for _ in range(7)];t=[0]
   for _ in range(6):t.append(t[-1]+rng.randint(1,12))
   x=[Q(a) for a in w];y=[x[j]*t[j] for j in range(7)]
  else:w,t,x,y=build(rng,neg)
  cert=packet(x,y);assert cert is not None and len(cert)==14
  cases.append({'negative_initial_columns':neg,'source_rows':[list(map(str,x)),list(map(str,y))],
    'certificates':cert})
 badx=list(map(Q,[1,1,0,-1,-1,-1,2]));bady=list(map(Q,[0,1,1,1,0,-2,1]))
 assert packet(badx,bady,require_positive_source=False) is None
 report={'schema':'marici.nima.seven-point-cyclic-farkas-packets.v1','external_Z':'Z_j=(1,j,j^2,j^3,j^4,j^5), j=1..7',
  'cases':cases,'negative_control_rejected':True,
  'identity':'Each noncyclic minor on a fixed target fibre equals alpha*cyclic_minor_p + beta*cyclic_minor_q + gamma with alpha,beta,gamma nonnegative rational. This proves whole-fibre implication for each frozen admitted target.',
  'scope':'Seven exact admitted targets, not a uniform all-target positive-geometry theorem.'}
 (N/'results/seven-point-cyclic-farkas-packets.json').write_text(json.dumps(report,indent=2)+'\n')
 print(json.dumps({'passed':True,'admitted_targets':len(cases),'inequality_certificates':sum(len(x['certificates']) for x in cases),
                   'negative_control_rejected':True},indent=2))
if __name__=='__main__':main()
