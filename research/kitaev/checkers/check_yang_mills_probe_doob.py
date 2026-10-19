"""Exact ground-state-transform/paired-transport controls; not SU2 dynamics."""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
from hashlib import sha256
import json
from check_yang_mills_probe_eigenstate import report as predecessor_report
from check_yang_mills_probe_pressure import spectral_packet, working_bound, require, scale, add, sub
from check_yang_mills_probe_clustering import mm, mv, eye, diagonal
from check_yang_mills_mesh_word import word_prefactor

ROOT = Path(__file__).resolve().parents[3]
BASE = 'research/kitaev/'
CONTRACT = BASE+'contracts/yang-mills-probe-doob.v1.json'
NOTE = BASE+'yang-mills-probe-doob-v1.md'
SELF = BASE+'checkers/check_yang_mills_probe_doob.py'
OUT = ROOT/(BASE+'results/yang-mills-probe-doob-v1.json')


def ceil_fraction(x):
    return (x.numerator+x.denominator-1)//x.denominator


def transport_envelope(n, m, coefficient, delta, horizon, nf, ng, gf, gg, gu):
    fg = nf*ng
    multiplier = 2**ceil_fraction(4*delta*horizon)
    word = coefficient*((4*n/m+horizon)*gu*fg+ng*gf+nf*gg)*F(81, 128)**n
    energy = horizon*fg*(delta/n+coefficient*gu*F(27, 64)**n)
    return 2*fg*F(4, 7)**n+multiplier*(word+energy)


def plan_pair_buffer(R, kappa, delta, horizon, nf, ng, gf, gg, gu, epsilon):
    delta, horizon, nf, ng, gf, gg, gu, epsilon = map(F, [delta, horizon, nf, ng, gf, gg, gu, epsilon])
    ceiling, coefficient = working_bound(R, kappa)
    m = 8*ceiling
    if min(delta, horizon, nf, ng, gf, gg, gu) < 0 or delta > ceiling or epsilon <= 0:
        raise ValueError('working norm ball, nonnegative source budgets and positive tolerance required')
    if coefficient == 0 or nf*ng == 0 or gf+gg == 0:
        return {'method': 'exact', 'buffer': 0, 'n': 0, 'error_bound': F(0)}
    if delta == 0 or gu == 0:
        b = 0
        while coefficient*(ng*gf+nf*gg)*F(3, 4)**b > epsilon:
            b += 1
        return {'method': 'original_word', 'buffer': b, 'n': 0,
                'error_bound': coefficient*(ng*gf+nf*gg)*F(3, 4)**b}
    n = 1
    while transport_envelope(n, m, coefficient, delta, horizon, nf, ng, gf, gg, gu) > epsilon:
        n += 1
    return {'method': 'filtered_pair', 'buffer': 4*n, 'n': n,
            'filter_parameter': F(n)/m, 'pressure_parameter': F(n)/(8*delta),
            'error_bound': transport_envelope(n, m, coefficient, delta, horizon, nf, ng, gf, gg, gu)}


def row_normalize(matrix):
    return [[x/sum(row) for x in row] for row in matrix]


def mean(law, values):
    return sum(p*x for p, x in zip(law, values))


def report():
    contract = json.loads((ROOT/CONTRACT).read_text())
    require(contract['batch_iteration'] == 7 and contract['batch_size'] == 100, 'batch provenance')
    require(all(v is False for v in contract['boundary'].values()) and not contract['parent_net']['discharges_parent'], 'scope')
    require(contract['subnet']['parent_outcome'] is None and contract['subnet']['ready_frontier'] == ['small-probe-quasilocal-ground-state'], 'regularity frontier')
    parent = json.loads((ROOT/contract['parent_net']['path']).read_text())
    require(next(n for n in parent['conjectures'] if n['id'] == contract['parent_net']['node'])['status'] == 'open', 'parent gate')
    previous = predecessor_report()
    require(previous['passed'] and previous == json.loads((ROOT/(BASE+'results/yang-mills-probe-eigenstate-v1.json')).read_text()), 'fresh predecessor receipt')
    kernel_cases = paired_cases = 0
    one = [F(1)]*2
    original = [F(1, 2)]*2
    for m, q, shift in product([F(1, 2), F(1), F(2)], [F(0), F(1, 32), F(1, 16)], [F(-1, 64), F(0), F(1, 64)]):
        _, overlap, projection = spectral_packet(m, q, shift)
        h = mv(projection, one)
        require(min(h) > 0, 'strict positive finite ground vector')
        tilted = [projection[i][i] for i in range(2)]
        require(tilted == [h[i]*h[i]/(2*overlap) for i in range(2)] and sum(tilted) == 1, 'canonical same-source change of measure')
        inverse_h = diagonal([1/x for x in h])
        for discount in [F(0), F(1, 4), F(1, 2), F(1)]:
            S = add(projection, scale(sub(eye(2), projection), discount))
            kernel = mm(mm(inverse_h, S), diagonal(h))
            expected = [[discount*eye(2)[i][j]+(1-discount)*tilted[j] for j in range(2)] for i in range(2)]
            require(kernel == expected and mv(kernel, one) == one and min(x for row in kernel for x in row) >= 0, 'positive conservative transformed kernel')
            require(all(tilted[i]*kernel[i][j] == tilted[j]*kernel[j][i] for i in range(2) for j in range(2)), 'symmetry in actual tilted base')
            quarter = [[F(1, 4)*eye(2)[i][j]+F(3, 4)*tilted[j] for j in range(2)] for i in range(2)]
            composed = [[discount*F(1, 4)*eye(2)[i][j]+(1-discount*F(1, 4))*tilted[j] for j in range(2)] for i in range(2)]
            require(mm(kernel, quarter) == composed, 'semigroup sewing')
            centered = [1-tilted[0], -tilted[0]]
            require(mv(kernel, centered) == [discount*x for x in centered], 'relative spectral discount')
            kernel_cases += 1
            for f, g in [([F(1), F(0)], [F(1), F(0)]), ([F(1), F(0)], [F(1), F(-1)]), (one, [F(1), F(-1)])]:
                exact = mean(tilted, [f[i]*x for i, x in enumerate(mv(kernel, g))])
                based = mean(original, [h[i]*f[i]*x for i, x in enumerate(mv(S, [h[j]*g[j] for j in range(2)]))])/overlap
                require(exact == based and abs(exact) <= 1, 'unitary paired-readout identity')
                for filter_discount in [F(0), F(1, 4), F(1)]:
                    x = [y+filter_discount*(1-y) for y in h]
                    denominator = mean(original, [y*y for y in x])
                    filtered = mean(original, [x[i]*f[i]*y for i, y in enumerate(mv(S, [x[j]*g[j] for j in range(2)]))])/denominator
                    r2 = (1-overlap)*filter_discount*filter_discount/overlap
                    require((exact-filtered)**2 <= 4*r2 <= filter_discount*filter_discount/2, 'uniform paired spectral-filter error')
                    paired_cases += 1
    _, _, projection = spectral_packet(F(1), F(1, 16), F(0))
    kernels = {d: row_normalize(add(projection, scale(sub(eye(2), projection), d))) for d in [F(1, 2), F(1, 3), F(1, 6)]}
    row_residual = mm(kernels[F(1, 2)], kernels[F(1, 3)])[0][0]-kernels[F(1, 6)][0][0]
    require(row_residual == F(333238023, 586794978)-F(1639, 2914) > 0, 'row-normalization destroys source composition')
    reset = [[F(1, 2)]*2 for _ in range(2)]
    original_kernel = add(scale(eye(2), F(1, 2)**16), scale(reset, 1-F(1, 2)**16))
    unshifted = scale(original_kernel, F(1, 2))
    energy_residual = 1-mv(unshifted, one)[0]
    require(energy_residual == F(1, 2) and mv(scale(unshifted, 2), one) == one, 'constant small probe missing-energy-shift conservation hostile')
    zero_weight_residual = mean(original, [F(0), F(1)])
    require(zero_weight_residual == F(1, 2) and mean([F(1), F(0)], [F(0), F(1)]) == 0, 'zero-weight inverse misses original-space direction')
    planner_cases = 0
    for R, kappa, gu, grads, horizon, epsilon in product([F(0), F(1, 128), F(9, 128), F(575, 4096)], [F(1, 2), F(1), F(2)], [F(0), F(1)], [(F(0), F(0)), (F(1), F(1))], [F(0), F(1)], [F(1, 100), F(1, 1000)]):
        m = kappa*(F(1, 2)-3*R)
        delta = m/8
        gf, gg = grads
        plan = plan_pair_buffer(R, kappa, delta, horizon, 1, 1, gf, gg, gu, epsilon)
        require(plan['error_bound'] <= epsilon, 'paired transport tolerance')
        if plan['method'] == 'filtered_pair':
            n = plan['n']
            require(plan['buffer'] == 4*n and plan['filter_parameter'] == F(n)/m and 2*delta*plan['pressure_parameter'] == F(n, 4), 'separate completion parameters')
            require(all(transport_envelope(j, m, word_prefactor(R), delta, horizon, F(1), F(1), gf, gg, gu) > epsilon for j in range(1, n)), 'least sufficient diagonal n')
        elif plan['method'] == 'original_word':
            require(gu == 0, 'constant probe original dynamics')
        else:
            require(R*(gf+gg) == 0, 'exact zero-source/constant-readout case')
        planner_cases += 1
    universal = plan_pair_buffer(None, 1, F(1, 128), 1, 1, 1, 1, 1, 1, F(1, 1000))
    require(universal['error_bound'] <= F(1, 1000), 'whole-window joint budget')
    require(plan_pair_buffer(F(9, 128), 1, 0, 1, 1, 1, 1, 1, 1, F(1, 1000))['method'] == 'original_word', 'zero probe')
    require((kernel_cases, paired_cases, planner_cases) == (108, 972, 192), 'frozen coverage')
    paths = [CONTRACT, NOTE, SELF, contract['parent_net']['path']]
    for name in ['probe-eigenstate', 'probe-pressure', 'mesh-word', 'source-clustering']:
        paths += [BASE+'contracts/yang-mills-'+name+'.v1.json', BASE+'yang-mills-'+name+'-v1.md', BASE+'checkers/check_yang_mills_'+name.replace('-', '_')+'.py', BASE+'results/yang-mills-'+name+'-v1.json']
    return {'schema': 'marici.yang-mills-probe-doob.result.v1', 'passed': True,
            'strength': 'written canonical L2 ground-state Markov realization and based bounded-horizon paired-readout transport; independently unreviewed source analysis',
            'exact_transformed_kernels': kernel_cases, 'filtered_paired_readouts': paired_cases, 'paired_transport_budgets': planner_cases,
            'zero_weight_inverse_hostile_residual': str(zero_weight_residual), 'missing_energy_shift_hostile_residual': str(energy_residual),
            'row_normalization_composition_hostile_residual': str(row_residual),
            'whole_window_unit_budgets_delta_1_128_horizon1_epsilon_1_1000_buffer': universal['buffer'],
            'Feller_realization_proved': False, 'independent_analytic_review': False, 'continuum_Yang_Mills': False,
            'ready_frontier': contract['subnet']['ready_frontier'], 'input_sha256': {p: sha256((ROOT/p).read_bytes()).hexdigest() for p in paths}}


if __name__ == '__main__':
    result = report()
    OUT.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({k: result[k] for k in ['passed', 'exact_transformed_kernels', 'filtered_paired_readouts', 'paired_transport_budgets',
                     'zero_weight_inverse_hostile_residual', 'missing_energy_shift_hostile_residual', 'row_normalization_composition_hostile_residual']}, indent=2))
