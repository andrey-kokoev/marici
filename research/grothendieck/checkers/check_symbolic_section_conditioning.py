"""Forced conditioning versus selector overhead for the owning symbolic section."""
from pathlib import Path
from fractions import Fraction as Q
import json,hashlib,importlib.util,sys,subprocess
HERE=Path(__file__).resolve().parent;ROOT=HERE.parents[1];R=HERE.parent/'results';NP=ROOT/'nima/checkers/check_symbolic_tail_interface.py'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
# Freshly replay the independent symbolic certificates, then use the actual API.
subprocess.run([sys.executable,str(ROOT/'nima/checkers/verify_symbolic_tail_interface.py')],check=True)
spec=importlib.util.spec_from_file_location('conditioning_symbolic_engine',NP);engine=importlib.util.module_from_spec(spec);sys.modules[spec.name]=engine;spec.loader.exec_module(engine)
contract={'schema':'symbolic-section-conditioning.v1','source':'owning admitted normalized boxes and actual Generator section','source_norm':'sum_j |delta t_j|','observable_norm':'|delta U|+|delta V|','m_values':[2,3,4,8,16,64,256,1024],'prediction':'The greedy interpolation section is globally Lipschitz with constant at most 1+R_m, while every section has Lipschitz constant at least R_m; R_m grows quadratically. No affine section exists for m>=3.','scope':'Norm-relative reconstruction sensitivity, not actual-source inference or audit invariance.'}
cp=R/'symbolic-section-conditioning-contract.json';cp.write_text(json.dumps(contract,indent=2)+'\n')
def enc(q):return str(q)
def profile(model,U):
 k,p,v=model.greedy(U);return [Q(100+2*j) if j<k else p if j==k else Q(0) for j in range(model.m)]
def section(model,U,V):
 packet=model.member((U,V));assert packet['admitted'];f=packet['lift'];theta=Q(f['theta']);hi=profile(model,U);com=profile(model,model.mass(model.m)-U);lo=[Q(100+2*j)-a for j,a in enumerate(com)]
 return [(1-theta)*a+theta*b for a,b in zip(lo,hi)]
records=[]
for m in contract['m_values']:
 G=engine.Generator(m);T=G.mass(m)
 k=sum(2*G.mass(j)+100+2*j<=T for j in range(m));Ck=G.mass(k)
 # D_j=h_j-l_j has a constant sign in U, determined by the order of its
 # two clamp breakpoints. Therefore its L1 norm is the following scalar.
 def ratio(U):
  high=G.greedy(U)[2];low=G.weighted(m)-G.greedy(T-U)[2];W=high-low;assert W>0
  norm=2*(min(U,Ck)-max(Q(0),U-(T-Ck)))
  return norm/W,norm,W
 breaks=sorted({G.mass(j) for j in range(m+1)}|{T-G.mass(j) for j in range(m+1)})
 candidates=[(Q(2)/(1-Q(1,128**(m-1))),Q(0))]
 candidates += [(ratio(U)[0],U) for U in breaks if 0<U<T]
 Rm,where=max(candidates);mid,midnorm,midgap=ratio(T/2)
 coarse=Q(128)*T/12700
 assert mid<=Rm<=coarse
 # Independent all-m growth lower estimate: midpoint profiles differ by at
 # least T-maxcap, while weighted gap is <=W_infinity.
 Winf=Q(100)/(1-Q(1,128))+2*Q(1,128)/(1-Q(1,128))**2
 growth=(T-(100+2*(m-1)))/Winf;assert growth<=mid
 # Exercise actual membership lift, not only the closed scalar formulas.
 cases=[]
 for U in sorted({Q(1,1024),T/2,T-Q(1,1024)}):
  hi=profile(G,U);lo=[Q(100+2*j)-a for j,a in enumerate(profile(G,T-U))]
  H=G.greedy(U)[2];L=G.weighted(m)-G.greedy(T-U)[2]
  assert sum(abs(a-b) for a,b in zip(hi,lo))==ratio(U)[1]
  lifted=[];membership_packets=[]
  for theta in (Q(0),Q(1,3),Q(1)):
   V=L+theta*(H-L);membership_packets.append({'V':str(V),'answer':G.member((U,V))});v=section(G,U,V)
   assert sum(v)==U and sum(a*Q(1,128**j) for j,a in enumerate(v))==V
   assert all(0<=a<=100+2*j for j,a in enumerate(v))
   assert v==[(1-theta)*a+theta*b for a,b in zip(lo,hi)]
   lifted.append(v)
  assert sum(abs(a-b) for a,b in zip(lifted[0],lifted[-1]))/(H-L)<=Rm
  cases.append({'U':str(U),'low':str(L),'high':str(H),'profile_distance':str(ratio(U)[1]),'membership_packets':membership_packets})
 records.append({'m':m,'total_capacity':str(T),'positive_prefix':k,'R_m':str(Rm),'maximizing_mass_or_tip':str(where),'global_greedy_upper':str(1+Rm),'midpoint_lower':str(mid),'quadratic_lower':str(growth),'quadratic_upper':str(coarse),'breakpoint_count':len(breaks),'lift_controls':cases})
# Any affine section A would satisfy A(1,r_j)=e_j on every exposed box edge.
# For j=0,1,2 the observable directions obey a nontrivial linear dependence,
# but their three required source images are independent.
r0,r1,r2=Q(1),Q(1,128),Q(1,128**2)
alpha=(r2-r0)/(r1-r0);beta=1-alpha
assert alpha*r1+beta*r0==r2 and alpha+beta==1
nonaffine={'m_min':3,'direction_relation':{'g2_equals_alpha_g1_plus_beta_g0':[str(alpha),str(beta)]},'impossible_source_relation':'e2=alpha*e1+beta*e0','reason':'Each projected generator edge has a unique source lift; endpoint differences force these identities for any affine section.'}
out={'schema':'symbolic-section-conditioning-result.v1','records':records,'nonaffine_obstruction':nonaffine,'contract_sha256':sha(cp),'bindings':{str(p):sha(p) for p in (Path(__file__),cp,NP,ROOT/'nima/results/symbolic-tail-interface-contract.json',R/'two-moment-tail-complexity.json')},'status':'INTRINSIC_QUADRATIC_CONDITIONING_WITH_ADDITIVE_ONE_SELECTOR_BOUND','scope':'General bounds rely on the piecewise derivative proof; finite exact controls check its implementation, not a sampled Lipschitz assertion.'}
(R/'symbolic-section-conditioning.json').write_text(json.dumps(out,indent=2)+'\n')
print([(r['m'],float(Q(r['R_m']))) for r in records])
