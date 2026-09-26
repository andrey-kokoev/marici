"""Source-labelled contact infinity grades and the ordinary-norm hostile control."""
from pathlib import Path
import hashlib,json
import sympy as S
HERE=Path(__file__).resolve().parent;ROOT=HERE.parents[2]
paths=[Path(__file__),HERE/'contact-infinity-filtered-recovery.md',ROOT/'src/ledger/20260824-2224 The Gaussian Score Selects the Contact-Infinity Cartier Grade.md',ROOT/'src/ledger/20260824-2225 The Two-Contact Infinity Grade Is Order-Independent.md',ROOT/'research/benincasa/checkers/contact_infinity_score_cartier.rs']
def hashes():return {p.relative_to(ROOT).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}
before=hashes()
s=S.symbols('s1:4',positive=True);l=S.symbols('l1:4',positive=True);x=S.Matrix(S.symbols('x1:4'));t=S.symbols('t',positive=True)
pairs=[(0,1),(1,2),(2,0)]
g=[s[j]*s[k] for j,k in pairs];h=[1/(l[j]*l[k]) for j,k in pairs]
B=S.Matrix([[1,2,0],[1,-1,-1],[1,-1,1]]).T
G=S.diag(*g);H=S.diag(*h);z=-8*B*G*H*x
normalized=S.simplify(B*G.inv()*B.inv()*z)
assert S.simplify(normalized+8*B*H*x)==S.zeros(3,1)
occ=B.inv()*z
for i,(j,k) in enumerate(pairs):
 forward=S.limit(S.limit(occ[i]/s[j],s[j],0)/s[k],s[k],0)
 reverse=S.limit(S.limit(occ[i]/s[k],s[k],0)/s[j],s[j],0)
 assert S.simplify(forward+8*h[i]*x[i])==0 and forward==reverse
path={s[0]:t,s[1]:t,s[2]:t**2,**{a:1 for a in l}}
leading=(z.subs(path)/t**2).applyfunc(lambda v:S.limit(v,t,0))
assert S.simplify(leading+8*B*S.Matrix([x[0],0,0]))==S.zeros(3,1)
assert S.simplify(normalized.subs(path)+8*B*x)==S.zeros(3,1)
assert B*B.T==S.diag(3,6,2)
e=S.Matrix([0,1,0]);raw=-8*t**3*B*e;graded=-8*B*e
samples=[]
for n in (2,10,100):
 raw_n=raw.subs(t,S.Rational(1,n))
 assert raw_n.dot(raw_n)==graded.dot(graded)/n**6
 samples.append({'t':f'1/{n}','raw_norm_squared':str(raw_n.dot(raw_n)),'graded_norm_squared':str(graded.dot(graded)),'source_norm_squared':1})
assert before==hashes()
report={'passed':True,'source_unchanged':True,'source_sha256':before,'labelled_grade_identity':True,'pairwise_order_controls':3,'single_leading_grade_retains_only':'12 occurrence on s=(t,t,t^2)','instability_samples':samples,'weighted_lower_bound':'8 sqrt(2) min|h_e|','scope':'Source-selected asymptotic coefficients; continuity in retained-grade coordinates, not ordinary raw-readout or experimental noise topology.'}
(HERE/'contact-infinity-filtered-recovery.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
print(json.dumps(report,indent=2))
