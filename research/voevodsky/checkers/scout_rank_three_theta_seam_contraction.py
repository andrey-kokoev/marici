"""Scout the exact rank-three seam decomposition and its standalone contraction.

The algebraic decomposition is exact. Numerical theta integration is exploratory.
"""
import json, sys
from pathlib import Path
try:
 import mpmath as mp
except ModuleNotFoundError:
 sys.path.insert(0,str(Path(__file__).parents[2]/'flavor'/'.venv'/'Lib'/'site-packages'));import mpmath as mp
mp.mp.dps=50;pi=mp.pi

def phi(u):
 e=mp.exp(2*u);s=mp.mpf('0')
 for n in range(1,24):
  term=(4*pi*pi*n**4*mp.exp(mp.mpf('4.5')*u)-6*pi*n*n*mp.exp(mp.mpf('2.5')*u))*mp.exp(-pi*n*n*e)
  s+=term
  if n>3 and abs(term)<mp.mpf('1e-55'):break
 return s

def moment(x,k):
 return mp.quad(lambda u:(1j*u)**k*phi(u)*mp.e**(1j*x*u),[0,1,2,4,7])

M0=moment(mp.mpf('0'),0).real
M1=(moment(mp.mpf('0'),1)/1j).real
M2=(-moment(mp.mpf('0'),2)).real
seam_trace_bulk=2*(M0*M2+M1*M1)
records=[]; worst=(mp.inf,None); combined_worst=(mp.inf,None)
for j in range(401):
 x=mp.mpf(j)/10
 F,F1,F2=(moment(x,k) for k in range(3))
 hp=(F+F2)/mp.sqrt(2); hm=(F-F2)/mp.sqrt(2)
 positive=abs(hp)**2; negative=abs(hm)**2+2*abs(F1)**2
 defect=positive-negative
 ratio=positive/negative if negative else mp.inf
 combined=(positive+seam_trace_bulk)/negative if negative else mp.inf
 r={'x':str(x),'positive_channels':mp.nstr(positive,30),'negative_channel':mp.nstr(negative,30),'seam_defect':mp.nstr(defect,30),'positive_over_negative':mp.nstr(ratio,30),'seam_invariant_trace_bulk':mp.nstr(seam_trace_bulk,30),'combined_positive_over_negative':mp.nstr(combined,30)}
 records.append(r)
 if ratio<worst[0]:worst=(ratio,r)
 if combined<combined_worst[0]:combined_worst=(combined,r)
out={'exact_identity':'2 Re(F2 conj(F)) - 2 |F1|^2 = |(F+F2)/sqrt(2)|^2 - |(F-F2)/sqrt(2)|^2 - 2|F1|^2','seam_signature':[1,2],'sample_range_x':[0,40],'sample_count':len(records),'minimum_positive_over_negative':mp.nstr(worst[0],30),'minimum_record':worst[1],'standalone_seam_contractive_on_samples':worst[0]>=1,'seam_invariant_trace_bulk':mp.nstr(seam_trace_bulk,30),'minimum_combined_positive_over_negative':mp.nstr(combined_worst[0],30),'minimum_combined_record':combined_worst[1],'bulk_plus_seam_contractive_on_samples':combined_worst[0]>=1,'interval_certified':False,'rh_proved':False}
if __name__=='__main__':
 p=Path(__file__).parents[1]/'results'/'rank-three-theta-seam-contraction-scout.json';p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
