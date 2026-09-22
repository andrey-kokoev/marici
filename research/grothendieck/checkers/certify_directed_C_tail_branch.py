"""Directed Abel enclosure; no new prime powers beyond N are evaluated.

A(u)=psi(exp(u))-psi(N) lies between zero and M(u)=U(exp(u))-psi(N).
Integration by parts gives tail=-integral K'(u)A(u)du. Boundary terms
vanish at log(N) (A=0) and infinity. For each whole cell, enclose -K'
then multiply by [0,M(right)]. No assumption about prime cancellation.
"""
from pathlib import Path
from fractions import Fraction as Q
import importlib.util,json,hashlib,copy,runpy
from flint import arb,ctx
HERE=Path(__file__).resolve().parent;R=HERE.parent/'results';NR=HERE.parents[1]/'nima'/'results'
def mod(n,p):
 spec=importlib.util.spec_from_file_location(n,p);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);return m
def load(p):return json.loads(p.read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
q=mod('pairing',HERE/'certify_signed_fixed_hat_pairing.py')
_,e=q.compute(N=1000000,bits=256,mesh_divisions=32)
def ball(z):return q.ball(Q(z))
def interval(z):return ball(z['lower']).union(ball(z['upper']))
psi=interval(e['psi_N']);ctx.prec=512
# Freshly replay both sign and critical-box certificates. Keep their actual
# interval endpoints, not rounded decimal display strings.
x=runpy.run_path(str(HERE/'check_signed_kernel_transition_variation.py'))
ts=x['ts'];pv=x['pv'];T=x['T'];B=x['B'];s=x['s'];beta=x['beta'];a=x['a'];lam=x['lam']
y=x['x'];mv=y['mv'];J=y['J'];d=y['d'];u0=arb(1000000).log()
def deriv(u,i,side):
 v=pv if side==0 else mv;m=(v[i+1]-v[i])/(ts[i+1]-ts[i]);p=v[i]+m*(u-ts[i])
 if side==0:
  cp=T[i+1]-(-lam*ts[i+1]).exp()*(v[i+1]/lam+m/lam**2)
  return -s*B*(-s*u).exp()+(-beta*u).exp()*(beta*(p/lam+m/lam**2)-m/lam)-a*cp*(a*u).exp()
 cm=J[i]-(d*ts[i]).exp()*(v[i]/d-m/d**2)
 return s*cm*(-s*u).exp()+(-beta*u).exp()*(beta*(p/d-m/d**2)-m/d)
def M(u):return 2*arb(2).log()*u.exp()+u+arb(2).log()-psi
# Partition additionally at every previously certified transition/critical edge.
edges=set()
for rows in (y['parts'],y['minus'],x['rows']):
 for _,l,r in rows:
  for z in (l,r):edges.update(q.ends(z))
critical=[(q.ends(l)[0],q.ends(r)[1]) for tag,l,r in x['rows'] if tag=='critical_box']
tails=[arb(0),arb(0)];charges=[arb(0),arb(0)];counts=[0,0,0];mesh=512
start=q.ends(u0)[0]
for i in range(len(ts)-1):
 lo=max(start,q.ends(ts[i])[0]);hi=q.ends(ts[i+1])[1]
 if lo>=hi:continue
 cuts=sorted({lo,hi}|{z for z in edges if lo<z<hi})
 for left,right in zip(cuts,cuts[1:]):
  while left<right:
   end=min(right,left+Q(1,mesh));u=ball(left).union(ball(end));width=ball(end-left)
   # Extend A by zero below log(N); this covers its tiny outward rounding strip.
   mass=arb(0).union(q.upper(M(ball(end))))
   iscritical=any(left<r and end>l for l,r in critical)
   for side in (0,1):
    z=-deriv(u,i,side)
    if iscritical:
     z=q.sym(abs(z));charges[side]+=width*q.upper(abs(z))*q.upper(mass)
    counts[0 if z>0 else 1 if z<0 else 2]+=1
    tails[side]+=width*z*mass
   left=end
# Beyond 64: K=c exp(-s u), with c=B or -J(64).
# Integral exp(-s u) M(u)du, in closed form; both coefficients negative.
h=arb(64)
W=2*arb(2).log()*((1-s)*h).exp()/(s-1)+(-s*h).exp()*((h+arb(2).log()-psi)/s+1/s**2)
assert W>0 and B<0 and J[-1]>0
for side,c in enumerate((B,-J[-1])):tails[side]+=(s*c*W).union(arb(0))
base=[interval(z) for z in e['bulk_before_prime_tail']]
C=sum(base,arb(0))+sum(tails,arb(0))+interval(e['endpoint'])+interval(e['h'])
# Intersect with the existing enclosure from the SAME fresh finite computation.
l,h=q.ends(C);ol,oh=q.ends(interval(e['C']));cc=(max(l,ol),min(h,oh));assert cc[0]<=cc[1]
old=load(R/'projection-resolution-conjecture-attack.json');theta=load(R/'theta-mass-refinement.json')
def bounds(z):return Q(z['lower']),Q(z['upper'])
H=bounds(old['h']);L=bounds(old['L']);X=[bounds(theta['windows'][w]['X']) for w in ('A1','B1')];mu=[bounds(theta['windows'][w]['mu']) for w in ('A1','B1')]
assert all(cc[k]+H[k]*(mu[j][k]-L[1-k])>0 for k in (0,1) for j in (0,1))
def gain(k):return 2*X[0][k]*X[1][k]*(cc[k]+H[k]*(mu[0][k]-L[1-k]))*(cc[k]+H[k]*(mu[1][k]-L[1-k]))
g=(gain(0),gain(1));dc=load(NR/'signed-functional-dpc-contract.json');threshold=Q(dc['threshold']);status='CERTIFIED_FEASIBLE' if g[0]>=threshold else 'CERTIFIED_INFEASIBLE' if g[1]<threshold else 'UNRESOLVED'
def enc(v):return {'lower':str(v[0]),'upper':str(v[1])}
branch={'schema':'directed-C-only-Abel-v1','N':1000000,'mesh':mesh,'status':status,'C':enc(cc),'tail_enclosures':[q.enc(z) for z in tails],'absolute_critical_box_charges':[q.enc(z) for z in charges],'critical_box_count':len(critical),'derivative_cell_counts':counts,'finite_pairing_evidence':e,'bindings':{str(p):sha(p) for p in (Path(__file__),HERE/'certify_signed_fixed_hat_pairing.py',HERE/'certify_signed_kernel_tail_signs.py',HERE/'certify_signed_kernel_transition_bands.py',HERE/'check_signed_kernel_transition_variation.py',R/'time-bin-cubic-observer.json',R/'theta-mass-refinement.json',R/'projection-resolution-conjecture-attack.json',NR/'signed-functional-dpc-contract.json')}}
bp=R/'directed-C-only-Abel-branch.json';bp.write_text(json.dumps(branch,indent=2)+'\n')
t=mod('task',HERE/'three_channel_source_task.py');parent=R/'three-channel-source-task-calibration-theta-taylor.json';cal=copy.deepcopy(t.SourceTask(parent).cal)
cal['parent_calibration_file']=parent.name;cal['parent_calibration_sha256']=sha(parent)
for mode in ('private','reuse'):cal['diagonal_refinements'][mode]['positive']={'lower':[str(g[0].numerator),str(g[0].denominator)],'upper':[str(g[1].numerator),str(g[1].denominator)]}
cal['refinement_evidence']={**cal['refinement_evidence'],'method':'directed-C-only-Abel','branch_sha256':sha(bp),'C_bin_lower':[str(cc[0].numerator),str(cc[0].denominator)],'C_bin_upper':[str(cc[1].numerator),str(cc[1].denominator)]}
cp=R/'three-channel-source-task-calibration-directed-Abel.json';cp.write_text(json.dumps(cal,indent=2)+'\n');result=t.SourceTask(cp).certify(dc['task']);assert result['status']==status
report={'passed':True,'status':status,'branch_sha256':sha(bp),'calibration_sha256':sha(cp),'gain':enc(g),'threshold':str(threshold),'task_result':result,'scope':'Quantitative Abel enclosure and frozen-task replay; no general source-coupling admission claimed.'}
(R/'directed-Abel-midpoint-replay.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps({'status':status,'C':enc(cc),'gain':enc(g)},indent=2))
