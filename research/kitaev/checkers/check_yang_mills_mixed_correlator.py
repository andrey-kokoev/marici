"""Exact coefficient/analytic/boundary budgets; no huge box is materialized."""
from fractions import Fraction as F
from itertools import combinations, product
from pathlib import Path
from hashlib import sha256
import json
from check_yang_mills_source_clustering import report as clustering_report
from check_yang_mills_linked_density import report as linked_report
from check_yang_mills_ground_state_transfer import box

ROOT = Path(__file__).resolve().parents[3]
BASE = 'research/kitaev/'
CONTRACT = BASE+'contracts/yang-mills-mixed-correlator.v1.json'
NOTE = BASE+'yang-mills-mixed-correlator-v1.md'
SELF = BASE+'checkers/check_yang_mills_mixed_correlator.py'
OUT = ROOT/(BASE+'results/yang-mills-mixed-correlator-v1.json')


def require(ok, label):
    if not ok:
        raise AssertionError(label)


def report():
    c = json.loads((ROOT/CONTRACT).read_text())
    require(c['batch_iteration'] == 5 and all(v is False for v in c['boundary'].values()), 'scope')
    require(not c['parent_net']['discharges_parent'] and c['subnet']['parent_outcome'] is None, 'parent promotion')
    require(c['subnet']['ready_frontier'] == ['actual-ground-weighted-orientation-readout'], 'frontier')
    parent = json.loads((ROOT/c['parent_net']['path']).read_text())
    require(next(n for n in parent['conjectures'] if n['id'] == c['parent_net']['node'])['status'] == 'open', 'continuum root')
    for name, fn in [('source-clustering', clustering_report), ('linked-density', linked_report)]:
        actual = fn()
        require(actual['passed'] and actual == json.loads((ROOT/(BASE+'results/yang-mills-'+name+'-v1.json')).read_text()), name+' stale')
    quaternions = [tuple(F(sign*(i == axis)) for i in range(4)) for axis in range(4) for sign in [-1, 1]]
    moments = {'F_squared': F(0), 'F0_squared': F(0), 'F1_squared': F(0), 'F0F1': F(0), 'FJ': F(0)}
    for x, y in product(quaternions, repeat=2):
        value = 4*x[0]*y[0]
        f0 = sum(v*w for v, w in zip(x, y))
        f1 = value-f0
        j = f0/54-f1/234
        vals = [value*value, f0*f0, f1*f1, f0*f1, value*j]
        for key, val in zip(moments, vals):
            moments[key] += val/64
    require(moments == {'F_squared': F(1), 'F0_squared': F(1, 4), 'F1_squared': F(3, 4), 'F0F1': F(0), 'FJ': F(1, 702)}, 'actual pair Haar channel moments')
    require(F(1, 216)-F(1, 312) == F(1, 702), 'pair coefficient')
    require(F(1, 9)+moments['FJ'] == F(79, 702), 'pq expectation coefficient before connected subtraction')
    require(2*F(1, 36)-F(1, 18) == 0 != moments['FJ'], 'independent-atom shortcut misses covariance')
    parity_cases = 0
    boxes = []
    for side in [2, 3]:
        vertices, edges, faces = box(side)
        masks = [sum(1 << edge for edge, sign in face) for face in faces]
        for size in range(1, 5):
            for chosen in combinations(masks, size):
                boundary = 0
                for mask in chosen:
                    boundary ^= mask
                require(boundary != 0, 'unexpected <=4-face cubical parity cycle')
                parity_cases += 1
        boxes.append({'L': side, 'E': len(edges), 'P': len(faces)})

    n = c['parameters']['n']
    require(n == 512, 'frozen witness exponent')
    d = 4*n
    M = d+2
    L = 2*M+1
    E = 3*L*L*(L-1)
    require(d == c['parameters']['buffer'] and L == c['parameters']['box_L'] and E == c['parameters']['box_E'], 'comparison geometry/count')
    require(M-2 == d, 'coordinate buffer lemma arithmetic')
    r_star = F(3, 4)**n
    r_low = r_star/2
    eta = F(3, 131072*E)
    require(0 < r_low < r_star < F(27, 262144), 'source coupling interval')
    require(E*F(4096, 3)*eta == F(1, 32), 'finite complex log-vacuum norm')
    require(F(262144, 27)*eta == F(2, 9*E) < 1, 'complex contraction disk')
    require(1/(1-F(1, 16)) == F(16, 15), 'exponential rational majorant')
    require(1-F(1, 15) == F(14, 15), 'partition denominator lower bound')
    require(F(32, 7)+F(16, 7)**2 == F(480, 49) < 10, 'analytic covariance bound')
    require(r_star <= eta/2, 'Cauchy tail regime')
    require(r_star <= eta**3/56160, 'uniform interval analytic error budget')
    B = F(8, 7)*(64+2*16+2*16)
    require(B == F(1024, 7), 'covariance thermodynamic error')
    require(F(3, 4)**d == r_star**4, 'matched boundary/coupling powers')
    require(B*r_star*r_star <= F(1, 11232), 'uniform interval boundary budget')
    require(20*r_star/eta**3 <= F(1, 2808), 'analytic error relative to r squared')
    require(B*r_star**4 <= r_low*r_low/2808, 'boundary error at smallest interval r')
    require(F(1, 702)-2*F(1, 2808) == F(1, 1404), 'positive lower coefficient')
    require(F(1, 702)+2*F(1, 2808) == F(3, 1404), 'upper coefficient')

    bad_cubic = 1/(351*r_star)
    bad_value = r_star*r_star/702-bad_cubic*r_star**3
    require(bad_value == -r_star*r_star/702 < 0, 'same leading coefficient without remainder flips sign')
    require(bad_cubic*eta**3 > 10, 'sign-flip hostile violates actual Cauchy majorant')
    normalization_hostiles = []
    for N in [1, 2, 16, 256]:
        # Omega(z)=(1+Nz,1-Nz), normalized Haar on two points.
        # Z(z)=1+N^2 z^2; evaluate at symbolic z=i/N without floats.
        require(1+N*N*F(-1, N*N) == 0, 'entire numerator normalization zero')
        require(1+N*N*r_star*r_star > 0, 'real positivity does not exclude complex zero')
        normalization_hostiles.append({'N': N, 'complex_zero': 'i/'+str(N)})
    inputs = [CONTRACT, NOTE, SELF, BASE+'contracts/yang-mills-gap-net.v1.json']
    for name in ['source-clustering', 'linked-density', 'anchored-casimir', 'thermodynamic-vacuum']:
        inputs += [BASE+'contracts/yang-mills-'+name+'.v1.json', BASE+'yang-mills-'+name+'-v1.md',
                   BASE+'checkers/check_yang_mills_'+name.replace('-', '_')+'.py',
                   BASE+'results/yang-mills-'+name+'-v1.json']
    return {'schema': 'marici.yang-mills-mixed-correlator.result.v1', 'passed': True,
            'strength': 'written actual-source nonproduct witness with exact coefficient/Cauchy/boundary budgets',
            'Haar_pair_cases': 64, 'Haar_channel_moments': {k: str(v) for k, v in moments.items()},
            'bounded_parity_cases': parity_cases, 'parity_fixture_boxes': boxes,
            'comparison_box_E': E, 'comparison_box_materialized': False,
            'r_star': '(3/4)^512', 'interval': '[r_star/2,r_star]',
            'eta': str(eta), 'lower_covariance': 'r^2/1404', 'upper_covariance': '3*r^2/1404',
            'interval_analytic_budget_exact': True, 'interval_boundary_budget_exact': True,
            'sign_flip_hostile': '-r_star^2/702', 'normalization_hostiles': normalization_hostiles,
            'independent_analytic_review': False, 'continuum_interaction_or_Yang_Mills': False,
            'ready_frontier': c['subnet']['ready_frontier'],
            'input_sha256': {p: sha256((ROOT/p).read_bytes()).hexdigest() for p in inputs}}


if __name__ == '__main__':
    result = report()
    OUT.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({k: result[k] for k in ['passed', 'Haar_pair_cases', 'bounded_parity_cases',
                     'comparison_box_E', 'comparison_box_materialized', 'interval_analytic_budget_exact',
                     'interval_boundary_budget_exact', 'lower_covariance']}, indent=2))
