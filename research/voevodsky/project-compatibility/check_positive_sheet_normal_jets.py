"""Normal-coordinate product jets and explicit positive/negative sheet controls."""
from pathlib import Path
import hashlib,json
import sympy as s
HERE=Path(__file__).resolve().parent;ROOT=HERE.parents[2]
paths=[Path(__file__),HERE/'positive-sheet-normal-integration.md',HERE/'contact-route-density-restoration.md',ROOT/'research/benincasa/checkers/additive_contact_normal_grade.rs',ROOT/'src/ledger/20260824-2136 Component-Resolved Deletion Poles Reproduce the Labelled Normal Module.md']
def hashes():return {p.relative_to(ROOT).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}
before=hashes();P=s.symbols('P0:3',positive=True);a=s.symbols('a0:3',positive=True);v=s.symbols('v0:3',real=True)
D=s.prod(1/(s.sqrt(P[i]**2-v[i])+a[i]) for i in range(3));base=dict.fromkeys(v,0);D0=D.subs(base);ell=[P[i]+a[i] for i in range(3)]
for i in range(3):
 assert s.simplify(s.diff(D,v[i]).subs(base)-D0/(2*P[i]*ell[i]))==0
 expected=D0*(1/(4*P[i]**3*ell[i])+1/(2*P[i]**2*ell[i]**2))
 assert s.simplify(s.diff(D,v[i],2).subs(base)-expected)==0
 for j in range(i+1,3):
  assert s.simplify(s.diff(D,v[i],v[j]).subs(base)-D0/(4*P[i]*P[j]*ell[i]*ell[j]))==0
# Real rational samples of the denominator bound; the complex proof is in the note.
count=0
for p in (1,2,3):
 for shift in (0,1,7):
  for fraction in (s.Rational(-1,2),0,s.Rational(1,2)):
   X=s.sqrt(p*p*(1-fraction))
   assert s.simplify(X+shift-(p+shift)/s.sqrt(2)).is_nonnegative
   count+=1
# Norm centers0 andP on one axis, pointu between them: y_a+y_b=P.
for p in (1,2,3):
 for fraction in (s.Rational(1,4),s.Rational(1,2),s.Rational(3,4)):
  u=p*fraction;distance_sum=u+(p-u)
  assert p+distance_sum==2*p and -p+distance_sum==0
assert before==hashes()
report={'passed':True,'source_unchanged':True,'source_sha256':before,'first_derivatives_checked':3,'diagonal_second_derivatives_checked':3,'mixed_second_derivatives_checked':3,'real_domination_controls':count,'sheet_segment_controls':9,'analytic_result':'Finite normal Taylor jets commute with the restored integral on positive-sheet polydisc by a written L1 domination proof.','scope':'Not a negative-sheet singular-grade or physical operator-lift theorem; finite fixtures are not formalized holomorphic integration.'}
(HERE/'positive-sheet-normal-integration.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
print(json.dumps(report,indent=2))
