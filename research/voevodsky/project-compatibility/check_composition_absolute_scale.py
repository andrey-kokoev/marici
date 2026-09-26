"""Audit a prior finite composition receipt and the scale-blindness counterexample."""
from pathlib import Path
from fractions import Fraction
import hashlib,json
HERE=Path(__file__).resolve().parent;ROOT=HERE.parents[2]
paths=[Path(__file__),HERE/'composition-reuse-and-absolute-scale-gap.md',ROOT/'research/nima/canonical-coherence-composites-need-depth-independent-condition-bounds.md',ROOT/'research/benincasa/cosmology-boundary-correction-composition-audit.md',ROOT/'research/benincasa/checkers/check_cosmology_boundary_correction_composition_audit.py',ROOT/'research/benincasa/results/cosmology_boundary_correction_composition_audit.json']
def hashes():return {p.relative_to(ROOT).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}
before=hashes();prior=json.loads(paths[-1].read_text(encoding='utf-8'))
assert prior['passed'] and 'single prime' in prior['limitations']
assert [(r['direct_source_rows'],r['composite_source_rows'],r['syzygy_nonzero_coefficients']) for r in prior['results'].values()]==[(40,40,0),(66,66,0)]
def U(a,b):return Fraction(2)**(b-a)
for a in range(9):
 for b in range(9):
  for c in range(9):assert U(b,c)*U(a,b)==U(a,c)
for n in range(17):
 t=U(0,n)
 assert abs(t)*abs(1/t)==1
 assert t*t==4**n
 assert U(n,0)==Fraction(1,2**n)
 # Transported readout compensates expansion exactly, while energy still grows.
 assert Fraction(1,2**n)*t==1
assert before==hashes()
report={'passed':True,'source_unchanged':True,'source_sha256':before,'prior_source_composition':'recorded exact coefficient equality for two lower-edge cases mod32003','prior_source_computation_rerun':False,'scalar_composition_triples':9**3,'scale_controls':17,'condition_number_controls_absolute_scale':False,'all_depth_argument':'T_n=2^n id has kappa=1 and quadratic energy amplification 4^n','physical_source_counterexample_claimed':False,'owner_adoption_claimed':False}
(HERE/'composition-absolute-scale-check.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
print(json.dumps(report,indent=2))
