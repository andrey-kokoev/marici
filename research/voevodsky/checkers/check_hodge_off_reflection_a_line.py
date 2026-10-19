"""Full regular-chart denominator-line screen at13, beyond known reflections."""
from fractions import Fraction as Q
from functools import lru_cache
from pathlib import Path
from hashlib import sha256
import json,subprocess,tempfile
import check_hodge_scalar_reflection_decomposition as reflection
import check_hodge_minimal_axis_second_prime as prior
from check_hodge_minimal_axis_frobenius_obstruction import za,zm,zs,zp,bar,zd,ints,require
from check_hodge_asymmetric_scalar_cover import modgcd_degree
from check_hodge_asymmetric_absolute import monic_quotient

ROOT=reflection.ROOT
CONTRACT=ROOT/'research/conjecture_net/contracts/hodge-off-reflection-a-line.v1.json'
NOTE=ROOT/'research/voevodsky/hodge-off-reflection-a-line-v1.md'
OUT=ROOT/'research/voevodsky/results/hodge-off-reflection-a-line-v1.json'
COUNTER='research/voevodsky/checkers/count_hodge_off_reflection_control.rs'
COUNTS='research/voevodsky/inputs/hodge-off-reflection-a-line-v1/counts.json'
INPUTS={'reflection':reflection.OUT,'arithmetic':prior.OUT}
REGULAR=[0,2,6,7,8,10,11,12];EXCLUDED=[0,7,8,10,11,12]
ARITH={'prime':13,'lambda':2,'b':2,'i_mod_p':5,'beta':[3,2],
 'regular_a_residues':REGULAR,'failed_model_a_residues':[1,3,4,5,9],
 'CM_ratio_excluded_a_residues':EXCLUDED,'CM_ratio_surviving_a_residues':[2,6],
 'ordinary_extension_degrees':[1,2,3,4,5],'twisted_extension_degrees':[1,2,3,4],
 'new_actual_off_reflection_control':[2,6,2],
 'negative_congruence_domain':'algebraic_integral_lambda_a_b_with_residues_lambda2_a_in_excluded_list_b2_or11_at_a_place_over13'}
POLICY=['all_denominator_parameters_excluded','failed_model_excludes_complex_source',
 'whole_a2_residue_class_excluded_by_exact_reflection','surviving_reduction_lifts_a_complex_CM_axis',
 'opposite_character_theta6_axis_constructed','finite_field_degree12_factor_identified_with_fixed_X6',
 'finite_field_degree12_factor_simple_proved','source_End0_computed','off_reflection_implies_target_compatible',
 'actual_source_constructions_invalidated','transcendental_parameters_excluded_by_this_arithmetic',
 'all_scalar_parameters_excluded','fixed_Y3_Prym_membership_constructed','nonzero_target_exceptional_cycle_constructed',
 'Hodge_proved','Hodge_refuted','global_witness_search_completed']


def branch_polynomials(a,b=2):
 s=reflection.src;d={2:Q(1),1:Q(-a),0:Q(2)};n={2:Q(b),0:Q(-2*b)}
 fs=[s.add(s.P,s.mul(s.add(s.scaled(d,c),n,-1),s.add(s.scaled(d,c),n,-1)),-1) for c in (0,1,-1)]
 return d,fs

def good_model(a,b=2):
 s=reflection.src;d,fs=branch_polynomials(a,b);v=prior.line.vec;g=modgcd_degree
 return (b%13 not in (0,1,12) and g(v(d),v(s.derivative(d)),13)==0 and g(v(d),v(s.P),13)==0 and
  g(v(d),v(fs[0]),13)==0 and all(f[4]%13 and g(v(f),v(s.derivative(f)),13)==0 and g(v(f),v(s.P),13)==0 for f in fs))

def pole_certificate():
 r=reflection;x=r.X;l=r.L;a=r.A
 p=r.mul(r.mul(x,r.sub(x,r.O)),r.sub(x,l));d=r.add(r.sub(r.power(x,2),r.mul(a,x)),l)
 require(r.sub(p,r.mul(r.sub(r.sub(a,l),r.O),r.power(x,2)))==r.mul(x,d),'generic denominator pole identity')
 return True

def prime_poles(a):return 4 if pow((a*a-8)%13,6,13)==1 and pow((a-3)%13,6,13)==1 else 0


@lru_cache(maxsize=1)
def run_counter():
 with tempfile.TemporaryDirectory(prefix='hodge-a-line-') as d:
  exe=Path(d)/'count.exe'
  subprocess.run(['rustc','-O',str(ROOT/COUNTER),'-o',str(exe)],check=True,capture_output=True,text=True,timeout=120)
  p=subprocess.run([str(exe)],check=True,capture_output=True,text=True,timeout=300)
 return json.loads(p.stdout)


def ga(f,x,y,a):
 xx=f.mul(x,x);d=f.add(f.sub(xx,f.mul(a,x)),2)
 return None if d==0 else f.mul(f.add(y,f.mul(2,f.sub(xx,2))),f.inv(d))


@lru_cache(maxsize=1)
def independent_counts():
 out={a:[] for a in REGULAR}
 for poly in ((2,1),(2,1,1)):
  f=prior.Field(13,poly);points=[(x,y) for x in range(f.q) for y in range(f.q) if f.mul(y,y)==f.wp(x)]
  for a in out:
   v=len(f.roots(6))
   for x,y in points:
    g=ga(f,x,y,a);v+=1 if g is None else len(f.roots(f.sub(f.mul(f.mul(g,g),g),g)))
   out[a].append(v)
 f=prior.Field(13,(2,1,1,0,1));points=[]
 for x in range(1,f.q):
  if f.pow(x,13)!=f.mul(2,f.inv(x)):continue
  for y in f.roots(f.wp(x)):
   if f.pow(y,13)==f.neg(f.mul(2,f.mul(y,f.inv(f.mul(x,x))))):points.append((x,y))
 require(len(points)==8,'independent a-line base torsor')
 for a in out:
  fixed=0
  for x,y in points:
   g=ga(f,x,y,a)
   if g is None:fixed+=1;continue
   fixed+=sum(f.mul(5,f.pow(w,13))==w for w in f.roots(f.sub(f.mul(f.mul(g,g),g),g)))
  out[a].append(fixed)
 return out


def reconstruct(rows,a):
 require(len(rows)==5 and [r['n'] for r in rows]==[1,2,3,4,5],'five extension counts')
 s=[];beta=(3,2)
 for n,r in enumerate(rows,1):
  q=13**n;require(r['a']==a and r['q']==q and r['full_primitive_generator_cycle_verified'] is True,'a-line field coverage')
  require(r['rational_poles']==(prime_poles(a) if n%2 else 4),'a-dependent pole normalization')
  require(r['W']==r['E'] and (r['W']-q-1)**2<=4*q and (r['V']-q-1)**2<=324*q,'a-line untwisted Weil bounds')
  if n<=4:
   require(r['twisted_base']==r['W'] and (r['rho_Frobenius_fixed_V']-q-1)**2<=324*q,'a-line torsor and twisted bound')
   s.append(za((Q(r['W']-r['V'],2),Q(r['rho_Frobenius_fixed_V']-r['W'],2)),zs(zp(beta,n),-1)))
 require(rows[0]['E']==8 and (3+5*2)%13==0,'oriented beta13')
 coeff=[(1,0)]
 for n in range(1,5):
  v=(0,0)
  for j in range(1,n+1):v=za(v,zm(coeff[n-j],s[j-1]))
  coeff.append(zs(v,Q(-1,n)))
 require(coeff[3]!=(0,0),'nonzero a3 required for four-moment reconstruction')
 det=zd(zs(coeff[4],13**3),bar(coeff[3]));coeff += [zs(zm(det,bar(coeff[2])),Q(1,13**2)),zs(zm(det,bar(coeff[1])),Q(1,13)),det]
 for j in range(8):require(coeff[7-j]==zs(zm(coeff[7],bar(coeff[j])),Q(1,13**j)),'a-line Gaussian reciprocity')
 g=[ints(z) for z in coeff]
 c=ints([sum(coeff[j][0]*coeff[k-j][0]+coeff[j][1]*coeff[k-j][1] for j in range(8) if 0<=k-j<8) for k in range(15)])
 require(c[-1]==13**7 and all(c[14-j]==13**(7-j)*c[j] for j in range(8)),'a-line rational reciprocity')
 moments=[14]
 for n in range(1,6):moments.append(-sum(c[j]*moments[n-j] for j in range(1,n))-n*c[n])
 for n,r in enumerate(rows,1):require(moments[n]==r['W']+r['E']-r['V']-r['q']-1,'unused fifth rational trace')
 return {'Gaussian_power_traces':[ints(z) for z in s],'Gaussian_characteristic_coefficients_descending':g,
  'Frobenius_characteristic_coefficients_descending':c,'rational_power_traces_through_degree5':moments[1:],
  'ordinary_reduction':c[7]%13!=0}


@lru_cache(maxsize=8)
def cm_certificate(c):return prior.cm_certificate(c,(3,2))


def actual_control():
 s=reflection.src;d,fs=branch_polynomials(6)
 require(src_gcd_one(d,s.derivative(d)) and src_gcd_one(d,s.P) and src_gcd_one(d,fs[0]) and
  all(max(f)==4 and src_gcd_one(f,s.derivative(f)) and src_gcd_one(f,s.P) for f in fs),'actual a6 source')
 return {'parameters_lambda_a_b':[2,6,2],'tower_genera':[17,9,5],'primitive_elliptic_theta_degree':4,
  'known_reflection_loci_escaped':True,'special_fibre_polynomials_ascending':[list(prior.line.vec(f)) for f in fs]}

def src_gcd_one(f,g):return reflection.src.gcd(f,g)=={0:Q(1)}
def source_paths():return {COUNTER,COUNTS}

def validate_contract(c):
 require(c['schema']=='marici.hodge-off-reflection-a-line.v1' and c['candidate_id']=='marici.hodge.nonsplit-sixfold.exp-sqrt-primes.v1' and
  c['node']=='off-reflection-a-line-screen' and c['excluded_control_node']=='off-reflection-a-line-target-transplant','a-line identity')
 require(c['arithmetic']==ARITH,'a-line arithmetic changed')
 require(set(c['scope_policy'])==set(POLICY) and all(v is False for v in c['scope_policy'].values()),'a-line evidence promoted beyond scope')


def report():
 c=json.loads(CONTRACT.read_text(encoding='utf-8'));validate_contract(c);pole_certificate()
 fresh={'reflection':reflection.report(),'arithmetic':prior.report()}
 for k,p in INPUTS.items():require(json.loads(p.read_text(encoding='utf-8'))==fresh[k] and fresh[k]['passed'],'stale a-line '+k)
 require([a for a in range(13) if good_model(a)]==REGULAR,'complete a-line chart partition')
 require(all(good_model(a,11) for a in EXCLUDED),'negative b congruence good model')
 data=json.loads((ROOT/COUNTS).read_text(encoding='utf-8'));require(data==run_counter() and len(data['rows'])==40 and
  (data['p'],data['lambda'],data['b'],data['i_mod_p'])==(13,2,2,5),'fresh a-line counts')
 small=independent_counts();cases=[]
 for a in REGULAR:
  rows=[r for r in data['rows'] if r['a']==a];result=reconstruct(rows,a)
  require(small[a]==[rows[0]['V'],rows[1]['V'],rows[0]['rho_Frobenius_fixed_V']],'independent a-line counts')
  if prime_poles(a)==0:
   require(result==prior.reconstruct({'p':13,'b':2,'i_mod_p':5,'rows':rows},{'p':13,'b':2,'i_mod_p':5,'beta':[3,2]}),'generic reconstruction consistency')
  cert=cm_certificate(tuple(result['Frobenius_characteristic_coefficients_descending']));roots=[]
  for kind,beta in (('beta',(3,2)),('conjugate_beta',(3,-2))):
   for unit in ((1,0),(-1,0),(0,1),(0,-1)):
    m=prior.line.linear_multiplicity(result['Gaussian_characteristic_coefficients_descending'],zm(beta,unit))
    if m:roots.append({'type':kind,'unit':list(unit),'multiplicity':m})
  require(sum(r['multiplicity'] for r in roots)==cert['geometric_reduction_Ei_multiplicity_in_complement'],'all CM factors accounted exactly')
  cases.append({'a':a,**result,**cert,'CM_Gaussian_linear_roots':roots})
 require([r['a'] for r in cases if r['geometric_reduction_Ei_multiplicity_in_complement']==0]==EXCLUDED,'computed excluded residues')
 six=next(r for r in cases if r['a']==6)
 require(six['CM_Gaussian_linear_roots']==[{'type':'conjugate_beta','unit':[1,0],'multiplicity':1}],'a6 opposite-type reduction factor')
 q=monic_quotient(tuple(reversed(six['Frobenius_characteristic_coefficients_descending'])),(13,-6,1))
 names=source_paths()|{prior.COUNTER,CONTRACT.relative_to(ROOT).as_posix(),NOTE.relative_to(ROOT).as_posix(),Path(__file__).relative_to(ROOT).as_posix()}|{p.relative_to(ROOT).as_posix() for p in INPUTS.values()}
 return {'schema':'marici.hodge-off-reflection-a-line-result.v1','candidate_id':c['candidate_id'],'node':c['node'],
  'excluded_control_node':c['excluded_control_node'],'target_transplant_verdict':'rejected','passed':True,'verdict':'constructed',
  'verification_level':'Complete regular F13 denominator-line census, fresh ordinary/twisted counts, independent counts, full Gaussian reconstruction and complete CM-ratio certificates; no positive Hom lift.',
  'checks':dict.fromkeys(['all13_a_residues_classified','fresh40_ordinary32_twisted_counts','independent_small_counts_for_all8_cases',
   'a_dependent_projective_poles','four_Gaussian_moments_and_unused_fifth_trace','complete_CM_factor_and_residual_certificates',
   'algebraic_congruence_veto_uses_faithful_Hom_specialization','new_actual_a6_theta4_source','scope'],True),
  'regular_a_residues':REGULAR,'failed_model_a_residues':[1,3,4,5,9],'excluded_a_residues':EXCLUDED,'surviving_a_residues':[2,6],
  'finite_field_cases':cases,'off_reflection_control_2_0_2_excluded_even_up_to_Y3_isogeny':True,
  'algebraic_congruence_boxes_excluded':[[2,a,b] for a in EXCLUDED for b in (2,11)],
  'actual_next_control':actual_control(),'a6_finite_field_residual_degree12_coefficients_descending':list(reversed(q)),
  **{k:False for k in POLICY},'source_sha256':{n:sha256((ROOT/n).read_bytes()).hexdigest() for n in sorted(names)}}


if __name__=='__main__':
 r=report();OUT.write_text(json.dumps(r,indent=2)+'\n',encoding='utf-8')
 print(json.dumps({k:v for k,v in r.items() if k not in ('source_sha256','finite_field_cases')},indent=2))
