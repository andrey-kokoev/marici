"""Arb polar-box certificate for Re F'(t) on 8.9 <= |t| <= 9, Im t >= 0."""
import json, math, sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).parents[2]/'benincasa'/'.tmp_flint'))
from flint import arb,acb,acb_series,ctx
ctx.dps=60
N=2048
pi=arb.pi(); min_lower=None; failures=[]
for j in range(N):
    mid=math.pi*(j+.5)/N; rad=math.pi/(2*N)
    theta=arb(mid,rad); radius=arb(8.95,.05)
    t=acb(radius)*(acb(0,theta)).exp(); z=t.sqrt()
    s=acb_series([acb(arb('.5'))+z,1],3)
    Xi=acb('.5')*s*(s-1)*((-s/2)*acb(pi).log()).exp()*(s/2).gamma()*s.zeta()
    X,X1,X2=Xi[0],Xi[1],2*Xi[2]
    if abs(X).lower()<=0:
        failures.append({'arc':j,'reason':'Xi contains zero'});continue
    m=X1/X; m1=X2/X-m*m
    A=2*z-1/(2*z); Az=2+1/(2*z*z)
    Fp=(Az*m+A*m1)/(2*z)
    lo=Fp.real.lower()
    if min_lower is None or lo<min_lower:min_lower=lo
    if lo<=0:failures.append({'arc':j,'lower':str(lo),'Fp':str(Fp)})
out={'precision_decimal_digits':ctx.dps,'angular_arc_count':N,'radial_interval':['8.9','9'],'minimum_Re_Fprime_lower':str(min_lower),'failure_count':len(failures),'all_boxes_positive':not failures,'failures':failures[:20],'interval_certified':not failures,'rh_proved':False}
if __name__=='__main__':
 p=Path(__file__).parents[1]/'results'/'arb-complex-pick-annulus-eight-point-nine-to-nine.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
