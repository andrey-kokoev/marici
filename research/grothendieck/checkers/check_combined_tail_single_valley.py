"""Whole-interval single-valley DPC for the combined signed tail kernel."""
from pathlib import Path
from fractions import Fraction as Q
import runpy,json,hashlib
from flint import arb,arb_series
HERE=Path(__file__).resolve().parent;R=HERE.parent/'results'
x=runpy.run_path(str(HERE/'check_cumulative_tail_observer.py'))
kernel=x['kernel'];ts=x['ts'];aq=x['aq'];ends=x['ends'];u0=x['u0'];rows=[]
def inspect(l,r,i,depth=0):
 u=aq(l).union(aq(r));z=kernel(u,i)[1]
 if z<0:rows.append(('negative',l,r,i));return
 if z>0:rows.append(('positive',l,r,i));return
 if depth==36:rows.append(('unresolved',l,r,i));return
 mid=(l+r)/2;inspect(l,mid,i,depth+1);inspect(mid,r,i,depth+1)
for i in range(len(ts)-1):
 l=max(ends(u0)[0],ts[i]);r=ts[i+1]
 if l>=r:continue
 while l<r:
  end=min(r,l+Q(1,8));inspect(l,end,i);l=end
negative=[z for z in rows if z[0]=='negative'];positive=[z for z in rows if z[0]=='positive'];unknown=[z for z in rows if z[0]=='unresolved']
assert negative and positive
# A rigorous opposite-sign ordered pair is a decisive counterexample.
bad=next(((p,n) for p in positive for n in negative if p[2]<=n[1]),None)
root=None;monotone=False
if bad is None and unknown:
 lo=min(z[1] for z in unknown);hi=max(z[2] for z in unknown);indices={z[3] for z in unknown}
 if len(indices)==1:
  i=next(iter(indices));u=aq(lo).union(aq(hi));second=kernel(arb_series([u,arb(1)],2),i)[1][1]
  monotone=second>0
  if monotone and kernel(aq(lo),i)[1]<0<kernel(aq(hi),i)[1]:root=(lo,hi)
# Analytic suffix: K=(B0-J64) exp(-s u), so K'>0 beyond 64.
assert x['T'][0]-x['J'][-1]<0
passed=bad is None and root is not None and all(z[2]<=root[0] for z in negative) and all(z[1]>=root[1] for z in positive)
# Interior certified sign cells within the bracket are harmless if second>0.
if bad is None and root is not None:
 passed=all(z[1]<root[1] for z in negative) and all(z[2]>root[0] for z in positive)
status='CORROBORATED' if passed else 'REFUTED' if bad else 'UNRESOLVED'
def row(z):return {'sign':z[0],'lower':str(z[1]),'upper':str(z[2]),'segment':z[3]}
extremum=None;relaxation_witness=None
if passed:
 # Closed exponential-polynomial antiderivatives, evaluated on the unique
 # root enclosure: the feasible schedule A=0 then A=M attains this value.
 psi=aq(x['psi'][0]).union(aq(x['psi'][1]));D=arb(2).log()-psi;c=2*arb(2).log()
 def primitive(u,rate,A,B):
  def polyexp(rate,p0,p1,p2):
   P=p0+p1*u+p2*u*u;P1=p1+2*p2*u
   return (rate*u).exp()*(P/rate-P1/rate**2+2*p2/rate**3)
  return c*polyexp(rate+1,A,B,arb(0))+polyexp(rate,A*D,A+B*D,B)
 integral=arb(0);rootball=aq(root[0]).union(aq(root[1]));s=x['s'];beta=x['b'];a=x['a'];lam=x['lam'];d=x['d']
 for i in range(len(ts)-1):
  if ts[i+1]<=root[0]:continue
  lo=rootball if ts[i]<=root[0] else aq(ts[i]);hi=aq(ts[i+1]);mp=x['slopes'][0][i];mm=x['slopes'][1][i];p=x['v'][0][i]-mp*aq(ts[i]);m=x['v'][1][i]-mm*aq(ts[i])
  cp=x['T'][i+1]-(-lam*hi).exp()*(x['v'][0][i+1]/lam+mp/lam**2)
  cm=x['J'][i]-(d*aq(ts[i])).exp()*(x['v'][1][i]/d-mm/d**2)
  terms=[(-s,-s*(x['T'][0]-cm),arb(0)),(-beta,beta*(p/lam+mp/lam**2+m/d-mm/d**2)-mp/lam-mm/d,beta*(mp/lam+mm/d)),(a,-a*cp,arb(0))]
  for rate,A,B in terms:integral+=primitive(hi,rate,A,B)-primitive(lo,rate,A,B)
 h=arb(64);W=c*((1-s)*h).exp()/(s-1)+(-s*h).exp()*((h+D)/s+1/s**2)
 integral+=-s*(x['T'][0]-x['J'][-1])*W
 extremum=x['enc'](ends(-integral))
 assert x['joint'][0]<=Q(extremum['lower'])<=Q(extremum['upper'])<=x['joint'][1]
 E=x['E'];components=E['bulk_before_prime_tail']+[E['endpoint'],E['h'],extremum]
 cc=tuple(sum(Q(z[k]) for z in components) for k in ('lower','upper'))
 old=x['load'](R/'projection-resolution-conjecture-attack.json');theta=x['load'](R/'theta-mass-refinement.json')
 def bounds(z):return tuple(Q(z[k]) for k in ('lower','upper'))
 H=bounds(old['h']);L=bounds(old['L']);X=[bounds(theta['windows'][w]['X']) for w in ('A1','B1')];mu=[bounds(theta['windows'][w]['mu']) for w in ('A1','B1')]
 assert all(cc[k]+H[k]*(mu[j][k]-L[1-k])>0 for j in (0,1) for k in (0,1))
 gain=tuple(2*X[0][k]*X[1][k]*(cc[k]+H[k]*(mu[0][k]-L[1-k]))*(cc[k]+H[k]*(mu[1][k]-L[1-k])) for k in (0,1))
 threshold=Q(x['load'](HERE.parents[1]/'nima'/'results'/'signed-functional-dpc-contract.json')['threshold'])
 relaxation_witness={'C_at_extremizer':x['enc'](cc),'gain_at_extremizer':x['enc'](gain),'threshold':str(threshold),'upper_gain_below_threshold':gain[1]<threshold,'scope':'Admissible relaxed measure, NOT prime-realizable evidence or a task infeasibility certificate.'}
out={'status':status,'sharp_tail_minimum':extremum,'relaxation_witness':relaxation_witness,'negative_cells':len(negative),'positive_cells':len(positive),'unresolved_cells':len(unknown),'minimum_box':None if root is None else [str(t) for t in root],'second_derivative_positive_on_box':monotone,'counterexample':None if bad is None else [row(t) for t in bad],'partition':[row(t) for t in rows],'suffix':'K=(B0-J64)exp(-7u/2), B0-J64<0, hence K_prime>0','bindings':{str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in (Path(__file__),HERE/'check_cumulative_tail_observer.py',R/'directed-C-only-Abel-branch.json')}}
(R/'combined-tail-single-valley.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps({k:v for k,v in out.items() if k not in ('partition','bindings')},indent=2))
