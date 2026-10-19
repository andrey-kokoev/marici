"""Integral self-adjoint spectral projector at3 and conditional sixfold norm parity."""
from fractions import Fraction as Q
from functools import lru_cache
from pathlib import Path
from hashlib import sha256
import json
import check_hodge_off_reflection_joint_screen as previous
from check_hodge_minimal_axis_frobenius_obstruction import za,zm,zs,zd,bar,ints,require

ROOT=previous.ROOT
CONTRACT=ROOT/'research/conjecture_net/contracts/hodge-inert-elliptic-projector.v1.json'
NOTE=ROOT/'research/voevodsky/hodge-inert-elliptic-projector-v1.md'
OUT=ROOT/'research/voevodsky/results/hodge-inert-elliptic-projector-v1.json'
ZERO=(0,0);ONE=(1,0)
ARITH={'good_prime':13,'inert_lattice_prime':3,'lambda_residue':2,'a_residue':2,'b_residues':[2,11],
 'first_axis_beta':[3,2],'opposite_axis_gamma':[-2,-3],'PV8_derivative_at_gamma':[-14400,-73600],
 'derivative_mod3':[0,2],'first_axis_primitive_theta_degree':4,'fixed_X6_End0':'Q(i)',
 'fixed_X6_Hermitian_determinant_class':-3,'fixed_X6_dimension':6,
 'literal_excluded_control':[2,-24,2],'remaining_control':[2,-7,2],
 'newly_excluded_CRT_classes_mod221':[54,80,158,197],'updated_excluded_count_mod221':201,
 'updated_joint_survivors_mod221':[214],'updated_uncertified_count_mod221':19}
POLICY=['complex_opposite_axis_constructed','nonunit_derivative_proves_a_bad_theta_degree',
 'finite_positive_CM_factor_lifted','source_End0_computed','isogeny_assumed_K_linear',
 'target_End_field_or_norm_class_omitted','principal_polarization_transferred_through_arbitrary_isogeny',
 'joint_axis_kernel_computed','remaining_a_minus7_control_excluded','third_prime_Frobenius_computed',
 'uncertified_chart_failure_alone_implies_exclusion','one_CRT_survivor_exhausts_complex_sources',
 'arbitrary_transcendental_parameters_excluded','all_scalar_parameters_excluded','actual_source_constructions_invalidated',
 'fixed_Y3_membership_constructed','nonzero_target_exceptional_cycle_constructed','Hodge_proved','Hodge_refuted','global_witness_search_completed']


def trim(a):
 a=list(a)
 while len(a)>1 and a[-1]==ZERO:a.pop()
 return tuple(a or [ZERO])

def add(a,b):return trim([za(a[j] if j<len(a) else ZERO,b[j] if j<len(b) else ZERO) for j in range(max(len(a),len(b)))])
def scale(a,z):return trim([zm(x,z) for x in a])
def sub(a,b):return add(a,scale(b,(-1,0)))
def mul(a,b):
 c=[ZERO]*(len(a)+len(b)-1)
 for j,x in enumerate(a):
  for k,y in enumerate(b):c[j+k]=za(c[j+k],zm(x,y))
 return trim(c)

def divrem(a,b):
 a=trim(a);b=trim(b);require(b!=(ZERO,),'nonzero Gaussian polynomial divisor');q=[ZERO]*max(1,len(a)-len(b)+1)
 while a!=(ZERO,) and len(a)>=len(b):
  k=len(a)-len(b);z=zd(a[-1],b[-1]);q[k]=z;a=sub(a,(ZERO,)*k+scale(b,z))
 return trim(q),a

def rem(a,f):return divrem(a,f)[1]
def evaluate(a,z):
 out=ZERO
 for c in reversed(a):out=za(zm(out,z),c)
 return out

def integral_at3(a):return all(Q(v).denominator%3 for z in a for v in z)
def mod3(a):
 require(integral_at3(a),'3-integral coefficients required')
 return [[Q(v).numerator*pow(Q(v).denominator,-1,3)%3 for v in z] for z in a]

def serial(a):return [[[Q(v).numerator,Q(v).denominator] for v in z] for z in a]
def valuation3(n):
 n=abs(int(n));require(n>0,'nonzero valuation input');v=0
 while n%3==0:n//=3;v+=1
 return v


@lru_cache(maxsize=3)
def spectral_certificate(f7_desc,beta,gamma,p=13):
 f=mul(tuple(reversed(f7_desc)),(zs(beta,-1),ONE));require(len(f)==9 and f[-1]==ONE,'PV8 Gaussian polynomial')
 r,left=divrem(f,(zs(gamma,-1),ONE));require(left==(ZERO,),'actual opposite CM root')
 d=evaluate(r,gamma);require(d!=ZERO,'simple opposite CM root')
 derivative=tuple(zs(f[j],j) for j in range(1,len(f)))
 require(d==evaluate(derivative,gamma),'spectral derivative identity')
 e=scale(r,zd(ONE,d));idem=rem(sub(mul(e,e),e),f)
 require(idem==(ZERO,) and rem(sub(mul((ZERO,ONE),e),scale(e,gamma)),f)==(ZERO,),'spectral idempotent and eigenvalue')
 tinv=scale(f[1:],zd((-1,0),f[0]));require(rem(mul((ZERO,ONE),tinv),f)==(ONE,),'Frobenius inverse')
 adj= (ZERO,);p_inv_t=scale(tinv,(p,0))
 for c in reversed(e):adj=add(rem(mul(adj,p_inv_t),f),(bar(c),))
 require(rem(sub(adj,e),f)==(ZERO,),'Rosati self-adjoint spectral projector')
 trace=ZERO
 for j in range(8):
  c=rem((ZERO,)*j+e,f);trace=za(trace,c[j] if j<len(c) else ZERO)
 require(trace==ONE,'rank-one Gaussian projector')
 nd=ints(zm(d,bar(d)))[0];v=valuation3(nd);require(v%2==0,'inert Gaussian norm valuation even')
 unit=v==0;require(integral_at3(e)==unit,'local integrality exactly matches derivative unit')
 return {'PV8_Gaussian_coefficients_descending':[ints(z) for z in reversed(f)],
  'opposite_eigenvalue':ints(gamma),'PV8_derivative_at_gamma':ints(d),'derivative_norm':nd,
  'derivative_norm_valuation3':v,'quotient_r_coefficients_ascending':[ints(z) for z in r],
  'projector_coefficients_ascending':serial(e),'projector_mod3_coefficients_ascending':mod3(e) if unit else None,
  'exact_idempotent':True,'exact_Rosati_self_adjoint':True,'Gaussian_rank':1,'integral_at3':unit,
  'conditional_unit_degree_implication_certified':unit}


def norm_parity_certificate(end0='Q(i)',det=-3,dimension=6,first_degree=4):
 require((end0,det,dimension,first_degree)==('Q(i)',-3,6,4),'fixed End field, norm class, dimension and primitive degree required')
 residues=[[a,b,(a*a+b*b)%3] for a in range(3) for b in range(3) if a or b]
 require(all(r[2]!=0 for r in residues),'3 inert: nonzero residue norm cannot vanish')
 source_total=0;first=valuation3(first_degree)%2;opposite=0
 forced_six=(source_total-first-opposite)%2;target=valuation3(det)%2
 require(dimension%2==0 and forced_six==0 and target==1,'sixfold determinant parity contradiction')
 return {'nonzero_F9_norm_residues':residues,'principal_source_determinant_valuation_parity':0,
  'first_axis_degree_valuation_parity':first,'conditional_opposite_axis_degree_valuation_parity':opposite,
  'forced_sixfold_determinant_valuation_parity':forced_six,'fixed_X6_determinant_valuation_parity':target,
  'polarization_rescaling_exponent':dimension,'norm_basis_changes_have_even_valuation':True,
  'conjugating_K_on_even_dimensional_sixfold_preserves_parity':True,'requires_target_End0_exactly_Qi':True,
  'hypothetical_unpolarized_isogeny_not_assumed_K_linear':True}


def updated_crt(old):
 extra=[a for a in range(221) if a%13==2];excluded=sorted(set(old['typed_excluded'])|set(extra))
 out={'modulus':221,'excluded':excluded,'joint_survivors':[a for a in old['typed_joint_survivors'] if a not in extra],
  'uncertified':[a for a in old['uncertified'] if a not in extra],'newly_excluded':sorted(set(extra)-set(old['typed_excluded']))}
 require(len(set(out['excluded'])|set(out['joint_survivors'])|set(out['uncertified']))==221 and
  len(out['excluded'])+len(out['joint_survivors'])+len(out['uncertified'])==221,'complete disjoint updated CRT partition')
 return out


def validate_contract(c):
 require(c['schema']=='marici.hodge-inert-elliptic-projector.v1' and c['candidate_id']=='marici.hodge.nonsplit-sixfold.exp-sqrt-primes.v1' and
  c['node']=='inert-elliptic-projector-gate' and c['excluded_control_node']=='inert-degree-parity-target-transplant','inert-projector identity')
 require(c['arithmetic']==ARITH,'inert-projector arithmetic changed')
 require(set(c['scope_policy'])==set(POLICY) and all(v is False for v in c['scope_policy'].values()),'inert-projector scope promotion')


def report():
 c=json.loads(CONTRACT.read_text(encoding='utf-8'));validate_contract(c)
 old=previous.report();require(old==json.loads(previous.OUT.read_text(encoding='utf-8')),'stale two-prime source')
 case=lambda a:next(r for r in old['finite_field_cases'] if (r['p'],r['a'])==(13,a))
 r=case(2);require(r['geometric_reduction_Ei_multiplicity_in_complement']==1 and
  r['CM_Gaussian_linear_roots']==[{'type':'conjugate_beta','unit':[0,-1],'multiplicity':1}],'unique opposite special-fibre factor')
 f=tuple(tuple(z) for z in r['Gaussian_characteristic_coefficients_descending']);beta=(3,2);gamma=(-2,-3)
 cert=spectral_certificate(f,beta,gamma)
 require(cert['integral_at3'] and cert['PV8_derivative_at_gamma']==ARITH['PV8_derivative_at_gamma'] and
  [v%3 for v in cert['PV8_derivative_at_gamma']]==ARITH['derivative_mod3'],'unit derivative certificate')
 conjugate=spectral_certificate(tuple(bar(z) for z in f),bar(beta),bar(gamma))
 require(conjugate['integral_at3'] and conjugate['derivative_norm']==cert['derivative_norm'],'either orientation above13')
 ctrl=spectral_certificate(tuple(tuple(z) for z in case(6)['Gaussian_characteristic_coefficients_descending']),beta,(3,-2))
 require(ctrl['integral_at3'] is False,'nonunit control must stay inconclusive')
 parity=norm_parity_certificate();signature=previous.signature_certificate(previous.SIGNATURE)
 require(signature['allowed_Ei_squared_native_signatures']==[[1,1]],'conditional target forces opposite complex axis')
 crt=updated_crt(old['CRT_partition']);require(crt['newly_excluded']==[54,80,158,197] and len(crt['excluded'])==201 and
  crt['joint_survivors']==[214] and len(crt['uncertified'])==19,'computed new CRT counts')
 require(previous.good_model(-24,13) and previous.good_model(-24,17) and not previous.good_model(-7,29) and
  previous.good_model(-7,37),'scoped control and next-prime branch certificates')
 paths={CONTRACT.relative_to(ROOT).as_posix(),NOTE.relative_to(ROOT).as_posix(),Path(__file__).relative_to(ROOT).as_posix(),
  previous.OUT.relative_to(ROOT).as_posix(),previous.endmodel.NOTE.relative_to(ROOT).as_posix(),previous.endmodel.OUT.relative_to(ROOT).as_posix()}
 return {'schema':'marici.hodge-inert-elliptic-projector-result.v1','candidate_id':c['candidate_id'],'node':c['node'],
  'excluded_control_node':c['excluded_control_node'],'target_transplant_verdict':'rejected','verdict':'constructed','passed':True,
  'verification_level':'Fresh inherited Frobenius data, exact Gaussian idempotent/Rosati algebra, local self-duality and conditional End-field/norm parity; no positive Hom lift.',
  'checks':dict.fromkeys(['fresh_full_two_prime_CM_certificate','unique_opposite_finite_CM_line','rank_one_spectral_projector',
   'exact_idempotency_and_Rosati_self_adjointness','integral_at_inert3','conjugate_orientation',
   'nonunit_control_inconclusive','conditional_primitive_axis_has_unit_degree','fixed_End_field_norm_parity_contradiction',
   'updated_CRT_keeps_unknown_classes','scope'],True),
  'projector_certificate':cert,'nonunit_a6_control':ctrl,'norm_parity_certificate':parity,'CRT_partition':crt,
  'literal_2_minus24_2_excluded_even_up_to_Y3_isogeny':True,
  'algebraic_congruence_boxes_excluded_mod13':[[2,2,2],[2,2,11]],
  'remaining_actual_control':old['actual_next_control'],'prime29_displayed_model_uncertified_for_remaining_control':True,
  'prime37_good_branch_certificate_for_remaining_control':True,
  **{k:False for k in POLICY},'source_sha256':{n:sha256((ROOT/n).read_bytes()).hexdigest() for n in sorted(paths)}}


if __name__=='__main__':
 r=report();OUT.write_text(json.dumps(r,indent=2)+'\n',encoding='utf-8')
 print(json.dumps({k:v for k,v in r.items() if k not in ('source_sha256','nonunit_a6_control')},indent=2))
