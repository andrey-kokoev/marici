"""Scout the exact two-bulk contraction equivalent to first Xi Laguerre positivity."""
import json,sys
from pathlib import Path
try: import mpmath as mp
except ModuleNotFoundError:
 sys.path.insert(0,str(Path(__file__).parents[2]/'flavor'/'.venv'/'Lib'/'site-packages'));import mpmath as mp
mp.mp.dps=50;pi=mp.pi

def phi(u):
 e=mp.exp(2*u);s=mp.mpf('0')
 for n in range(1,24):
  a=(4*pi*pi*n**4*mp.exp(mp.mpf('4.5')*u)-6*pi*n*n*mp.exp(mp.mpf('2.5')*u))*mp.exp(-pi*n*n*e);s+=a
  if n>3 and abs(a)<mp.mpf('1e-55'):break
 return s

def moment(x,k):return mp.quad(lambda u:(1j*u)**k*phi(u)*mp.e**(1j*x*u),[0,1,2,4,7])
M0=moment(0,0).real;M2=(-moment(0,2)).real;bulk=4*M0*M2
records=[];worst=(-mp.inf,None);minimum=(mp.inf,None)
for j in range(161):
 x=mp.mpf(j)/4;F,F1,F2=(moment(x,k) for k in range(3))
 X=2*mp.re(F); X1=2*mp.re(F1); X2=2*mp.re(F2)
 lag=X1*X1-X*X2
 residual=bulk-lag;ratio=residual/bulk
 r={'x':str(x),'laguerre':mp.nstr(lag,30),'residual_bulk':mp.nstr(residual,30),'residual_over_total_bulk':mp.nstr(ratio,30)};records.append(r)
 if ratio>worst[0]:worst=(ratio,r)
 if lag<minimum[0]:minimum=(lag,r)
out={'identity':'Xprime^2-X Xdoubleprime = 4 M0 M2 - (R_difference+R_sum)','total_invariant_bulk':mp.nstr(bulk,30),'sample_range_x':[0,40],'sample_count':len(records),'maximum_residual_over_bulk':mp.nstr(worst[0],30),'maximum_record':worst[1],'minimum_laguerre':mp.nstr(minimum[0],30),'minimum_record':minimum[1],'contraction_on_samples':worst[0]<=1,'interval_certified':False,'rh_proved':False}
if __name__=='__main__':
 p=Path(__file__).parents[1]/'results'/'first-laguerre-two-bulk-contraction-scout.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
