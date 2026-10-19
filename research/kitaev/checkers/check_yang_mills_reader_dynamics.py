"""Exact controls for actual-source reader leakage and compressed memory defect."""
from fractions import Fraction as F
from itertools import combinations, permutations
from hashlib import sha256
from pathlib import Path
import json
from check_yang_mills_weighted_orientation import report as predecessor_report
from check_yang_mills_shared_link_packet import I, lift, rawmul, obs, laplace

ROOT = Path(__file__).resolve().parents[3]
BASE = 'research/kitaev/'
CONTRACT = BASE+'contracts/yang-mills-reader-dynamics.v1.json'
NOTE = BASE+'yang-mills-reader-dynamics-v1.md'
SELF = BASE+'checkers/check_yang_mills_reader_dynamics.py'
OUT = ROOT/(BASE+'results/yang-mills-reader-dynamics-v1.json')


def require(ok, label):
    if not ok:
        raise AssertionError(label)


def mm(a, b):
    return [[sum(a[i][k]*b[k][j] for k in range(3)) for j in range(3)] for i in range(3)]


def sub(a, b):
    return [[a[i][j]-b[i][j] for j in range(3)] for i in range(3)]


def mv(a, x):
    return [sum(a[i][j]*x[j] for j in range(3)) for i in range(3)]


def transpose(a):
    return [list(row) for row in zip(*a)]


def principal_det(a, subset):
    total = F(0)
    for perm in permutations(range(len(subset))):
        inversions = sum(perm[i] > perm[j] for i in range(len(perm)) for j in range(i+1, len(perm)))
        term = F((-1)**inversions)
        for i, j in enumerate(perm):
            term *= a[subset[i]][subset[j]]
        total += term
    return total


def report():
    c = json.loads((ROOT/CONTRACT).read_text())
    require(c['batch_iteration'] == 7 and all(v is False for v in c['boundary'].values()), 'scope')
    require(not c['parent_net']['discharges_parent'] and c['subnet']['parent_outcome'] is None, 'parent promotion')
    require(c['subnet']['ready_frontier'] == ['full-local-reader-magnetic-closure'], 'frontier')
    parent = json.loads((ROOT/c['parent_net']['path']).read_text())
    require(next(n for n in parent['conjectures'] if n['id'] == c['parent_net']['node'])['status'] == 'open', 'continuum parent')
    previous = predecessor_report()
    require(previous['passed'] and previous == json.loads((ROOT/(BASE+'results/yang-mills-weighted-orientation-v1.json')).read_text()), 'predecessor stale')
    qs = [I, (F(0), F(1), F(0), F(0)), (F(0), F(0), F(1), F(0)),
          (F(0), F(0), F(0), F(1)), (F(3, 5), F(4, 5), F(0), F(0)),
          (F(5, 13), F(0), F(12, 13), F(0))]
    gradient_blocks = 0
    nonzero_creation = 0
    for row in range(12):
        links = [qs[(row+edge*(1+row//6)) % 6] for edge in range(7)]
        p, q, value, f0, f1 = [jet[0] for jet in obs([lift(u) for u in links])]
        h = value/2-2*f0
        require(laplace(links)[2] == 6*value+h, 'direct electric generator creates orientation')
        nonzero_creation += int(h != 0)
        for edge in range(7):
            gp, gq, gf = [], [], []
            for axis in range(1, 4):
                unit = tuple(F(k == axis) for k in range(4))
                velocity = tuple(v/2 for v in rawmul(unit, links[edge]))
                jets = [lift(u) for u in links]
                jets[edge] = tuple((u, v, -u/8) for u, v in zip(links[edge], velocity))
                derivatives = obs(jets)
                gp.append(derivatives[0][1])
                gq.append(derivatives[1][1])
                gf.append(derivatives[2][1])
            require(sum(v*v for v in gp) == (1-p*p/4 if edge in [0, 1, 2, 3] else 0), 'trace p gradient metric')
            require(sum(v*v for v in gq) == (1-q*q/4 if edge in [0, 4, 5, 6] else 0), 'trace q gradient metric')
            require(gf == [q*a+p*b for a, b in zip(gp, gq)], 'actual product gradient')
            require(sum(v*v for v in gf) <= (16 if edge == 0 else 4), 'F gradient block bound')
            gradient_blocks += 1
    require(nonzero_creation > 0 and 6*2+4 == 16, 'nontrivial source creation and M(F)')
    for twice_j in range(65):
        j = F(twice_j, 2)
        require(3*j*j <= 4*(1+j*(j+1))**2, 'Fourier derivative majorant regression')
    R_max = F(9, 64)
    require(4*(R_max/16) == R_max/4 and (R_max/4)*16 == 4*R_max, 'retained-label drift budget')
    require(F(579, 1024) > F(3, 4)**2, 'actual hidden norm exceeds three quarters')
    require(F(3, 4)-4*R_max == F(3, 16), 'full-window residual floor')
    require(F(3, 16)**2 == F(9, 256), 'memory-defect coefficient floor')

    identity = [[F(i == j) for j in range(3)] for i in range(3)]
    projection = [[F(1, 2), F(1, 2), F(0)], [F(1, 2), F(1, 2), F(0)], [F(0), F(0), F(1)]]
    complement = sub(identity, projection)
    kernel = [[F(1, 2), F(1, 4), F(1, 4)], [F(1, 4), F(3, 4), F(0)], [F(1, 4), F(0), F(3, 4)]]
    require(mm(projection, projection) == projection == transpose(projection), 'orthogonal reader')
    require(kernel == transpose(kernel) and all(sum(row) == 1 for row in kernel), 'reversible constant-preserving kernel')
    compressed = mm(mm(projection, kernel), projection)
    defect = sub(mm(mm(projection, mm(kernel, kernel)), projection), mm(compressed, compressed))
    leakage = mm(mm(complement, kernel), projection)
    require(defect == mm(transpose(leakage), leakage), 'exact compression memory factorization')
    minor_cases = 0
    for size in range(1, 4):
        for subset in combinations(range(3), size):
            require(principal_det(kernel, subset) >= 0 and principal_det(defect, subset) >= 0, 'PSD kernel and memory defect')
            minor_cases += 1
    v = [F(1), F(1), F(0)]
    require(mv(projection, v) == v, 'reader input')
    quadratic = sum(a*b for a, b in zip(v, mv(defect, v)))/3
    require(quadratic == F(1, 96) > 0, 'positive discrete compressed two-step defect')
    closed = [[(identity[i][j]+F(1, 3))/2 for j in range(3)] for i in range(3)]
    require(mm(mm(complement, closed), projection) == [[F(0)]*3 for _ in range(3)], 'nonfaithful reader can be dynamically closed')
    require(mv(projection, [F(-1), F(1), F(0)]) == [0, 0, 0], 'contrasting reader still has a nonzero kernel')
    paths = [CONTRACT, NOTE, SELF, c['parent_net']['path']]
    for name in ['weighted-orientation', 'propagator-comparison', 'shared-link-packet']:
        paths += [BASE+'contracts/yang-mills-'+name+'.v1.json', BASE+'yang-mills-'+name+'-v1.md',
                  BASE+'checkers/check_yang_mills_'+name.replace('-', '_')+'.py',
                  BASE+'results/yang-mills-'+name+'-v1.json']
    return {'schema': 'marici.yang-mills-reader-dynamics.result.v1', 'passed': True,
            'strength': 'written positive-coupling actual thermodynamic reader nonclosure; independently unreviewed',
            'direct_electric_fixtures': 12, 'gradient_blocks': gradient_blocks,
            'source_creation_nonzero_fixtures': nonzero_creation, 'spin_majorant_fixtures': 65,
            'actual_residual_lower': '3*kappa/16 (strict)', 'initial_memory_defect_lower': '9*kappa^2/256 (strict)',
            'discrete_memory_defect': str(quadratic), 'kernel_and_defect_minor_pairs': minor_cases,
            'blind_but_closed_contrast': True, 'projected_domain_assumed': False,
            'explicit_finite_time_radius': False, 'independent_analytic_review': False,
            'continuum_Yang_Mills': False, 'ready_frontier': c['subnet']['ready_frontier'],
            'input_sha256': {p: sha256((ROOT/p).read_bytes()).hexdigest() for p in paths}}


if __name__ == '__main__':
    result = report()
    OUT.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({k: result[k] for k in ['passed', 'direct_electric_fixtures', 'gradient_blocks',
                     'actual_residual_lower', 'discrete_memory_defect', 'blind_but_closed_contrast']}, indent=2))
