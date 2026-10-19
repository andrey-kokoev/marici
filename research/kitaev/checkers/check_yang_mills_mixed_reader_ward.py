"""Exact support/Ward/budget controls,not a constructive source-limit prover."""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
from hashlib import sha256
import json
from check_yang_mills_interacting_magnetic_coercivity import report as predecessor_report
from check_yang_mills_free_magnetic_fluctuations import faces, edges

ROOT = Path(__file__).resolve().parents[3]
BASE = 'research/kitaev/'
NAME = 'yang-mills-mixed-reader-ward'
CONTRACT = BASE+'contracts/'+NAME+'.v1.json'
NOTE = BASE+NAME+'-v1.md'
SELF = BASE+'checkers/check_yang_mills_mixed_reader_ward.py'
OUT = ROOT/(BASE+'results/'+NAME+'-v1.json')


def require(ok, why):
    if not ok:
        raise AssertionError(why)


def shell_constant(L):
    c = 2*L+6
    return 6*c**3+36*c*c+216*c+624


def report():
    c = json.loads((ROOT/CONTRACT).read_text())
    require(c['batch'] == {'kind': 'spatial-scaling', 'iteration': 7, 'size': 10}, 'batch scope')
    require(all(v is False for v in c['boundary'].values()), 'no channel/operator/limit promotion')
    require(c['net_update']['ready_frontier'] == ['positive-coupling-critical-mixed-two-point-limit'] and c['net_update']['parent_outcome'] is None, 'executable positive-coupling next test')
    previous = predecessor_report()
    previous_path = BASE+'results/yang-mills-interacting-magnetic-coercivity-v1.json'
    require(previous['passed'] and previous == json.loads((ROOT/previous_path).read_text()), 'fresh frozen predecessor replay')
    counts = {}
    etas = [F(0), F(1, 65536), F(1, 16384)]
    count = 0
    for eta, fs, law in product(etas, [(1, 1, 1, 1), (1, 2, 3, 4), (-2, 0, 1, 3)], [(F(1, 4), F(1, 2), F(1, 4)), (F(1, 6), F(1, 3), F(1, 2))]):
        # Algebraic finite function fixture for support-wise Ward and actual centering.
        anchor = F(sum(fs), 4)
        constant = eta/7
        lhs, defect = [], []
        for x in [-1, 0, 1]:
            redistribution = [eta*x*x/2, -eta*x*x/2, eta*x/2, -eta*x/2]
            r = [eta*x/4+z-constant/4 for z in redistribution]
            require(sum(r) == eta*x-constant, 'component Ward sum includes scalar Haar-centering residue')
            a = sum(f*y for f, y in zip(fs, r))-eta*anchor*x
            b = sum((f-anchor)*y for f, y in zip(fs, r))
            require(a-b == -anchor*constant, 'uncentered identity has a scalar,not an omitted mean')
            lhs.append(a)
            defect.append(b)
        centered_lhs = [a-sum(p*v for p, v in zip(law, lhs)) for a in lhs]
        centered_defect = [a-sum(p*v for p, v in zip(law, defect)) for a in defect]
        require(centered_lhs == centered_defect, 'actual probability centering kills the scalar independently of Haar component means')
        count += 1
    counts['component_Ward_centering_packets'] = count
    count = 0
    plaq_labels = [frozenset(edges(v)) for _, _, v in faces(1)]
    for R, augmented in product([F(1, 64), F(1, 16), F(9, 64)], [False, True]):
        labels = list(plaq_labels)
        if augmented:
            labels += list({a | b for a in plaq_labels for b in plaq_labels if a & b and a != b})
        labels = sorted(labels, key=lambda a: (len(a), sorted(a)))
        raw_weights = [F(1, i+1) for i in range(len(labels))]
        universe = set().union(*labels)
        input_norm = max(sum(2**len(a)*w for a, w in zip(labels, raw_weights) if i in a) for i in universe)
        weights = [R*w/input_norm for w in raw_weights]
        activity = [{e: 2*w/(3*len(a)) for e in a} for a, w in zip(labels, weights)]
        output = {}
        for a, w in zip(labels, weights):
            output[a] = output.get(a, F(0))+w  # kinetic upper majorant
        for ai, a in enumerate(labels):
            for bi, b in enumerate(labels):
                gamma = 3*sum(activity[ai][e]*activity[bi][e] for e in a & b)
                if gamma:
                    output[a | b] = output.get(a | b, F(0))+gamma
        norm = max(sum(2**len(a)*w for a, w in output.items() if i in a) for i in universe)
        require(norm <= R+F(8, 3)*R*R, 'edge-resolved raw electric activity bound,not cardinality times volume')
        count += 1
    counts['anchored_electric_activity_packets'] = count
    count = 0
    first_order_quadratic_defect = None
    for spacing in [F(1), F(1, 2), F(1, 4)]:
        for r, s in [(0, 1), (0, 2), (1, 2)]:
            vertices = next(v for rr, ss, v in faces(1) if (rr, ss) == (r, s) and v[0] == (0, 0, 0))
            midpoints = [tuple(spacing*F(a+b, 2) for a, b in zip(vertices[i], vertices[(i+1) % 4])) for i in range(4)]
            center = tuple(spacing*F(sum(v[j] for v in vertices), 4) for j in range(3))
            for power in [1, 2]:
                discrepancy = sum((x[0]**power for x in midpoints), F(0))/4-center[0]**power
                expected = spacing**2/8 if power == 2 and 0 in (r, s) else F(0)
                require(discrepancy == expected, 'actual first-order r_e=eta/4 sum adjacent w_p does not give exact local cancellation for quadratic weights')
                if spacing == 1 and power == 2 and (r, s) == (0, 1):
                    first_order_quadratic_defect = discrepancy
                count += 1
    counts['first_order_midpoint_defect_packets'] = count
    count = 0
    for n in range(4, 21):
        require(n*n <= 2**n and F((n+1)**2, 2*n*n) <= F(25, 32) < 1, 'reserve half the exponential support weight; induction base4 is exact')
        count += 1
    counts['exponential_support_reserve_packets'] = count
    count = 0
    moments = [2, 2, 6, 26]
    for L in [1, 2, 4, 8]:
        c0 = 2*L+6
        summed = 3*(c0**3*moments[0]+6*c0*c0*moments[1]+12*c0*moments[2]+8*moments[3])
        require(summed == shell_constant(L), 'three orientation shell bound from exact geometric-series moments')
        count += 1
    require(shell_constant(1) == 7728, 'unit-cube shell constant')
    counts['shell_moment_polynomial_packets'] = count
    count = 0
    for spacing, L, N in product([F(1), F(1, 2), F(1, 4)], [1, 2], [1, 2, 4]):
        total = F(0)
        for axis in range(3):
            for n in product(range(-N, N+1), repeat=3):
                x = [spacing*(F(n[i])+F(i == axis, 2)) for i in range(3)]
                distance = max(F(0), max(abs(y) for y in x)-(L+1))
                k = int(distance // spacing)
                total += F(1, 2**k)
        require(total <= shell_constant(L)/spacing**3, 'finite shifted link-grid prefixes respect the volume-independent analytic shell majorant')
        count += 1
    counts['shifted_grid_shell_prefix_packets'] = count
    count = 0
    for beta, d in product([F(0), F(1, 64), F(9, 128)], [(F(1), F(1)), (F(1), F(2)), (F(0), F(1))]):
        quad = (d[0]**2+d[1]**2+2*beta*d[0]*d[1])/(1-beta**2)
        require(quad <= sum(x*x for x in d)/(1-beta), 'symmetric resolvent Schur bound uses l2 oscillations')
        count += 1
    counts['symmetric_covariance_resolvent_packets'] = count
    count = 0
    for eta, z in product(etas, [(1, 1), (10, 1), (1, 10), (-1, -1), (-10, -1)]):
        R = F(4096, 3)*eta
        S = R+F(8, 3)*R*R
        electric, magnetic = z
        m = magnetic+eta*electric
        require(abs(m) == abs(magnetic)+eta*abs(electric) and m != 0, 'same-sign effective coefficient cannot cancel')
        require(abs(electric)*S/abs(m) <= F(5632, 3), 'uniform relative Ward error across small-coupling nets')
        count += 1
    counts['same_sign_relative_budget_packets'] = count
    count = 0
    eta = F(1, 65536)
    R = F(4096, 3)*eta
    S = R+F(8, 3)*R*R
    for N in [2, 4, 8, 16]:
        magnetic = -eta+eta/N**2
        m = eta+magnetic
        relative = F(1, N)*S/abs(m)
        require(magnetic < 0 and m == eta/N**2 and relative == N*S/eta >= F(4096, 3)*N, 'near Ward-null opposite signs destroy the uniform relative-small-error inference')
        count += 1
    counts['near_null_scope_packets'] = count
    count = 0
    for root_Q, epsilon in product([1, 2, 4], [F(0), F(1, 4), F(1, 2)]):
        proxy_filter_norm = F(root_Q, 32)
        error = epsilon*proxy_filter_norm
        mixed_lower = proxy_filter_norm-error
        require(mixed_lower**2 >= F(root_Q**2, 4096), 'filtered triangle inequality transfers actual magnetic growth without requiring absolute vector error0')
        count += 1
    counts['fixed_filter_growth_packets'] = count
    count = 0
    for N, growth in product([2, 4, 8, 16], [0, 1, 2]):
        amplitude, relative = N**growth, F(1, N)
        budget = amplitude*(relative+relative**2)
        if growth == 0:
            require(budget == F(1, N)+F(1, N**2), 'bounded-amplitude joint comparison tends to0')
        elif growth == 2:
            require(budget == N+1, 'relative Ward error0 does not imply absolute two-point comparison at diverging amplitude')
        else:
            require(budget == 1+F(1, N), 'even a constant nonvanishing absolute budget is possible')
        count += 1
    counts['relative_vs_absolute_two_point_packets'] = count
    count = 0
    for g_squared, spacing in product([512, 1024, 2048], [F(1, 2), F(1, 4), F(1, 8)]):
        kappa, lam = F(g_squared, 2)/spacing, 4/(spacing*g_squared)
        eta = lam/kappa
        electric, magnetic = -kappa/spacing**3, -lam/spacing**3
        m = magnetic+eta*electric
        require(0 < eta < F(27, 262144), 'actual positive retained coupling in declared bare convention')
        require(m == -2*lam/spacing**3 and m*m*spacing**3 == 8*eta/spacing**5, 'magnetic-minus-electric signs give effective2lambda,not the Hamiltonian Ward-null coefficient')
        count += 1
    counts['canonical_effective_coefficient_packets'] = count
    count = 0
    c0 = F(1, 65536)
    for exponent, N in product([4, 5, 6], [1, 2, 4, 8, 16]):
        h = F(1, N)
        eta = c0*h**exponent
        amplitude = 8*eta/h**5
        require(0 < eta < F(27, 262144), 'critical path uses positive sources,not eta=0 at finite mesh')
        if exponent == 4:
            require(amplitude == 8*c0*N, 'fixed-test divergence regime at bounded clocks')
        elif exponent == 5:
            require(amplitude == 8*c0, 'actual critical limit remains to be constructed')
        else:
            require(amplitude == 8*c0/N, 'weak-zero regime,not universal retained-window divergence')
        count += 1
    counts['canonical_critical_threshold_packets'] = count
    require(counts == c['frozen_coverage'] and sum(counts.values()) == 154, 'frozen substantive coverage')
    paths = [CONTRACT, NOTE, SELF, previous_path,
             BASE+'yang-mills-anchored-casimir-v1.md', BASE+'yang-mills-source-clustering-v1.md',
             BASE+'yang-mills-electric-magnetic-reader-v1.md', BASE+'yang-mills-interacting-magnetic-coercivity-v1.md']
    return {
        'schema': 'marici.yang-mills-mixed-reader-ward.result.v1',
        'passed': True, 'new_exact_controls': 154, 'coverage': counts,
        'predecessor_magnetic_coercivity_controls_replayed': previous['new_exact_controls'],
        'strength': 'written actual-source local Ward vacuum-channel comparison,joint tempered finite-amplitude comparison and normalization threshold; no individual critical or Lorentz limit',
        'unit_cube_shell_constant': 7728,
        'uniform_electric_activity_over_eta': '5632/3',
        'first_order_quadratic_midpoint_defect_over_eta_at_h1': str(first_order_quadratic_defect),
        'mixed_filtered_mass_lower_denominator': 4096,
        'canonical_effective_variance_scale': '8eta/h^5',
        'near_null_opposite_sign_class_uniformly_covered': False,
        'vacuum_channel_identity_is_operator_identity': False,
        'individual_critical_or_Lorentz_limit_constructed': False,
        'finite_controls_certify_analytic_theorem': False,
        'independent_analytic_review_complete': False,
        'continuum_Yang_Mills_root_discharged': False,
        'next_executable': 'positive-coupling-critical-mixed-two-point-limit',
        'input_sha256': {p: sha256((ROOT/p).read_bytes()).hexdigest() for p in paths}
    }


if __name__ == '__main__':
    r = report()
    OUT.write_text(json.dumps(r, indent=2)+'\n', encoding='utf-8')
    print(json.dumps({k: v for k, v in r.items() if k != 'input_sha256'}, indent=2))
