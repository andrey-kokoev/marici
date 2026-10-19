"""Two-prime scalar screen, transverse Weierstrass chart, native-type veto."""
from fractions import Fraction as Q
from functools import lru_cache
from pathlib import Path
from hashlib import sha256
import json,subprocess,tempfile
import check_hodge_off_reflection_a_line as previous
import check_hodge_indecomposable_principal_model as endmodel
import check_hodge_minimal_axis_frobenius_obstruction as first17
from check_hodge_minimal_axis_frobenius_obstruction import za,zm,zs,zp,bar,zd,ints,require

ROOT=previous.ROOT;prior=previous.prior;src=previous.reflection.src;gcdmod=previous.modgcd_degree;vec=prior.line.vec
CONTRACT=ROOT/'research/conjecture_net/contracts/hodge-off-reflection-joint-screen.v1.json'
NOTE=ROOT/'research/voevodsky/hodge-off-reflection-joint-screen-v1.md'
OUT=ROOT/'research/voevodsky/results/hodge-off-reflection-joint-screen-v1.json'
COUNTER='research/voevodsky/checkers/count_hodge_off_reflection_joint_screen.rs'
COUNTS='research/voevodsky/inputs/hodge-off-reflection-joint-screen-v1/counts.json'
REG={13:[0,2,5,6,7,8,10,11,12],17:[0,1,2,4,6,7,8,9,10,11,13,14,15,16]}
BETA={13:(3,2),17:(1,4)};IMOD={13:5,17:4}
MODULI={13:((2,1),(2,1,1),(6,1,0,1),(2,1,1,0,1),(2,4,0,0,0,1)),
 17:((3,1),(3,1,1),(3,1,0,1),(11,1,0,0,1),(3,1,0,0,0,1))}
ARITH={'lambda':2,'b':2,'primes':[13,17],'beta':[[3,2],[1,4]],'i_mod_p':[5,4],
 'regular_a_mod13':REG[13],'regular_a_mod17':REG[17],'new_Weierstrass_chart_cases':[[13,5],[17,1]],
 'raw_CM_absence_a_mod13':[0,5,7,8,10,11,12],'raw_CM_absence_a_mod17':[0,1,2,4,6,8,9,11,13,14,15,16],
 'same_type_only_a_mod17':[7],'opposite_type_survivors_a_mod13':[2,6],'opposite_type_survivors_a_mod17':[10],
 'CRT_modulus':221,'CM_only_joint_survivors':[41,58,197,214],'typed_joint_survivors':[197,214],
 'CRT_excluded_count':197,'CRT_uncertified_count':22,'new_actual_control':[2,-7,2]}
SIGNATURE={'source_native_K_signature':[4,4],'fixed_X6_signature':[3,3],'fixed_X6_End0':'Q(i)',
 'target_unpolarized_isogeny_type':'X6_times_Ei_squared','forced_elliptic_isotypic_signature':[1,1]}
POLICY=['isogeny_assumed_K_linear_for_unpolarized_veto','same_type_positive_factor_mistaken_for_absent_CM',
 'positive_reduction_factor_lifted_to_complex_axis','primitive_theta6_axis_constructed','joint_elliptic_kernel_computed',
 'residual_sixfold_identified_with_fixed_X6','new_source_End0_computed','uncertified_chart_failure_alone_implies_exclusion',
 'two_CRT_survivors_exhaust_all_complex_sources','least_absolute_two_good_prime_lift_is_global_minimum',
 'native_type_veto_omits_target_End_field_hypothesis','source_constructions_invalidated',
 'arbitrary_transcendental_parameters_excluded','all_scalar_parameters_excluded','fixed_Y3_membership_constructed',
 'nonzero_target_exceptional_cycle_constructed','Hodge_proved','Hodge_refuted','global_witness_search_completed']


def good_model(a,p,b=2):
 d,fs=previous.branch_polynomials(a,b)
 return (b%p not in (0,1,p-1) and gcdmod(vec(d),vec(src.derivative(d)),p)==0 and
  gcdmod(vec(d),vec(src.P),p)==0 and gcdmod(vec(d),vec(fs[0]),p)==0 and
  all(f[4]%p and gcdmod(vec(f),vec(src.derivative(f)),p)==0 for f in fs))


def weierstrass_chart_certificate():
 out=[]
 for p,a in ((13,5),(17,1)):
  d,fs=previous.branch_polynomials(a);n={2:Q(2),0:Q(-4)};ev=lambda f,x:sum(int(v)*pow(x,k,p) for k,v in f.items())%p
  require(good_model(a,p) and any(gcdmod(vec(f),vec(src.P),p)>0 for f in fs),'genuine new Weierstrass chart')
  for c,f in zip((0,1,-1),fs):
   for x in (0,1,2):
    if (c*ev(d,x)-ev(n,x))%p:continue
    dd=ev(d,x);pp=ev(src.derivative(src.P),x)
    require(dd and pp and ev(src.derivative(f),x)==pp,'transverse special fibre at Weierstrass point')
    out.append({'p':p,'a':a,'special_value':c,'x':x,'D_unit':dd,'P_derivative_unit':pp,'local_dg_dy':pow(dd,-1,p),'branch_multiplicity':1})
 require(len(out)==4,'all new Weierstrass intersections')
 return out


def signature_certificate(s):
 require(s==SIGNATURE,'native-type veto requires fixed End field and signatures')
 allowed=[]
 for r in range(3):
  if [3+r,3+2-r]==s['source_native_K_signature']:allowed.append([r,2-r])
 require(allowed==[[1,1]],'forced balanced elliptic isotypic signature')
 return {'target_End_block_algebra':'Q(i) x M_2(Q(i))','X6_signature_for_either_K_embedding':[[3,3],[3,3]],
  'allowed_Ei_squared_native_signatures':allowed,'unpolarized_isogeny_need_not_be_K_linear':True}


@lru_cache(maxsize=1)
def run_counter():
 with tempfile.TemporaryDirectory(prefix='hodge-joint-screen-') as d:
  exe=Path(d)/'count.exe';subprocess.run(['rustc','-O',str(ROOT/COUNTER),'-o',str(exe)],check=True,capture_output=True,text=True,timeout=120)
  r=subprocess.run([str(exe)],check=True,capture_output=True,text=True,timeout=300)
 return json.loads(r.stdout)


@lru_cache(maxsize=2)
def independent_counts(p):
 ases=[5] if p==13 else REG[17];out={a:[] for a in ases}
 for poly in MODULI[p][:2]:
  f=prior.Field(p,poly);points=[(x,y) for x in range(f.q) for y in range(f.q) if f.mul(y,y)==f.wp(x)]
  for a in ases:
   v=len(f.roots(6))
   for x,y in points:
    g=previous.ga(f,x,y,a);v+=1 if g is None else len(f.roots(f.sub(f.mul(f.mul(g,g),g),g)))
   out[a].append(v)
 f=prior.Field(p,MODULI[p][3]);points=[]
 for x in range(1,f.q):
  if f.pow(x,p)!=f.mul(2,f.inv(x)):continue
  for y in f.roots(f.wp(x)):
   if f.pow(y,p)==f.neg(f.mul(2,f.mul(y,f.inv(f.mul(x,x))))):points.append((x,y))
 require(len(points)==p+1-2*BETA[p][0],'independent joint-screen torsor base')
 for a in ases:
  fixed=0
  for x,y in points:
   g=previous.ga(f,x,y,a)
   if g is None:fixed+=1;continue
   fixed+=sum(f.mul(IMOD[p],f.pow(w,p))==w for w in f.roots(f.sub(f.mul(f.mul(g,g),g),g)))
  out[a].append(fixed)
 return out


def prime_poles(a,p):return 4 if pow((a*a-8)%p,(p-1)//2,p)==1 and pow((a-3)%p,(p-1)//2,p)==1 else 0


def reconstruct(rows,a,p):
 require(len(rows)==5 and [r['n'] for r in rows]==[1,2,3,4,5],'joint-screen extension coverage')
 beta=BETA[p];require(zm(beta,bar(beta))==(p,0) and (beta[0]+IMOD[p]*beta[1])%p==0 and
  2*beta[0]==p+1-rows[0]['E'],'joint-screen beta orientation')
 s=[]
 for n,r in enumerate(rows,1):
  q=p**n;require(r['a']==a and r['q']==q and tuple(r['modulus'])==MODULI[p][n-1] and r['full_primitive_generator_cycle_verified'] is True,'joint-screen certified field')
  require(r['rational_poles']==(prime_poles(a,p) if n%2 else 4),'joint-screen projective poles')
  require(r['W']==r['E'] and (r['W']-q-1)**2<=4*q and (r['V']-q-1)**2<=324*q,'joint-screen untwisted Weil bounds')
  if n<=4:
   require(r['twisted_base']==r['W'] and (r['rho_Frobenius_fixed_V']-q-1)**2<=324*q,'joint-screen twisted torsor and bounds')
   s.append(za((Q(r['W']-r['V'],2),Q(r['rho_Frobenius_fixed_V']-r['W'],2)),zs(zp(beta,n),-1)))
 coeff=[(1,0)]
 for n in range(1,5):
  z=(0,0)
  for j in range(1,n+1):z=za(z,zm(coeff[n-j],s[j-1]))
  coeff.append(zs(z,Q(-1,n)))
 require(coeff[3]!=(0,0),'joint-screen nonzero a3')
 det=zd(zs(coeff[4],p**3),bar(coeff[3]));coeff += [zs(zm(det,bar(coeff[2])),Q(1,p**2)),zs(zm(det,bar(coeff[1])),Q(1,p)),det]
 for j in range(8):require(coeff[7-j]==zs(zm(coeff[7],bar(coeff[j])),Q(1,p**j)),'joint-screen Gaussian reciprocity')
 gaussian=[ints(z) for z in coeff]
 c=ints([sum(coeff[j][0]*coeff[k-j][0]+coeff[j][1]*coeff[k-j][1] for j in range(8) if 0<=k-j<8) for k in range(15)])
 require(c[-1]==p**7 and all(c[14-j]==p**(7-j)*c[j] for j in range(8)),'joint-screen rational reciprocity')
 moments=[14]
 for n in range(1,6):moments.append(-sum(c[j]*moments[n-j] for j in range(1,n))-n*c[n])
 for n,r in enumerate(rows,1):require(moments[n]==r['W']+r['E']-r['V']-r['q']-1,'joint-screen unused fifth trace')
 return {'Gaussian_power_traces':[ints(z) for z in s],'Gaussian_characteristic_coefficients_descending':gaussian,
  'Frobenius_characteristic_coefficients_descending':c,'rational_power_traces_through_degree5':moments[1:],'ordinary_reduction':c[7]%p!=0}


@lru_cache(maxsize=23)
def cm_certificate(c,p):return prior.cm_certificate(c,BETA[p])


def annotated_case(rows,a,p):
 result=reconstruct(rows,a,p);cert=cm_certificate(tuple(result['Frobenius_characteristic_coefficients_descending']),p);roots=[]
 require(zd(BETA[p],bar(BETA[p])) not in ((1,0),(-1,0),(0,1),(0,-1)),'CM types disjoint even after finite extension')
 for kind,beta in (('beta',BETA[p]),('conjugate_beta',bar(BETA[p]))):
  for unit in ((1,0),(-1,0),(0,1),(0,-1)):
   m=prior.line.linear_multiplicity(result['Gaussian_characteristic_coefficients_descending'],zm(beta,unit))
   if m:roots.append({'type':kind,'unit':list(unit),'multiplicity':m})
 require(sum(r['multiplicity'] for r in roots)==cert['geometric_reduction_Ei_multiplicity_in_complement'],'complete native-type CM accounting')
 return {'p':p,'a':a,**result,**cert,'CM_Gaussian_linear_roots':roots,
  'opposite_type_reduction_multiplicity':sum(r['multiplicity'] for r in roots if r['type']=='conjugate_beta')}


def crt_partition(cases):
 by={(r['p'],r['a']):r for r in cases};out={'modulus':221,'CM_only_joint_survivors':[],
  'typed_joint_survivors':[],'raw_CM_excluded':[],'typed_excluded':[],'uncertified':[]}
 for a in range(221):
  rs=[by.get((p,a%p)) for p in (13,17)]
  cm_bad=any(r is not None and r['geometric_reduction_Ei_multiplicity_in_complement']==0 for r in rs)
  typed_bad=any(r is not None and r['opposite_type_reduction_multiplicity']==0 for r in rs)
  if cm_bad:out['raw_CM_excluded'].append(a)
  if not cm_bad and all(r is not None for r in rs):out['CM_only_joint_survivors'].append(a)
  if typed_bad:out['typed_excluded'].append(a)
  elif all(r is not None for r in rs):out['typed_joint_survivors'].append(a)
  else:out['uncertified'].append(a)
 require(len(out['typed_excluded'])+len(out['typed_joint_survivors'])+len(out['uncertified'])==221,'complete disjoint CRT classification')
 return out


def actual_control():
 a=-7;d,fs=previous.branch_polynomials(a)
 require(a not in (2,4) and src.gcd(d,src.derivative(d))=={0:Q(1)} and src.gcd(d,src.P)=={0:Q(1)} and
  src.gcd(d,fs[0])=={0:Q(1)} and all(max(f)==4 and src.gcd(f,src.derivative(f))=={0:Q(1)} for f in fs),'new actual a=-7 source')
 return {'parameters_lambda_a_b':[2,-7,2],'tower_genera':[17,9,5],'primitive_elliptic_theta_degree':4,
  'known_reflection_loci_escaped':True,'regular_residues_at13_and17':[6,10],
  'special_fibre_polynomials_ascending':[list(vec(f)) for f in fs]}


def source_paths():return {COUNTER,COUNTS}

def validate_contract(c):
 require(c['schema']=='marici.hodge-off-reflection-joint-screen.v1' and c['candidate_id']=='marici.hodge.nonsplit-sixfold.exp-sqrt-primes.v1' and
  c['node']=='off-reflection-two-prime-screen' and c['excluded_control_node']=='off-reflection-two-prime-target-transplant','joint-screen identity')
 require(c['arithmetic']==ARITH,'joint-screen arithmetic changed');signature_certificate(c['signature_argument'])
 require(set(c['scope_policy'])==set(POLICY) and all(v is False for v in c['scope_policy'].values()),'joint-screen scope promotion')


def report():
 c=json.loads(CONTRACT.read_text(encoding='utf-8'));validate_contract(c)
 require(json.loads(previous.OUT.read_text(encoding='utf-8'))==previous.report(),'stale first denominator-line receipt')
 require(json.loads(endmodel.OUT.read_text(encoding='utf-8'))==endmodel.report(),'stale target End/signature model')
 require(all([a for a in range(p) if good_model(a,p)]==REG[p] for p in (13,17)),'complete extended branch-chart partition')
 chart=weierstrass_chart_certificate();sig=signature_certificate(c['signature_argument']);previous.pole_certificate()
 data=json.loads((ROOT/COUNTS).read_text(encoding='utf-8'));require(data==run_counter() and len(data['rows'])==75 and
  (data['lambda'],data['b'])==(2,2),'fresh joint-screen counts')
 require(all(r['i_mod_p']==IMOD[r['p']] for r in data['rows']),'joint-screen native CM embeddings')
 old=json.loads((ROOT/previous.COUNTS).read_text(encoding='utf-8'));cases=[]
 for p in (13,17):
  small=independent_counts(p)
  for a in REG[p]:
   inherited=p==13 and a!=5;rows=[r for r in (old if inherited else data)['rows'] if r['a']==a and (inherited or r['p']==p)]
   result=annotated_case(rows,a,p)
   if inherited:require({k:result[k] for k in previous.reconstruct(rows,a)}==previous.reconstruct(rows,a),'inherited Gaussian reconstruction agrees')
   else:require(small[a]==[rows[0]['V'],rows[1]['V'],rows[0]['rho_Frobenius_fixed_V']],'independent extended-chart counts')
   cases.append(result)
 require(next(r for r in cases if (r['p'],r['a'])==(17,4))['Frobenius_characteristic_coefficients_descending']==first17.EXPECTED,'old good17 control independently recovered')
 for p in (13,17):
  cc=[r for r in cases if r['p']==p]
  require([r['a'] for r in cc if r['geometric_reduction_Ei_multiplicity_in_complement']==0]==ARITH['raw_CM_absence_a_mod'+str(p)],'computed CM absence residues')
  require([r['a'] for r in cc if r['opposite_type_reduction_multiplicity']>0]==ARITH['opposite_type_survivors_a_mod'+str(p)],'computed opposite-type residues')
 seven=next(r for r in cases if (r['p'],r['a'])==(17,7));six=next(r for r in cases if (r['p'],r['a'])==(17,6))
 require(seven['CM_Gaussian_linear_roots']==[{'type':'beta','unit':[1,0],'multiplicity':1}] and
  six['geometric_reduction_Ei_multiplicity_in_complement']==0,'same-type veto and literal a6 CM veto')
 crt=crt_partition(cases)
 require(crt['CM_only_joint_survivors']==ARITH['CM_only_joint_survivors'] and crt['typed_joint_survivors']==ARITH['typed_joint_survivors'] and
  len(crt['typed_excluded'])==197 and len(crt['uncertified'])==22,'computed CRT partition')
 centered=[a if a<=110 else a-221 for a in crt['typed_joint_survivors']]
 require(min(centered,key=lambda a:(abs(a),a))==-7,'least absolute certified two-prime lift')
 paths=source_paths()|{prior.COUNTER,CONTRACT.relative_to(ROOT).as_posix(),NOTE.relative_to(ROOT).as_posix(),
  Path(__file__).relative_to(ROOT).as_posix(),previous.OUT.relative_to(ROOT).as_posix(),endmodel.OUT.relative_to(ROOT).as_posix(),endmodel.NOTE.relative_to(ROOT).as_posix()}
 return {'schema':'marici.hodge-off-reflection-joint-screen-result.v1','candidate_id':c['candidate_id'],'node':c['node'],
  'excluded_control_node':c['excluded_control_node'],'target_transplant_verdict':'rejected','passed':True,'verdict':'constructed',
  'verification_level':'Two-prime full CM/type certificates, transverse Weierstrass chart, signature/End-field unpolarized veto and conditional CRT classification; no positive Hom lift.',
  'checks':dict.fromkeys(['complete_extended_branch_charts','fresh75_ordinary60_twisted_rows','independent_new_counts',
   'transverse_Weierstrass_branch_points','a_dependent_poles','unused_fifth_traces','complete55_order_certificates',
   'all_CM_native_types_accounted','faithful_equivariant_Hom_specialization','balanced_signature_forced_without_K_linear_isogeny',
   'CRT_partition_keeps_uncertified_classes','actual_new_a_minus7_theta4_source','scope'],True),
  'Weierstrass_chart_certificate':chart,'signature_certificate':sig,'finite_field_cases':cases,'CRT_partition':crt,
  'raw_CM_excluded_count_mod221':len(crt['raw_CM_excluded']),'typed_excluded_count_mod221':len(crt['typed_excluded']),
  'same_type_only_special_fibre_is_not_declared_CM_free':True,'literal_2_6_2_excluded_even_up_to_Y3_isogeny':True,
  'algebraic_congruence_boxes_excluded_mod17':[[2,a,b] for a in REG[17] if a!=10 for b in (2,15)],
  'new_algebraic_congruence_boxes_excluded_mod13':[[2,5,b] for b in (2,11)],'actual_next_control':actual_control(),
  **{k:False for k in POLICY},'source_sha256':{n:sha256((ROOT/n).read_bytes()).hexdigest() for n in sorted(paths)}}


if __name__=='__main__':
 r=report();OUT.write_text(json.dumps(r,indent=2)+'\n',encoding='utf-8')
 print(json.dumps({k:v for k,v in r.items() if k not in ('source_sha256','finite_field_cases')},indent=2))
