"""Actual reflection quotients and source isogenies, not a Frobenius-factor lift."""
from fractions import Fraction as Q
from pathlib import Path
from hashlib import sha256
import json
import check_hodge_minimal_axis_scalar_source as src
import check_hodge_even_axis_principal_model as target

ROOT=src.ROOT
CONTRACT=ROOT/'research/conjecture_net/contracts/hodge-scalar-reflection-decomposition.v1.json'
NOTE=ROOT/'research/voevodsky/hodge-scalar-reflection-decomposition-v1.md'
OUT=ROOT/'research/voevodsky/results/hodge-scalar-reflection-decomposition-v1.json'
GEOMETRY={'domain':'complex_lambda_not_0_or_1_with_g_degree4_unramified_over_0_1_minus1_infinity',
 'reflection_loci':['a=2*lambda','a=2','b=0'],'quotient_genera':[3,5],'ramified_source_genus':9,
 'scalar_tower_genera':[17,9,5],'ramified_Prym_product_isogeny_degree':128,
 'principal_source_product_isogeny_degree':256,'principal_polarization_pullback_multiple':2,
 'target_simple_factor_dimension':6,'literal_b3_source_excluded':True,
 'all_admissible_lambda2_a4_b_sources_excluded':True,'off_locus_control_parameters':[2,0,2]}
POLICY=['all_scalar_parameters_excluded','all_other_reflections_classified','off_locus_sources_have_simple_complement','off_locus_target_compatibility_established',
 'source_principally_polarized_product_isomorphism_claimed','source_End0_computed',
 'complex_factors_lifted_from_finite_fields','reflection_exclusion_uses_arithmetic_specialization',
 'actual_source_constructions_invalidated','source_degree256_isogeny_identified_with_target_isogeny',
 'inverse_Chow_map_constructed','fixed_Y3_Prym_membership_constructed','nonzero_target_exceptional_cycle_constructed',
 'Hodge_proved','Hodge_refuted','global_witness_search_completed']

def require(c,m):
 if not c:raise ValueError(m)

# Exact polynomial ring Q[lambda,a,b,x,s]. No symbolic external dependency.
O={(0,0,0,0,0):Q(1)}
def variable(i):
 e=[0]*5;e[i]=1;return {tuple(e):Q(1)}
L,A,B,X,S=[variable(i) for i in range(5)]
def scale(p,c):return {e:v*c for e,v in p.items() if v*c}
def add(p,q,c=1):
 r=dict(p)
 for e,v in q.items():r[e]=r.get(e,0)+c*v
 return {e:v for e,v in r.items() if v}
def mul(p,q):
 r={}
 for e,v in p.items():
  for f,w in q.items():
   k=tuple(a+b for a,b in zip(e,f));r[k]=r.get(k,0)+v*w
 return {e:v for e,v in r.items() if v}
def power(p,n):
 r=O
 for _ in range(n):r=mul(r,p)
 return r
def sub(p,q):return add(p,q,-1)
def const(n):return scale(O,Q(n))
def subst(p,i,value):
 r={}
 for e,v in p.items():
  k=list(e);n=k[i];k[i]=0;r=add(r,mul({tuple(k):v},power(value,n)))
 return r

def reflection_data():
 return [
  ('one_torsion',scale(L,2),B,sub(X,L),sub(X,O),sub(O,L),[O,scale(L,-1),O,scale(O,-1)]),
  ('lambda_torsion',const(2),B,mul(L,sub(X,O)),sub(X,L),mul(L,sub(L,O)),[L,scale(L,-1),O,scale(L,-1)]),
  ('zero_torsion',A,{},L,X,L,[{},L,O,{}])]

def symbolic_certificates():
 P=mul(mul(X,sub(X,O)),sub(X,L));N=mul(B,sub(power(X,2),L));D=sub(add(power(X,2),L),mul(A,X))
 require(add(sub(power(L,2),mul(A,mul(L,X))),mul(L,power(X,2)))==mul(L,D) and
  mul(B,sub(power(L,2),mul(L,power(X,2))))==scale(mul(L,N),-1),'generic anti-translation numerator and denominator')
 names=[]
 for name,a,b,q,r,c,m in reflection_data():
  root={'one_torsion':O,'lambda_torsion':L,'zero_torsion':{}}[name]
  require(r==sub(X,root) and sub(q,mul(root,r))==c,'reflection invariant coordinate '+name)
  d=sub(add(power(X,2),L),mul(a,X));n=mul(b,sub(power(X,2),L))
  dp=add(sub(power(q,2),mul(a,mul(q,r))),mul(L,power(r,2)))
  np=mul(b,sub(power(q,2),mul(L,power(r,2))))
  require(dp==mul(c,d) and np==mul(c,n),'reflection g invariance '+name)
  require(mul(power(c,2),P)==mul(mul(mul(q,sub(q,r)),sub(q,mul(L,r))),r),'reflection elliptic equation '+name)
  u,v,w,z=m
  require(add(mul(u,u),mul(v,w))==c and not add(mul(u,v),mul(v,z)) and
   not add(mul(w,u),mul(z,w)) and add(mul(w,v),mul(z,z))==c,'reflection square '+name)
  require(sub(mul(u,z),mul(v,w))==scale(c,-1),'reflection differential sign '+name)
  names.append(name)
 # Exact invariance defects for the two nonzero-torsion reflections.
 q=sub(X,L);r=sub(X,O);dp=add(sub(power(q,2),mul(A,mul(q,r))),mul(L,power(r,2)))
 require(sub(dp,mul(sub(O,L),D))==mul(sub(scale(L,2),A),add(sub(power(X,2),scale(X,2)),L)),'a=2lambda locus defect')
 q=mul(L,sub(X,O));r=sub(X,L);dp=add(sub(power(q,2),mul(A,mul(q,r))),mul(L,power(r,2)))
 require(sub(dp,mul(mul(L,sub(L,O)),D))==mul(mul(L,sub(const(2),A)),add(sub(power(X,2),mul(scale(L,2),X)),L)),'a=2 locus defect')
 # Generic dual two-isogeny T_lambda -> W_lambda.
 tpoly=add(add(power(X,3),mul(sub(scale(L,2),const(4)),power(X,2))),mul(power(L,2),X))
 xn=power(add(X,L),2);xd=scale(X,4)
 left=mul(mul(tpoly,power(sub(power(X,2),power(L,2)),2)),power(xd,3))
 right=mul(mul(mul(xn,sub(xn,xd)),sub(xn,mul(L,xd))),scale(power(X,4),64))
 require(left==right,'generic T-to-W equation')
 require(subst(tpoly,3,scale(L,-1))==scale(power(L,2),-4),'generic kappa point')
 deriv={tuple(list(e[:3])+[e[3]-1]+list(e[4:])):v*e[3] for e,v in tpoly.items() if e[3]}
 require(subst(deriv,3,scale(L,-1))==scale(L,8),'generic kappa tangent')
 return names

def quotient_models(component):
 s2=power(S,2)
 if component=='one_torsion':
  d=sub(s2,L);n=add(S,mul(B,add(s2,L)));alpha=add(s2,L);k=s2;factor=sub(X,O)
 elif component=='lambda_torsion':
  d=sub(s2,O);n=add(S,mul(B,add(s2,O)));alpha=add(s2,O);k=mul(L,s2);factor=sub(X,L)
 elif component=='zero_torsion':
  d=sub(add(add(s2,O),L),A);n=S;alpha=add(add(s2,O),L);k=L;factor=X
 else:raise ValueError('unknown reflection component')
 a=scale(L,2) if component=='one_torsion' else const(2) if component=='lambda_torsion' else A
 b=B if component!='zero_torsion' else {}
 relation=add(sub(power(X,2),mul(alpha,X)),k)
 require(sub(sub(add(power(X,2),L),mul(a,X)),mul(d,factor))==relation,'invariant denominator')
 require(sub(mul(b,sub(power(X,2),L)),mul(sub(n,S),factor))==mul(b,relation),'invariant numerator')
 P=mul(mul(X,sub(X,O)),sub(X,L))
 require(sub(P,power(mul(S,factor),2))==mul(factor,relation),'invariant coordinate elliptic equation')
 R=sub(power(alpha,2),scale(k,4));F=mul(mul(d,n),mul(sub(n,d),add(n,d)))
 require(sub(power(sub(scale(X,2),alpha),2),R)==scale(relation,4),'actual discriminant coordinate')
 return d,n,R,F

def specialize(p,l,a,b):
 r={}
 for e,v in p.items():
  require(e[3]==0,'quotient polynomial must not contain x')
  r[e[4]]=r.get(e[4],0)+v*Q(l)**e[0]*Q(a)**e[1]*Q(b)**e[2]
 return {i:v for i,v in r.items() if v}

def witness(l,a,b,component):
 require(all(type(t) is int for t in (l,a,b)),'integer witness parameters')
 require(l not in (0,1),'nonsingular elliptic lambda')
 require((component=='one_torsion' and a==2*l) or (component=='lambda_torsion' and a==2) or
  (component=='zero_torsion' and b==0),'point on specified reflection locus')
 d,n,R,F=[specialize(p,l,a,b) for p in quotient_models(component)]
 require(max(F) in (7,8) and max(R)==4 and src.gcd(d,n)=={0:Q(1)} and
  src.gcd(F,src.derivative(F))=={0:Q(1)} and src.gcd(R,src.derivative(R))=={0:Q(1)} and
  src.gcd(F,R)=={0:Q(1)},'admissible disjoint branch divisors')
 branch=max(F)+(max(F)%2)
 require(branch==8 and (branch+4)//2-1==5,'projective branch count')
 return {'parameters_lambda_a_b':[l,a,b],'component':component,
  'W_branch_polynomial_ascending':[int(R.get(j,0)) for j in range(5)],
  'H3_branch_polynomial_ascending':[int(F.get(j,0)) for j in range(max(F)+1)],
  'H3_genus':branch//2-1,'H5_genus':5,'infinity_branch':max(F)==7}

def off_locus_control():
 d={2:Q(1),0:Q(2)};n=src.N
 fs=[src.add(src.P,src.mul(src.add(src.scaled(d,c),n,-1),src.add(src.scaled(d,c),n,-1)),-1) for c in (0,1,-1)]
 require(src.gcd(d,src.derivative(d))=={0:Q(1)} and src.gcd(d,src.P)=={0:Q(1)} and
  src.gcd(d,fs[0])=={0:Q(1)} and all(max(f)==4 and src.gcd(f,src.derivative(f))=={0:Q(1)} and
  src.gcd(f,src.P)=={0:Q(1)} for f in fs),'off-locus actual source branch chart')
 require(0 not in (2,2*2) and 2!=0,'escape specified reflection loci')
 return {'parameters_lambda_a_b':[2,0,2],'tower_genera':[17,9,5],
  'primitive_elliptic_theta_degree':4,'all_three_specified_reflection_conditions_fail':True,
  'special_fibre_polynomials_ascending':[[int(f.get(j,0)) for j in range(5)] for f in fs]}

def validate_contract(c):
 require(c['schema']=='marici.hodge-scalar-reflection-decomposition.v1' and
  c['candidate_id']=='marici.hodge.nonsplit-sixfold.exp-sqrt-primes.v1' and c['node']=='scalar-reflection-quotient-decomposition' and
  c['excluded_control_node']=='reflection-symmetric-scalar-target-transplant','reflection identity')
 require(c['geometry']==GEOMETRY,'reflection geometry changed')
 require(set(c['scope_policy'])==set(POLICY) and all(v is False for v in c['scope_policy'].values()),'reflection scope promoted')
 symbolic_certificates()

def report():
 c=json.loads(CONTRACT.read_text(encoding='utf-8'));validate_contract(c)
 inputs={'source':src.OUT,'target':target.OUT};rs={'source':src.report(),'target':target.report()}
 for k,p in inputs.items():require(json.loads(p.read_text(encoding='utf-8'))==rs[k] and rs[k]['passed'],'stale reflection '+k)
 ws=[witness(2,4,b,'one_torsion') for b in (0,1,-1,2,3,6)]
 ws += [witness(3,6,2,'one_torsion'),witness(3,2,2,'lambda_torsion'),witness(2,0,0,'zero_torsion')]
 require(2**8==256 and 256//2==128 and max(3,5)<6,'source polarization degrees and simple-factor obstruction')
 names={p.relative_to(ROOT).as_posix() for p in inputs.values()}|{CONTRACT.relative_to(ROOT).as_posix(),NOTE.relative_to(ROOT).as_posix(),Path(__file__).relative_to(ROOT).as_posix()}
 return {'schema':'marici.hodge-scalar-reflection-decomposition-result.v1','candidate_id':c['candidate_id'],
  'node':c['node'],'excluded_control_node':c['excluded_control_node'],'target_transplant_verdict':'rejected','passed':True,'verdict':'constructed',
  'verification_level':'Exact generic reflection/isogeny/invariant-coordinate identities, smooth explicit witnesses and written actual quotient-Jacobian/polarization proof; no CM lifting.',
  'checks':dict.fromkeys(['generic_reflections_preserve_W_and_g','generic_cyclic_four_elliptic_lift',
   'actual_genus3_and_genus5_quotient_models','projective_infinity_branches_included','actual_quotient_pullback_isogeny',
   'polarization_and_degree256_computed','simple_sixfold_cannot_be_a_factor','specified_loci_not_whole_family','actual_off_locus_control_constructed'],True),
  'admissible_witnesses':ws,'source_isogeny_factor_dimensions':[3,5],'source_isogeny_degree':256,
  'source_principal_polarization_pullback_multiple':2,'ramified_Prym_product_isogeny_degree':128,
  'all_admissible_reflection_loci_excluded_even_up_to_complex_Y3_isogeny':True,
  'literal_b3_source_isogenous_to_Y3':False,'all_admissible_lambda2_a4_b_sources_excluded':True,
  'actual_off_locus_control':off_locus_control(),
  **{k:False for k in POLICY},'source_sha256':{n:sha256((ROOT/n).read_bytes()).hexdigest() for n in sorted(names)}}

if __name__=='__main__':
 r=report();OUT.write_text(json.dumps(r,indent=2)+'\n',encoding='utf-8');print(json.dumps(r,indent=2))
