"""Complete source Gaussian covariance-response tower, without owner mutations."""
from pathlib import Path
import hashlib,json,itertools
import sympy as s
HERE=Path(__file__).resolve().parent;ROOT=HERE.parents[2]
paths=[Path(__file__),HERE/'contact-full-score-tower.md',ROOT/'src/ledger/20260824-2174 The Generic Contact Kernel Is a Destructive-Interference Packet.md',ROOT/'src/ledger/20260824-2231 The Complete Gaussian Score Tower Reconstructs Every Boolean Route Packet.md',ROOT/'src/ledger/20260824-2218 The Raw Gaussian Score Does Not Isolate the Contact Packet.md']
def hashes():return {p.relative_to(ROOT).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}
before=hashes();g=s.symbols('g0:3');C=s.symbols('C',positive=True)
subsets=[frozenset(i for i in range(3) if mask&(1<<i)) for mask in range(8)]
for absent in range(3):
 pair=set(range(3))-{absent}
 F=8*C*s.prod(g[i] for i in pair)*(1-g[absent]);M={}
 for T in subsets:
  expr=F
  for i in sorted(T):expr=g[i]*s.diff(expr,g[i])
  M[T]=s.expand(expr.subs(dict.fromkeys(g,1)))
  assert M[T]==(-8*C if absent in T else 0)
 for S in subsets:
  recovered=s.simplify(sum((-1)**(len(T)-len(S))*M[T] for T in subsets if S<=T))
  expected=8*C if S==pair else -8*C if len(S)==3 else 0
  assert recovered==expected
 dual=s.expand(sum(2**len(T)*M[T]**2 for T in subsets))
 assert dual==1152*C**2
 # Coefficients of the normalized Riesz test in the product-score basis.
 coeff={T:s.simplify(2**len(T)*M[T]/dual) for T in subsets}
 assert s.simplify(sum(coeff[T]*M[T] for T in subsets))==1
 assert s.simplify(sum(coeff[T]**2/s.Integer(2)**len(T) for T in subsets))==1/(1152*C**2)
samples=[]
for n in (2,10,100):
 t=s.Rational(1,n);signal=1152*t**6;cost=1/signal
 assert signal*cost==1
 samples.append({'t':str(t),'full_squared_response_norm':str(signal),'minimum_squared_tower_test_norm':str(cost)})
assert before==hashes()
report={'passed':True,'source_unchanged':True,'source_sha256':before,'cyclic_channels_checked':3,'response_slots_per_channel':8,'mobius_recovery':True,'full_dual_norm_squared':'1152 C^2','first_score_dual_norm_squared':'128 C^2','minimum_normalized_tower_test_norm_squared':'1/(1152 C^2)','path_controls':samples,'scope':'Frozen contact-normal channel; all labelled distinct covariance responses. Not all physical observables or empirical mixed-product estimator variances.'}
(HERE/'contact-full-score-tower.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
print(json.dumps(report,indent=2))
