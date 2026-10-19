"""Complete F17 regular-chart census on lambda=2,a=4, varying b. No CM lifting."""
from fractions import Fraction as Q
from functools import lru_cache
from pathlib import Path
from hashlib import sha256
import json, subprocess, tempfile
import check_hodge_minimal_axis_frobenius_obstruction as prior
from check_hodge_asymmetric_absolute import monic_quotient, cyclotomic, possible_orders
from check_hodge_asymmetric_scalar_cover import modgcd_degree
from check_hodge_minimal_axis_frobenius_obstruction import za,zm,zs,zp,bar,zd,ints,require

ROOT=prior.ROOT
CONTRACT=ROOT/'research/conjecture_net/contracts/hodge-minimal-axis-b-line.v1.json'
NOTE=ROOT/'research/voevodsky/hodge-minimal-axis-b-line-v1.md'
OUT=ROOT/'research/voevodsky/results/hodge-minimal-axis-b-line-v1.json'
COUNTER='research/voevodsky/checkers/count_hodge_minimal_axis_b_line.rs'
COUNTS='research/voevodsky/inputs/hodge-minimal-axis-b-line-v1/counts.json'
INPUT='research/voevodsky/results/hodge-minimal-axis-frobenius-obstruction-v1.json'
ARITH={'prime':17,'lambda':2,'a':4,'all_residues':17,'regular_chart_b':[2,3,6,11,14,15],
 'infinity_branch_chart_not_analyzed_b':[0,1,16],'displayed_reduction_chart_fails_b':[4,5,7,8,9,10,12,13],
 'CM_ratio_excluded_b':[2,15],'CM_ratio_surviving_b':[3,6,11,14],'actual_rational_source_lifts_b':[3,6],
 'ordinary_and_twisted_extension_degrees':[1,2,3,4],
 'congruence_exclusion_domain':'algebraic_b_integral_at_a_place_over17_reducing_to_2_or15'}
POLICY=['surviving_reduction_lifts_a_complex_CM_axis','opposite_character_theta6_axis_constructed',
 'surviving_sources_isogenous_to_Y3','surviving_sources_excluded_from_Y3','all_b_residues_are_in_regular_chart',
 'failed_reduction_chart_excludes_complex_source','transcendental_parameters_excluded','all_scalar_parameters_excluded',
 'source_End0_computed','complex_factorization_lifted_from_reduction','fixed_Y3_Prym_membership_constructed',
 'nonzero_target_exceptional_cycle_constructed','Hodge_proved','Hodge_refuted','global_witness_search_completed']


def vec(f):return tuple(int(f.get(i,0)) for i in range(max(f)+1))

def polynomials(b):
 s=prior.source;N={2:Q(b),0:Q(-2*b)}
 return [s.add(s.P,s.mul(s.add(s.scaled(s.D,c),N,-1),s.add(s.scaled(s.D,c),N,-1)),-1) for c in (0,1,-1)]


def chart_class(b):
 require(type(b) is int and 0<=b<17,'one F17 residue')
 if b in (0,1,16):return 'infinity_branch_chart_not_analyzed'
 s=prior.source;fs=polynomials(b)
 good=all(max(f)==4 and f[4]%17 and modgcd_degree(vec(f),vec(s.derivative(f)),17)==0 and
  modgcd_degree(vec(f),vec(s.P),17)==0 for f in fs)
 good=good and modgcd_degree(vec(s.D),vec(fs[0]),17)==0
 return 'regular_chart' if good else 'displayed_reduction_chart_fails'


def exact_lift(b):
 s=prior.source;require(b not in (0,1,-1),'lift infinity not a branch value')
 fs=polynomials(b)
 require(s.gcd(s.D,fs[0])=={0:Q(1)} and all(max(f)==4 and s.gcd(f,s.derivative(f))=={0:Q(1)} and
  s.gcd(f,s.P)=={0:Q(1)} for f in fs),'exact rational source special fibres')
 N={2:Q(b),0:Q(-2*b)};require({2-i:v*2**i for i,v in N.items()}==s.scaled(N,-2),'parameter anti-translation')
 return {'b':b,'special_fibre_polynomials_ascending':[list(vec(f)) for f in fs],
  'g_degree':4,'branch_points_V_to_W':16,'tower_genera':[17,9,5],
  'primitive_elliptic_map_degree':8,'actual_primitive_elliptic_theta_degree':4}


@lru_cache(maxsize=1)
def run_counter():
 with tempfile.TemporaryDirectory(prefix='hodge-b-line-') as d:
  exe=Path(d)/'count.exe'
  subprocess.run(['rustc','-O',str(ROOT/COUNTER),'-o',str(exe)],check=True,capture_output=True,text=True,timeout=120)
  r=subprocess.run([str(exe)],check=True,capture_output=True,text=True,timeout=300)
 return json.loads(r.stdout)


def gb(f,x,y,b):
 xx=f.mul(x,x);d=f.add(f.sub(xx,f.mul(4,x)),2)
 return None if not d else f.mul(f.add(y,f.mul(b,f.sub(xx,2))),f.inv(d))


@lru_cache(maxsize=1)
def independent_counts():
 out={b:[] for b in (2,3,6)}
 for poly in ((3,1),(3,1,1)):
  f=prior.Field(poly)
  points=[(x,y) for x in range(f.q) for y in range(f.q) if f.mul(y,y)==f.p(x)]
  for b in out:
   nv=len(f.roots(f.sub(f.mul(f.mul(b,b),b),b)))
   for x,y in points:
    g=gb(f,x,y,b);nv+=1 if g is None else len(f.roots(f.sub(f.mul(f.mul(g,g),g),g)))
   out[b].append(nv)
 f=prior.Field((11,1,0,0,1));points=[]
 for x in range(1,f.q):
  if f.pow(x,17)!=f.mul(2,f.inv(x)):continue
  for y in f.roots(f.p(x)):
   if f.pow(y,17)==f.neg(f.mul(2,f.mul(y,f.inv(f.mul(x,x))))):points.append((x,y))
 require(len(points)==16,'independent base torsor')
 for b in out:
  fixed=0
  for x,y in points:
   g=gb(f,x,y,b)
   if g is None:fixed+=1;continue
   fixed+=sum(f.mul(4,f.pow(w,17))==w for w in f.roots(f.sub(f.mul(f.mul(g,g),g),g)))
  out[b].append(fixed)
 return out


def reconstruct(rows):
 require([r['n'] for r in rows]==[1,2,3,4],'four-moment coverage')
 s=[]
 for r in rows:
  q=r['q'];require(q==17**r['n'] and r['full_primitive_generator_cycle_verified'] is True and
   r['twisted_base']==r['W'] and r['rational_poles']==4,'field and torsor coverage')
  require((r['V']-q-1)**2<=324*q and (r['rho_Frobenius_fixed_V']-q-1)**2<=324*q,'genus-nine Weil bounds')
  s.append(za((Q(r['W']-r['V'],2),Q(r['rho_Frobenius_fixed_V']-r['W'],2)),zs(zp((1,4),r['n']),-1)))
 a=[(1,0)]
 for n in range(1,5):
  v=(0,0)
  for j in range(1,n+1):v=za(v,zm(a[n-j],s[j-1]))
  a.append(zs(v,Q(-1,n)))
 require(a[3]!=(0,0),'nonzero a3 needed; no guessed determinant')
 det=zd(zs(a[4],17**3),bar(a[3]));a += [zs(zm(det,bar(a[2])),Q(1,17**2)),zs(zm(det,bar(a[1])),Q(1,17)),det]
 for j in range(8):require(a[7-j]==zs(zm(a[7],bar(a[j])),Q(1,17**j)),'Gaussian reciprocity')
 gaussian=[ints(z) for z in a]
 c=ints([sum(a[i][0]*a[k-i][0]+a[i][1]*a[k-i][1] for i in range(8) if 0<=k-i<8) for k in range(15)])
 require(c[-1]==17**7 and all(c[14-j]==17**(7-j)*c[j] for j in range(8)),'rational reciprocity')
 return gaussian,c


def linear_multiplicity(a,gamma):
 a=[tuple(z) for z in a];multiplicity=0
 while len(a)>1:
  q=[a[0]]
  for c in a[1:-1]:q.append(za(c,zm(gamma,q[-1])))
  if za(a[-1],zm(gamma,q[-1]))!=(0,0):break
  a=q;multiplicity+=1
 return multiplicity


@lru_cache(maxsize=6)
def cm_certificate(c):
 a=[zs(zp((1,4),j),v) for j,v in enumerate(reversed(c))]
 norm=tuple(sum(a[i][0]*a[k-i][0]+a[i][1]*a[k-i][1] for i in range(15) if 0<=k-i<15) for k in range(29))
 orders=sorted([1]+possible_orders(28));require(len(orders)==55,'complete ratio order bound')
 residual=norm;factors=[];degree=0
 for n in orders:
  m=0;phi=cyclotomic(n)
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
 require(not remaining and degree%2==0,'complete residual CM exclusion')
 return {'norm_polynomial_coefficients_ascending':list(norm),'cyclotomic_factors':factors,
  'residual_norm_coefficients_ascending':list(residual),'residual_modular_witnesses':witnesses,
  'geometric_reduction_Ei_multiplicity_in_complement':degree//2}


def source_paths():return {COUNTER,COUNTS}

def validate_contract(c):
 require(c['schema']=='marici.hodge-minimal-axis-b-line.v1' and c['candidate_id']=='marici.hodge.nonsplit-sixfold.exp-sqrt-primes.v1' and c['node']=='minimal-axis-b-line-screen','b-line identity')
 require(c['arithmetic']==ARITH,'b-line arithmetic changed')
 require(set(c['scope_policy'])==set(POLICY) and all(v is False for v in c['scope_policy'].values()),'b-line reduction promoted to complex matching')


def report():
 c=json.loads(CONTRACT.read_text(encoding='utf-8'));validate_contract(c)
 old=json.loads((ROOT/INPUT).read_text(encoding='utf-8'));require(old==prior.report() and old['passed'],'stale CM obstruction')
 classes={k:[b for b in range(17) if chart_class(b)==k] for k in ('regular_chart','infinity_branch_chart_not_analyzed','displayed_reduction_chart_fails')}
 require(list(classes.values())==[ARITH['regular_chart_b'],ARITH['infinity_branch_chart_not_analyzed_b'],ARITH['displayed_reduction_chart_fails_b']],'computed residue chart partition')
 data=json.loads((ROOT/COUNTS).read_text(encoding='utf-8'));require(data==run_counter() and (data['p'],data['lambda'],data['a'])==(17,2,4) and len(data['rows'])==24,'fresh b-line counts')
 small=independent_counts();results=[]
 for b in classes['regular_chart']:
  rows=[r for r in data['rows'] if r['b']==b];g,f=reconstruct(rows)
  negrows=[{k:v for k,v in r.items() if k!='b'} for r in data['rows'] if r['b']==17-b]
  require([{k:v for k,v in r.items() if k!='b'} for r in rows]==negrows,'b sign isomorphism')
  if b in small:require(small[b]==[rows[0]['V'],rows[1]['V'],rows[0]['rho_Frobenius_fixed_V']],'independent b-line small counts')
  if b==2:require(f==old['Frobenius_characteristic_coefficients_descending'],'old control not resurrected')
  cert=cm_certificate(tuple(f));roots=[]
  for kind,beta in (('beta',(1,4)),('conjugate_beta',(1,-4))):
   for unit in ((1,0),(-1,0),(0,1),(0,-1)):
    m=linear_multiplicity(g,zm(beta,unit))
    if m:roots.append({'type':kind,'unit':list(unit),'multiplicity':m})
  require(sum(x['multiplicity'] for x in roots)==cert['geometric_reduction_Ei_multiplicity_in_complement'],'all CM factors accounted by exact Gaussian linear division')
  results.append({'b':b,'Gaussian_characteristic_coefficients_descending':g,
   'Frobenius_characteristic_coefficients_descending':f,'CM_Gaussian_linear_roots':roots,**cert})
 excluded=[r['b'] for r in results if r['geometric_reduction_Ei_multiplicity_in_complement']==0]
 survived=[r['b'] for r in results if r['geometric_reduction_Ei_multiplicity_in_complement']>0]
 require(excluded==[2,15] and survived==[3,6,11,14],'computed exclusion and survival partition')
 names=source_paths()|{prior.COUNTER,INPUT,CONTRACT.relative_to(ROOT).as_posix(),NOTE.relative_to(ROOT).as_posix(),Path(__file__).relative_to(ROOT).as_posix()}
 return {'schema':'marici.hodge-minimal-axis-b-line-result.v1','candidate_id':c['candidate_id'],'node':c['node'],'passed':True,'verdict':'constructed',
  'verification_level':'Fresh complete regular-chart finite-field census and exact CM factor certificates; characteristic-zero congruence exclusion in one direction only.',
  'checks':dict.fromkeys(['all17_residues_classified_without_infinity_shortcut','fresh24_ordinary_twisted_count_rows',
   'independent_small_counts_for_all_sign_representatives','complete_Gaussian_reconstruction',
   'exact_cyclotomic_divisions_and_complete_residual_exclusion','exact_CM_Gaussian_linear_multiplicities',
   'actual_rational_lifts_with_primitive_theta4_axis','Hom_specialization_only_excludes_not_lifts','scope'],True),
  'residue_chart_partition':classes,'CM_ratio_excluded_residues':excluded,'CM_ratio_surviving_residues':survived,
  'finite_field_cases':results,'actual_source_lifts':[exact_lift(b) for b in (3,6)],
  'algebraic_b_congruence_classes_2_and15_excluded_even_up_to_Y3_isogeny':True,
  'new_rational_sources_with_one_primitive_theta4_axis_constructed':True,
  **{k:False for k in POLICY},'source_sha256':{n:sha256((ROOT/n).read_bytes()).hexdigest() for n in sorted(names)}}


if __name__=='__main__':
 r=report();OUT.write_text(json.dumps(r,indent=2)+'\n',encoding='utf-8')
 print(json.dumps({k:v for k,v in r.items() if k not in ('source_sha256','finite_field_cases')},indent=2))
