"""Exact generic quartics: factorwise LCM, FLINT polynomial expansion, resumable."""
from pathlib import Path
from functools import lru_cache
import hashlib,json,itertools,time,sys
import sympy as s
from flint import fmpq_mpoly_ctx
root=Path(__file__).resolve().parents[1];source=root/'results/seven-point-generic-reduced-parity.json';raw=source.read_bytes();data=json.loads(raw)
assert data['passed'] and data['stage']=='construction complete'
assert len(data['terms'])==12 and all(t['Ward_residual_zero'] for t in data['terms'])
for filename,expected in data['source_sha256'].items():
 assert hashlib.sha256((Path(__file__).parent/filename).read_bytes()).hexdigest()==expected
names=('a','b','c','d','e','f');symbols=s.symbols(' '.join(names));ctx=fmpq_mpoly_ctx.get(names)
one=ctx.constant(1);zero=ctx.constant(0)
@lru_cache(None)
def polynomial(expr):
 p=s.Poly(expr,*symbols,domain=s.ZZ)
 return ctx.from_dict({powers:int(coeff) for powers,coeff in p.terms()})
# All irreducible factors below are primitive integer polynomials. Never use floats.
@lru_cache(None)
def factors(expr):
 coefficient,entries=s.factor_list(expr,*symbols)
 result={}
 for factor,power in entries:
  assert s.Poly(factor,*symbols).domain==s.ZZ
  result[factor]=power
 return s.Rational(coefficient),result

def product(factor_powers):
 result=one
 for factor,power in factor_powers.items():result*=polynomial(factor)**int(power)
 return result

weights=[s.sympify(t['signed_weight']) for t in data['terms']];vectors=[[s.sympify(v) for v in t['pivot_vector']] for t in data['terms']]
out=root/'results/seven-point-generic-quartics-lcm.json';digest=hashlib.sha256(raw).hexdigest();checker_digest=hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
report={'passed':False,'field':'Q(a,b,c,d,e,f)','source_sha256':digest,'checker_sha256':checker_digest,'identities':[],'method':'Exact factored denominator LCM and FLINT integer polynomial numerator summation; no rational gcd in the sum'}
if out.exists() and '--fresh' not in sys.argv:
 previous=json.loads(out.read_text())
 if previous.get('source_sha256')==digest:
  report=previous
  report.setdefault('checker_lineage',[])
  if report['checker_sha256'] not in report['checker_lineage']:report['checker_lineage'].append(report['checker_sha256'])
  report['checker_sha256']=checker_digest
completed={tuple(row['indices']) for row in report['identities']};start=time.monotonic()
for indices in itertools.combinations_with_replacement(range(3),4):
 if indices in completed:continue
 print('starting',indices,flush=True);terms=[];common={}
 for w,v in zip(weights,vectors):
  expr=s.factor(w*s.prod(v[i] for i in indices))
  if expr==0:continue
  numerator,denominator=s.fraction(expr);cn,fn=factors(numerator);cd,fd=factors(denominator)
  terms.append((cn/cd,fn,fd))
  for factor,power in fd.items():common[factor]=max(common.get(factor,0),power)
 # Clear the numeric denominators too, keeping all FLINT arithmetic integral.
 numeric_lcm=s.ilcm(*(coefficient.q for coefficient,_,_ in terms))
 scaled_terms=[]
 for coefficient,numerator,denominator in terms:
  merged=dict(numerator)
  for factor,power in common.items():merged[factor]=merged.get(factor,0)+power-denominator.get(factor,0)
  scaled_terms.append((int(coefficient*numeric_lcm),merged))
 # Remove the common nonzero polynomial factor BEFORE expansion. This is
 # exact in the integral domain and avoids enormous spurious helicity powers.
 shared={factor:min(powers.get(factor,0) for _,powers in scaled_terms) for factor in scaled_terms[0][1]}
 total=zero
 for scaled,powers in scaled_terms:
  reduced={factor:power-shared.get(factor,0) for factor,power in powers.items() if power>shared.get(factor,0)}
  total+=scaled*product(reduced)
 assert total==zero,indices
 report['identities'].append({'indices':indices,'numerator':'0','nonzero_terms':len(terms),'distinct_denominator_factors':len(common)})
 report['last_run_seconds']=round(time.monotonic()-start,3);out.write_text(json.dumps(report,indent=2)+'\n');print('proved',indices,flush=True)
report['passed']=True;report['scope']='All15 generic rational quartic identities from the source-digest-bound12 Ward-verified terms; with universal Ward basis this proves full parity on the regular six-modulus chart.'
out.write_text(json.dumps(report,indent=2)+'\n');print('passed',len(report['identities']),flush=True)
