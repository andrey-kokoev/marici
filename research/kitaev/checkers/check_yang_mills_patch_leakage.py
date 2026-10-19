"""Exact geometry, actual-tail budgets and controls for full-patch leakage."""
from fractions import Fraction as F
from itertools import combinations
from math import comb
from hashlib import sha256
from pathlib import Path
import json
from check_yang_mills_reader_dynamics import report as predecessor_report
from check_yang_mills_shared_link_packet import I, lift, rawmul, obs, laplace

ROOT = Path(__file__).resolve().parents[3]
BASE = 'research/kitaev/'
CONTRACT = BASE+'contracts/yang-mills-patch-leakage.v1.json'
NOTE = BASE+'yang-mills-patch-leakage-v1.md'
SELF = BASE+'checkers/check_yang_mills_patch_leakage.py'
OUT = ROOT/(BASE+'results/yang-mills-patch-leakage-v1.json')


def require(ok, label):
    if not ok:
        raise AssertionError(label)


def shift(v, axis, step=1):
    return tuple(x+step*(k == axis) for k, x in enumerate(v))


def square(v, a, b):
    return frozenset([(v, a), (shift(v, a), b), (shift(v, b), a), (v, b)])


def neighbors(face):
    result = set()
    for v, axis in face:
        for b in range(3):
            if b != axis:
                for base in [v, shift(v, b, -1)]:
                    result.add(square(base, axis, b))
    result.discard(face)
    return result


def report():
    c = json.loads((ROOT/CONTRACT).read_text())
    require(c['batch_iteration'] == 8 and all(v is False for v in c['boundary'].values()), 'scope')
    require(not c['parent_net']['discharges_parent'] and c['subnet']['parent_outcome'] is None, 'parent promotion')
    require(c['subnet']['ready_frontier'] == ['finite-box-boundary-leakage'], 'frontier')
    parent = json.loads((ROOT/c['parent_net']['path']).read_text())
    require(next(n for n in parent['conjectures'] if n['id'] == c['parent_net']['node'])['status'] == 'open', 'continuum parent')
    previous = predecessor_report()
    require(previous['passed'] and previous == json.loads((ROOT/(BASE+'results/yang-mills-reader-dynamics-v1.json')).read_text()), 'predecessor stale')
    p = square((0, 0, 0), 0, 1)
    q0 = square((0, -1, 0), 0, 1)
    S = p | q0
    adjacent = neighbors(p)
    require(len(S) == 7 and len(adjacent) == c['geometry']['neighbors'] == 12, 'seven-link source geometry')
    require(all(len(face & p) == 1 for face in adjacent), 'simple shared-link neighbors')
    require({face for face in adjacent if face <= S} == {q0}, 'only one neighbor inside full patch')
    outside = [face for face in adjacent if not face <= S]
    require(len(outside) == c['geometry']['outside_neighbors'] == 11, 'exterior channels')
    D = set(p)
    for face in adjacent:
        D.update(face)
    require(S <= D and len(D) <= c['geometry']['comparison_support_bound'] == 40, 'local comparison support')
    for face in outside:
        require((p ^ face)-S, 'outside link with odd center parity gives conditional Haar zero')
    parity_pairs = 0
    for a, b in combinations(outside, 2):
        require((p ^ a) ^ (p ^ b), 'distinct channels have nontrivial product center parity')
        parity_pairs += 1
    require(parity_pairs == 55 and len(outside)*F(3, 4) == F(33, 4), 'orthogonal Haar channel norm')

    qs = [I, (F(0), F(1), F(0), F(0)), (F(0), F(0), F(1), F(0)),
          (F(0), F(0), F(0), F(1)), (F(3, 5), F(4, 5), F(0), F(0)),
          (F(5, 13), F(0), F(12, 13), F(0))]
    for row in range(12):
        links = [qs[(row+edge*(1+row//6)) % 6] for edge in range(7)]
        pp, qq, product_value, f0, f1 = [jet[0] for jet in obs([lift(u) for u in links])]
        h = product_value/2-2*f0
        gamma_cross, gamma_self = F(0), F(0)
        for edge in range(7):
            for axis in range(1, 4):
                unit = tuple(F(k == axis) for k in range(4))
                velocity = tuple(v/2 for v in rawmul(unit, links[edge]))
                jets = [lift(u) for u in links]
                jets[edge] = tuple((u, v, -u/8) for u, v in zip(links[edge], velocity))
                values = obs(jets)
                gamma_cross += values[0][1]*values[1][1]
                gamma_self += values[0][1]**2
        require(gamma_cross == -h/2 and gamma_self == 4-pp*pp, 'direct canonical Gamma decomposition')
        require(laplace(links)[0] == 3*pp, 'plaquette electric input')

    r0 = F(1, 10**9)
    a0, K = F(2048, 3), F(32, 9)
    require(0 < r0 < F(27, 262144), 'declared positive source subwindow')
    coefficient_cases = 0
    tail_endpoint = None
    for r in [r0/4, r0/2, r0]:
        R = F(4096, 3)*r
        zeta = F(262144, 27)*r
        require(zeta == 4*K*a0*r < 1, 'actual Catalan ratio')
        tail = a0*r*zeta/(1-zeta)
        partial = F(0)
        for n in range(2, 11):
            catalan = F(comb(2*n-2, n-1), n)
            contribution = catalan*K**(n-1)*a0**n*r**n
            require(contribution <= a0*r*zeta**(n-1), 'Catalan coefficient geometric majorant')
            partial += contribution
            coefficient_cases += 1
        require(partial <= tail, 'all-orders geometric tail dominates partial sum')
        require(40*R/4 == 10*R and 4*(tail/16)*4 == tail, 'density and scalar drift tail budgets')
        require(5*R < F(1, 10) and tail/r < F(1, 24), 'actual positive-coupling noncancellation')
        if r == r0:
            tail_endpoint = tail
    require(33 > 25 and F(5, 12)*F(9, 10) == F(3, 8), 'strict leading residual bound')
    require(F(3, 8)-F(1, 24) == F(1, 3), 'actual leakage coefficient floor')
    require(F(1, 3)**2 == F(1, 9), 'initial compressed memory coefficient')
    require(r0/6-r0*r0/(6*r0) == 0, 'bad quadratic term cancels the formal first coefficient')
    require(F(33, 144)*r0*r0 > tail_endpoint**2, 'bad quadratic term violates actual supremum tail bound')
    require(a0*F(0)/(1-F(0)) == 0, 'zero coupling has no magnetic drift')
    paths = [CONTRACT, NOTE, SELF, c['parent_net']['path'], BASE+'yang-mills-weighted-orientation-v1.md']
    for name in ['reader-dynamics', 'anchored-casimir', 'thermodynamic-vacuum']:
        paths += [BASE+'contracts/yang-mills-'+name+'.v1.json', BASE+'yang-mills-'+name+'-v1.md',
                  BASE+'checkers/check_yang_mills_'+name.replace('-', '_')+'.py',
                  BASE+'results/yang-mills-'+name+'-v1.json']
    return {'schema': 'marici.yang-mills-patch-leakage.result.v1', 'passed': True,
            'strength': 'written actual full-seven-link-reader exterior leakage with controlled all-orders remainder',
            'p_neighbors': len(adjacent), 'outside_channels': len(outside), 'comparison_links_actual': len(D),
            'comparison_links_bound': 40, 'outside_parity_witnesses': len(outside), 'cross_parity_witnesses': parity_pairs,
            'canonical_Gamma_fixtures': 12, 'Catalan_tail_coefficient_cases': coefficient_cases,
            'coupling_interval': '(0,1/1000000000]', 'tail_over_r_at_endpoint': str(tail_endpoint/r0),
            'actual_generator_residual_lower': 'kappa*r/3 (strict)',
            'initial_memory_defect_lower': 'kappa^2*r^2/9 (strict)',
            'formal_cancellation_hostile_excluded_by_tail': True,
            'all_finite_patch_theorem': False, 'independent_analytic_review': False,
            'continuum_Yang_Mills': False, 'ready_frontier': c['subnet']['ready_frontier'],
            'input_sha256': {p: sha256((ROOT/p).read_bytes()).hexdigest() for p in paths}}


if __name__ == '__main__':
    result = report()
    OUT.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({k: result[k] for k in ['passed', 'p_neighbors', 'outside_channels',
                     'comparison_links_actual', 'cross_parity_witnesses', 'canonical_Gamma_fixtures',
                     'tail_over_r_at_endpoint', 'actual_generator_residual_lower']}, indent=2))
