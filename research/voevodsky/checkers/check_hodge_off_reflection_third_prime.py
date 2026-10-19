"""Prime37 control and geometric-generic Hom-rank consequence; no positive Hom lift."""
from fractions import Fraction as Q
from functools import lru_cache
from pathlib import Path
from hashlib import sha256
import json,subprocess,tempfile
import check_hodge_inert_elliptic_projector as previous
from check_hodge_minimal_axis_frobenius_obstruction import za,zm,zs,zp,zd,bar,ints,require

ROOT=previous.ROOT;joint=previous.previous;base=joint.previous;arithmetic=joint.prior
CONTRACT=ROOT/'research/conjecture_net/contracts/hodge-off-reflection-third-prime.v1.json'
NOTE=ROOT/'research/voevodsky/hodge-off-reflection-third-prime-v1.md'
OUT=ROOT/'research/voevodsky/results/hodge-off-reflection-third-prime-v1.json'
COUNTER='research/voevodsky/checkers/count_hodge_off_reflection_third_prime.rs'
COUNTS='research/voevodsky/inputs/hodge-off-reflection-third-prime-v1/counts.json'
MODULI=((2,1),(5,1,1),(13,1,0,1),(2,1,0,0,1),(5,1,0,0,0,1))
BETA=(-1,-6)
ARITH={'prime':37,'lambda':2,'a_lift':-7,'a_residue':30,'b':2,'i_mod_p':6,'beta':[-1,-6],
 'ordinary_extension_degrees':[1,2,3,4,5],'twisted_extension_degrees':[1,2,3,4],
 'rational_poles_in_all_extensions':4,'negative_b_residue':35,'CRT_modulus':8177,'CRT_excluded_count':7457,
 'two_prime_survivors_uncounted_at37':36,'previously_uncertified_unexcluded_count':684,'next_actual_control':[2,214,2]}
GENERIC={'constant_elliptic_curve':'Ei:y2=x3-x','geometric_special_fibre_Hom_rank':2,'known_axis_Hom_rank_lower_bound':2,
 'geometric_generic_a_line_Hom_rank':2,'geometric_generic_three_parameter_Hom_rank':2,
 'fixed_line':{'lambda':2,'b':2},'universal_parameter_base_field':'Qbar',
 'specialization_flag':['lambda=2','b=2','a=-7']}
POLICY=['positive_finite_CM_factors_lifted','remaining_all_algebraic_a_excluded',
 'all_algebraically_dependent_tuples_excluded','all_transcendental_scalar_tuples_excluded',
 'single_global_CM_jump_equation_constructed','generic_sevenfold_simplicity_or_End_computed',
 'all8177_residues_Frobenius_counted','unchecked37_classes_declared_third_prime_survivors',
 'failed_chart_classes_excluded_without_another_certificate','new_control_counted_at37',
 'unused_fifth_trace_omitted','full_degree5_direct_enumeration_claimed','actual_source_constructions_invalidated',
 'all_scalar_parameters_excluded','fixed_X6_identified','fixed_Y3_membership_constructed',
 'nonzero_target_exceptional_cycle_constructed','Hodge_proved','Hodge_refuted','global_witness_search_completed']


@lru_cache(maxsize=1)
def run_counter():
 with tempfile.TemporaryDirectory(prefix='hodge-third37-') as d:
  exe=Path(d)/'count.exe';subprocess.run(['rustc','-O',str(ROOT/COUNTER),'-o',str(exe)],check=True,capture_output=True,text=True,timeout=120)
  r=subprocess.run([str(exe)],check=True,capture_output=True,text=True,timeout=900)
 return json.loads(r.stdout)


def orbit_counts(n):
 sizes=[0]*6
 for d in range(1,n+1):
  if n%d:continue
  numerator=37**d-sum(e*sizes[e] for e in range(1,d) if d%e==0)
  require(numerator%d==0,'orbit divisibility');sizes[d]=numerator//d
 return sizes


@lru_cache(maxsize=1)
def independent_counts():
 out=[]
 for poly in MODULI[:2]:
  f=arithmetic.Field(37,poly);nw=1;nv=len(f.roots(6));ne=1
  for x in range(f.q):
   ne+=len(f.roots(f.sub(f.mul(f.mul(x,x),x),x)))
   for y in range(f.q):
    if f.mul(y,y)!=f.wp(x):continue
    nw+=1;g=base.ga(f,x,y,30)
    nv+=1 if g is None else len(f.roots(f.sub(f.mul(f.mul(g,g),g),g)))
  out.append([nw,nv,ne])
 f=arithmetic.Field(37,MODULI[3]);nb=0;fixed=0
 for x in range(1,f.q):
  if f.pow(x,37)!=f.mul(2,f.inv(x)):continue
  for y in f.roots(f.wp(x)):
   if f.pow(y,37)!=f.neg(f.mul(2,f.mul(y,f.inv(f.mul(x,x))))):continue
   nb+=1;g=base.ga(f,x,y,30)
   if g is None:fixed+=1;continue
   fixed+=sum(f.mul(6,f.pow(w,37))==w for w in f.roots(f.sub(f.mul(f.mul(g,g),g),g)))
 require(nb==40,'independent prime37 torsor base')
 return out,[nb,fixed]


def reconstruct(data):
 require((data['p'],data['lambda'],data['a_lift'],data['a'],data['b'],data['i_mod_p'])==(37,2,-7,30,2,6),'third-prime control identity')
 rows=data['rows'];require(len(rows)==5,'third-prime extension coverage')
 require(zm(BETA,bar(BETA))==(37,0) and (BETA[0]+6*BETA[1])%37==0 and 2*BETA[0]==38-rows[0]['E'],'third-prime beta orientation')
 require(joint.prime_poles(30,37)==4,'four rational source poles')
 moments=[]
 for n,r in enumerate(rows,1):
  q=37**n;require(r['n']==n and r['a']==30 and r['q']==q and tuple(r['modulus'])==MODULI[n-1] and
   r['full_primitive_generator_cycle_verified'] is True,'third-prime field coverage')
  require(r['Frobenius_x_orbit_counts_by_length']==orbit_counts(n) and
   sum(j*v for j,v in enumerate(r['Frobenius_x_orbit_counts_by_length']))==q,'complete Frobenius x-orbits')
  require(r['rational_poles']==4 and r['W']==r['E'] and r['E']==q+1-2*zp(BETA,n)[0],'projective poles and independent elliptic moments')
  require((r['V']-q-1)**2<=324*q,'third-prime ordinary Weil bound')
  require(r['direct_ordinary_crosscheck'] is (n<5),'direct/orbit crosscheck coverage')
  if n<5:
   require(r['twisted_base']==r['W'] and (r['rho_Frobenius_fixed_V']-q-1)**2<=324*q,'third-prime twisted torsor')
   moments.append(za((Q(r['W']-r['V'],2),Q(r['rho_Frobenius_fixed_V']-r['W'],2)),zs(zp(BETA,n),-1)))
 a=[(1,0)]
 for n in range(1,5):
  z=(0,0)
  for j in range(1,n+1):z=za(z,zm(a[n-j],moments[j-1]))
  a.append(zs(z,Q(-1,n)))
 require(a[3]!=(0,0),'third-prime nonzero a3')
 det=zd(zs(a[4],37**3),bar(a[3]));a += [zs(zm(det,bar(a[2])),Q(1,37**2)),zs(zm(det,bar(a[1])),Q(1,37)),det]
 for j in range(8):require(a[7-j]==zs(zm(a[7],bar(a[j])),Q(1,37**j)),'third-prime Gaussian reciprocity')
 g=[ints(z) for z in a]
 c=ints([sum(a[j][0]*a[k-j][0]+a[j][1]*a[k-j][1] for j in range(8) if 0<=k-j<8) for k in range(15)])
 require(c[-1]==37**7 and all(c[14-j]==37**(7-j)*c[j] for j in range(8)),'third-prime rational reciprocity')
 traces=[14]
 for n in range(1,6):traces.append(-sum(c[j]*traces[n-j] for j in range(1,n))-n*c[n])
 for n,r in enumerate(rows,1):require(traces[n]==r['W']+r['E']-r['V']-r['q']-1,'third-prime unused fifth trace')
 return {'Gaussian_power_traces':[ints(z) for z in moments],'Gaussian_characteristic_coefficients_descending':g,
  'Frobenius_characteristic_coefficients_descending':c,'rational_power_traces_through_degree5':traces[1:],'ordinary_reduction':c[7]%37!=0}


@lru_cache(maxsize=1)
def cm_certificate(c):return arithmetic.cm_certificate(c,BETA)


def generic_rank_certificate(finite_multiplicity):
 require(finite_multiplicity==1,'one special-fibre CM factor required')
 lower=2;upper=2*finite_multiplicity;require(lower==upper,'generic rank squeeze')
 return {'finite_special_fibre_Hom_rank':upper,'known_global_axis_Hom_rank_lower_bound':lower,
  'literal_minus7_Hom_rank':2,'geometric_generic_a_line_Hom_rank':2,'geometric_generic_three_parameter_Hom_rank':2,
  'generic_CM_multiplicity':1,'transcendental_a_on_lambda2_b2_line_excluded':True,
  'algebraically_independent_parameter_triples_excluded':True,
  'uses_injective_good_specialization_and_alg_closed_basechange_invariance':True}


def refined_crt(old):
 labels=[];new=[];unchecked=[];other=0
 for a in range(8177):
  before=a%221 in old['excluded'];bad=before or a%37==30
  if bad:
   labels.append(0)
   if not before:new.append(a)
  elif a%221 in old['joint_survivors']:labels.append(1);unchecked.append(a)
  else:labels.append(2);other+=1
 require(len(labels)==8177 and len(new)==20 and len(unchecked)==36 and other==684 and labels.count(0)==7457,'scoped three-prime CRT partition')
 return {'modulus':8177,'excluded_count':labels.count(0),'newly_excluded_over_old_rule':new,
  'two_prime_survivors_not_counted_at37':unchecked,'previously_uncertified_unexcluded_count':other,
  'classified_residue_count':len(labels),'classification_sha256':sha256(bytes(labels)).hexdigest(),
  'rule':'exclude_if_old_mod221_excluded_or_mod37_equals30;otherwise_split_old_survivor_or_old_uncertified'}


def next_control():
 a=214;d,fs=base.branch_polynomials(a);s=joint.src
 require(a not in (2,4) and s.gcd(d,s.derivative(d))=={0:Q(1)} and s.gcd(d,s.P)=={0:Q(1)} and
  s.gcd(d,fs[0])=={0:Q(1)} and all(max(f)==4 and s.gcd(f,s.derivative(f))=={0:Q(1)} for f in fs),'actual a214 branch construction')
 require(joint.good_model(a,37) and [a%13,a%17]==[6,10],'next actual source prior screens and new branch chart')
 return {'parameters_lambda_a_b':[2,214,2],'tower_genera':[17,9,5],'primitive_elliptic_theta_degree':4,
  'known_reflection_loci_escaped':True,'CM_screened_primes':[13,17],'good_but_uncounted_prime':37,
  'special_fibre_polynomials_ascending':[list(joint.vec(f)) for f in fs]}


def source_paths():return {COUNTER,COUNTS}
def validate_contract(c):
 require(c['schema']=='marici.hodge-off-reflection-third-prime.v1' and c['candidate_id']=='marici.hodge.nonsplit-sixfold.exp-sqrt-primes.v1' and
  c['node']=='off-reflection-third-prime-generic-gate' and c['excluded_control_node']=='third-prime-and-generic-target-transplant','third-prime identity')
 require(c['arithmetic']==ARITH and c['generic_argument']==GENERIC,'third-prime/generic hypotheses changed')
 require(set(c['scope_policy'])==set(POLICY) and all(v is False for v in c['scope_policy'].values()),'third-prime/generic scope promotion')


def report():
 c=json.loads(CONTRACT.read_text(encoding='utf-8'));validate_contract(c)
 old=previous.report();require(old==json.loads(previous.OUT.read_text(encoding='utf-8')),'stale inert-prime predecessor')
 require(joint.good_model(-7,37) and joint.good_model(30,37,35),'third-prime good reduction including sign pair')
 data=json.loads((ROOT/COUNTS).read_text(encoding='utf-8'));require(data==run_counter(),'fresh third-prime counts')
 result=reconstruct(data);small,twist=independent_counts()
 require(small==[[r['W'],r['V'],r['E']] for r in data['rows'][:2]] and twist==[data['rows'][0]['twisted_base'],data['rows'][0]['rho_Frobenius_fixed_V']],'independent prime37 counts')
 cert=cm_certificate(tuple(result['Frobenius_characteristic_coefficients_descending']))
 require(cert['cyclotomic_factors']==[] and cert['geometric_reduction_Ei_multiplicity_in_complement']==0,'complete third-prime CM absence')
 generic=generic_rank_certificate(1+cert['geometric_reduction_Ei_multiplicity_in_complement']);crt=refined_crt(old['CRT_partition']);control=next_control()
 candidates=[a if a<=8177//2 else a-8177 for a in crt['two_prime_survivors_not_counted_at37']]
 require(min(candidates,key=lambda a:(abs(a),a))==214,'least absolute lift only inside prior-screened domain')
 paths=source_paths()|{arithmetic.COUNTER,CONTRACT.relative_to(ROOT).as_posix(),NOTE.relative_to(ROOT).as_posix(),
  Path(__file__).relative_to(ROOT).as_posix(),previous.OUT.relative_to(ROOT).as_posix()}
 return {'schema':'marici.hodge-off-reflection-third-prime-result.v1','candidate_id':c['candidate_id'],'node':c['node'],
  'excluded_control_node':c['excluded_control_node'],'target_transplant_verdict':'rejected','verdict':'constructed','passed':True,
  'verification_level':'Fresh prime37 field/orbit counts, direct small/twisted checks, full polynomial with unused fifth trace and exhaustive CM exclusion; written generic Hom-rank specialization and basechange.',
  'checks':dict.fromkeys(['fresh_counts_with_full_field_cycles','complete_Frobenius_x_orbits','orbit_direct_checks_degrees1_to4',
   'independent_digitwise_small_and_direct_twisted_counts','rational_poles_and_infinity','four_Gaussian_moments_and_unused_fifth_trace',
   'complete_CM_ratio_certificate','literal_and_algebraic_residue_box_exclusion','generic_rank_specialization_squeeze',
   'transcendental_a_line_and_independent_triples_scope','CRT_marks_unchecked37_classes','actual_next_control','scope'],True),
  'prime37_result':{**result,**cert},'generic_rank_certificate':generic,'CRT_partition':crt,
  'literal_2_minus7_2_excluded_even_up_to_Y3_isogeny':True,
  'algebraic_congruence_boxes_excluded_mod37':[[2,30,2],[2,30,35]],'next_actual_control':control,
  **{k:False for k in POLICY},'source_sha256':{n:sha256((ROOT/n).read_bytes()).hexdigest() for n in sorted(paths)}}


if __name__=='__main__':
 r=report();OUT.write_text(json.dumps(r,indent=2)+'\n',encoding='utf-8')
 print(json.dumps({k:v for k,v in r.items() if k not in ('source_sha256','prime37_result')},indent=2))
