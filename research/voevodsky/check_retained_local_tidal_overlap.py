"""Audit retained source/reference data and the calibrated-refinement hostile.
Universal equivalence/obstruction results are Agda proofs, not sampling claims.
"""
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json
base=Path(__file__).resolve().parent
formal_path=base/'retained-local-tidal-overlap-formal.json'
formal=json.loads(formal_path.read_text())
checks={}
checks['fresh_formal_closure']=formal['passed'] and formal['fresh'] and formal['retained_overlap_mode']
checks['both_intended_rejections']=len(formal['results'])==3 and all(r['passed'] for r in formal['results']) and sum(r['expected_rejection'] for r in formal['results'])==2
checks['proof_dependencies_current']=all(Path(p).exists() and hashlib.sha256(Path(p).read_bytes()).hexdigest()==h for p,h in formal['source_snapshot_hashes'].items())
checks['checker_current']=hashlib.sha256((base/'check_native_radar_formal.py').read_bytes()).hexdigest()==formal['checker_sha256']
reference=base/'source-anchored-tidal-overlap-is-local-and-stops-at-the-next-jet.md'
digest='9e7fb956af22885ab81855b752c2f786af67dcd92ac6584908b14fee856cca80'
checks['retained_analytic_reference_current']=hashlib.sha256(reference.read_bytes()).hexdigest()==digest
D=13824
E=(-432,0,0,0,432,0,0,0,0)
newton=E+(-144,);rosen=E+(0,)
checks['shared_electric_reading']=tuple(F(n,D) for n in E)==(F(-1,32),0,0,0,F(1,32),0,0,0,0)
checks['source_third_derivative_normalized']=F(newton[-1],D)==F(-1,96)
checks['newton_derivative_crosscheck']=6*36*D==144*12**4
checks['distinct_refined_readings']=newton!=rosen
checks['coarse_projection_agrees']=newton[:-1]==rosen[:-1]
# Source distinction is retained separately; no test replaces analytic admission.
source_packets=[dict(sector='newtonian',declaration={'masses':[36,18],'radii':[12,12],'directions':['x','z']},
  context={'jet_denominator':1728,'affine_value_numerator':7776,'affine_gradient_numerators':[432,0,216],'controlled_radius':1,'taylor_bound':'216/14641'}),
 dict(sector='rosen',declaration={'shape':'cosh/cos','a_denominator':4},
  context={'proper_clock_square_denominator':2,'u_domain':[-1,2],'epsilon_power_of_h':4,'sigma_power_of_h':8})]
for packet in source_packets:
    packet['analytic_reference']={'path':str(reference.relative_to(base.parent.parent)),'sha256':digest,'status':'written analytic derivation, not compiler-proved continuum physics'}
    packet['observation_profile']={'channel':'electric corner','denominator':D,'frame':'fixed nonrotating xyz at corner','finite_radar_equals_corner':False}
checks['different_source_records']=source_packets[0]!=source_packets[1]
checks['different_calibration_contexts']=source_packets[0]['context']!=source_packets[1]['context']
checks['same_observation_profile']=source_packets[0]['observation_profile']==source_packets[1]['observation_profile']
def shift(v):return v[:-1]+(v[-1]+144,)
def unshift(v):return v[:-1]+(v[-1]-144,)
def distance(v,w):return max(abs(a-b) for a,b in zip(v,w))
checks['unrestricted_filler_aligns_marked_values']=shift(newton)==rosen
checks['unrestricted_filler_violates_calibrated_gradient']=shift(newton)[-1]!=newton[-1]
# It is bijective/isometric, NOT a collapse of two points within one carrier.
checks['no_intracarrier_collapse']=shift(newton)!=shift(rosen)
probes=[newton,rosen,tuple(range(10)),tuple(-i for i in range(10)),(999,)*10]
for i,v in enumerate(probes):
    checks[f'inverse_left_{i}']=unshift(shift(v))==v
    checks[f'inverse_right_{i}']=shift(unshift(v))==v
    checks[f'electric_unchanged_{i}']=shift(v)[:-1]==v[:-1]
    for j,w in enumerate(probes):
        checks[f'fixed_coordinate_isometry_{i}_{j}']=distance(shift(v),shift(w))==distance(v,w)
receipt=dict(passed=all(checks.values()),checks=checks,source_packets=source_packets,
    formal_receipt_sha256=hashlib.sha256(formal_path.read_bytes()).hexdigest(),
    result='A retained actual boundary comparison exists over E. An unrestricted refined filler also exists, but none preserving the calibrated gradient channel can align the selected readings. Metric isometry alone does not enforce observation compatibility.',
    scope='Agda proves the finite/typed comparisons, generic admission-parameterized history recovery, isomorphism and refinement obstruction. The concrete citation instance retains written analytic provenance, not a formal proof of field equations.')
(base/'retained-local-tidal-overlap.json').write_text(json.dumps(receipt,indent=2)+'\n')
print('passed=',receipt['passed'],'checks=',len(checks))
raise SystemExit(0 if receipt['passed'] else 1)
