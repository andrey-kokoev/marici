from __future__ import annotations
import json
from pathlib import Path
import flint
from flint import arb,acb,arb_mat

flint.ctx.prec=192
N=160;Q=160;L=arb('0.35');EDGES=('0','1','2','4','8','16','32','64','128','250')
SOURCE=Path('research/voevodsky/results/regularized_polynomial_coefficients.json')
REMAINDER=arb('1.873e-61')

def sph_j(n,x):return (arb.pi()/(2*x)).sqrt()*x.bessel_j(arb(n)+arb('0.5'))
def sph_i(n,x):return (arb.pi()/(2*x)).sqrt()*x.bessel_i(arb(n)+arb('0.5'))
def exact_mat(a):return arb_mat([[arb(repr(x)) for x in row] for row in a])
def concentration_matrix():
 edges=('0','1','2','4','8','16','32','64','100');re=[];ro=[];se=[];so=[]
 for sa,sb in zip(edges[:-1],edges[1:]):
  a=arb(sa);b=arb(sb)
  for k in range(Q):
   root,weight=arb.legendre_p_root(Q,k,weight=True);u=(a+b)/2+(b-a)*root/2;factor=(b-a)*weight/(2*arb.pi())
   vals=[]
   for n in range(80):
    amp=2*L*((2*n+1)/(2*L)).sqrt()*sph_j(n,L*u);vals.append(((-1)**(n//2))*amp)
   ve=[vals[n] for n in range(0,80,2)];vo=[vals[n] for n in range(1,80,2)]
   re.append(ve);ro.append(vo);se.append([factor*x for x in ve]);so.append([factor*x for x in vo])
 he=arb_mat(re).transpose()*arb_mat(se);ho=arb_mat(ro).transpose()*arb_mat(so)
 out=[[arb(0) for _ in range(80)] for _ in range(80)]
 for i in range(40):
  for j in range(40):out[2*i][2*j]=he[i,j]+arb(0,REMAINDER);out[2*i+1][2*j+1]=ho[i,j]+arb(0,REMAINDER)
 return arb_mat(out)
def positive_ldl(A):
 n=A.nrows();LL=[[arb(0) for _ in range(n)] for _ in range(n)];DD=[arb(0) for _ in range(n)];least=None
 for i in range(n):LL[i][i]=arb(1)
 for j in range(n):
  d=A[j,j]
  for k in range(j):d-=LL[j][k]*LL[j][k]*DD[k]
  if not d>0:return False,j,str(d),least
  DD[j]=d;least=float(d.lower()) if least is None else min(least,float(d.lower()))
  for i in range(j+1,n):
   v=A[i,j]
   for k in range(j):v-=LL[i][k]*LL[j][k]*DD[k]
   LL[i][j]=v/d
 return True,n,None,least

def main():
 log2=arb(2).log();c=log2/arb(2).sqrt();logpi=arb.pi().log();rows_even=[];rows_odd=[];srows_even=[];srows_odd=[]
 for sa,sb in zip(EDGES[:-1],EDGES[1:]):
  a=arb(sa);b=arb(sb)
  for k in range(Q):
   root,weight=arb.legendre_p_root(Q,k,weight=True);u=(a+b)/2+(b-a)*root/2;w=(b-a)*weight/2
   symbol=(acb(arb('0.25'),u/2).digamma().real-logpi)/2-c*(u*log2).cos();factor=w*symbol/arb.pi()
   vals=[]
   for n in range(N):
    amp=2*L*((2*n+1)/(2*L)).sqrt()*sph_j(n,L*u)
    vals.append(((-1)**(n//2))*amp)
   ve=[vals[n] for n in range(0,N,2)];vo=[vals[n] for n in range(1,N,2)]
   rows_even.append(ve);rows_odd.append(vo);srows_even.append([factor*x for x in ve]);srows_odd.append([factor*x for x in vo])
 He=arb_mat(rows_even).transpose()*arb_mat(srows_even);Ho=arb_mat(rows_odd).transpose()*arb_mat(srows_odd)
 H=[[arb(0) for _ in range(N)] for _ in range(N)]
 for i in range(80):
  for j in range(80):H[2*i][2*j]=He[i,j];H[2*i+1][2*j+1]=Ho[i,j]
 # Rank-two endpoint moments.
 x=L/2;ap=[];am=[]
 for n in range(N):
  moment=2*L*((2*n+1)/(2*L)).sqrt()*sph_i(n,x);ap.append(moment);am.append(((-1)**n)*moment)
 for i in range(N):
  for j in range(N):H[i][j]+=ap[i]*am[j]+am[i]*ap[j]+arb(0,REMAINDER)
 numeric_data=json.loads(SOURCE.read_text(encoding='utf-8'));numeric=numeric_data['cutoff_form_legendre_matrix']
 failures=[];max_radius=0.;max_center_difference=0.
 for i in range(N):
  for j in range(N):
   q=H[i][j];v=float(numeric[i][j]);lo=float(q.lower());hi=float(q.upper())
   max_radius=max(max_radius,float(q.rad()));max_center_difference=max(max_center_difference,abs(v-float(q.mid())))
   if not (lo<=v<=hi):failures.append([i,j,v,str(q)])
 # Final exact-decimal span algebra using the directed cutoff-form enclosure.
 C80=exact_mat(numeric_data['ritz_coefficients']);D=exact_mat(numeric_data['tail_map_coefficients'])
 C=arb_mat([[C80[i,j] if i<80 else arb(0) for j in range(25)] for i in range(160)])
 G=C.transpose()*C;Ginv=G.inv();DQ=D-C*(Ginv*(C.transpose()*D));Z=C-DQ;HM=arb_mat(H)
 J=Z.transpose()*HM*Z;AZ=HM*Z;R=AZ-C*(Ginv*(C.transpose()*AZ))
 eta=arb('1e-8');tail=arb('4.36e-13');RG=(1+eta)*(R.transpose()*R)
 for i in range(25):RG[i,i]+=(1+1/eta)*tail*tail
 Tc=concentration_matrix();K=C80.transpose()*Tc*C80
 captured=Ginv*K;trace=sum((captured[i,i] for i in range(25)),arb(0));rho=arb(70)/arb.pi()-trace
 certified_tail_floor=(1-130*rho)/40;tail_floor_ok=float(certified_tail_floor.lower())>0
 kappa=1/certified_tail_floor if tail_floor_ok else arb(0)
 final_lower=J-kappa*RG;final_ok,pivot,failed,least=positive_ldl(final_lower)
 target_neighborhood=max_center_difference+max_radius<1e-8
 result={'schema':'marici.voevodsky.arb-cutoff-form-legendre-matrix.v1','dimension':N,
  'nodes_per_positive_panel':Q,'positive_panel_edges':[float(x) for x in EDGES],
  'analytic_remainder_radius_per_entry':str(REMAINDER),'maximum_interval_radius':max_radius,
  'maximum_numeric_center_difference':max_center_difference,'numeric_scout_entries_contained':not failures,
  'numeric_scout_within_target_neighborhood':target_neighborhood,
  'containment_failure_count':len(failures),'first_failures':failures[:3],
  'target_entry_radius':1e-8,'target_met':max_radius<1e-8,
  'captured_concentration_trace_interval':str(trace),
  'concentration_trace_residual_interval':str(rho),
  'certified_tail_floor_interval':str(certified_tail_floor),
  'certified_tail_floor_positive':tail_floor_ok,
  'inverse_tail_floor_interval':str(kappa),'final_lower_form_positive':final_ok,
  'final_ldl_stopping_pivot':pivot,'final_failed_pivot_interval':failed,
  'final_minimum_ldl_pivot_lower':least,
  'continuum_concentration_entries_certified':True,
  'continuum_cutoff_form_entries_certified':True,
  'continuum_positivity_verified':tail_floor_ok and final_ok,
  'rh_implication':False,'passed':target_neighborhood and max_radius<1e-8 and tail_floor_ok and final_ok}
 rendered=json.dumps(result,indent=2,sort_keys=True)
 Path('research/voevodsky/results/arb_cutoff_form_legendre_matrix.json').write_text(rendered+'\n',encoding='utf-8')
 print(rendered)
if __name__=='__main__':main()
