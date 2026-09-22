"""Classify derivative orientation on signed transition cells."""
import runpy,json
from pathlib import Path
from flint import arb
x=runpy.run_path(str(__file__).replace('check_signed_kernel_transition_variation.py','certify_signed_kernel_transition_bands.py'))
# Reuse the exact fixed segment formula. K+ transition negativity occurs in 14--16.
ts=x['ts'];pv=x['pv'];T=x['T'];B=x['B'];s=x['s'];beta=x['beta'];a=x['a'];lam=x['lam'];parts=x['parts']
i=ts.index(arb(14));m=(pv[i+1]-pv[i])/(ts[i+1]-ts[i]);cp=T[i+1]-(-lam*ts[i+1]).exp()*(pv[i+1]/lam+m/lam**2)
def derivative(u):
 b=pv[i]+m*(u-ts[i]);return -s*B*(-s*u).exp()+beta*(-beta*u).exp()*(b/lam+m/lam**2)-m*(-beta*u).exp()/lam-a*cp*(a*u).exp()
rows=[]
def split(l,r,depth=40):
 z=derivative(l.union(r))
 if z>0:return [('increasing_K',l,r)]
 if z<0:return [('decreasing_K',l,r)]
 if depth==0:return [('critical_box',l,r)]
 mid=(l+r)/2;return split(l,mid,depth-1)+split(mid,r,depth-1)
for sign,l,r in parts:
 if sign!='positive':rows+=split(l,r)
assert all(tag!='critical_box' or r-l<arb(2)**-30 for tag,l,r in rows)
out={'passed':True,'adverse_K_plus_derivative_orientations':[tag for tag,_,_ in rows],
 'critical_boxes':[{'lower':str(l),'upper':str(r)} for tag,l,r in rows if tag=='critical_box'],
 'meaning':'increasing_K means adverse f=-K decreases and admits direct Abel bound; decreasing_K is grouped as one finite block before applying Abel to the decaying suffix.'}
(Path(__file__).parents[1]/'results'/'signed-kernel-transition-variation.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
