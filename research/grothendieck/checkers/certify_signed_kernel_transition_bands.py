"""Adaptive whole-cell sign partition of the two post-log(1e6) transition bands."""
from pathlib import Path
import runpy,json
from flint import arb
x=runpy.run_path(str(__file__).replace('certify_signed_kernel_transition_bands.py','certify_signed_kernel_tail_signs.py'))
ts=x['ts'];pv=x['pv'];mv=x['mv'];T=x['T'];J=x['J'];B=x['B'];s=x['s'];beta=x['beta'];a=x['a'];lam=x['lam'];d=x['d']
def kp(u,i):
 m=(pv[i+1]-pv[i])/(ts[i+1]-ts[i]);cp=T[i+1]-(-lam*ts[i+1]).exp()*(pv[i+1]/lam+m/lam**2)
 return B*(-s*u).exp()-(-beta*u).exp()*((pv[i]+m*(u-ts[i]))/lam+m/lam**2)-cp*(a*u).exp()
def jj(u,i):
 m=(mv[i+1]-mv[i])/(ts[i+1]-ts[i]);b=mv[i]+m*(u-ts[i]);return J[i]+(d*u).exp()*(b/d-m/d**2)-(d*ts[i]).exp()*(mv[i]/d-m/d**2)
def partition(fun,i,lo,hi,depth=40):
 out=[]
 def go(l,r,n):
  z=fun(l.union(r),i)
  if z>0:out.append(('positive',l,r));return
  if z<0:out.append(('negative',l,r));return
  if n==depth:out.append(('root_box',l,r));return
  m=(l+r)/2;go(l,m,n+1);go(m,r,n+1)
 go(lo,hi,0);return out
# K+ starts at log(10^6), crossing two fixed hat segments. J crosses in 16--20.
u0=arb(1000000).log();parts=[]
for i in range(len(ts)-1):
 lo=max(ts[i],u0);hi=min(ts[i+1],arb(16))
 if lo<hi:parts+=partition(kp,i,lo,hi)
mi=ts.index(arb(16));minus=partition(jj,mi,arb(16),arb(20))
def emit(rows):return [{'sign':z,'lower':str(l),'upper':str(r)} for z,l,r in rows]
assert all(z!='root_box' or r-l<arb(2)**-30 for z,l,r in parts+minus)
assert any(z=='positive' for z,_,_ in parts) and any(z=='negative' for z,_,_ in parts)
assert any(z=='positive' for z,_,_ in minus) and any(z=='negative' for z,_,_ in minus)
def psi_upper(u):return 2*arb(2).log()*u+u.log()+arb(2).log()
def adverse(rows,fun,i):
 total=arb(0)
 for sign,l,r in rows:
  if sign!='positive':total+=abs(fun(l.union(r),i))*psi_upper(r.exp())
 return total
# This deliberately overcounts Chebyshev mass cell-by-cell. It is a sound
# reconnaissance radius; the next Stieltjes step must telescope psi instead.
plus_cell_adverse=adverse(parts,kp,ts.index(arb(14)))
minus_cell_adverse=adverse(minus,lambda u,i:-(-s*u).exp()*jj(u,i),mi)
out={'passed':True,'K_plus_transition':emit(parts),'J_minus_transition':emit(minus),
 'non_telescoped_adverse_cell_bounds':{'plus':str(plus_cell_adverse),'minus':str(minus_cell_adverse)},
 'root_box_width_upper':'2^-30','rule':'positive J means negative K_minus; transition root boxes must retain absolute bounds in the subsequent Stieltjes certificate.',
 'scope':'Certified sign partition only; no prime-power tail mass has yet been assigned to these cells.'}
(Path(__file__).parents[1]/'results'/'signed-kernel-transition-bands.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({'passed':True,'K_plus_cells':len(parts),'J_cells':len(minus),'root_boxes':sum(z=='root_box' for z,_,_ in parts+minus)},indent=2))
