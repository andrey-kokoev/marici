"""Exact retained matrix executions, with source binding and partial readouts."""
import json
from dataclasses import dataclass, replace
from hashlib import sha256
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(Path(__file__).resolve().parent))
import check_source_projective_bridge as source
s, EPS = source.s, source.EPS
PATHS = source.PATHS + [
    'research/nima/retained-projective-correspondence-protocol.md',
    'research/nima/checkers/check_retained_projective_correspondence.py',
]


def require(ok, why):
    if not ok:
        raise ValueError(why)


def frozen(m):
    return s.ImmutableMatrix(m.applyfunc(s.factor))


def apply(points, matrix):
    return tuple(frozen(p*matrix) for p in points)


@dataclass(frozen=True)
class Step:
    occurrence: tuple
    matrix: object


@dataclass(frozen=True)
class Execution:
    source_id: tuple
    origin: tuple
    steps: tuple
    outputs: tuple


def empty(source_id, points):
    return Execution(source_id, points, (), ())


def extend(packet, steps):
    points = packet.outputs[-1] if packet.outputs else packet.origin
    outputs = list(packet.outputs)
    for step in steps:
        points = apply(points, step.matrix)
        outputs.append(points)
    return Execution(packet.source_id, packet.origin, packet.steps+tuple(steps), tuple(outputs))


def product(steps):
    M = s.eye(2)
    for step in steps:
        M = M*step.matrix
    return frozen(M)


def readout(matrix, points):
    rank = matrix.rank()
    zero_points = [i for i, p in enumerate(points) if p == s.zeros(1, 2)]
    try:
        chi = str(source.four_point(points))
    except ValueError:
        chi = None
    return {'rank': rank, 'matrix_projective_class_defined': rank != 0,
            'zero_point_indices': zero_points,
            'determinant_sign': int(s.sign(matrix.det())),
            'cross_ratio': chi}


def verify(packet, expected_source_id, expected_points, expected_steps):
    require(packet.source_id == expected_source_id, 'source identity drift')
    require(packet.origin == expected_points, 'origin does not match recomputed source')
    require(packet.steps == tuple(expected_steps), 'factor/occurrence drift')
    require(packet == extend(empty(expected_source_id, expected_points), expected_steps), 'output record drift')
    return True


def main():
    paths = list(dict.fromkeys(PATHS))
    pins = {p: sha256((ROOT/p).read_bytes()).hexdigest() for p in paths}
    # Polynomial proof independent of the finite census.
    a,b,c,d = s.symbols('a b c d', real=True)
    symbolic = s.Matrix([[a,b],[c,d]])
    require((symbolic*EPS*symbolic.T-symbolic.det()*EPS).applyfunc(s.expand) == s.zeros(2), 'polynomial form law')
    records = source.compile_nnmhv_histories(8)
    rows, collisions, hostiles = [], [], []
    rank_counts = {0: 0, 1: 0, 2: 0}
    retained_examples = []
    for shift in range(3):
        Z, lam, x = source.twistors(shift)
        localization = source.localize(lam, x)
        W = source.line_plane_point(Z[5], Z[6], Z[8], Z[1], Z[2])
        Q = source.line_plane_point(Z[5], Z[6], Z[1], Z[2], Z[3])
        points = tuple(frozen(V[:2, 0].T*EPS) for V in (Z[5], Z[6], W, Q))
        chi = source.four_point(points)
        require(chi == source.ratio(lam, x)[0], 'source coefficient binding')
        sid = ('history6-line', 8, 6, shift)
        for index, history in enumerate(records):
            if not source.supports_component_23(history):
                continue
            vertices = (8,)+history.inner_prefix
            steps = []
            for k, (u,v) in enumerate(zip(vertices, vertices[1:])):
                X = source.x_interval(x, u, v)
                matrix = X if k % 2 == 0 else source.adjugate2(X)
                steps.append(Step((index, k, u, v, 'x' if k % 2 == 0 else 'adjugate'), frozen(matrix)))
            steps = tuple(steps)
            packet = extend(empty(sid, points), steps)
            require(verify(packet, sid, points, steps), 'packet binding')
            M = product(steps)
            require(M == source.transport(x, vertices), 'owning prefix product')
            require(packet.outputs[-1] == apply(points, M), 'direct/staged points')
            require(extend(packet, ()) == packet, 'empty continuation')
            for cut in range(len(steps)+1):
                require(extend(extend(empty(sid, points), steps[:cut]), steps[cut:]) == packet, 'word splitting')
            # Three-piece association, in the declared matrix envelope only.
            extra = Step(('envelope-identity',), frozen(s.eye(2)))
            require(extend(extend(extend(empty(sid, points), steps[:1]), steps[1:]), (extra,)) ==
                    extend(empty(sid, points), steps+(extra,)), 'concatenation associativity')
            for matrix in [step.matrix for step in steps]+[M]:
                require((matrix*EPS*matrix.T-matrix.det()*EPS).applyfunc(s.factor) == s.zeros(2), 'form law')
            r = readout(M, packet.outputs[-1])
            rank_counts[r['rank']] += 1
            if r['rank'] == 2:
                require(r['cross_ratio'] == str(chi), 'invertible preservation')
            else:
                require(r['rank'] == 1 and r['cross_ratio'] is None, 'singular status')
                kernel = frozen(M.T.nullspace()[0].T)
                require(kernel*M == s.zeros(1, 2), 'row kernel')
                # Same M and outputs, hence same image/kernel data. This is an
                # ambient linear-packet rival, not an asserted new native fixture.
                witness = None
                for slot in range(4):
                    for amount in (1, 2, 3, 5):
                        other = list(points)
                        other[slot] = frozen(other[slot]+amount*kernel)
                        other = tuple(other)
                        if any(source.det_rows(p, q) == 0 for j, p in enumerate(other) for q in other[j+1:]):
                            continue
                        try:
                            other_chi = source.four_point(other)
                        except ValueError:
                            continue
                        if other_chi != chi:
                            require(apply(other, M) == packet.outputs[-1], 'kernel collision')
                            witness = {'slot': slot, 'amount': amount, 'original': str(chi), 'rival': str(other_chi)}
                            break
                    if witness:
                        break
                require(witness is not None, 'missing rank-one collision')
                collisions.append({'shift': shift, 'history_index': index, **witness})
            require(source.four_point(packet.origin) == chi, 'retained source observable')
            rows.append({'shift': shift, 'history_index': index, 'prefix': list(vertices), **r,
                         'source_localization_checked': bool(localization)})
            retained_examples.append((packet, sid, points, steps))

    packet, sid, points, steps = retained_examples[0]
    def reject(name, bad):
        try:
            verify(bad, sid, points, steps)
        except ValueError:
            hostiles.append(name)
        else:
            raise AssertionError('accepted corruption: '+name)
    reject('wrong-source-id', replace(packet, source_id=('other',)))
    reject('changed-origin', replace(packet, origin=(frozen(points[0]*2),)+points[1:]))
    reject('reordered-factors', replace(packet, steps=steps[::-1]))
    reject('changed-factor', replace(packet, steps=(replace(steps[0], matrix=frozen(s.eye(2))),)+steps[1:]))
    reject('changed-occurrence-tag', replace(packet, steps=(replace(steps[0], occurrence=('other',)),)+steps[1:]))
    reject('missing-intermediate-output', replace(packet, outputs=packet.outputs[1:]))
    reject('altered-output', replace(packet, outputs=(points,)+packet.outputs[1:]))

    # Controls are explicit matrix-envelope words, not native history claims.
    A, B = frozen(s.diag(1,0)), frozen(s.diag(0,1))
    zero_steps = (Step(('synthetic-A',), A), Step(('synthetic-B',), B))
    zero_packet = extend(empty(sid, points), zero_steps)
    zr = readout(product(zero_steps), zero_packet.outputs[-1])
    require(zr['rank'] == 0 and not zr['matrix_projective_class_defined'] and len(zr['zero_point_indices']) == 4,
            'zero product projectivized')
    require(zero_packet.origin == points, 'zero-product provenance lost')
    hostiles.append('nonzero-factors-zero-product-is-not-projective')
    negative = frozen(s.diag(-1,1))
    nr = readout(negative, apply(points, negative))
    require(nr['determinant_sign'] == -1 and nr['cross_ratio'] == str(source.four_point(points)), 'negative determinant control')
    hostiles.append('negative-determinant-not-positive-PSL')
    # Equal final maps need not identify retained words.
    identity = Step(('synthetic-I',), frozen(s.eye(2)))
    short = extend(empty(sid, points), (identity,))
    long = extend(empty(sid, points), (identity, identity))
    require(short != long and short.outputs[-1] == long.outputs[-1], 'execution history erased')
    hostiles.append('equal-output-does-not-identify-executions')
    require(rank_counts == {0:0, 1:9, 2:9} and len(collisions) == 9, 'rank census')
    require(all(sha256((ROOT/p).read_bytes()).hexdigest() == h for p,h in pins.items()), 'source drift')
    result = {'schema':'marici.nima.retained-projective-correspondence.v1','passed':True,
              'verdict':'retained_execution_composes_but_collapsed_readouts_do_not_reconstruct_cross_ratio',
              'native_prefix_cases':len(rows),'native_rank_counts':rank_counts,
              'native_prefix_readouts':rows,'rank_one_collisions':collisions,
              'zero_product_control':zr,'hostiles':hostiles,
              'scope':'Actual prefix words acting on a source-defined row packet; arbitrary word composition is a declared matrix envelope, not native continuation closure. Retention is not recovery from outputs or geometric emergence.',
              'real_endpoint_comparison_constructed':False,'source_sha256':pins}
    (ROOT/'research/nima/results/retained-projective-correspondence.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in result.items() if k not in ('source_sha256','native_prefix_readouts','rank_one_collisions')},indent=2))


if __name__ == '__main__':
    main()
