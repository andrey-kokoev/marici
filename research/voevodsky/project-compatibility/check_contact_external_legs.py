"""Primary-source stripped/unstripped comparison and contact response jets."""
from pathlib import Path
import hashlib,json
import sympy as s
HERE=Path(__file__).resolve().parent;ROOT=HERE.parents[2]
primary=ROOT/'temp/triangle-measure-primary-2401.05207-source/GeomCosmoCorr.tex'
paths=[Path(__file__),HERE/'contact-external-leg-comparison.md',primary,ROOT/'src/ledger/20260824-2159 Component Factorization Canonically Normalizes the Moving Contact Kernel.md']
def hashes():return {p.relative_to(ROOT).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}
before=hashes();text=primary.read_text(encoding='utf-8')
for label in ('eq:CC3','eq:CG','eq:CGrules'):assert '\\eqlabel{'+label+'}' in text
P,q,y,C,L0=s.symbols('P q y C L0',nonzero=True)
assert s.simplify((4*P*2*q/y-8*C).subs(P,C*y/q))==0
g=s.symbols('g0:3',positive=True)
for i in range(3):
 others=[j for j in range(3) if j!=i]
 f=8*C*s.prod(g[j] for j in others)*(1-g[i])
 L=L0*s.prod(g[j]**(j+1) for j in range(3));base=dict.fromkeys(g,1)
 assert f.subs(base)==0
 assert s.simplify((g[i]*s.diff(L*f,g[i])).subs(base)+8*C*L0)==0
z=s.symbols('z',positive=True);f=8*C*(1-z)
D=lambda expr:z*s.diff(expr,z)
controls=[]
for m in range(5):
 L=L0*z**m;physical=L*f
 assert s.simplify(D(physical).subs(z,1)+8*C*L0)==0
 second=s.simplify(D(D(physical)).subs(z,1))
 assert s.simplify(second+8*C*L0*(2*m+1))==0
 cov=physical;plain=f
 for n in range(1,4):
  cov=s.expand(D(cov)-m*cov);plain=s.expand(D(plain))
  assert s.simplify(cov-L*plain)==0
 controls.append({'external_multiplicity':m,'second_response_over_minus8CL0':2*m+1})
assert before==hashes()
report={'passed':True,'source_unchanged':True,'source_sha256':before,'cyclic_first_response_controls':3,'higher_response_controls':controls,'covariant_orders_checked':[1,2,3],'source_comparison':'F_phys=L_ext F_prime','scope':'Contracted graph/readout level; no double vacuum normalization, no uncontracted operator lift or boundary norm equivalence inferred.'}
(HERE/'contact-external-leg-comparison.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
print(json.dumps(report,indent=2))
