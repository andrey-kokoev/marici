"""High-precision scout for a Cauchy remainder bound on |t|=1.

Not interval-certified.  It estimates the maximum modulus of
Q(t)=4[4L(t)-(1-4t)L'(t)] by parameterizing t=z^2 with |z|=1.
"""
import json, sys
from pathlib import Path
try:
    import mpmath as mp
except ModuleNotFoundError:
    sys.path.insert(0, str(Path(__file__).parents[2] / 'flavor' / '.venv' / 'Lib' / 'site-packages'))
    import mpmath as mp
mp.mp.dps=70

def xi(z):
    s=mp.mpf('.5')+z
    return mp.mpf('.5')*s*(s-1)*mp.power(mp.pi,-s/2)*mp.gamma(s/2)*mp.zeta(s)

def Q_from_z(z):
    X=xi(z); X1=mp.diff(xi,z,1); X2=mp.diff(xi,z,2)
    m=X1/X; m1=X2/X-m*m
    L=m/(2*z)
    Lt=(z*m1-m)/(4*z**3)
    return 4*(4*L-(1-4*z*z)*Lt)

samples=[]; maximum=None
N=720
for j in range(N):
    th=2*mp.pi*j/N; z=mp.e**(1j*th); q=Q_from_z(z); a=abs(q)
    samples.append(a)
    if maximum is None or a>maximum[0]: maximum=(a,th,q)
T=mp.mpf('0.007225'); margin=mp.mpf('0.36981997796728245512935065376058')
threshold=margin*(1-T)/(T**5)
out={
 'precision_decimal_digits':mp.mp.dps,'circle_radius_t':'1','sample_count':N,
 'sampled_max_abs_Q':mp.nstr(maximum[0],50),'angle_at_max':mp.nstr(maximum[1],50),
 'Q_at_max':mp.nstr(maximum[2],50),'degree_four_cauchy_acceptance_threshold':mp.nstr(threshold,50),
 'threshold_over_sampled_max':mp.nstr(threshold/maximum[0],50),
 'interval_certified':False,'rh_proved':False}
if __name__=='__main__':
 p=Path(__file__).parents[1]/'results'/'normalized-margin-cauchy-circle-scout.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
