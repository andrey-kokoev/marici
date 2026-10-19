"""Independent split-prime veto of b6; b3 survives two necessary screens, no lift."""
from fractions import Fraction as Q
from functools import lru_cache
from pathlib import Path
from hashlib import sha256
import json, subprocess, tempfile
import check_hodge_minimal_axis_b_line as line
from check_hodge_minimal_axis_frobenius_obstruction import za,zm,zs,zp,bar,zd,ints,require
from check_hodge_asymmetric_absolute import cyclotomic,possible_orders,monic_quotient
from check_hodge_asymmetric_scalar_cover import modgcd_degree

ROOT=line.ROOT
CONTRACT=ROOT/'research/conjecture_net/contracts/hodge-minimal-axis-second-prime.v1.json'
NOTE=ROOT/'research/voevodsky/hodge-minimal-axis-second-prime-v1.md'
OUT=ROOT/'research/voevodsky/results/hodge-minimal-axis-second-prime-v1.json'
COUNTER='research/voevodsky/checkers/count_hodge_minimal_axis_second_prime.rs'
COUNTS='research/voevodsky/inputs/hodge-minimal-axis-second-prime-v1/counts.json'
INPUT='research/voevodsky/results/hodge-minimal-axis-b-line-v1.json'
CONTROLS=[{'b':3,'p':13,'i_mod_p':5,'beta':[3,2],'extra_Ei_multiplicity_in_reduction':2},
 {'b':6,'p':29,'i_mod_p':12,'beta':[-5,-2],'extra_Ei_multiplicity_in_reduction':0}]
ARITH={'lambda':2,'a':4,'controls':CONTROLS,'ordinary_extension_degrees':[1,2,3,4,5],
 'twisted_extension_degrees':[1,2,3,4],'b6_exclusion_congruences_mod29':[6,23],
 'congruence_exclusion_domain':'algebraic_b_integral_at_a_place_over29_reducing_to_6_or23'}
POLICY=['b6_source_construction_invalidated','b6_exclusion_transferred_to_b3',
 'b3_surviving_reductions_lift_a_complex_CM_axis','b3_two_prime_survival_proves_target_match',
 'opposite_character_theta6_axis_constructed','source_End0_computed','complex_factorization_lifted_from_reduction',
 'all_four_poles_rational_in_every_extension','all_b_line_parameters_excluded','all_scalar_parameters_excluded',
 'transcendental_parameters_excluded','fixed_Y3_Prym_membership_constructed','nonzero_target_exceptional_cycle_constructed',
 'Hodge_proved','Hodge_refuted','global_witness_search_completed']


def good_reduction(b,p):
 s=line.prior.source;fs=line.polynomials(b)
 require(b%p not in (0,1,p-1) and all(f[4]%p and modgcd_degree(line.vec(f),line.vec(s.derivative(f)),p)==0 and
  modgcd_degree(line.vec(f),line.vec(s.P),p)==0 for f in fs),'good prime special fibres')
 require(modgcd_degree(line.vec(s.D),line.vec(s.derivative(s.D)),p)==0 and
  modgcd_degree(line.vec(s.D),line.vec(s.P),p)==0 and modgcd_degree(line.vec(s.D),line.vec(fs[0]),p)==0,'good prime genuine poles')
 return True


@lru_cache(maxsize=1)
def run_counter():
 with tempfile.TemporaryDirectory(prefix='hodge-second-prime-') as d:
  exe=Path(d)/'count.exe'
  subprocess.run(['rustc','-O',str(ROOT/COUNTER),'-o',str(exe)],check=True,capture_output=True,text=True,timeout=120)
  r=subprocess.run([str(exe)],check=True,capture_output=True,text=True,timeout=300)
 return json.loads(r.stdout)


class Field:
 """Independent digitwise arithmetic, no Rust p^2-chunk table."""
 def __init__(self,p,poly):
  self.p=p;self.q=p**(len(poly)-1);self.exp=[];self.log=[-1]*self.q
  red=[sum((-t*c%p)*p**j for j,c in enumerate(poly[:-1])) for t in range(p)];v=1
  for j in range(self.q-1):
   require(v and self.log[v]<0,'independent generator cycle');self.log[v]=j;self.exp.append(v)
   v=self.add(v*p%self.q,red[v//(self.q//p)])
  require(v==1 and all(j>=0 for j in self.log[1:]),'independent field coverage')
 def add(self,a,b):
  r=0;t=1;p=self.p
  while a or b:r+=((a%p+b%p)%p)*t;a//=p;b//=p;t*=p
  return r
 def neg(self,a):return self.exp[(self.log[a]+(self.q-1)//2)%(self.q-1)] if a else 0
 def sub(self,a,b):return self.add(a,self.neg(b))
 def mul(self,a,b):return self.exp[(self.log[a]+self.log[b])%(self.q-1)] if a and b else 0
 def inv(self,a):
  require(a!=0,'nonzero independent divisor');return self.exp[-self.log[a]%(self.q-1)]
 def pow(self,a,n):return self.exp[self.log[a]*n%(self.q-1)] if a else 0
 def roots(self,a):
  if a==0:return [0]
  if self.log[a]%2:return []
  r=self.exp[self.log[a]//2];return [r,self.neg(r)]
 def wp(self,x):return self.mul(self.mul(x,self.sub(x,1)),self.sub(x,2))


@lru_cache(maxsize=2)
def independent_counts(p,b,i,moduli):
 out=[]
 for poly in moduli[:2]:
  f=Field(p,poly);nw=1;nv=len(f.roots(f.sub(f.mul(f.mul(b,b),b),b)));ne=1
  for x in range(f.q):
   ne+=len(f.roots(f.sub(f.mul(f.mul(x,x),x),x)))
   for y in range(f.q):
    if f.mul(y,y)!=f.wp(x):continue
    nw+=1;g=line.gb(f,x,y,b)
    nv+=1 if g is None else len(f.roots(f.sub(f.mul(f.mul(g,g),g),g)))
  out.append([nw,nv,ne])
 f=Field(p,moduli[3]);base=0;fixed=0
 for x in range(1,f.q):
  if f.pow(x,p)!=f.mul(2,f.inv(x)):continue
  for y in f.roots(f.wp(x)):
   if f.pow(y,p)!=f.neg(f.mul(2,f.mul(y,f.inv(f.mul(x,x))))):continue
   base+=1;g=line.gb(f,x,y,b)
   if g is None:fixed+=1;continue
   fixed+=sum(f.mul(i,f.pow(w,p))==w for w in f.roots(f.sub(f.mul(f.mul(g,g),g),g)))
 return out,[base,fixed]


def reconstruct(case,control):
 p=control['p'];beta=tuple(control['beta']);rows=case['rows'];i=control['i_mod_p'];b=control['b']
 require((case['p'],case['b'],case['i_mod_p'])==(p,b,i) and len(rows)==5,'second-prime count coverage')
 require(zm(beta,bar(beta))==(p,0) and (beta[0]+i*beta[1])%p==0 and i*i%p==p-1 and
  2*beta[0]==p+1-rows[0]['E'],'oriented CM elliptic Frobenius')
 s=[]
 for n,r in enumerate(rows,1):
  q=p**n;require(r['n']==n and r['q']==q and r['full_primitive_generator_cycle_verified'] is True,'extension field coverage')
  require(r['rational_poles']==(4 if n%2==0 else 0),'nonrational pole normalization')
  require(r['W']==r['E'] and (r['W']-q-1)**2<=4*q and (r['V']-q-1)**2<=324*q,'untwisted Weil bounds')
  if n<=4:
   require(r['twisted_base']==r['W'] and (r['rho_Frobenius_fixed_V']-q-1)**2<=324*q,'twisted Lang torsor and Weil bound')
   s.append(za((Q(r['W']-r['V'],2),Q(r['rho_Frobenius_fixed_V']-r['W'],2)),zs(zp(beta,n),-1)))
 a=[(1,0)]
 for n in range(1,5):
  z=(0,0)
  for j in range(1,n+1):z=za(z,zm(a[n-j],s[j-1]))
  a.append(zs(z,Q(-1,n)))
 require(a[3]!=(0,0),'nonzero a3, not a guessed determinant')
 det=zd(zs(a[4],p**3),bar(a[3]));a += [zs(zm(det,bar(a[2])),Q(1,p**2)),zs(zm(det,bar(a[1])),Q(1,p)),det]
 for j in range(8):require(a[7-j]==zs(zm(a[7],bar(a[j])),Q(1,p**j)),'unitary coefficient reciprocity')
 gaussian=[ints(z) for z in a]
 c=ints([sum(a[j][0]*a[k-j][0]+a[j][1]*a[k-j][1] for j in range(8) if 0<=k-j<8) for k in range(15)])
 require(c[-1]==p**7 and all(c[14-j]==p**(7-j)*c[j] for j in range(8)),'rational Weil reciprocity')
 moments=[14]
 for n in range(1,6):moments.append(-sum(c[j]*moments[n-j] for j in range(1,n))-n*c[n])
 for n,r in enumerate(rows,1):require(moments[n]==r['W']+r['E']-r['V']-r['q']-1,'unused fifth rational trace control')
 return {'Gaussian_power_traces':[ints(z) for z in s],'Gaussian_characteristic_coefficients_descending':gaussian,
  'Frobenius_characteristic_coefficients_descending':c,'rational_power_traces_through_degree5':moments[1:],
  'ordinary_reduction':c[7]%p!=0}


@lru_cache(maxsize=2)
def cm_certificate(c,beta):
 a=[zs(zp(beta,j),v) for j,v in enumerate(reversed(c))]
 norm=tuple(sum(a[j][0]*a[k-j][0]+a[j][1]*a[k-j][1] for j in range(15) if 0<=k-j<15) for k in range(29))
 orders=sorted([1]+possible_orders(28));require(len(orders)==55,'complete cyclotomic ratio coverage')
 residual=norm;factors=[];degree=0
 for n in orders:
  phi=cyclotomic(n);m=0
  while len(residual)>=len(phi):
   try:q=monic_quotient(residual,phi)
   except ValueError:break
   residual=q;m+=1
  if m:factors.append({'order':n,'multiplicity':m});degree+=m*(len(phi)-1)
 remaining=set(orders);witnesses=[]
 for ell in (101,103,107,109,113,127,131):
  removed=[n for n in sorted(remaining) if modgcd_degree(residual,cyclotomic(n),ell)==0]
  remaining-=set(removed);witnesses.append({'prime':ell,'orders_excluded':removed,'remaining_orders':sorted(remaining)})
  if not remaining:break
 require(not remaining and degree%2==0,'complete residual CM ratio exclusion')
 require(zd(beta,bar(beta)) not in ((1,0),(-1,0),(0,1),(0,-1)),'ordinary Ei ratio not torsion')
 return {'norm_polynomial_coefficients_ascending':list(norm),'cyclotomic_factors':factors,
  'residual_norm_coefficients_ascending':list(residual),'residual_modular_witnesses':witnesses,
  'geometric_reduction_Ei_multiplicity_in_complement':degree//2}


def source_paths():return {COUNTER,COUNTS}

def validate_contract(c):
 require(c['schema']=='marici.hodge-minimal-axis-second-prime.v1' and c['candidate_id']=='marici.hodge.nonsplit-sixfold.exp-sqrt-primes.v1' and
  c['node']=='minimal-axis-second-prime-screen' and c['excluded_control_node']=='minimal-axis-b6-target-transplant','second-prime identity')
 require(c['arithmetic']==ARITH,'second-prime arithmetic changed')
 require(set(c['scope_policy'])==set(POLICY) and all(v is False for v in c['scope_policy'].values()),'second-prime evidence promoted beyond scope')


def report():
 c=json.loads(CONTRACT.read_text(encoding='utf-8'));validate_contract(c)
 old=json.loads((ROOT/INPUT).read_text(encoding='utf-8'));require(old==line.report() and old['passed'],'stale b-line screen')
 data=json.loads((ROOT/COUNTS).read_text(encoding='utf-8'));require(data==run_counter() and len(data['cases'])==2,'fresh second-prime extension counts')
 good_reduction(23,29)  # the negative-b reduction is isomorphic over F29 via (-p,i*w)
 results=[]
 for case,control in zip(data['cases'],CONTROLS):
  p=control['p'];b=control['b'];good_reduction(b,p);result=reconstruct(case,control)
  small,twist=independent_counts(p,b,control['i_mod_p'],tuple(tuple(r['modulus']) for r in case['rows']))
  require(small==[[r['W'],r['V'],r['E']] for r in case['rows'][:2]] and twist==[case['rows'][0]['twisted_base'],case['rows'][0]['rho_Frobenius_fixed_V']],'independent second-prime counts')
  cert=cm_certificate(tuple(result['Frobenius_characteristic_coefficients_descending']),tuple(control['beta']))
  require(cert['geometric_reduction_Ei_multiplicity_in_complement']==control['extra_Ei_multiplicity_in_reduction'],'second-prime CM multiplicity')
  roots=[]
  for kind,beta in (('beta',tuple(control['beta'])),('conjugate_beta',bar(tuple(control['beta'])))):
   for unit in ((1,0),(-1,0),(0,1),(0,-1)):
    m=line.linear_multiplicity(result['Gaussian_characteristic_coefficients_descending'],zm(beta,unit))
    if m:roots.append({'type':kind,'unit':list(unit),'multiplicity':m})
  require(sum(r['multiplicity'] for r in roots)==cert['geometric_reduction_Ei_multiplicity_in_complement'],'exact Gaussian CM factors exhaustive')
  results.append({'b':b,'p':p,'beta':control['beta'],**result,**cert,'CM_Gaussian_linear_roots':roots})
 names=source_paths()|{INPUT,CONTRACT.relative_to(ROOT).as_posix(),NOTE.relative_to(ROOT).as_posix(),Path(__file__).relative_to(ROOT).as_posix()}
 return {'schema':'marici.hodge-minimal-axis-second-prime-result.v1','candidate_id':c['candidate_id'],'node':c['node'],
  'excluded_control_node':c['excluded_control_node'],'b6_control_verdict':'rejected','passed':True,'verdict':'constructed',
  'verification_level':'Fresh generic-prime Rust enumeration, independent Python small counts, full Gaussian reconstruction, unused fifth traces, complete CM-ratio certificates and one-way Hom specialization.',
  'checks':dict.fromkeys(['both_good_reduction_primes_certified','fresh_10_ordinary_8_twisted_count_rows','independent_small_counts_and_direct_twisted_counts',
   'Gaussian_unitary_reconstruction','unused_fifth_trace_for_both_sources','complete_cyclotomic_CM_ratio_certificates',
   'b6_absence_specializes_against_complex_CM_factor','b3_survival_not_lifted','scope'],True),
  'finite_field_cases':results,'b3_necessary_prime_screens_survived':[13,17],
  'b6_complex_complement_has_no_Ei_factor':True,'b6_source_Ei_isogeny_multiplicity':1,
  'fixed_Y3_Ei_isogeny_multiplicity':2,'b6_source_isogenous_to_fixed_Y3':False,
  'algebraic_b_congruence_classes_6_and23_mod29_excluded':True,
  **{k:False for k in POLICY},'source_sha256':{n:sha256((ROOT/n).read_bytes()).hexdigest() for n in sorted(names)}}


if __name__=='__main__':
 r=report();OUT.write_text(json.dumps(r,indent=2)+'\n',encoding='utf-8')
 print(json.dumps({k:v for k,v in r.items() if k not in ('source_sha256','finite_field_cases')},indent=2))
