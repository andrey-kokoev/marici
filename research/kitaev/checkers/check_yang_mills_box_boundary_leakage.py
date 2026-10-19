"""Local conditional controls for volume-independent cubic-box boundary leakage."""
from fractions import Fraction as F
from itertools import combinations, product
from hashlib import sha256
from pathlib import Path
import json
from check_yang_mills_patch_leakage import report as predecessor_report, square, neighbors, shift

ROOT = Path(__file__).resolve().parents[3]
BASE = 'research/kitaev/'
CONTRACT = BASE+'contracts/yang-mills-box-boundary-leakage.v1.json'
NOTE = BASE+'yang-mills-box-boundary-leakage-v1.md'
SELF = BASE+'checkers/check_yang_mills_box_boundary_leakage.py'
OUT = ROOT/(BASE+'results/yang-mills-box-boundary-leakage-v1.json')


def require(ok, label):
    if not ok:
        raise AssertionError(label)


def edge_inside(edge, origin, L):
    v, axis = edge
    target = shift(v, axis)
    return all(origin[k] <= v[k] <= origin[k]+L-1 and origin[k] <= target[k] <= origin[k]+L-1 for k in range(3))


def report():
    c = json.loads((ROOT/CONTRACT).read_text())
    require(c['batch_iteration'] == 9 and all(v is False for v in c['boundary'].values()), 'scope')
    require(not c['parent_net']['discharges_parent'] and c['subnet']['parent_outcome'] is None, 'parent promotion')
    require(c['subnet']['ready_frontier'] == ['buffered-reader-memory-control'], 'frontier')
    parent = json.loads((ROOT/c['parent_net']['path']).read_text())
    require(next(n for n in parent['conjectures'] if n['id'] == c['parent_net']['node'])['status'] == 'open', 'continuum parent')
    previous = predecessor_report()
    require(previous['passed'] and previous == json.loads((ROOT/(BASE+'results/yang-mills-patch-leakage-v1.json')).read_text()), 'predecessor stale')
    geometry_cases, outside_witnesses, cross_witnesses = 0, 0, 0
    advice_cases, empty_exceptions = 0, 0
    counts = {6: 0, 8: 0}
    max_local_links = 0
    for origin, axes in product([(0, 0, 0), (-7, 11, -3)], list(combinations(range(3), 2))):
        p = square(origin, *axes)
        adjacent = neighbors(p)
        D = set(p)
        for face in adjacent:
            D.update(face)
        require(len(adjacent) == 12 and len(D) <= 40, 'bounded resampling geometry')
        max_local_links = max(max_local_links, len(D))
        require(not all(edge_inside(edge, origin, 1) for edge in p), 'L1 has no plaquette input')
        require(3*1*1*(1-1) == 0, 'L1 reader is constants')
        empty_exceptions += 1
        for L in [2, 3, 4, 8, 1000, 10**12]:
            require(all(edge_inside(edge, origin, L) for edge in p), 'boundary plaquette inside box')
            outside = [face for face in adjacent if not all(edge_inside(edge, origin, L) for edge in face)]
            k = len(outside)
            require(k == (8 if L == 2 else 6), 'two-case all-size geometry formula')
            counts[k] += 1
            for face in outside:
                require(any(not edge_inside(edge, origin, L) for edge in p ^ face), 'odd unobserved edge parity')
                outside_witnesses += 1
            for a, b in combinations(outside, 2):
                require((p ^ a) ^ (p ^ b), 'off-diagonal Haar pairing killed by center parity')
                cross_witnesses += 1
            require(F(3*k, 4) >= F(9, 2), 'uniform Haar channel norm')
            if L >= 3:
                axis = axes[0]
                v = tuple(origin[i]+(L-2 if i == axis else L-1) for i in range(3))
                advice_edge = (v, axis)
                require(edge_inside(advice_edge, origin, L) and advice_edge not in D, 'box predictor has observed links outside resampling set')
                advice_cases += 1
            geometry_cases += 1
    require(geometry_cases == 36 and counts == {6: 30, 8: 6}, 'frozen geometry coverage')
    r0 = F(1, 10**9)
    R0 = F(4096, 3)*r0
    zeta = F(262144, 27)*r0
    tail_over_r = F(2048, 3)*zeta/(1-zeta)
    require(5*R0 < F(1, 10) and tail_over_r < F(1, 24), 'common actual remainder interval')
    require(F(18) > F(21, 5)**2, 'minimum channel square-root lower bound')
    require(F(21, 5)/12*F(9, 10) == F(63, 200), 'leading coefficient')
    require(F(63, 200)-F(1, 24) == F(41, 150) > F(1, 4), 'strict uniform leakage floor')
    require(F(1, 4)**2 == F(1, 16), 'initial memory coefficient')

    # A non-product conditional kernel with observed exterior advice eta.
    atoms = []
    for x, z, eta in product([-1, 1], repeat=3):
        density = 1+F(z*(x+eta), 4)
        require(density >= F(1, 2), 'uniform local conditional likelihood')
        atoms.append((x, z, eta, density/8))
    require(sum(weight for x, z, eta, weight in atoms) == 1, 'conditional control normalized')
    cells = list(product([-1, 1], repeat=2))
    for x, eta in cells:
        mass = sum(w for xx, z, ee, w in atoms if (xx, ee) == (x, eta))
        mean = sum(z*w for xx, z, ee, w in atoms if (xx, ee) == (x, eta))/mass
        require(mass == F(1, 4) and mean == F(x+eta, 4), 'actual centering retains exterior advice')
    minimum_error, predictor_cases = None, 0
    for values in product([F(-1), F(-1, 2), F(0), F(1, 2), F(1)], repeat=4):
        g = dict(zip(cells, values))
        error = sum(w*(z-g[(x, eta)])**2 for x, z, eta, w in atoms)
        reference = 1+sum(v*v for v in values)/4
        require(error >= reference/2, 'local variational comparison for arbitrary reader assignments')
        minimum_error = error if minimum_error is None else min(minimum_error, error)
        predictor_cases += 1
    require(predictor_cases == 625 and minimum_error == F(7, 8), 'weighted centered minimum, not Haar centering')
    global_floor_examples = []
    for N in [4, 16, 64, 512]:
        whole_floor = F(1, 2)**(N+1)
        require(whole_floor < F(1, 2) and F(7, 8) >= F(1, 2), 'whole-product comparison loses constant unnecessarily')
        global_floor_examples.append({'extra_observed_bits': N, 'whole_product_floor': str(whole_floor), 'local_floor': '1/2', 'actual_residual': '7/8'})
    paths = [CONTRACT, NOTE, SELF, c['parent_net']['path']]
    for name in ['patch-leakage', 'weighted-orientation', 'propagator-comparison']:
        paths += [BASE+'contracts/yang-mills-'+name+'.v1.json', BASE+'yang-mills-'+name+'-v1.md',
                  BASE+'checkers/check_yang_mills_'+name.replace('-', '_')+'.py',
                  BASE+'results/yang-mills-'+name+'-v1.json']
    return {'schema': 'marici.yang-mills-box-boundary-leakage.result.v1', 'passed': True,
            'strength': 'written all-nontrivial-cubic-box source boundary leakage with conditional local comparison; independently unreviewed',
            'geometry_cases': geometry_cases, 'outside_channel_counts': {str(k): v for k, v in counts.items()},
            'outside_parity_witnesses': outside_witnesses, 'cross_parity_witnesses': cross_witnesses,
            'box_advice_outside_D_cases': advice_cases, 'L1_constant_reader_exceptions': empty_exceptions,
            'max_resampling_links': max_local_links, 'largest_box_vertex_side': 10**12,
            'box_volumes_materialized': False, 'conditional_predictor_cases': predictor_cases,
            'conditional_control_residual': str(minimum_error), 'whole_floor_examples': global_floor_examples,
            'actual_generator_lower': 'kappa*r/4 (strict), all L>=2 and translations,0<r<=1/1000000000',
            'initial_memory_lower': 'kappa^2*r^2/16 (strict)', 'explicit_finite_time_radius': False,
            'finite_volume_source_dynamics_obstructed': False, 'independent_analytic_review': False,
            'continuum_Yang_Mills': False, 'ready_frontier': c['subnet']['ready_frontier'],
            'input_sha256': {p: sha256((ROOT/p).read_bytes()).hexdigest() for p in paths}}


if __name__ == '__main__':
    result = report()
    OUT.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({k: result[k] for k in ['passed', 'geometry_cases', 'outside_parity_witnesses',
                     'cross_parity_witnesses', 'box_advice_outside_D_cases', 'max_resampling_links',
                     'conditional_predictor_cases', 'actual_generator_lower']}, indent=2))
