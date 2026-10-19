"""Complete regular F37 chart: CM types, inert projector and CRT rules."""
from fractions import Fraction as Q
from functools import lru_cache
from pathlib import Path
from hashlib import sha256
import json,subprocess,tempfile
import check_hodge_off_reflection_third_prime as previous
import check_hodge_inert_elliptic_projector as pol
from check_hodge_minimal_axis_frobenius_obstruction import za,zm,zs,zp,zd,bar,ints,require

ROOT=previous.ROOT;joint=previous.joint;arithmetic=previous.arithmetic
CONTRACT=ROOT/'research/conjecture_net/contracts/hodge-scalar-37-census.v1.json'
NOTE=ROOT/'research/voevodsky/hodge-scalar-37-census-v1.md'
OUT=ROOT/'research/voevodsky/results/hodge-scalar-37-census-v1.json'
COUNTER='research/voevodsky/checkers/count_hodge_scalar_37_census.rs'
COUNTS='research/voevodsky/inputs/hodge-scalar-37-census-v1/counts.json'
REGULAR=[0,1,2,4,5,6,7,8,9,10,12,13,14,15,16,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36]
BETA=(-1,-6)
CM_ABSENT=[1,4,5,6,7,9,10,12,14,15,18,19,20,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36]
ARITH={'prime':37,'lambda':2,'b':2,'i_mod_p':6,'beta':[-1,-6],'known_axis_theta_degree':4,'known_axis_split_prime':3,'regular_residues':REGULAR,
 'uncertified_model_residues':[3,11,17],'CM_absent_residues':CM_ABSENT,'opposite_type_absent_residues':[21],
 'inert3_degree_parity_residues':[2,8,13],'necessary_screen_survivors':[0,16],'ordinary_rows':170,'twisted_rows':136,
 'CRT_modulus':8177,'CRT_excluded_count':8077,'CRT_joint_survivors':[3087,6623],
 'CRT_uncertified_count':98,'literal_excluded_control':[2,214,2],'next_actual_control':[2,-1554,2],
 'conditional_surviving_target_axis_v3_degree':1}
POLICY=['positive_finite_factors_lifted_to_complex_axes','finite_CM_multiplicity3_alone_excludes_target',
 'coefficient_denominator_bound_is_actual_degree','nonunit_projector_proves_odd_degree_without_target_hypothesis',
 'primitive_theta6_axis_constructed','joint_axis_kernel_computed','source_End0_or_residual_simplicity_computed',
 'fixed_End_field_and_norm_hypotheses_omitted','target_isogeny_assumed_K_linear',
 'uncertified_model_residues_excluded_without_other_rule','two_CRT_survivors_exhaust_complex_sources',
 'all_algebraic_parameters_excluded','all_transcendental_tuples_excluded','special_Hom_locus_equation_constructed',
 'actual_source_constructions_invalidated','all_scalar_parameters_excluded','fixed_X6_or_Y3_identified',
 'nonzero_target_exceptional_cycle_constructed','Hodge_proved','Hodge_refuted','global_witness_search_completed']


def reconstruct(rows,a):
 require(len(rows)==5 and [r['n'] for r in rows]==[1,2,3,4,5],'census five extension rows')
 s=[]
 for n,r in enumerate(rows,1):
  q=37**n;require(r['a']==a and r['q']==q and tuple(r['modulus'])==previous.MODULI[n-1] and r['full_primitive_generator_cycle_verified'] is True,'census field coverage')
  require(r['Frobenius_x_orbit_counts_by_length']==previous.orbit_counts(n),'census full Frobenius orbits')
  require(r['direct_ordinary_crosscheck'] is (n<5),'census direct ordinary coverage')
  require(r['rational_poles']==(joint.prime_poles(a,37) if n%2 else 4),'census a-dependent poles')
  require(r['W']==r['E'] and r['E']==q+1-2*zp(BETA,n)[0] and (r['V']-q-1)**2<=324*q,'census ordinary moments')
  if n<5:
   require(r['twisted_base']==r['W'] and r['twist_power_crosscheck'] is (n<=2) and (r['rho_Frobenius_fixed_V']-q-1)**2<=324*q,'census twisted bounds and power audits')
   s.append(za((Q(r['W']-r['V'],2),Q(r['rho_Frobenius_fixed_V']-r['W'],2)),zs(zp(BETA,n),-1)))
 acoeff=[(1,0)]
 for n in range(1,5):
  z=(0,0)
  for j in range(1,n+1):z=za(z,zm(acoeff[n-j],s[j-1]))
  acoeff.append(zs(z,Q(-1,n)))
 require(acoeff[3]!=(0,0),'census nonzero a3')
 det=zd(zs(acoeff[4],37**3),bar(acoeff[3]));acoeff += [zs(zm(det,bar(acoeff[2])),Q(1,37**2)),zs(zm(det,bar(acoeff[1])),Q(1,37)),det]
 for j in range(8):require(acoeff[7-j]==zs(zm(acoeff[7],bar(acoeff[j])),Q(1,37**j)),'census Gaussian reciprocity')
 gauss=[ints(z) for z in acoeff]
 c=ints([sum(acoeff[j][0]*acoeff[k-j][0]+acoeff[j][1]*acoeff[k-j][1] for j in range(8) if 0<=k-j<8) for k in range(15)])
 require(c[-1]==37**7 and all(c[14-j]==37**(7-j)*c[j] for j in range(8)),'census rational reciprocity')
 traces=[14]
 for n in range(1,6):traces.append(-sum(c[j]*traces[n-j] for j in range(1,n))-n*c[n])
 for n,r in enumerate(rows,1):require(traces[n]==r['W']+r['E']-r['V']-r['q']-1,'census unused fifth trace')
 return {'Gaussian_power_traces':[ints(z) for z in s],'Gaussian_characteristic_coefficients_descending':gauss,
  'Frobenius_characteristic_coefficients_descending':c,'rational_power_traces_through_degree5':traces[1:],'ordinary_reduction':c[7]%37!=0}


@lru_cache(maxsize=34)
def cm_certificate(c):return arithmetic.cm_certificate(c,BETA)


def monic_gcd(a,b):
 a=pol.trim(a);b=pol.trim(b)
 while b!=(pol.ZERO,):a,b=b,pol.divrem(a,b)[1]
 return pol.scale(a,zd(pol.ONE,a[-1]))


def native_factors(f7,control,orders):
 residual=tuple(zm(z,zp(control,j)) for j,z in enumerate(reversed(f7)));factors=[];degree=0
 for order in orders:
  phi=tuple((v,0) for v in arithmetic.cyclotomic(order))
  while True:
   d=monic_gcd(residual,phi)
   if len(d)==1:break
   residual,r=pol.divrem(residual,d);require(r==(pol.ZERO,),'exact native Gaussian CM division')
   degree+=len(d)-1;factors.append({'order':order,'degree_over_K':len(d)-1,'factor_coefficients_ascending':pol.serial(d)})
 return {'degree':degree,'factors':factors,'residual_coefficients_ascending':pol.serial(residual)}


@lru_cache(maxsize=34)
def projector(f7,gamma):return pol.spectral_certificate(f7,BETA,gamma,37)


def known_axis_split_certificate(degree=4):
 require(isinstance(degree,int) and degree>0,'positive actual axis degree')
 coefficient=Q(1,degree);require(coefficient.denominator%3!=0,'known axis degree must be a3-unit')
 require(coefficient*coefficient*degree==coefficient,'adjoint scalar projector identity')
 return {'actual_axis_theta_degree':degree,'u_dagger_u_scalar':degree,'projector_coefficient':[1,degree],
  'integral_at3':True,'orthogonal_complement_self_dual_at3':True,'uses_actual_axis_not_a_Frobenius_polynomial':True}


@lru_cache(maxsize=34)
def complement_projector(f7,gamma):
 # The actual degree-four first axis gives a3-integral self-adjoint split,
 # so its orthogonal complement, unlike an arbitrary rational factor, is3-self-dual.
 known_axis_split_certificate()
 f=tuple(reversed(f7));r,left=pol.divrem(f,(zs(gamma,-1),pol.ONE));require(left==(pol.ZERO,),'complement CM root')
 d=pol.evaluate(r,gamma);require(d!=pol.ZERO,'simple complement CM root')
 e=pol.scale(r,zd(pol.ONE,d));require(pol.rem(pol.sub(pol.mul(e,e),e),f)==(pol.ZERO,),'complement exact idempotency')
 require(pol.rem(pol.sub(pol.mul((pol.ZERO,pol.ONE),e),pol.scale(e,gamma)),f)==(pol.ZERO,),'complement eigenvalue')
 tinv=pol.scale(f[1:],zd((-1,0),f[0]));require(pol.rem(pol.mul((pol.ZERO,pol.ONE),tinv),f)==(pol.ONE,),'complement Frobenius inverse')
 adj=(pol.ZERO,)
 for c in reversed(e):adj=pol.add(pol.rem(pol.mul(adj,pol.scale(tinv,(37,0))),f),(bar(c),))
 require(pol.rem(pol.sub(adj,e),f)==(pol.ZERO,),'complement Rosati self-adjoint')
 trace=pol.ZERO
 for j in range(7):
  v=pol.rem((pol.ZERO,)*j+e,f);trace=za(trace,v[j] if j<len(v) else pol.ZERO)
 require(trace==pol.ONE,'complement Gaussian rank1')
 norm=ints(zm(d,bar(d)))[0];v=pol.valuation3(norm);require(v%2==0,'complement inert norm valuation')
 require(pol.integral_at3(e)==(v==0),'complement local integrality')
 return {'ambient_Gaussian_rank':7,'first_axis_theta_degree':4,'first_axis_split_integral_at3':True,
  'derivative_at_gamma':ints(d),'derivative_norm':norm,'derivative_norm_valuation3':v,
  'projector_coefficients_ascending':pol.serial(e),'integral_at3':pol.integral_at3(e),
  'exact_idempotent':True,'exact_Rosati_self_adjoint':True,'Gaussian_rank':1}


def annotate(rows,a):
 result=reconstruct(rows,a);cert=cm_certificate(tuple(result['Frobenius_characteristic_coefficients_descending']));m=cert['geometric_reduction_Ei_multiplicity_in_complement']
 f7=tuple(tuple(z) for z in result['Gaussian_characteristic_coefficients_descending']);orders=[r['order'] for r in cert['cyclotomic_factors']]
 if m:
  same=native_factors(f7,BETA,orders);opposite=native_factors(f7,bar(BETA),orders)
 else:same={'degree':0,'factors':[]};opposite={'degree':0,'factors':[]}
 require(same['degree']+opposite['degree']==m,'all CM factors assigned to native types')
 gamma=None;pc=None;comp=None
 if opposite['degree']==1:
  fac=opposite['factors'];require(len(fac)==1 and fac[0]['degree_over_K']==1,'unique opposite native factor')
  pair=fac[0]['factor_coefficients_ascending'][0];constant=tuple(Q(n,d) for n,d in pair)
  gamma=tuple(ints(zm(bar(BETA),zs(constant,-1))));pc=projector(f7,gamma);comp=complement_projector(f7,gamma)
 bound=None;target_values=None
 if comp is not None:
  bound=comp['derivative_norm_valuation3']//2
  e=tuple(tuple(Q(n,d) for n,d in z) for z in comp['projector_coefficients_ascending'])
  require(pol.integral_at3(pol.scale(e,(3**bound,0))),'projector denominator upper bound')
  target_values=[v for v in range(bound+1) if v%2==1]
 if m==0:verdict='CM_absent'
 elif opposite['degree']==0:verdict='opposite_type_absent'
 elif comp is not None and comp['integral_at3']:verdict='inert3_degree_parity'
 else:verdict='necessary_screen_survives'
 return {'a':a,**result,**cert,'same_type_certificate':same,'opposite_type_certificate':opposite,
  'unique_opposite_eigenvalue':list(gamma) if gamma else None,'inert3_projector':pc,'known_axis_complement_projector':comp,
  'conditional_primitive_axis_v3_upper_bound':bound,'conditional_target_axis_v3_values':target_values,'screen_verdict':verdict}


@lru_cache(maxsize=1)
def run_counter():
 with tempfile.TemporaryDirectory(prefix='hodge-census37-') as d:
  exe=Path(d)/'count.exe';subprocess.run(['rustc','-O',str(ROOT/COUNTER),'-o',str(exe)],check=True,capture_output=True,text=True,timeout=120)
  r=subprocess.run([str(exe)],check=True,capture_output=True,text=True,timeout=3600)
 return json.loads(r.stdout)


@lru_cache(maxsize=1)
def independent_counts():
 out={a:[] for a in REGULAR}
 for poly in previous.MODULI[:2]:
  f=arithmetic.Field(37,poly);points=[(x,y) for x in range(f.q) for y in range(f.q) if f.mul(y,y)==f.wp(x)]
  for a in REGULAR:
   v=len(f.roots(6))
   for x,y in points:
    g=previous.base.ga(f,x,y,a);v+=1 if g is None else len(f.roots(f.sub(f.mul(f.mul(g,g),g),g)))
   out[a].append(v)
 f=arithmetic.Field(37,previous.MODULI[3]);points=[]
 for x in range(1,f.q):
  if f.pow(x,37)!=f.mul(2,f.inv(x)):continue
  for y in f.roots(f.wp(x)):
   if f.pow(y,37)==f.neg(f.mul(2,f.mul(y,f.inv(f.mul(x,x))))):points.append((x,y))
 require(len(points)==40,'independent full census torsor base')
 for a in REGULAR:
  fixed=0
  for x,y in points:
   g=previous.base.ga(f,x,y,a)
   if g is None:fixed+=1;continue
   fixed+=sum(f.mul(6,f.pow(w,37))==w for w in f.roots(f.sub(f.mul(f.mul(g,g),g),g)))
  out[a].append(fixed)
 return out


def crt_partition(old,cases):
 by={r['a']:r for r in cases};excluded=[];survivors=[];unknown=[];labels=[]
 for a in range(8177):
  r=by.get(a%37);old_bad=a%221 in old['excluded'];new_bad=r is not None and r['screen_verdict']!='necessary_screen_survives'
  if old_bad or new_bad:excluded.append(a);labels.append(0)
  elif a%221 in old['joint_survivors'] and r is not None:survivors.append(a);labels.append(1)
  else:unknown.append(a);labels.append(2)
 require(len(excluded)+len(survivors)+len(unknown)==8177,'complete census CRT partition')
 return {'modulus':8177,'excluded_count':len(excluded),'joint_survivors':survivors,'uncertified_count':len(unknown),
  'uncertified_residues':unknown,'classification_sha256':sha256(bytes(labels)).hexdigest(),
  'reconstruction_rule':'exclude_if_old_mod221_excluded_or_certified37_veto;survive_only_if_both_certified;otherwise_uncertified'}


def next_control():
 a=-1554;d,fs=previous.base.branch_polynomials(a);s=joint.src
 require(a not in (2,4) and s.gcd(d,s.derivative(d))=={0:Q(1)} and s.gcd(d,s.P)=={0:Q(1)} and
  s.gcd(d,fs[0])=={0:Q(1)} and all(max(f)==4 and s.gcd(f,s.derivative(f))=={0:Q(1)} for f in fs),'actual next source branch certificate')
 require([a%p for p in (13,17,37)]==[6,10,0] and all(joint.good_model(a,p) for p in (13,17,37)),'next source all three good charts')
 return {'parameters_lambda_a_b':[2,a,2],'tower_genera':[17,9,5],'primitive_elliptic_theta_degree':4,
  'known_reflection_loci_escaped':True,'good_prime_residues':[6,10,0],'necessary_CM_type_screened_primes':[13,17,37],
  'opposite_complex_axis_not_constructed':True,'special_fibre_polynomials_ascending':[list(joint.vec(f)) for f in fs]}


def source_paths():return {COUNTER,COUNTS}

def validate_contract(c):
 require(c['schema']=='marici.hodge-scalar-37-census.v1' and c['candidate_id']=='marici.hodge.nonsplit-sixfold.exp-sqrt-primes.v1' and
  c['node']=='scalar-37-full-screen' and c['excluded_control_node']=='scalar-37-typed-polarized-target-transplant','census identity')
 require(c['arithmetic']==ARITH,'census arithmetic changed')
 require(set(c['scope_policy'])==set(POLICY) and all(v is False for v in c['scope_policy'].values()),'census scope promotion')


def report():
 c=json.loads(CONTRACT.read_text(encoding='utf-8'));validate_contract(c)
 old=previous.report();require(old==json.loads(previous.OUT.read_text(encoding='utf-8')),'stale third-prime/generic predecessor')
 require([a for a in range(37) if joint.good_model(a,37)]==REGULAR,'complete regular F37 branch chart')
 data=json.loads((ROOT/COUNTS).read_text(encoding='utf-8'));require(data==run_counter() and len(data['rows'])==170 and
  (data['p'],data['lambda'],data['b'],data['i_mod_p'])==(37,2,2,6),'fresh complete census counts')
 small=independent_counts();cases=[]
 for a in REGULAR:
  rows=[r for r in data['rows'] if r['a']==a];result=annotate(rows,a)
  require(small[a]==[rows[0]['V'],rows[1]['V'],rows[0]['rho_Frobenius_fixed_V']],'independent every-case counts')
  cases.append(result)
 # The earlier slow twisted method and original character counts agree in the overlapping control.
 prior_data=json.loads((ROOT/previous.COUNTS).read_text(encoding='utf-8'))
 for row,oldrow in zip([r for r in data['rows'] if r['a']==30],prior_data['rows']):
  for key in ('W','V','E','rational_poles','Frobenius_x_orbit_counts_by_length','rho_Frobenius_fixed_V'):
   if key in oldrow:require(row[key]==oldrow[key],'old prime37 control recovered')
 verdicts={v:[r['a'] for r in cases if r['screen_verdict']==v] for v in ('CM_absent','opposite_type_absent','inert3_degree_parity','necessary_screen_survives')}
 require(verdicts=={'CM_absent':CM_ABSENT,'opposite_type_absent':[21],'inert3_degree_parity':[2,8,13],'necessary_screen_survives':[0,16]},'computed census verdicts')
 require(all(joint.good_model(a,37,35) for a in REGULAR),'negative-b chart conditions')
 require(all(r['conditional_target_axis_v3_values']==[1] for r in cases if r['screen_verdict']=='necessary_screen_survives'),'conditional exact surviving target degree valuation')
 pol.norm_parity_certificate();joint.signature_certificate(joint.SIGNATURE);axis_split=known_axis_split_certificate(ARITH['known_axis_theta_degree'])
 old221=json.loads(pol.OUT.read_text(encoding='utf-8'))['CRT_partition'];crt=crt_partition(old221,cases)
 require(crt['excluded_count']==8077 and crt['joint_survivors']==[3087,6623] and crt['uncertified_count']==98,'computed final census CRT counts')
 centered=[a if a<=4088 else a-8177 for a in crt['joint_survivors']]
 require(min(centered,key=lambda a:(abs(a),a))==-1554,'least absolute jointly certified lift')
 paths=source_paths()|{arithmetic.COUNTER,CONTRACT.relative_to(ROOT).as_posix(),NOTE.relative_to(ROOT).as_posix(),
  Path(__file__).relative_to(ROOT).as_posix(),previous.OUT.relative_to(ROOT).as_posix()}
 return {'schema':'marici.hodge-scalar-37-census-result.v1','candidate_id':c['candidate_id'],'node':c['node'],
  'excluded_control_node':c['excluded_control_node'],'target_transplant_verdict':'rejected','verdict':'constructed','passed':True,
  'verification_level':'Full regular F37 chart with170 ordinary/136 twisted rows, fresh fifth traces, exact native Gaussian CM factors and inherited End/norm polarization tests; no positive lift.',
  'checks':dict.fromkeys(['all37_residues_chart_partitioned','fresh_all_case_counts_and_fifth_traces',
   'orbit_character_factorization_and_direct_controls','pure_imaginary_twist_character_identity_and_power_audits',
   'independent_all34_small_and_direct_twisted_counts','all_Gaussian_polynomials_reciprocal_and_integral',
   'complete_CM_certificates_and_native_factor_divisions','opposite_type_and_inert3_veto_hypotheses',
   'conditional_surviving_axis_v3_bounds','overlap_with_previous_slow37_counter','CRT_unknown_classes_retained','actual_next_source','scope'],True),
  'known_axis_split_certificate':axis_split,'finite_field_cases':cases,'verdicts_by_a_residue':verdicts,'uncertified_model_residues':[3,11,17],'CRT_partition':crt,
  'literal_2_214_2_excluded_even_up_to_Y3_isogeny':True,
  'algebraic_congruence_boxes_excluded_mod37':[[2,a,b] for a in REGULAR if a not in (0,16) for b in (2,35)],
  'next_actual_control':next_control(),**{k:False for k in POLICY},
  'source_sha256':{n:sha256((ROOT/n).read_bytes()).hexdigest() for n in sorted(paths)}}


if __name__=='__main__':
 r=report();OUT.write_text(json.dumps(r,indent=2)+'\n',encoding='utf-8')
 print(json.dumps({k:v for k,v in r.items() if k not in ('source_sha256','finite_field_cases')},indent=2))
