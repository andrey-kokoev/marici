"""Exact geometry-derived identity-bearing port equations; no native producers.

Identity is a discrete carried label. Three coordinate components are rational.
The connection is explicitly declared flat; native transfer is not substituted.
"""
from dataclasses import dataclass
from fractions import Fraction as F
from hashlib import sha256
from itertools import combinations
from pathlib import Path
import json
import subprocess

ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve()
CONTRACT = ROOT / 'research/strominger/contracts/identity-bearing-port-equations-v1.json'
OUT = ROOT / 'research/strominger/results/identity-bearing-port-equations-v1.json'
SOURCE = ROOT / 'research/strominger/demos/particle-overlap-tetrahedron/carrier.mjs'
MODEL = SOURCE.with_name('model.mjs')
checks = {}


def ck(name, yes):
    assert yes, name
    checks[name] = True


def eye(n):
    return [[F(i == j) for j in range(n)] for i in range(n)]


def transpose(a):
    return [list(row) for row in zip(*a)]


def mm(a, b):
    return [[sum((x * y for x, y in zip(row, col)), F(0)) for col in zip(*b)] for row in a]


def mv(a, v):
    return [sum((x * y for x, y in zip(row, v)), F(0)) for row in a]


def sub(a, b):
    return [x - y for x, y in zip(a, b)]


def add(a, b):
    return [x + y for x, y in zip(a, b)]


def dot(a, b):
    return sum((x * y for x, y in zip(a, b)), F(0))


def rref(a):
    a = [list(map(F, row)) for row in a]
    pivots = []
    for col in range(len(a[0])):
        row = len(pivots)
        pivot = next((i for i in range(row, len(a)) if a[i][col]), None)
        if pivot is None:
            continue
        a[row], a[pivot] = a[pivot], a[row]
        scale = a[row][col]
        a[row] = [x / scale for x in a[row]]
        for i in range(len(a)):
            if i != row and a[i][col]:
                scale = a[i][col]
                a[i] = [x - scale * y for x, y in zip(a[i], a[row])]
        pivots.append(col)
        if len(pivots) == len(a):
            break
    return a, pivots


def rank(a):
    return len(rref(a)[1])


def inv(a):
    n = len(a)
    reduced, pivots = rref([row + unit for row, unit in zip(a, eye(n))])
    assert pivots[:n] == list(range(n))
    assert [row[:n] for row in reduced] == eye(n)
    result = [row[n:] for row in reduced]
    assert mm(a, result) == mm(result, a) == eye(n)
    return result


def solve(a, b):
    n = len(a[0])
    reduced, pivots = rref([row + [value] for row, value in zip(a, b)])
    if n in pivots:
        return None
    result = [F(0)] * n
    for row, col in enumerate(pivots):
        result[col] = reduced[row][-1]
    assert mv(a, result) == b
    return result


def serial(value):
    if isinstance(value, F):
        return str(value)
    if isinstance(value, dict):
        return {k: serial(v) for k, v in value.items()}
    if isinstance(value, (tuple, list)):
        return [serial(v) for v in value]
    return value


def frames_for(points, bodies):
    frames = {}
    parents = {}
    for name in points:
        body = next(b for b in bodies if name in b['nodes'])
        neighbors = [n for n in body['nodes'] if n != name]
        frame = transpose([sub(points[n], points[name]) for n in neighbors])
        inv(frame)
        frames[name] = frame
        parents[name] = {'body': body['id'], 'ordered_edge_targets': neighbors}
    return frames, parents


def edges_for(bodies):
    return sorted({tuple(sorted(pair)) for b in bodies for pair in combinations(b['nodes'], 2)})


def system(points, frames, edges, fixed=None):
    names = list(points)
    index = {name: 3 * i for i, name in enumerate(names)}
    a, b = [], []
    for u, v in edges:
        for axis in range(3):
            row = [F(0)] * (3 * len(names))
            for j in range(3):
                row[index[v] + j] = frames[v][axis][j]
                row[index[u] + j] = -frames[u][axis][j]
            a.append(row);b.append(F(0))
    for name, state in (fixed or {}).items():
        for axis in range(3):
            row = [F(0)] * (3 * len(names));row[index[name] + axis] = F(1)
            a.append(row);b.append(state[axis])
    return a, b


@dataclass(frozen=True)
class Packet:
    identity: str
    configuration: tuple
    history: tuple


def along(packet, path, frames):
    q = list(packet.configuration)
    assert path[0] == packet.history[-1]
    history = list(packet.history)
    for u, v in zip(path, path[1:]):
        q = mv(mm(inv(frames[v]), frames[u]), q)
        history.append(v)
    return Packet(packet.identity, tuple(q), tuple(history))


def path_matrix(path, frames):
    result = eye(3)
    for u, v in zip(path, path[1:]):
        result = mm(mm(inv(frames[v]), frames[u]), result)
    return result


def merge(packets):
    if len({p.identity for p in packets}) != 1:
        raise ValueError('identity mismatch')
    if len({p.configuration for p in packets}) != 1:
        raise ValueError('configuration mismatch')
    return {'identity': packets[0].identity, 'configuration': packets[0].configuration,
            'histories': [p.history for p in packets]}


def rejected(fn):
    try:
        fn()
    except ValueError:
        return True
    return False


def simple_paths(edges, start, end):
    adjacency = {}
    for u, v in edges:
        adjacency.setdefault(u, set()).add(v);adjacency.setdefault(v, set()).add(u)
    found = []
    def visit(path):
        if path[-1] == end:
            found.append(tuple(path));return
        for v in sorted(adjacency[path[-1]] - set(path)):
            visit(path + [v])
    visit([start])
    return found


def add_second_electron(points, bodies):
    face = ['M2', 'C1', 'C2']
    a, b, c = [points[n] for n in face]
    u, v = sub(b, a), sub(c, a)
    normal = [u[1]*v[2]-u[2]*v[1], u[2]*v[0]-u[0]*v[2], u[0]*v[1]-u[1]*v[0]]
    scale = 2 * dot(sub(points['M1'], a), normal) / dot(normal, normal)
    m3 = sub(points['M1'], [scale * x for x in normal])
    return {**points, 'M3': m3}, [*bodies, {'id': 'electron2', 'nodes': [*face, 'M3'], 'window': face, 'continuation': 'M3'}]


def main():
    contract = json.loads(CONTRACT.read_text(encoding='utf-8'))
    assert contract['checker'].endswith(HERE.name)
    js = "import * as C from './research/strominger/demos/particle-overlap-tetrahedron/carrier.mjs';import * as M from './research/strominger/demos/particle-overlap-tetrahedron/model.mjs';console.log(JSON.stringify({points:C.trial.points,bodies:C.trial.bodies,walk:M.walk,original:M.pentachoron}));"
    live = json.loads(subprocess.run(['node', '--input-type=module', '-e', js], cwd=ROOT, capture_output=True, text=True, encoding='utf-8', check=True).stdout)
    points = {n: [F(str(v)).limit_denominator(10**6) for v in p] for n, p in live['points'].items()}
    ck('exact_rational_coordinates_match_the_live_geometry', all(abs(float(x)-y) < 1e-12 for n, p in points.items() for x, y in zip(p, live['points'][n])))
    ck('live_M2_and_original_directed_history_are_retained', points['M2'] == [F(-31, 9), F(-1, 9), F(-1, 9)] and live['walk'] == ['C0','M0','C1','M1','C1','C2'])
    bodies = live['bodies'];edges = edges_for(bodies)
    ck('three_ordered_four_vertex_carriers_are_loaded', [b['nodes'] for b in bodies] == [['C0','M0','C1','M1'], ['M0','C1','M1','C2'], ['M1','C1','C2','M2']])
    frames, parents = frames_for(points, bodies)
    ck('all_six_port_frames_are_actual_invertible_tetrahedral_edge_frames', len(frames) == 6 and all(rank(f) == 3 for f in frames.values()))
    links = {}
    for u, v in edges:
        t = mm(inv(frames[v]), frames[u]);reverse = mm(inv(frames[u]), frames[v])
        assert mm(reverse, t) == eye(3)
        gu = mm(transpose(frames[u]), frames[u]);gv = mm(transpose(frames[v]), frames[v])
        assert mm(transpose(t), mm(gv, t)) == gu
        links[u + '->' + v] = t
    ck('all_twelve_links_are_reversible_and_preserve_the_induced_metric', len(links) == 12)
    input_state = [F(1, 7), F(-2, 5), F(3, 11)]
    packet = Packet('complex:C0-C2', tuple(input_state), ('C0',))
    expected_matrix = mm(inv(frames['C2']), frames['C0'])
    expected = mv(expected_matrix, input_state)
    ck('input_output_matrix_is_computed_from_the_actual_frames', expected_matrix == [[F(1,3),F(-2,3),F(-2,3)], [F(-2,3),F(1,3),F(-2,3)], [F(-2,3),F(-2,3),F(1,3)]])
    paths = [('C0', v, 'C2') for v in ['M0','C1','M1']]
    incoming = [along(packet, path[:2], frames) for path in paths]
    outgoing = [along(p, path[1:], frames) for p, path in zip(incoming, paths)]
    result = merge(outgoing)
    ck('three_geometric_paths_recover_the_same_identity_and_configuration', result['identity'] == packet.identity and list(result['configuration']) == expected)
    ck('all_three_histories_remain_distinct_after_recombination', len(set(result['histories'])) == 3)
    all_paths = simple_paths(edges, 'C0', 'C2')
    ck('every_simple_geometric_path_gives_the_same_boundary_map', len(all_paths) >= 3 and all(path_matrix(path, frames) == expected_matrix and list(along(packet, path, frames).configuration) == expected for path in all_paths))
    original_packet = along(packet, live['walk'], frames)
    ck('original_repeated_C1_walk_has_the_same_map_and_keeps_its_occurrences', path_matrix(live['walk'], frames) == expected_matrix and list(original_packet.configuration) == expected and original_packet.history.count('C1') == 2)
    wrong_id = Packet('different-complex', outgoing[0].configuration, outgoing[0].history)
    wrong_q = Packet(packet.identity, tuple(add(list(outgoing[0].configuration), [F(1),F(0),F(0)])), outgoing[0].history)
    ck('identity_mismatch_is_rejected_even_when_coordinates_match', rejected(lambda: merge([wrong_id, *outgoing[1:]])))
    ck('configuration_mismatch_is_rejected_even_when_identities_match', rejected(lambda: merge([wrong_q, *outgoing[1:]])))

    # Three incoming cut presentations: R_a q_a = common input configuration.
    cuts = ['M0','C1','M1']
    decoders = [mm(inv(frames['C0']), frames[v]) for v in cuts]
    injection = [row for r in decoders for row in inv(r)]  # 9x3
    decoder = [[x/F(3) for r in decoders for x in r[i]] for i in range(3)]  # 3x9
    projector = mm(injection, decoder)
    residual = [[eye(9)[i][j] - projector[i][j] for j in range(9)] for i in range(9)]
    cut_a = []
    for left, right in [(0,1), (1,2)]:
        for i in range(3):
            row = [F(0)] * 9
            for j in range(3):
                row[3*left+j] = decoders[left][i][j];row[3*right+j] = -decoders[right][i][j]
            cut_a.append(row)
    ck('three_cut_system_has_six_constraints_and_three_free_coordinates', rank(cut_a) == 6 and len(cut_a[0])-rank(cut_a) == 3)
    ck('compatible_incoming_presentations_decode_losslessly', mm(decoder, injection) == eye(3) and mm(projector, projector) == projector and mm(cut_a, injection) == [[F(0)]*3 for _ in range(6)])
    ck('all_six_incompatible_coordinate_directions_are_retained', rank(residual) == 6 and [[projector[i][j]+residual[i][j] for j in range(9)] for i in range(9)] == eye(9))
    triple = [v for p in incoming for v in p.configuration]
    ck('the_actual_three_branch_packets_have_zero_compatibility_residual', mv(residual, triple) == [F(0)]*9 and mv(decoder, triple) == input_state)
    hostile = list(triple);hostile[0] += 1
    ck('one_bad_incoming_coordinate_is_detected_instead_of_averaged_away', mv(residual, hostile) != [F(0)]*9 and add(mv(projector, hostile), mv(residual, hostile)) == hostile)

    a, b = system(points, frames, edges)
    fixed_a, fixed_b = system(points, frames, edges, {'C0': input_state})
    solution = solve(fixed_a, fixed_b)
    by_port = {n: solution[3*i:3*i+3] for i, n in enumerate(points)}
    ck('one_electron_network_has_three_free_configuration_coordinates', len(a) == 36 and len(a[0]) == 18 and rank(a) == 15)
    ck('fixed_input_uniquely_determines_every_port_and_C2_output', rank(fixed_a) == 18 and by_port['C2'] == expected and all(mv(frames[n], q) == mv(frames['C0'], input_state) for n,q in by_port.items()))
    bad_rhs = list(fixed_b);bad_rhs[0] = F(1,13)
    ck('a_corrupted_link_with_nonzero_loop_offset_makes_the_network_inconsistent', solve(fixed_a, bad_rhs) is None)

    # Nonmonomial local frame changes are coordinate changes, not new dynamics.
    gauges = {n: [[F(1),F(i+1),F(0)],[F(0),F(1),F(1)],[F(0),F(0),F(1)]] for i,n in enumerate(points)}
    changed = {n: mm(frames[n], inv(gauges[n])) for n in points}
    changed_input = mv(gauges['C0'], input_state)
    ca, cb = system(points, changed, edges, {'C0': changed_input})
    changed_solution = solve(ca, cb)
    ck('nonmonomial_frame_changes_preserve_all_decoded_port_configurations', all(mv(changed[n], changed_solution[3*i:3*i+3]) == mv(frames[n], by_port[n]) for i,n in enumerate(points)))
    shift = [F(2,3),F(-4,5),F(6,7)]
    translated = {n: add(p, shift) for n,p in points.items()}
    translated_frames, _ = frames_for(translated, bodies)
    ck('common_rigid_position_shifts_leave_the_equations_unchanged', translated_frames == frames)

    points2, bodies2 = add_second_electron(points, bodies)
    frames2, parents2 = frames_for(points2, bodies2);edges2 = edges_for(bodies2)
    ck('second_MCC_attachment_adds_a_distinct_M3_without_moving_existing_ports', points2['M3'] == [F(-83,27),F(13,27),F(-77,27)] and all(points2[n] == p and frames2[n] == frames[n] for n,p in points.items()))
    ck('second_attachment_is_regular_and_has_disjoint_interiors', all(dot(sub(points2[u],points2[v]),sub(points2[u],points2[v])) == 8 for u,v in combinations(bodies2[-1]['nodes'],2)) and all(sum(points2[n]) <= -1 and -5*points2[n][0]+points2[n][1]+points2[n][2] >= 5 for n in bodies2[-1]['nodes']) and dot([F(-7),F(5),F(-13)],points2['M3']) > 25 and dot([F(-7),F(5),F(-13)],points2['M1']) < 25)
    a2, b2 = system(points2, frames2, edges2)
    fa2, fb2 = system(points2, frames2, edges2, {'C0': input_state})
    solution2 = solve(fa2, fb2)
    ck('same_port_law_admits_a_second_geometric_electron_attachment', solution2 is not None and len(a2[0]) == 21 and rank(a2) == 18 and rank(fa2) == 21)
    ck('second_attachment_preserves_existing_solution_and_boundary_transport', all(solution2[3*i:3*i+3] == by_port[n] for i,n in enumerate(points)) and mm(inv(frames2['C2']), frames2['C0']) == expected_matrix)
    paths2 = simple_paths(edges2, 'C0','C2')
    ck('all_second_attachment_paths_preserve_the_same_identity_and_boundary_map', all(path_matrix(path,frames2) == expected_matrix and along(packet,path,frames2).identity == packet.identity and list(along(packet,path,frames2).configuration) == expected for path in paths2))

    report = {
        'schema': 'marici.identity-bearing-port-equations.v1', 'status': 'pass', 'checks': checks,
        'construction': {'identity_semantics': 'Discrete boundary-supplied label, copied across links and checked for agreement; not a homogeneous scalar or native identity derivation.',
            'coordinate_semantics': 'Three configuration displacement components in a local tetrahedral frame.',
            'transport_law': 'q_v = inverse(F_v) F_u q_u; identity_v=identity_u; append the edge to retained history.',
            'connection': 'Flat geometric frame connection; all inverse/coherence squares follow from the shared decoded displacement.',
            'kernel_theorem': 'A=(incidence(graph) tensor I3) blockdiag(F_v). Invertible frames on a connected n-vertex graph give rank3(n-1), hence three free coordinates for any such attachment graph.',
            'source_paths': 'Three geometric wireframe paths, not three claimed native primitive histories.'},
        'points': points, 'frames': frames, 'frame_parents': parents, 'links': links,
        'three_cut': {'ports': cuts, 'R': decoders, 'A': cut_a, 'b': [F(0)]*6,
            'injection': injection, 'decoder': decoder, 'retained_residual': residual,
            'coordinate_rank': 6, 'free_coordinate_components': 3, 'identity_labels_after_agreement': 1},
        'boundary': {'input': 'C0', 'output': 'C2', 'matrix': expected_matrix,
            'sample_identity': packet.identity, 'sample_input': input_state, 'sample_output': expected,
            'three_paths': paths, 'retained_histories': result['histories'],
            'original_walk_history': original_packet.history,
            'simple_geometric_paths_checked': len(all_paths)},
        'one_electron': {'variables': 18, 'edge_equations': len(a), 'rank': rank(a), 'free_coordinates': 3,
            'identity_components': 1, 'A': a, 'b': b, 'fixed_input_solution': by_port},
        'second_attachment': {'new_vertex': 'M3', 'position': points2['M3'], 'body': bodies2[-1],
            'variables': 21, 'edge_equations': len(a2), 'rank': rank(a2), 'free_coordinates': 3,
            'fixed_input_solution_exists': solution2 is not None, 'boundary_matrix_unchanged': True,
            'simple_geometric_paths_checked': len(paths2),
            'interpretation': 'The geometric attachment is admitted. These variables do not establish an independent electron excitation or a one-electron occupancy law.'},
        'verdict': {'identity_bearing_geometric_port_equations': 'constructed_and_solved',
            'second_attachment_exclusion': 'not_obtained',
            'exclusion_from_frame_compatibility_alone': 'impossible_for_connected_invertible_frame_attachments_under_this_law',
            'native_operators_and_stability_dynamics': 'not_derived'},
        'source_sha256': {p.relative_to(ROOT).as_posix(): sha256(p.read_bytes()).hexdigest() for p in [CONTRACT,HERE,SOURCE,MODEL]},
        'scope': contract['excluded_claims'],
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(serial(report), indent=2)+'\n', encoding='utf-8')
    print(json.dumps({'status':'pass','checks':len(checks),'one_electron_rank':rank(a),'one_electron_variables':18,
        'second_attachment_rank':rank(a2),'second_attachment_variables':21,'second_attachment_compatible':solution2 is not None,
        'path_counts':[len(all_paths),len(paths2)],'receipt':OUT.relative_to(ROOT).as_posix()}))


if __name__ == '__main__':
    main()
