import json, math, sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[2]/'.ai/tmp/flavor-dpc-python-deps'))
import mpmath as mp
mp.mp.dps=30
t=mp.mpf('0.7'); ds=[0,1,2]
# von Mangoldt values through a conservative finite cutoff for d<=2
N=20000
lam=[0.0]*(N+1); isprime=[True]*(N+1); isprime[0]=isprime[1]=False
for p in range(2,N+1):
 if isprime[p]:
  q=p
  while q<=N:
   lam[q]=math.log(p); q*=p
  for q in range(p*p,N+1,p): isprime[q]=False
def K(d):
 d=mp.mpf(d)
 endpoint=mp.e**(t/4)*mp.cosh(d/2)
 gamma=-mp.log(mp.pi)/(4*mp.sqrt(mp.pi*t))*mp.e**(-d*d/(4*t))+mp.quad(lambda u: mp.e**(-t*u*u)*mp.cos(d*u)*mp.re(mp.digamma(mp.mpf(1)/4+1j*u/2)),[-mp.inf,mp.inf])/(4*mp.pi)
 prime=-sum(lam[n]/mp.sqrt(n)*(mp.e**(-(mp.log(n)-d)**2/(4*t))+mp.e**(-(mp.log(n)+d)**2/(4*t))) for n in range(2,N+1) if lam[n])/(4*mp.sqrt(mp.pi*t))
 return endpoint+gamma+prime
ks=[K(d) for d in ds];det=ks[0]**3-2*ks[0]*ks[1]**2+2*ks[1]**2*ks[2]-ks[0]*ks[2]**2
out={'schema':'marici.nima.qRB-rank-three-corrected-target.v1','t':str(t),'deltas':ds,'values':[str(x) for x in ks],'toeplitz_determinant':str(det),'checks':{'finite_evaluation':all(mp.isfinite(x) for x in ks),'even_character_kernel':True,'rank_three_psd':det>=0},'passed':det>=0,'scope':'numerical reconnaissance with finite prime cutoff and mpmath quadrature; not a certificate','rh_proved':False}
p=Path(__file__).resolve().parents[2]/'research/nima/results/qRB-rank-three-corrected-target.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
