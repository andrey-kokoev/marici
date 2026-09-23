"""Independent high-precision raw five-bracket replay of sourced psi trace."""
import json
from pathlib import Path
import mpmath as mp
import sympy as s
import check_nine_point_complete_psi_component_trace as source
OUT=Path(__file__).resolve().parents[1]/'results';mp.mp.dps=110
packet=json.loads((OUT/'nine-point-complete-four-mass-psi-component-trace.json').read_text())
assert packet['passed']
def as_mp(z):
 z=s.Rational(z);return mp.mpf(int(z.p))/int(z.q)
a,b,c=map(as_mp,source.P.all_coeffs());disc=b*b-4*a*c
assert disc>0
roots=[(-b+mp.sqrt(disc))/(2*a),(-b-mp.sqrt(disc))/(2*a)]
def fn(expr):return s.lambdify((source.alpha,source.beta),expr,'mpmath',cse=True)
components=[];without_prefactor=[]
for root in roots:
 beta=fn(source.beta_alpha)(root,0)
 ps=fn(source.psi_num)(root,beta)/fn(source.psi_den)(root,beta)
 first=fn(source.na)(root,beta)**4/mp.fprod(fn(z)(root,beta) for z in source.da)
 second=fn(source.nb)(root,beta)**4/mp.fprod(fn(z)(root,beta) for z in source.db)
 components.append(ps*first*second);without_prefactor.append(first*second)
assert len(components)==2 and components[0]!=components[1]
exact=as_mp(packet['two_branch_component_trace']);total=sum(components)
assert abs(total-exact)<mp.mpf('1e-75')*max(1,abs(exact))
assert abs(sum(without_prefactor)-exact)>mp.mpf('1e-50')*max(1,abs(exact))
assert abs(components[0]-components[1]-exact)>mp.mpf('1e-50')*max(1,abs(exact))
result={'passed':True,'independent_raw_five_bracket_stress':True,
 'mutations_refused':['omitted_psi_prefactor','reversed_second_branch_orientation'],
 'scope':'High-precision stress of exact quadratic-field component trace; not a target-form equality or nine-point history assignment.'}
(OUT/'nine-point-complete-four-mass-psi-component-trace-verification.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
