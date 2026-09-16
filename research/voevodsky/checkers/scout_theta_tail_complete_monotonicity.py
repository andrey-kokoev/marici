"""Scout complete monotonicity of the theta tail C(u)=int_u^inf Phi."""
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
# For k>=1, (-1)^k C^(k)= -Phi^(k-1) times (-1)^k.
violations=[]; minima={}
for k in range(1,9):
 vals=[]
 for j in range(161):
  u=mp.mpf(j)/40
  v=(-1)**(k+1)*mp.diff(phi,u,k-1)
  vals.append((v,u))
  if v<0: violations.append({'order':k,'u':str(u),'signed_derivative':mp.nstr(v,30)})
 minima[str(k)]={'value':mp.nstr(min(vals)[0],30),'u':str(min(vals)[1])}
out={'candidate':'C(u)=integral_u^infinity Phi(v)dv','tested_u_range':[0,4],'orders_tested':[1,8],'signed_derivative_minima':minima,'violation_count':len(violations),'first_violations':violations[:20],'complete_monotonicity_supported':not violations,'interval_certified':False,'rh_proved':False}
if __name__=='__main__':
 p=Path(__file__).parents[1]/'results'/'theta-tail-complete-monotonicity-scout.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
