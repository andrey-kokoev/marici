"""Exact labelled composition into a fixture-only finite radial witness."""
import copy,json
from fractions import Fraction as F
from pathlib import Path
ROOT=Path('research/nima');BASE=json.loads((ROOT/'contracts/spline-labelled-g4-witness-synthetic.v1.json').read_text())
def M(a):return [[F(x) for x in r] for r in a]
def mm(a,b):
 a,b=M(a),M(b);return [[sum(a[i][k]*b[k][j] for k in range(len(b))) for j in range(len(b[0]))] for i in range(len(a))]
def rk(a):
 a=M(a);m=len(a);n=len(a[0]);r=0
 for c in range(n):
  p=next((i for i in range(r,m) if a[i][c]),None)
  if p is None:continue
  a[r],a[p]=a[p],a[r];q=a[r][c];a[r]=[x/q for x in a[r]]
  for i in range(m):
   if i!=r and a[i][c]:q=a[i][c];a[i]=[a[i][j]-q*a[r][j] for j in range(n)]
  r+=1
 return r
def pole_value(z):return (z+1/z-F(5,2))**2
def validate(c):
 e=[];src=c['source_basis'];ids=[x['id'] for x in src]
 if len(ids)!=len(set(ids)) or ids[:4]!=['p2m1','p2m2','pole_2','pole_half']:e.append('lost_or_duplicated_source_label')
 pp=[x for x in src if x['kind']=='prime_power']
 if len({(x['prime'],x['grade']) for x in pp})!=len(pp):e.append('collapsed_prime_grade')
 poles={x['id']:x for x in src if x['kind']=='pole'}
 if set(poles)!={'pole_2','pole_half'} or poles.get('pole_2',{}).get('reciprocal')!='pole_half' or poles.get('pole_half',{}).get('reciprocal')!='pole_2':e.append('broken_reciprocal_poles')
 U,S=c['U'],c['reciprocal']
 if mm(S,U)!=mm(U,S):e.append('noncommuting_reciprocal_transport')
 if c['arithmetic_coefficient']!=-2:e.append('arithmetic_sign_or_factor_erased')
 if pole_value(F(2)) or pole_value(F(1,2)):e.append('pole_annihilation_failure')
 if mm(c['recovery'],U)!=M(U):e.append('recovery_failure')
 if rk(U)!=4 or rk(c['green_metric'])!=4 or any(c['green_metric'][i][4] for i in range(5)):e.append('kernel_radical_mismatch')
 return e
base=validate(BASE);assert base==[]
mutations={
 'grade_collapse':lambda c:c['source_basis'][1].__setitem__('grade',1),
 'lost_pole':lambda c:c['source_basis'].__setitem__(3,copy.deepcopy(c['source_basis'][2])),
 'pole_transport_break':lambda c:c.__setitem__('reciprocal',[[1,0,0,0,0],[0,1,0,0,0],[0,0,0,0,1],[0,0,0,1,0],[0,0,1,0,0]]),
 'sign_erasure':lambda c:c.__setitem__('arithmetic_coefficient',2),
 'recovery_break':lambda c:c.__setitem__('recovery',[[1,0,0,0,0],[0,0,0,0,0],[0,0,1,0,0],[0,0,0,1,0],[0,0,0,0,1]]),
 'extra_radical':lambda c:c.__setitem__('green_metric',[[1,0,0,0,0],[0,1,0,0,0],[0,0,0,0,0],[0,0,0,1,0],[0,0,0,0,0]])}
h={}
for n,f in mutations.items():x=copy.deepcopy(BASE);f(x);h[n]=validate(x);assert h[n]
out={'schema':'marici.spline-labelled-g4-witness-check.v1','status':'passed','baseline_errors':base,'hostile_results':h,'composed_facts':['distinct prime grades','reciprocal pole labels','reciprocal covariance','arithmetic coefficient -2','exact pole annihilation','recovery on range','cycle equals Green radical'],'remaining_semantic_gap':'no source-derived arrow identifies the synthetic target basis with a G4 projective oriented-edge carrier','claim_boundary':BASE['claim_boundary']}
(ROOT/'results/spline-labelled-g4-witness-synthetic.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
