"""Primary-equation provenance and normalized-insertion type control."""
from pathlib import Path
import hashlib,json
import sympy as s
HERE=Path(__file__).resolve().parent;ROOT=HERE.parents[2]
primary=ROOT/'temp/triangle-measure-primary-2401.05207-source/GeomCosmoCorr.tex'
paths=[Path(__file__),HERE/'contact-primary-operator-typing.md',primary,ROOT/'src/ledger/20260824-2211 The Gaussian Two-Point Kernel Induces the Deletion Tangent.md',ROOT/'src/ledger/20260824-2216 The Contact Packet Has a Fixed-State Mixed Readout.md']
def hashes():return {p.relative_to(ROOT).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}
before=hashes();text=primary.read_text(encoding='utf-8');labels=['eq:PD1','eq:PD2','eq:Oav','eq:OavP','eq:CC','eq:CC2']
for label in labels:assert '\\eqlabel{'+label+'}' in text
l,g=s.symbols('lambda g',positive=True)
expect=(g+3*l*g*g)/(1+l*g)
coefficient=s.simplify(s.diff(expect,l).subs(l,0))
assert coefficient==2*g*g
assert s.simplify(g*s.diff(coefficient,g))==4*g*g
assert 3*g*g-g*g==coefficient
assert g*s.diff(3*g*g,g)==6*g*g
assert s.Rational(2,3)*3*g*g==coefficient
# Same expectation family does not identify the physical observable or its L2 norm.
physical_norm2=3*g*g;moment_lift_norm2=s.Rational(4,9)*105*g**4
assert physical_norm2.subs(g,1)!=moment_lift_norm2.subs(g,1)
assert before==hashes()
report={'passed':True,'source_unchanged':True,'source_sha256':before,'primary_equation_labels_present':labels,'normalized_first_coefficient':str(coefficient),'unnormalized_insertion':'3*g**2','normalized_log_covariance_response':'4*g**2','physical_observable_norm_squared_at_g1':3,'moment_lift_norm_squared_at_g1':'140/3','scope':'Primary source defines the field-product observable; no operator-level contact-normal lift or physical norm equivalence is certified.'}
(HERE/'contact-primary-operator-typing.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
print(json.dumps(report,indent=2))
