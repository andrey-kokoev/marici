"""Numerical consistency check for the theta-weighted shift Green identity."""
import json,sys
from pathlib import Path
try: import mpmath as mp
except ModuleNotFoundError:
 sys.path.insert(0,str(Path(__file__).parents[2]/'flavor'/'.venv'/'Lib'/'site-packages'));import mpmath as mp
mp.mp.dps=50;pi=mp.pi

def phi(u):
 e=mp.exp(2*u);s=mp.mpf('0')
 for n in range(1,30):
  a=(4*pi*pi*n**4*mp.exp(mp.mpf('4.5')*u)-6*pi*n*n*mp.exp(mp.mpf('2.5')*u))*mp.exp(-pi*n*n*e);s+=a
  if n>3 and abs(a)<mp.mpf('1e-55'):break
 return s

def test(a,b):
 f=lambda u:mp.e**(-a*u);g=lambda u:mp.e**(-b*u)
 lhs=mp.quad(lambda u:((-mp.diff(f,u))*g(u)+f(u)*(-mp.diff(g,u)))*phi(u),[0,1,2,4,7])
 rhs=phi(0)*f(0)*g(0)+mp.quad(lambda u:f(u)*g(u)*mp.diff(phi,u),[0,1,2,4,7])
 return {'a':str(a),'b':str(b),'lhs':mp.nstr(lhs,35),'rhs':mp.nstr(rhs,35),'absolute_residual':mp.nstr(abs(lhs-rhs),10)}
rows=[test(mp.mpf(a),mp.mpf(b)) for a,b in [('0.3','0.7'),('1.0','2.0'),('0.2','3.0')]]
derivatives=[mp.diff(phi,mp.mpf(j)/40) for j in range(1,161)]
out={'identity':'<Af,g>+<f,Ag> = Phi(0) f(0) conjugate(g(0)) + integral f conjugate(g) Phi_prime','A':'-d/du on L2(Phi du)','rows':rows,'sampled_Phi_prime_max':mp.nstr(max(derivatives),30),'sampled_Phi_prime_strictly_negative_for_u_gt_0':max(derivatives)<0,'interval_certified':False,'rh_proved':False}
if __name__=='__main__':
 p=Path(__file__).parents[1]/'results'/'theta-weighted-shift-green-identity-scout.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
