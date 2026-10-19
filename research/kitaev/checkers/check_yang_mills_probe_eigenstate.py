"""Exact positive-filter/state-transport controls; not SU2 evaluations."""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
from hashlib import sha256
import json
from check_yang_mills_probe_pressure import report as predecessor_report, spectral_packet, working_bound, require
from check_yang_mills_probe_clustering import mv, eye
from check_yang_mills_mesh_word import word_prefactor

ROOT = Path(__file__).resolve().parents[3]
BASE = 'research/kitaev/'
CONTRACT = BASE+'contracts/yang-mills-probe-eigenstate.v1.json'
NOTE = BASE+'yang-mills-probe-eigenstate-v1.md'
SELF = BASE+'checkers/check_yang_mills_probe_eigenstate.py'
OUT = ROOT/(BASE+'results/yang-mills-probe-eigenstate-v1.json')


def envelope(n, m, coefficient, norm_f, gradient_f, gradient_u):
    return 2*norm_f*F(4, 7)**n+coefficient*(gradient_f+4*n*gradient_u*norm_f/m)*F(81, 128)**n


def plan_state_buffer(R, kappa, delta, norm_f, gradient_f, gradient_u, epsilon):
    delta, norm_f, gradient_f, gradient_u, epsilon = map(F, [delta, norm_f, gradient_f, gradient_u, epsilon])
    ceiling, coefficient = working_bound(R, kappa)
    m = 8*ceiling
    if delta < 0 or delta > ceiling or min(norm_f, gradient_f, gradient_u) < 0 or epsilon <= 0:
        raise ValueError('working norm ball, nonnegative budgets and positive tolerance required')
    if coefficient == 0 or norm_f == 0 or gradient_f == 0:
        return {'method': 'exact', 'n': 0, 'buffer': 0, 'parameter': None, 'error_bound': F(0)}
    if delta == 0 or gradient_u == 0:
        b = 0
        while coefficient*gradient_f*F(3, 4)**b > epsilon:
            b += 1
        return {'method': 'original_state', 'n': 0, 'buffer': b, 'parameter': None,
                'error_bound': coefficient*gradient_f*F(3, 4)**b}
    n = 1
    while envelope(n, m, coefficient, norm_f, gradient_f, gradient_u) > epsilon:
        n += 1
    return {'method': 'filtered_state', 'n': n, 'buffer': 4*n, 'parameter': F(n)/m,
            'error_bound': envelope(n, m, coefficient, norm_f, gradient_f, gradient_u)}


def filtered_mean(projection, discount, observable):
    p = mv(projection, [F(1), F(1)])
    x = [y+discount*(1-y) for y in p]
    require(all(y > 0 for y in x), 'positive spectral filter')
    denominator = sum(y*y for y in x)/2
    numerator = sum(y*y*f for y, f in zip(x, observable))/2
    return numerator/denominator, denominator


def report():
    contract = json.loads((ROOT/CONTRACT).read_text())
    require(contract['batch_iteration'] == 6 and contract['batch_size'] == 100, 'batch provenance')
    require(all(v is False for v in contract['boundary'].values()) and not contract['parent_net']['discharges_parent'], 'scope')
    require(contract['subnet']['parent_outcome'] is None and contract['subnet']['ready_frontier'] == ['small-probe-doob-dynamics'], 'next source constructor')
    parent = json.loads((ROOT/contract['parent_net']['path']).read_text())
    require(next(n for n in parent['conjectures'] if n['id'] == contract['parent_net']['node'])['status'] == 'open', 'parent gate')
    previous = predecessor_report()
    require(previous['passed'] and previous == json.loads((ROOT/(BASE+'results/yang-mills-probe-pressure-v1.json')).read_text()), 'fresh predecessor receipt')
    discounts = [F(0), F(1, 16), F(1, 4), F(1, 2), F(1)]
    geometry_cases = 0
    for overlap, discount in product([F(8, 9), F(9, 10), F(1)], discounts):
        r2 = (1-overlap)*discount*discount/overlap
        require(r2 <= discount*discount/8 and 1-r2/2 >= 0, 'orthogonal filter ratio')
        require((1+r2)*(1-r2/2)**2 <= 1, 'squared rational certificate for normalized-vector distance')
        require(4*r2 <= discount*discount/2, 'local readout filter bound')
        geometry_cases += 1
    filter_cases = 0
    for m, q, shift in product([F(1, 2), F(2)], [F(0), F(1, 16)], [F(-1, 64), F(0), F(1, 64)]):
        _, overlap, projection = spectral_packet(m, q, shift)
        _, _, unshifted = spectral_packet(m, q, F(0))
        require(projection == unshifted, 'constant probe shifts preserve eigenstate')
        for discount, observable in product(discounts, [[F(1), F(1)], [F(1), F(0)], [F(1), F(-1)]]):
            value, denominator = filtered_mean(projection, discount, observable)
            ground = sum(projection[i][i]*observable[i] for i in range(2))
            r2 = (1-overlap)*discount*discount/overlap
            require(abs(value) <= 1 and denominator == overlap+(1-overlap)*discount*discount, 'based sandwich denominator')
            require((value-ground)**2 <= 4*r2 <= discount*discount/2, 'exact finite spectral filtering readout')
            if discount == 0:
                require(value == ground, 'completed eigenstate readout')
            if observable == [F(1), F(1)]:
                require(value == 1, 'probability normalization')
            filter_cases += 1
    quotient_cases = 0
    for d, dl, v, vl in product([F(1, 4), F(1, 2), F(1)], [F(1, 4), F(1, 2), F(1)], [F(-1), F(0), F(1)], [F(-1), F(0), F(1)]):
        n, nl = d*v, dl*vl
        require(abs(nl/dl-n/d) <= (abs(nl-n)+abs(dl-d))/dl, 'one inverse denominator with positive state-effect packet')
        quotient_cases += 1
    _, overlap, projection = spectral_packet(F(1), F(1, 16), F(0))
    correct, omitted = filtered_mean(projection, F(0), [F(1), F(1)])
    normalization_residual = abs(correct-omitted)
    require(normalization_residual == 1-overlap == F(1, 257), 'missing norm denominator hostile')
    laws = [[F(1, 2), F(1, 2)], [F(1, 3), F(2, 3)]]
    for law in laws:
        A = [[eye(2)[i][j]-law[j] for j in range(2)] for i in range(2)]
        require(mv(A, [F(1), F(1)]) == [0, 0], 'identical constant filters for zero probe')
        require(all(law[i]*A[i][j] == law[j]*A[j][i] for i in range(2) for j in range(2)), 'actual reversible original bases')
        require(sum(A[i][i] for i in range(2)) == 1, 'gap1 reset source')
    base_residual = abs(laws[0][0]-laws[1][0])
    require(base_residual == F(1, 6), 'same filter coordinates do not identify original-state pairings')
    planner_cases = 0
    for R, kappa, ratio, gu, gf, epsilon in product([F(0), F(1, 128), F(9, 128), F(575, 4096)], [F(1, 2), F(1), F(2)], [F(1, 16), F(1, 8)], [F(0), F(1)], [F(0), F(1)], [F(1, 100), F(1, 1000)]):
        m = kappa*(F(1, 2)-3*R)
        plan = plan_state_buffer(R, kappa, m*ratio, 1, gf, gu, epsilon)
        require(plan['error_bound'] <= epsilon, 'state readout tolerance')
        if plan['method'] == 'filtered_state':
            n = plan['n']
            require(plan['buffer'] == 4*n and plan['parameter'] == F(n)/m, 'typed diagonal filter/spatial budget')
            require(all(envelope(j, m, word_prefactor(R), F(1), gf, gu) > epsilon for j in range(1, n)), 'least sufficient n without assuming monotonicity')
        elif plan['method'] == 'original_state':
            require(gu == 0, 'constant probe branch')
            if plan['buffer']:
                require(word_prefactor(R)*gf*F(3, 4)**(plan['buffer']-1) > epsilon, 'least original-state buffer')
        else:
            require(R*gf == 0, 'exact source or constant observable')
        planner_cases += 1
    examples = [plan_state_buffer(R, 1, F(1, 128), 1, 1, 1, F(1, 1000))['buffer'] for R in [None, F(9, 128)]]
    require(examples == [140, 112] == list(contract['transport']['buffers_kappa1_delta_1_128_F1_Mf1_MU1_epsilon_1_1000'].values()), 'worked state transport buffers')
    require(plan_state_buffer(F(9, 128), 1, 0, 1, 1, 1, F(1, 1000))['method'] == 'original_state', 'zero-norm probe')
    require(plan_state_buffer(None, 1, F(1, 128), 0, 1, 1, F(1, 1000))['method'] == 'exact', 'zero observable upper norm')
    require((geometry_cases, filter_cases, quotient_cases, planner_cases) == (15, 180, 81, 192), 'frozen coverage')
    paths = [CONTRACT, NOTE, SELF, contract['parent_net']['path']]
    for name in ['probe-pressure', 'probe-limit', 'mesh-word', 'source-clustering']:
        paths += [BASE+'contracts/yang-mills-'+name+'.v1.json', BASE+'yang-mills-'+name+'-v1.md',
                  BASE+'checkers/check_yang_mills_'+name.replace('-', '_')+'.py', BASE+'results/yang-mills-'+name+'-v1.json']
    return {'schema': 'marici.yang-mills-probe-eigenstate.result.v1', 'passed': True,
            'strength': 'written based eigenstate/filter and weak local-state transport; independently unreviewed source analysis',
            'orthogonal_filter_packets': geometry_cases, 'exact_filter_readouts': filter_cases,
            'positive_quotient_packets': quotient_cases, 'transport_budget_cases': planner_cases,
            'missing_denominator_hostile_residual': str(normalization_residual),
            'unbased_coordinate_hostile_residual': str(base_residual),
            'buffers_kappa1_delta_1_128_F1_Mf1_MU1_epsilon_1_1000': examples,
            'state_transport_topology': 'weak probability measures on compact product X',
            'tilted_markov_dynamics_constructed': False, 'independent_analytic_review': False,
            'continuum_Yang_Mills': False, 'ready_frontier': contract['subnet']['ready_frontier'],
            'input_sha256': {p: sha256((ROOT/p).read_bytes()).hexdigest() for p in paths}}


if __name__ == '__main__':
    result = report()
    OUT.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({k: result[k] for k in ['passed', 'orthogonal_filter_packets', 'exact_filter_readouts',
                     'positive_quotient_packets', 'transport_budget_cases', 'missing_denominator_hostile_residual',
                     'unbased_coordinate_hostile_residual']}, indent=2))
