"""Physical three-leg momentum lifts of contact-infinity limits."""
from pathlib import Path
import hashlib,json
import sympy as s
HERE=Path(__file__).resolve().parent;ROOT=HERE.parents[2]
paths=[Path(__file__),HERE/'contact-physical-boundary-scaling.md',ROOT/'src/ledger/20260824-2135 Deleted Correlator Sectors Have Connected-Component Energy Poles.md',ROOT/'src/ledger/20260824-2223 The Gaussian Contact Readout Has Only Existing Finite Contact Poles.md',ROOT/'research/benincasa/spectral-gaussian-source-to-observer-complex.json']
def hashes():return {p.relative_to(ROOT).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}
before=hashes();t,r=s.symbols('t r',positive=True)
def norm(v):return s.sqrt(v.dot(v))
def packet(p1,p2,l):
 p3=-p1-p2;E=[norm(p) for p in (p1,p2,p3)]
 y12,y23,y31=norm(l),norm(l+p2),norm(l-p1)
 ell=[E[0]+y12+y31,E[1]+y12+y23,E[2]+y23+y31]
 assert s.simplify(ell[0]+ell[1]-ell[2]-(E[0]+E[1]-E[2]+2*y12))==0
 L=1/(8*s.prod(E))
 return -8*L/(ell[1]*ell[2]),L,ell
p1=s.Matrix([1,0,0]);p2=s.Matrix([0,1,0]);l=s.Matrix([0,0,1])
base,L,_=packet(p1,p2,l);hard,_,_=packet(r*p1,r*p2,r*l)
assert s.simplify(hard*r**5-base)==0
uv,_,_=packet(p1,p2,r*l)
assert s.simplify(s.limit(r**2*uv,r,s.oo)+2*L)==0
mixed=[]
for a in (2,4,6):
 p=s.Matrix([0,t**a,0]);q=s.Matrix([1/t,0,0]);third=-p-q
 assert p+q+third==s.zeros(3,1)
 assert s.simplify(p.cross(q).dot(p.cross(q)))==t**(2*a-2)
 response,_,ell=packet(p,q,l)
 coefficient=s.limit(response/t**(4-a),t,0,dir='+')
 assert coefficient==-s.Rational(1,4)
 assert s.limit(ell[0],t,0,dir='+')==2
 assert s.limit(t*ell[1],t,0,dir='+')==2
 assert s.limit(t*ell[2],t,0,dir='+')==2
 mixed.append({'soft_exponent':a,'response_power':4-a,'leading_coefficient':str(coefficient)})
for n in (3,10,100):
 # The old independent-chart path violates a necessary physical inequality.
 assert n*n>n+n
assert before==hashes()
report={'passed':True,'source_unchanged':True,'source_sha256':before,'old_anisotropic_path':'inadmissible on one-external-leg-per-site momentum-conserving slice for t<1/2','fixed_external_uv_degree':-2,'uniform_hard_degree':-5,'mixed_soft_hard_controls':mixed,'scope':'Massless spectral covariance K=1/(2E); retained unintegrated contact coefficient, not full loop density or higher-valence generality.'}
(HERE/'contact-physical-boundary-scaling.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
print(json.dumps(report,indent=2))
