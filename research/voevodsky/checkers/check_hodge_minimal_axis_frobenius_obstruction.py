"""One explicit source lacks the SECOND square-lattice elliptic factor. Not family exclusion."""
from fractions import Fraction as Q
from functools import lru_cache
from pathlib import Path
from hashlib import sha256
import json, subprocess, tempfile
import check_hodge_minimal_axis_scalar_source as source
from check_hodge_asymmetric_absolute import possible_orders, cyclotomic
from check_hodge_asymmetric_scalar_cover import modgcd_degree

ROOT=Path(__file__).resolve().parents[3]
CONTRACT=ROOT/'research/conjecture_net/contracts/hodge-minimal-axis-frobenius-obstruction.v1.json'
NOTE=ROOT/'research/voevodsky/hodge-minimal-axis-frobenius-obstruction-v1.md'
OUT=ROOT/'research/voevodsky/results/hodge-minimal-axis-frobenius-obstruction-v1.json'
COUNTER='research/voevodsky/checkers/count_hodge_minimal_axis_frobenius.rs'
COUNTS='research/voevodsky/inputs/hodge-minimal-axis-frobenius-v1/counts.json'
INPUT='research/voevodsky/results/hodge-minimal-axis-scalar-source-v1.json'
POLICY=['all_scalar_parameters_excluded','source_Prym_End0_computed',
 'complex_complementary_sevenfold_simple_proved','reduction_sevenfold_simple',
 'finite_field_factorization_lifted_to_complex_fibre','all_elliptic_factors_excluded',
 'all_Frobenius_root_ratios_excluded','fixed_Y3_Prym_membership_constructed',
 'nonzero_target_exceptional_cycle_constructed','Hodge_proved','Hodge_refuted','global_witness_search_completed']
ARITH={'prime':17,'ordinary_extension_degrees':[1,2,3,4,5],'twisted_extension_degrees':[1,2,3,4],
 'i_mod_prime':4,'known_elliptic_Frobenius':[1,4],'complement_dimension':7,
 'reconstruction':'four_Gaussian_moments_and_unitary_reciprocity_with_nonzero_a3',
 'independent_rational_trace_degree':5,'CM_ratio_norm_polynomial_degree':28,
 'cyclotomic_order_bound':1568,'include_order_one':True}
EXPECTED=[1,-6,11,-28,-39,-186,8187,-47048,139179,-53754,-191607,-2338588,15618427,-144825414,410338673]


def require(c,m):
 if not c:raise ValueError(m)


def za(a,b):return (a[0]+b[0],a[1]+b[1])
def zm(a,b):return (a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0])
def zs(a,c):return (a[0]*c,a[1]*c)
def bar(a):return (a[0],-a[1])
def zd(a,b):return zs(zm(a,bar(b)),Q(1,b[0]**2+b[1]**2))
def zp(a,n):
 r=(1,0)
 for _ in range(n):r=zm(r,a)
 return r

def ints(a):
 require(all(Q(x).denominator==1 for x in a),'Gaussian integrality')
 return [int(x) for x in a]


@lru_cache(maxsize=1)
def run_counter():
 with tempfile.TemporaryDirectory(prefix='hodge-minimal-frob-') as d:
  exe=Path(d)/'count.exe'
  subprocess.run(['rustc','-O',str(ROOT/COUNTER),'-o',str(exe)],check=True,capture_output=True,text=True,timeout=120)
  r=subprocess.run([str(exe)],check=True,capture_output=True,text=True,timeout=300)
 return json.loads(r.stdout)


class Field:
 """Independent digitwise Python arithmetic; no Rust block-addition tables."""
 def __init__(self,poly):
  self.n=len(poly)-1;self.q=17**self.n;self.exp=[];self.log=[-1]*self.q
  red=[sum((-t*c%17)*17**j for j,c in enumerate(poly[:-1])) for t in range(17)];v=1
  for i in range(self.q-1):
   require(v and self.log[v]<0,'Python generator cycle');self.log[v]=i;self.exp.append(v)
   v=self.add(v*17%self.q,red[v//(self.q//17)])
  require(v==1 and all(i>=0 for i in self.log[1:]),'Python field coverage')
 def add(self,a,b):
  v=0;p=1
  while a or b:v+=((a%17+b%17)%17)*p;a//=17;b//=17;p*=17
  return v
 def neg(self,a):return self.exp[(self.log[a]+(self.q-1)//2)%(self.q-1)] if a else 0
 def sub(self,a,b):return self.add(a,self.neg(b))
 def mul(self,a,b):return self.exp[(self.log[a]+self.log[b])%(self.q-1)] if a and b else 0
 def inv(self,a):return self.exp[-self.log[a]%(self.q-1)]
 def pow(self,a,n):return self.exp[self.log[a]*n%(self.q-1)] if a else 0
 def roots(self,a):
  if not a:return [0]
  if self.log[a]%2:return []
  v=self.exp[self.log[a]//2];return [v,self.neg(v)]
 def p(self,x):return self.mul(self.mul(x,self.sub(x,1)),self.sub(x,2))
 def g(self,x,y):
  xx=self.mul(x,x);d=self.add(self.sub(xx,self.mul(4,x)),2)
  return None if not d else self.mul(self.add(y,self.mul(2,self.sub(xx,2))),self.inv(d))


@lru_cache(maxsize=1)
def independent_small_counts():
 rows=[]
 for poly in ((3,1),(3,1,1)):
  f=Field(poly);nw=1;nv=len(f.roots(6));ne=1
  for x in range(f.q):
   ne+=len(f.roots(f.sub(f.mul(f.mul(x,x),x),x)))
   # Direct enumeration of y, not the Rust quadratic-character loop.
   for y in range(f.q):
    if f.mul(y,y)!=f.p(x):continue
    nw+=1;g=f.g(x,y);nv+=1 if g is None else len(f.roots(f.sub(f.mul(f.mul(g,g),g),g)))
  rows.append((nw,nv,ne))
 # All rho*Frob17 fixed points lie over F_(17^4). Directly test the coordinates.
 f=Field((11,1,0,0,1));base=0;fixed=0
 for x in range(1,f.q):
  if f.pow(x,17)!=f.mul(2,f.inv(x)):continue
  for y in f.roots(f.p(x)):
   if f.pow(y,17)!=f.neg(f.mul(2,f.mul(y,f.inv(f.mul(x,x))))):continue
   base+=1;g=f.g(x,y)
   if g is None:fixed+=1;continue
   for w in f.roots(f.sub(f.mul(f.mul(g,g),g),g)):
    fixed+=int(f.mul(4,f.pow(w,17))==w)
 return rows,(base,fixed)


def good_reduction():
 vec=lambda f:tuple(int(f.get(i,0)) for i in range(max(f)+1))
 for f in (source.D,)+(tuple(source.fibre_polynomial(c) for c in (0,1,-1))):
  require(modgcd_degree(vec(f),vec(source.derivative(f)),17)==0 and
   modgcd_degree(vec(f),vec(source.P),17)==0,'good reduction special fibres')
 require(modgcd_degree(vec(source.D),vec(source.fibre_polynomial(0)),17)==0,'good reduction genuine poles')
 return True


def reconstruct(data):
 require(data['p']==17 and data['i_mod_p']==4 and len(data['rows'])==5,'count coverage')
 s=[];beta=(1,4)
 require(zm(beta,bar(beta))==(17,0) and sum((beta[0],beta[0]))==18-data['rows'][0]['E'] and
  (beta[0]+4*beta[1])%17==0,'oriented CM elliptic Frobenius')
 for n,r in enumerate(data['rows'],1):
  require(r['n']==n and r['q']==17**n and r['full_primitive_generator_cycle_verified'] is True,'field coverage')
  require(r['rational_poles']==4 and (r['V']-r['q']-1)**2<=324*r['q'],'pole normalization and Weil bound')
  require((r['W']-r['q']-1)**2<=4*r['q'] and (r['E']-r['q']-1)**2<=4*r['q'],'elliptic Weil bounds')
  if n<=4:
   require(r['twisted_base']==r['W'] and (r['rho_Frobenius_fixed_V']-r['q']-1)**2<=324*r['q'],'Lang torsor and twisted bound')
   s.append(za((Q(r['W']-r['V'],2),Q(r['rho_Frobenius_fixed_V']-r['W'],2)),zs(zp(beta,n),-1)))
 a=[(Q(1),Q(0))]
 for n in range(1,5):
  v=(0,0)
  for j in range(1,n+1):v=za(v,zm(a[n-j],s[j-1]))
  a.append(zs(v,Q(-1,n)))
 require(a[3]!=(0,0),'nonzero a3 required for four-moment reconstruction')
 det=zd(zs(a[4],17**3),bar(a[3]))
 a += [zs(zm(det,bar(a[2])),Q(1,17**2)),zs(zm(det,bar(a[1])),Q(1,17)),det]
 gaussian=[ints(z) for z in a]
 for j in range(8):require(a[7-j]==zs(zm(a[7],bar(a[j])),Q(1,17**j)),'unitary coefficient reciprocity')
 c=[sum(a[i][0]*a[k-i][0]+a[i][1]*a[k-i][1] for i in range(8) if 0<=k-i<8) for k in range(15)]
 c=ints(c);require(c==EXPECTED,'full sevenfold characteristic polynomial')
 moments=[14]
 for n in range(1,6):moments.append(-sum(c[j]*moments[n-j] for j in range(1,n))-n*c[n])
 for n,r in enumerate(data['rows'],1):require(moments[n]==r['W']+r['E']-r['V']-r['q']-1,'independent rational trace control')
 require(c[7]%17==8,'ordinary middle coefficient')
 f4=[1,2,2,34,289];f10=[1,-8,25,-96,86,1296,1462,-27744,122825,-668168,1419857]
 product=[sum(f4[i]*f10[k-i] for i in range(5) if 0<=k-i<11) for k in range(15)]
 require(product==c,'nontrivial reduction factorization')
 return {'Gaussian_power_traces':[ints(z) for z in s],'Gaussian_characteristic_coefficients_descending':gaussian,
  'Frobenius_characteristic_coefficients_descending':c,'rational_power_traces_through_degree5':moments[1:],
  'reduction_factor_coefficients_descending':[f4,f10]}


def cm_ratio_certificate(c):
 beta=(1,4);a=[zs(zp(beta,j),v) for j,v in enumerate(reversed(c))]
 norm=[sum(a[i][0]*a[k-i][0]+a[i][1]*a[k-i][1] for i in range(15) if 0<=k-i<15) for k in range(29)]
 remaining=set([1]+possible_orders(28));require(len(remaining)==55 and max(remaining)==90,'complete CM ratio orders')
 rows=[]
 for ell in (101,103):
  excluded=[n for n in sorted(remaining) if modgcd_degree(norm,cyclotomic(n),ell)==0]
  remaining-=set(excluded);rows.append({'prime':ell,'orders_excluded':excluded,'remaining_orders':sorted(remaining)})
 require(not remaining,'unexcluded CM elliptic root ratio')
 return {'CM_ratio_norm_polynomial_coefficients_ascending':norm,'cyclotomic_orders_checked_including_one':55,
  'cyclotomic_order_search_bound':1568,'CM_ratio_modular_witnesses':rows,
  'all_roots_of_unity_ratios_to_known_CM_Frobenius_excluded':True}


def source_paths():return {COUNTER,COUNTS}

def validate_contract(c):
 require(c['schema']=='marici.hodge-minimal-axis-frobenius-obstruction.v1' and c['candidate_id']=='marici.hodge.nonsplit-sixfold.exp-sqrt-primes.v1' and c['node']=='minimal-axis-scalar-target-transplant','minimal Frobenius identity')
 require(c['arithmetic']==ARITH,'minimal Frobenius arithmetic changed')
 require(set(c['scope_policy'])==set(POLICY) and all(v is False for v in c['scope_policy'].values()),'minimal Frobenius promoted beyond control')


def report():
 c=json.loads(CONTRACT.read_text(encoding='utf-8'));validate_contract(c);good_reduction()
 old=json.loads((ROOT/INPUT).read_text(encoding='utf-8'));require(old==source.report() and old['actual_primitive_theta4_axis_constructed'],'stale minimal source')
 data=json.loads((ROOT/COUNTS).read_text(encoding='utf-8'));require(data==run_counter(),'fresh extension counts changed')
 small,twist=independent_small_counts();require(small==[(r['W'],r['V'],r['E']) for r in data['rows'][:2]] and twist==(data['rows'][0]['twisted_base'],data['rows'][0]['rho_Frobenius_fixed_V']),'independent Python point counts')
 result=reconstruct(data);cert=cm_ratio_certificate(result['Frobenius_characteristic_coefficients_descending'])
 names=source_paths()|{INPUT,CONTRACT.relative_to(ROOT).as_posix(),NOTE.relative_to(ROOT).as_posix(),Path(__file__).relative_to(ROOT).as_posix()}
 return {'schema':'marici.hodge-minimal-axis-frobenius-obstruction-result.v1','passed':True,
  'candidate_id':c['candidate_id'],'node':c['node'],'verdict':'rejected',
  'verification_level':'Fresh ordinary/twisted finite-field counts, Gaussian reciprocity reconstruction and complete CM-ratio exclusion; written specialization excludes this one source, not its family.',
  'checks':dict.fromkeys(['good_reduction_at17','Rust_counts_reexecuted','independent_Python_small_counts',
   'four_Gaussian_moments_and_unitary_reciprocity','unused_fifth_rational_trace_matches',
   'complete_cyclotomic_CM_ratio_exclusion','Hom_specialization_in_correct_direction','one_control_not_whole_family'],True),
  **result,**cert,'reduction_ordinary_at17':True,'reduction_factorization_degrees':[4,10],
  'complement_has_no_square_lattice_elliptic_factor_over_F17bar':True,
  'complex_complement_has_no_square_lattice_elliptic_factor':True,
  'source_square_lattice_elliptic_isogeny_multiplicity':1,'fixed_Y3_square_lattice_elliptic_isogeny_multiplicity':2,
  'this_source_isogenous_to_fixed_Y3':False,**{k:False for k in POLICY},
  'source_sha256':{n:sha256((ROOT/n).read_bytes()).hexdigest() for n in sorted(names)}}


if __name__=='__main__':
 r=report();OUT.write_text(json.dumps(r,indent=2)+'\n',encoding='utf-8')
 print(json.dumps({k:v for k,v in r.items() if k not in ('source_sha256','CM_ratio_norm_polynomial_coefficients_ascending')},indent=2))
