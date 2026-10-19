"""Source-bound port conjectures: forward maps, route compatibility, readout descent.
Standard library exact arithmetic. Does not execute native producers.
"""
from collections import Counter
from dataclasses import dataclass, replace
from fractions import Fraction as F
from hashlib import sha256
from itertools import product as pairs
from pathlib import Path
import json

from assemble_metric_coefficient_protocol import (
    ROOT, A, ZERO, ONE, read_operator, product, sharp, integer_trace, encode)
from electron_packet_interface import (
    Interface, ACTIONS, E, I, G0, G1, adj, gmm, sm, act)
from native_path_sector_calculus import sector_certificate, verify_sector
from check_native_path_sector_calculus import matrix_word, inner
from check_photon_one_direction_trial import (
    Z as PZERO, ONE as PONE, OMEGA, add as pa, mul as pm, scale as ps,
    conj as pc, inverse as pi, eye as pe, mm as pmm, ma as pma, ms as pms,
    act as pact, vs as pvs)

CONTRACT = ROOT/'research/strominger/contracts/port-incidence-conjectures.v1.json'
RESULT = ROOT/'research/strominger/results/port-incidence-conjectures-v1.json'


def digest(p):
    return sha256(p.read_bytes()).hexdigest()


def semantic_digest(c):
    c = {k: v for k, v in c.items() if k not in ('status', 'disposition')}
    return sha256(json.dumps(c, sort_keys=True, separators=(',', ':')).encode()).hexdigest()


def identity(n):
    return {(i, i): ONE for i in range(n)}


def transpose(a, conjugate=False):
    return {(j, i): x.flip(8) if conjugate else x for (i, j), x in a.items()}


def pivot_columns(matrix, rows, cols):
    """Exact elimination only; no rank inferred from the advertised measures."""
    a = [[matrix.get((i, j), ZERO) for j in range(cols)] for i in range(rows)]
    pivots = []
    for col in range(cols):
        r = len(pivots)
        q = next((i for i in range(r, rows) if a[i][col] != ZERO), None)
        if q is None:
            continue
        a[r], a[q] = a[q], a[r]
        inverse = a[r][col].inverse()
        a[r] = [x*inverse for x in a[r]]
        for i in range(r+1, rows):
            if a[i][col] != ZERO:
                factor = a[i][col]
                a[i] = [x-factor*y for x, y in zip(a[i], a[r])]
        pivots.append(col)
        if len(pivots) == rows:
            break
    return pivots


def invert(matrix, n):
    a = [[matrix.get((i, j), ZERO) for j in range(n)] +
         [ONE if i == j else ZERO for j in range(n)] for i in range(n)]
    for j in range(n):
        q = next(i for i in range(j, n) if a[i][j] != ZERO)
        a[j], a[q] = a[q], a[j]
        v = a[j][j].inverse()
        a[j] = [x*v for x in a[j]]
        for i in range(n):
            if i != j and a[i][j] != ZERO:
                v = a[i][j]
                a[i] = [x-v*y for x, y in zip(a[i], a[j])]
    return {(i, j): a[i][n+j] for i in range(n) for j in range(n)
            if a[i][n+j] != ZERO}


def factor(projector, n, metric):
    columns = pivot_columns(projector, n, n)
    r = len(columns)
    K = {(i, j): projector[i, col] for j, col in enumerate(columns)
         for i in range(n) if (i, col) in projector}
    rows = pivot_columns(transpose(K), r, n)
    assert len(rows) == r
    square = {(i, j): K[row, j] for i, row in enumerate(rows)
              for j in range(r) if (row, j) in K}
    selected = {(i, j): projector[row, j] for i, row in enumerate(rows)
                for j in range(n) if (row, j) in projector}
    D = product(invert(square, r), selected)
    assert product(D, K) == identity(r) and product(K, D) == projector
    assert r == integer_trace(projector)
    gram = product(transpose(K, True), product({(i, i): A(m) for i, m in enumerate(metric)}, K))
    # This is a channel basis with a derived metric, not an assumed orthonormal
    # spinor frame and not r independent copies of a state.
    assert product(gram, D) == product(transpose(K, True), {(i, i): A(m) for i, m in enumerate(metric)})
    return {'rank': r, 'K': K, 'D': D, 'gram': gram, 'columns': columns, 'rows': rows}


def incidence(matrix):
    adjacency = {}
    for i, j in matrix:
        x, y = ('out', i), ('in', j)
        adjacency.setdefault(x, set()).add(y)
        adjacency.setdefault(y, set()).add(x)
    unseen = set(adjacency)
    components = []
    while unseen:
        todo = [min(unseen)]
        found = set()
        while todo:
            x = todo.pop()
            if x in found:
                continue
            found.add(x)
            todo.extend(adjacency[x]-found)
        unseen -= found
        ins = sorted(x[1] for x in found if x[0] == 'in')
        outs = sorted(x[1] for x in found if x[0] == 'out')
        edges = sum((i, j) in matrix for i in outs for j in ins)
        components.append({'inputs': ins, 'outputs': outs, 'edges': edges,
                           'complete': edges == len(ins)*len(outs)})
    return sorted(components, key=lambda c: (c['inputs'], c['outputs']))


def stage_interfaces(contract):
    rows = {}
    for name in ('proton', 'neutron', 'electron'):
        path = ROOT/f'research/strominger/results/common-three-carrier-protocol/{name}.json'
        source = json.loads(path.read_text(encoding='utf-8'))
        n = len(source['source']['metric'])
        metric = tuple(map(F, source['source']['metric']))
        ops = {s: read_operator(source['operators'][s], n) for s in 'LGN'}
        assert ops['L'] == read_operator(source['source']['local'], n)
        assert ops['G'] == read_operator(source['source']['alignment'], n)
        assert product(ops['L'], ops['G']) == product(ops['G'], ops['L']) == ops['N']
        for P in ops.values():
            assert product(P, P) == P and sharp(P, metric) == P
        f = {s: factor(ops[s], n, metric) for s in 'LGN'}
        a, b = f['L'], f['G']
        cross = product(b['D'], product(ops['G'], a['K']))
        reverse = product(a['D'], product(ops['L'], b['K']))
        assert product(b['K'], cross) == product(ops['G'], a['K'])
        assert product(a['K'], reverse) == product(ops['L'], b['K'])
        assert product(b['K'], product(cross, a['D'])) == ops['N']
        assert product(transpose(cross, True), b['gram']) == product(a['gram'], reverse)
        assert len(pivot_columns(cross, b['rank'], a['rank'])) == f['N']['rank']
        assert [f[s]['rank'] for s in 'LGN'] == [source['measures'][k] for k in ('local_rank','alignment_rank','return_rank')]
        rows[name] = {
            'native_source': path.relative_to(ROOT).as_posix(),
            'raw_coordinates': n,
            'image_channels_L_G_N': [f[s]['rank'] for s in 'LGN'],
            'stage_supports': [len(ops[s]) for s in 'LGN'],
            'native_stage_support_components': {s: incidence(ops[s]) for s in 'LGN'},
            'image_interface': {'incoming': a['rank'], 'outgoing': b['rank'],
                                'candidate_pairs': a['rank']*b['rank'],
                                'nonzero_basis_coefficients': len(cross),
                                'transfer_rank': f['N']['rank'],
                                'matrix': encode(cross), 'reverse': encode(reverse)},
            'factors': {s: {'rank': v['rank'], 'encoder': encode(v['K']),
                            'decoder': encode(v['D']), 'metric': encode(v['gram']),
                            'source_column_indices': v['columns'], 'source_row_indices': v['rows']}
                        for s, v in f.items()},
            'geometric_main_codimension_attachment': None}
    assert rows['proton']['image_channels_L_G_N'] == [12, 3, 1]
    assert rows['neutron']['image_channels_L_G_N'] == [3, 12, 1]
    assert rows['electron']['image_channels_L_G_N'] == [4, 2, 2]
    return rows


@dataclass(frozen=True)
class SectorState:
    port: int
    initial_port: int
    hops: tuple
    packet: object


class SectorInterface:
    def __init__(self):
        self.native = Interface()
        self.certificates = tuple(sector_certificate(k, signs) for k in range(3)
                                  for signs in pairs((-1, 1), repeat=2))
        assert all(verify_sector(c) for c in self.certificates)
        self.frames = tuple(matrix_word(c['left']) for c in self.certificates)
        self.transports = {(t, s): gmm(self.frames[t], adj(self.frames[s]))
                           for t, s in pairs(range(12), repeat=2)}
        assert all(T in ACTIONS for T in self.transports.values())

    def execution(self, word):
        return tuple(sm(sign, E[axis]) for axis, sign in reversed(word))

    def transfer_word(self, target, source):
        left = self.certificates[source]['left']
        return self.certificates[target]['left'] + tuple((a, -s) for a, s in reversed(left))

    def seed(self, port, reference):
        p = self.native.extract(self.native.seed(reference))
        for U in self.execution(self.certificates[port]['left']):
            p = self.native.packet_step(p, U)
        return SectorState(port, port, (), p)

    def validate(self, state):
        if state.port not in range(12) or state.initial_port not in range(12):
            raise ValueError('port domain')
        expected = state.initial_port
        word = self.execution(self.certificates[expected]['left'])
        for t, s in state.hops:
            if s != expected or t not in range(12):
                raise ValueError('port trace')
            word += self.execution(self.transfer_word(t, s))
            expected = t
        if expected != state.port:
            raise ValueError('port trace')
        self.native.validate_packet(state.packet)
        if state.packet.archive.word != word:
            raise ValueError('execution trace')
        if state.packet.spinor != act(self.frames[state.port], state.packet.archive.initial_spinor):
            raise ValueError('sector frame')

    def step(self, state, target, source):
        self.validate(state)
        if state.port != source or target not in range(12):
            raise ValueError('source port')
        p = state.packet
        for U in self.execution(self.transfer_word(target, source)):
            p = self.native.packet_step(p, U)
        result = SectorState(target, state.initial_port, state.hops+((target, source),), p)
        self.validate(result)
        return result


def reject(f, residual):
    try:
        f()
    except ValueError as e:
        assert residual in str(e), str(e)
    else:
        raise AssertionError('accepted hostile '+residual)


def sector_interfaces():
    f = SectorInterface()
    native = f.native
    transfers = []
    for t, s in pairs(range(12), repeat=2):
        T = f.transports[t, s]
        assert matrix_word(f.transfer_word(t, s)) == T
        assert gmm(T, f.frames[s]) == f.frames[t]
        raw = native.raw_actions[T]
        assert gmm(raw, native.K) == gmm(native.K, T)
        assert gmm(native.D, raw) == gmm(T, native.D)
        assert f.transports[s, t] == adj(T)
        transfers.append({'target_port': t, 'source_port': s, 'native_operation_index': ACTIONS.index(T),
                          'algebraic_word': f.transfer_word(t, s)})
    for u, t, s in pairs(range(12), repeat=3):
        assert gmm(f.transports[u, t], f.transports[t, s]) == f.transports[u, s]
    # Full source/state/archive roundtrips and explicit word retention.
    for reference in ((G1, G0), (G0, G1), ((F(3,5),F(0)),(F(0),F(4,5)))):
        for t, s in pairs(range(12), repeat=2):
            initial = f.seed(s, reference)
            final = f.step(initial, t, s)
            returned = f.step(final, s, t)
            assert native.recover(final.packet).raw == act(native.K, act(f.frames[t], reference))
            assert returned.packet.spinor == initial.packet.spinor
            assert returned.packet.archive != initial.packet.archive
    first = f.seed(0, (G1, G0))
    reject(lambda: f.step(first, 1, 1), 'source port')
    alias = next(i for i in range(1,12) if f.frames[i] == f.frames[0])
    reject(lambda: f.validate(replace(first, port=alias)), 'port trace')
    reject(lambda: f.validate(replace(first, packet=replace(first.packet,
        archive=replace(first.packet.archive, source_sha256='wrong')))), 'source binding')
    direct = f.step(first, 2, 0)
    via = f.step(f.step(first, 1, 0), 2, 1)
    assert direct.packet.spinor == via.packet.spinor and direct.hops != via.hops
    assert direct.packet.archive != via.packet.archive

    # A proposed12->3 fold forgets signs and retains only the omitted axis.
    # Test ALL coarse-fibre constancy constraints, not just one chosen gauge.
    buckets = {}
    for (t,s), T in f.transports.items():
        key = (f.certificates[t]['omitted_axis'], f.certificates[s]['omitted_axis'])
        buckets.setdefault(key, set()).add(T)
    assert len(buckets) == 9 and all(len(v) == 2 for v in buckets.values())
    s0 = 0
    s1 = next(s for s in range(12) if f.certificates[s]['omitted_axis'] == 0
              and f.frames[s] == sm(-1, f.frames[s0]))
    t = 0
    T0, T1 = f.transports[t,s0], f.transports[t,s1]
    assert T1 == sm(-1,T0)
    x, y = act(T0, (G1,G0)), act(T1, (G1,G0))
    assert inner(x,y) == (-F(1),F(0)) and x != y
    assert gmm(native.K, T0) != gmm(native.K, T1)
    multiplicities = Counter(ACTIONS.index(T) for T in f.transports.values())
    assert len(set(f.frames)) == 6 and len(multiplicities) == 8
    return {'ports': list(f.certificates), 'frame_native_indices': [ACTIONS.index(U) for U in f.frames],
            'connections': transfers, 'ordered_pairs': 144, 'composition_triples': 1728,
            'distinct_frame_matrices': 6, 'distinct_transfer_matrices': 8,
            'matrix_multiplicities': dict(sorted(multiplicities.items())),
            'retained_execution': 'Two signed native generators per chart frame; four per inter-port connection; all port traces and central comparison certificates retained.',
            'fold_counterexample': {'source_ports': [s0,s1], 'same_omitted_axis': 0,
                'target_port': t, 'native_transfer_indices': [ACTIONS.index(T0),ACTIONS.index(T1)],
                'relative_phase': -1, 'reference_pairing': [-1,0],
                'coarse_bucket_distinct_matrices': {str(k): len(v) for k,v in sorted(buckets.items())}},
            'source_guards_and_history_hostiles': True,
            'geometric_codimension_only_assignment': None}


def photon_interface():
    source = json.loads((ROOT/'research/strominger/results/photon_shared_edge_seed.json').read_text(encoding='utf-8'))
    arrows = source['arrows']
    K = tuple(tuple((F(a[1] == b[0]),F(0)) for a in arrows) for b in arrows)
    assert K == tuple(tuple((F(x),F(0)) for x in row) for row in source['continuation']['matrix'])
    plus, minus = [tuple((F(c['real']),F(c['imaginary_sqrt3_coefficient'])) for c in source['modes'][key]['coefficients']) for key in ('plus','minus')]
    real = pma(pma(pmm(K,K),pms((F(-1),F(0)),K)),pms((F(-1),F(0)),pe(6)))
    other = pma(K,pms(ps(-1,pc(OMEGA)),pe(6)))
    denominator = pm(pm(OMEGA,pa(pa(pm(OMEGA,OMEGA),ps(-1,OMEGA)),ps(-1,PONE))),pa(OMEGA,ps(-1,pc(OMEGA))))
    P = pms(pi(denominator),pmm(pmm(K,real),other))
    encoder, decoder = tuple((x,) for x in plus), (P[0],)
    assert pmm(decoder,encoder) == pe(1) and pmm(encoder,decoder) == P
    assert pmm(P,P) == P and pmm(K,encoder) == pmm(encoder,((OMEGA,),))
    assert pmm(decoder,K) == pmm(((OMEGA,),),decoder)
    for power in range(4):
        Kr, w = pe(6), PONE
        for _ in range(power):
            Kr, w = pmm(Kr,K), pm(w,OMEGA)
        assert pmm(decoder,pmm(Kr,encoder)) == ((w,),)
    # Chosen-mode interface must not silently become the full photon source.
    assert pact(P,minus) == (PZERO,)*6 and plus != minus
    shared = [i for i,a in enumerate(arrows) if set(a) == {'A','B'}]
    assert tuple(plus[i] for i in shared) == tuple(minus[i] for i in shared)
    assert tuple(pact(K,plus)[i] for i in shared) != tuple(pact(K,minus)[i] for i in shared)
    support = {(i,j): ONE for i,row in enumerate(K) for j,x in enumerate(row) if x != PZERO}
    return {'full_arrow_occurrences': len(arrows), 'full_continuation_nonzeros': len(support),
            'full_continuation_components': incidence(support),
            'selected_mode_channels': [1,1], 'selected_mode': 'plus',
            'encoder': encoder, 'decoder': decoder, 'projector': P,
            'logical_continuation': OMEGA, 'cyclic_order': 3,
            'other_mode_and_shared_edge_hostiles': True,
            'geometric_main_codimension_assignment': None}


def serial(x):
    if isinstance(x,F):
        return str(x)
    if isinstance(x,dict):
        return {str(k):serial(v) for k,v in x.items()}
    if isinstance(x,(tuple,list)):
        return [serial(v) for v in x]
    return x


def main():
    contract = json.loads(CONTRACT.read_text(encoding='utf-8'))
    pins = {}
    for rel in contract['source']['prerequisite_receipts']:
        prior = json.loads((ROOT/rel).read_text(encoding='utf-8'))
        if prior['schema'] == 'marici.photon-one-direction-trial.v1':
            assert prior['verification_passed'] is True
        else:
            assert prior['status'] in ('pass','passed')
        assert all(prior['checks'].values())
        for path,h in prior['source_sha256'].items():
            assert digest(ROOT/path) == h, ('stale prerequisite',path)
            assert path not in pins or pins[path] == h
            pins[path] = h
        pins[rel] = digest(ROOT/rel)
    for rel in contract['source']['native_packets']:
        assert (ROOT/rel).is_file()
        pins[rel] = digest(ROOT/rel)
    # Pin every imported source module, including this checker's helpers.
    import sys
    for module in tuple(sys.modules.values()):
        file = getattr(module,'__file__',None)
        if file:
            p = Path(file).resolve()
            if p.is_relative_to(ROOT/'research') and p.suffix == '.py':
                pins[p.relative_to(ROOT).as_posix()] = digest(p)
    pins[CONTRACT.relative_to(ROOT).as_posix()] = digest(CONTRACT)
    for cell in contract['interface_candidates']:
        incoming, outgoing = cell['incoming'][1],cell['outgoing'][1]
        assert len(tuple(pairs(range(incoming),range(outgoing)))) == cell['candidate_pairs']
    for family in ('A','B'):
        cells = [x for x in contract['interface_candidates'] if x['id'].startswith(family+'-')]
        assert len(cells) == 4
        for c in cells:
            assert any(d['incoming'] == c['outgoing'] and d['outgoing'] == c['incoming'] for d in cells)
    native = stage_interfaces(contract)
    sectors = sector_interfaces()
    photon = photon_interface()
    # Native protocol occurrence incidence is staged, not a12x12 port graph.
    electron_path = ROOT/'research/voevodsky/results/electron_tetrahedral_spinor_store.json'
    arrows = json.loads(electron_path.read_text(encoding='utf-8'))['arrows']
    input_roles = {(a['stage'],a['source']) for a in arrows}
    output_roles = {(a['stage'],a['target']) for a in arrows}
    degrees = Counter((a['stage'],a['source']) for a in arrows)
    assert len(arrows) == 144 and len(input_roles) == len(output_roles) == 24
    assert Counter(degrees.values()) == {2:8,8:16}
    assert len(input_roles) != 12 and any(d != 12 for d in degrees.values())
    literal = {'native_occurrences':144,'native_staged_input_roles':24,'native_staged_output_roles':24,
               'native_input_degree_histogram':dict(Counter(degrees.values())),
               'candidate_port_roles_each_side':12,'candidate_degree_each_port':12,
               'incidence_preserving_primitive_bijection':False,
               'scope':'Primitive native staged occurrences. This does not rule out the separately constructed sector interface or a future composite adapter.'}
    assert contract['source']['neutrino'] is None
    # The smaller family is not the same n-rule merely at another n.
    n = contract['families']['B']['main_space_ports']
    same_rule = n*2**(n-1)
    assert n == 1 and same_rule == 1 != contract['families']['B']['codimension_sector_ports']
    checks = {key:True for key in (
        'source_pins_and_frozen_semantic_contract',
        'nine_candidate_inventories_and_both_orientation_exchanges',
        'actual_L_G_N_metric_projectors_and_native_incidence_components',
        'all_three_stage_image_encoder_decoder_recoveries',
        'cross_interface_raw_squares_metric_adjoint_and_native_return',
        'actual_proton_neutron_image_patterns_exchange_not_electron',
        'twelve_native_sector_frames_and_all144_native_transfers',
        'all1728_connection_composition_equations',
        '432_full_state_roundtrips_retain_words_and_source_guards',
        'electron_native144_primitive_incidence_bijection_rejected',
        'all_nine_coarse_sector_pairs_fail_single_matrix_descent',
        'full_phase_fold_counterexample_is_minus_identity',
        'three_over_one_not_an_instance_of_same_codimension_rule',
        'selected_photon_spectral_line_recovery_and_cyclic_continuation',
        'photon_opposite_mode_and_shared_edge_erasure_hostiles',
        'missing_geometry_and_neutrino_not_counted_as_tested_particles')}
    assert all(digest(ROOT/p) == h for p,h in pins.items()), 'source changed during check'
    report = {'schema':'marici.port-incidence-conjectures-check.v1','status':'pass',
        'coherence_obligation':'Source realization, route compatibility, then full-amplitude quotient/readout descent.',
        'contract_semantic_sha256':semantic_digest(contract),'checks':checks,
        'candidate_inventory':contract['interface_candidates'],'native_stage_interfaces':native,
        'electron_sector_interface':sectors,'electron_literal144_comparison':literal,
        'small_family_same_rule':{'outgoing_n':n,'rule_incoming':same_rule,'proposed_incoming':3,'matches':False},
        'photon':photon,'neutrino':{'tested':False,'first_missing_object':'Independent neutrino source and typed native operations/port constructor',
            'rivals':['A-MM:3main->3main','shifted-neutron:3codim->12codim','B-CC:3codim->3codim']},
        'geometric_assignment':{'tested':False,'first_missing_object':'Source-derived main/codimension port embedding with incidence and transport'},
        'physical_particle_identification':False,'native_producers_executed':False,'formal_proof_recompiled':False,
        'source_sha256':pins}
    RESULT.write_text(json.dumps(serial(report),indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'status':'pass','checks':len(checks),
        'native_image_interfaces':{k:[v['image_interface'][x] for x in ('incoming','outgoing','nonzero_basis_coefficients','transfer_rank')] for k,v in native.items()},
        'electron_sector_transfers':144,'electron_distinct_transfer_matrices':8,
        'primitive144_identification':False,'faithful_sign_forgetting_fold':False,
        'photon_selected_channels':[1,1],'neutrino_tested':False},indent=2))


if __name__ == '__main__':
    main()
