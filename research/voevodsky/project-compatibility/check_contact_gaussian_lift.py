"""Exact Gaussian lifts and two distinct tomography ambiguity controls."""
from pathlib import Path
import hashlib,json
import sympy as s
HERE=Path(__file__).resolve().parent;ROOT=HERE.parents[2]
paths=[Path(__file__),HERE/'contact-gaussian-lift-ambiguity.md',ROOT/'src/ledger/20260824-2215 Gaussian Susceptibility Equals a Connected Score Pairing.md',ROOT/'src/ledger/20260824-2216 The Contact Packet Has a Fixed-State Mixed Readout.md',ROOT/'src/ledger/20260824-2231 The Complete Gaussian Score Tower Reconstructs Every Boolean Route Packet.md']
def hashes():return {p.relative_to(ROOT).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}
before=hashes();X=s.symbols('X0:3',real=True);g=s.symbols('g0:3',positive=True);C=s.symbols('C',positive=True)
def E(expr,var=(1,1,1)):
 total=0
 for powers,coef in s.Poly(s.expand(expr),*X).terms():
  if any(p%2 for p in powers):continue
  total+=coef*s.prod((s.factorial2(p-1) if p else 1)*v**(p//2) for p,v in zip(powers,var))
 return s.simplify(total)
score=[(a*a-1)/2 for a in X]
for i in range(3):
 j,k=[a for a in range(3) if a!=i]
 O=8*C*X[j]**2*X[k]**2*(1-X[i]**2);Z=X[i]*X[j];H=X[i]**4-6*X[i]**2+3
 assert s.simplify(E(O,g)-8*C*g[j]*g[k]*(1-g[i]))==0
 assert E(O)==0 and E(O*O)==1152*C*C
 assert E(Z,g)==0 and E(Z*Z)==1 and E(O*Z)==0
 assert E((O+Z)**2)==1152*C*C+1 and E((O+Z)*Z)==1
 assert E(H*H)==24 and s.expand(E(H,g)-3*(g[i]-1)**2)==0
 for mask in range(8):
  test=s.prod(score[a] for a in range(3) if mask&(1<<a))
  assert E(Z*test)==0 and E(H*test)==0
 assert s.expand(O+16*C*score[i]*(1+2*score[j])*(1+2*score[k]))==0
assert before==hashes()
report={'passed':True,'source_unchanged':True,'source_sha256':before,'cyclic_lifts_checked':3,'square_free_score_tests_per_lift':8,'canonical_norm_squared':'1152 C^2','same_full_covariance_family_alternative_norm_squared':'1152 C^2 + 1','even_finite_tower_invisible_H4_norm_squared':24,'scope':'Gaussian-model data-sufficiency controls, not physical admission of X_i X_j or H4. Full-observable uniqueness requires source conditions; Hermite completeness is a written argument.'}
(HERE/'contact-gaussian-lift-ambiguity.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
print(json.dumps(report,indent=2))
