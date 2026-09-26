"""Exact Gaussian score metric and source contact-response amplification."""
from pathlib import Path
import hashlib,json
import sympy as s
HERE=Path(__file__).resolve().parent;ROOT=HERE.parents[2]
paths=[Path(__file__),HERE/'contact-score-fisher-gate.md',ROOT/'src/ledger/20260824-2214 The Gaussian Kernel Tangent Has a Normalized Quadratic Score.md',ROOT/'src/ledger/20260824-2219 Gaussian Score Insertion Commutes with the Contact-Normal Grade.md',ROOT/'src/ledger/20260824-2235 The Minimal Real Homogeneous Occurrence Adapter Is Gaussian Quadrupole Rank Two.md',ROOT/'src/ledger/20260824-2236 The Gaussian Quadrupole Resolves the Homogeneous Contact Kernel.md']
def hashes():return {p.relative_to(ROOT).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}
before=hashes();a=s.symbols('a',positive=True)
m2=1/(2*a);m4=3/(4*a**2)
assert s.simplify(a*m2-s.Rational(1,2))==0
assert s.simplify(a*a*m4-a*m2+s.Rational(1,4))==s.Rational(1,2)
Q=s.Matrix([[1,2,0],[1,-1,-1],[1,-1,1]])
F=Q.T*Q/2;assert F==s.diag(s.Rational(3,2),3,1)
C=s.symbols('C1:4',positive=True);x=s.Matrix(s.symbols('x1:4',real=True));D=s.diag(*C)
r=-8*Q.T*D*x
norm=s.expand((r.T*F.inv()*r)[0])
assert s.simplify(norm-128*sum(C[i]**2*x[i]**2 for i in range(3)))==0
f=-16*D*x
assert Q.T*f/2==r
assert s.simplify((f.T*f)[0]/2-norm)==0
for i in range(3):
 e=s.eye(3)[:,i];L=-e/(8*C[i])
 assert s.simplify((f.T*L)[0]/2-x[i])==0
 assert s.simplify((L.T*L)[0]/2-1/(128*C[i]**2))==0
samples=[]
for n in (2,10,100):
 t=s.Rational(1,n);signal=128*t**6;cost=1/(128*t**6)
 assert signal*cost==1
 samples.append({'t':str(t),'squared_response_norm':str(signal),'squared_extractor_norm':str(cost),'graded_squared_response_norm':128})
assert before==hashes()
report={'passed':True,'source_unchanged':True,'source_sha256':before,'port_fisher_diagonal':['3/2','3','1'],'dual_response_norm_squared':'128 sum C_e^2 x_e^2','extractor_norm_squared':'1/(128 C_e^2)','path_controls':samples,'scope':'Independent real-mode source scores and retained contact-response covectors; not variance of O times score, universal sampling complexity or a no-go for all physical ports.'}
(HERE/'contact-score-fisher-gate.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
print(json.dumps(report,indent=2))
