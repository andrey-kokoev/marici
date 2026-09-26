"""Exact finite-energy geometry fixtures; analytic proof is in the note."""
from fractions import Fraction as F
from pathlib import Path
import hashlib,json
ROOT=Path(__file__).resolve().parents[3]
HERE=Path(__file__).resolve().parent
paths=[Path(__file__),HERE/'triangle-joint-profile.md',ROOT/'temp/arxiv-2408.16386-source/sections/applications.tex']
def inventory():return {p.relative_to(ROOT).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}
before=inventory();centers=[];count=0
# Rational isosceles triangles with rational altitude, approaching E=0.
for a in map(F,(1,3)):
 b=a
 for u in map(F,('1/4','1/8','1/16','1/32')):
  ell=2*a*(1-u*u)/(1+u*u);E=a+b-ell
  g=(a*a+b*b-ell*ell)/2;d=a-g/a
  v=4*a*u*(1-u*u)/(1+u*u)**2
  H=E*(E-2*a)*(E-2*b)*(2*a+2*b-E)
  assert v*v==H/(4*a*a) and ell*ell==d*d+v*v
  for ratio in map(F,('1/4','1/2','3/4')):
   x=a*ratio;s0=a-x;root_star=v*s0/d;w_star=root_star**2
   assert w_star/E==H*s0*s0/(4*a*a*d*d*E)
   sc=ell*s0/d;tc=ell*(d-s0)/d
   assert sc>0 and tc>0 and sc+tc==ell
   assert sc*sc==s0*s0+w_star
   assert tc*tc==b*b+x*x+w_star-2*g*x/a-2*v*root_star
   centers.append({'a':str(a),'E':str(E),'x':str(x),'lambda_E':str(w_star/E)})
   for k in map(F,('1/2','1','2','4')):
    root_w=k*root_star;w=root_w**2
    for z in map(F,('-1','-1/2','0','1/2','1')):
     s2=s0*s0+w;t2=b*b+x*x+w-2*g*x/a-2*v*root_w*z
     height2=s2-(d*s0+v*root_w*z)**2/(ell*ell)
     decomposition=((d*root_w-v*s0)**2+2*v*d*s0*root_w*(1-z)+v*v*w*(1-z*z))/(ell*ell)
     assert height2==decomposition>=0
     assert 4*s2*t2-(s2+t2-ell*ell)**2==4*ell*ell*height2
     assert (height2==0)==(k==1 and z==1)
     omega=k*k+1-2*k*z
     assert omega-k*k*(1-z*z)==(k*z-1)**2>=0
     count+=1
assert before==inventory()
report={'passed':True,'center_fixture_count':len(centers),'height_heron_fixture_count':count,
 'source_sha256':before,'source_unchanged':True,'centers':centers,
 'collision':'w_star=v^2*(a-x)^2/d^2; z=1',
 'definitions':'ell=a+b-E; g=(a^2+b^2-ell^2)/2; d=a-g/a; v=sqrt(H)/(2a)',
 'recenter':'nu=w/(E*lambda_E), lambda_E=w_star/E',
 'analytic_result':'conditional localized limit E^(1-epsilon) P_chi(E) equals the joint-profile pairing for 0<Re(epsilon)<1',
 'verification_boundary':'Finite rational geometric identities only; uniform comparison and dominated-convergence proof are written, not machine-formalized. No physical cycle or regulator removal certified.'}
(HERE/'triangle-moving-collision.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in report.items() if k!='centers'},indent=2))
