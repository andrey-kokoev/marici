"""Compare a specified S3 filtration with actual seed incidence and cofiber models.

Exact, dependency-free bounded tests. The zero-arrow example lives in
Perf(Q) x Perf(Q), so its two K0 generators are independent. It is a
counterexample model, not a claimed realization of the universal source.
"""
import ast
from collections import Counter
from itertools import combinations, product
from pathlib import Path
import hashlib
import json
from check_triangle_half_phase import TwoPacket, cycle_from_packets, mm, I

ROOT = Path(__file__).resolve().parents[3]
SEED = ROOT/'research/nima/checkers/check_two_triangle_half_phase.py'
HELPER = ROOT/'research/nima/checkers/check_triangle_half_phase.py'
TORUS = ROOT/'research/nima/check_tate_torus_cofiber_octahedra.py'


def read_seed_declarations():
    """Read the actual literal left/right primitives without running their audit."""
    module = ast.parse(SEED.read_text(encoding='utf-8'))
    main = next(n for n in module.body if isinstance(n, ast.FunctionDef) and n.name == 'main')
    out = {}
    for node in main.body:
        if not isinstance(node, ast.Assign) or len(node.targets) != 1:
            continue
        target = node.targets[0]
        if not isinstance(target, ast.Name) or target.id not in ('left', 'right'):
            continue
        assert isinstance(node.value, ast.Tuple)
        packets = []
        for call in node.value.elts:
            assert isinstance(call, ast.Call) and isinstance(call.func, ast.Name)
            assert call.func.id == 'TwoPacket' and len(call.args) == 3 and not call.keywords
            packets.append(TwoPacket(*(ast.literal_eval(a) for a in call.args)))
        out[target.id] = tuple(packets)
    assert set(out) == {'left', 'right'}
    return out


def add(a, b): return tuple(x+y for x, y in zip(a, b))
def neg(a): return tuple(-x for x in a)
def minus(a, b): return add(a, neg(b))
def signed_edge(i, j): return ((min(i, j), max(i, j)), 1 if i < j else -1)
def boundary(cycle):
    result = Counter()
    for i, j in cycle:
        edge, sign = signed_edge(i, j)
        result[edge] += sign
    return {e: c for e, c in result.items() if c}


def signature(obj):
    """Homology signature of a zero-differential, two-colour complex."""
    return Counter((degree, colour) for _, degree, colour in obj)
def euler(obj):
    return tuple(sum((-1)**degree for _, degree, c in obj if c == colour)
                 for colour in ('X', 'Y'))
def shift(obj): return tuple(('s'+name, degree+1, colour) for name, degree, colour in obj)
def connecting_rank(source, target, mapping):
    src = {name: (degree, colour) for name, degree, colour in source}
    tgt = {name: (degree, colour) for name, degree, colour in target}
    assert all(a in src and b in tgt and src[a] == tgt[b] for a, b in mapping.items())
    assert len(set(mapping.values())) == len(mapping)
    return len(mapping)  # These declared maps send distinct basis vectors to distinct basis vectors.


def zero_arrow_triangle(a, b):
    c = b + shift(a)
    return (a, b, c, {}, {name: name for name, _, _ in b},
            {name: name for name, _, _ in shift(a)})


def coordinate_inclusion_triangle(a, b):
    assert set(a) <= set(b)
    c = tuple(v for v in b if v not in a)
    return (a, b, c, {name: name for name, _, _ in a},
            {name: name for name, _, _ in c}, {})


def verify_homology_exactness(triangle):
    a, b, c, f, q, delta = triangle
    connecting_rank(a, b, f)
    connecting_rank(b, c, q)
    rank_delta = connecting_rank(c, shift(a), delta)
    assert not set(f.values()) & set(q) and not set(q.values()) & set(delta)
    def rank_at(obj, mapping, degree, colour):
        return sum(name in mapping and (n, k) == (degree, colour) for name, n, k in obj)
    for n in range(-1, 4):
        for colour in ('X', 'Y'):
            rf = rank_at(a, f, n, colour)
            rq = rank_at(b, q, n, colour)
            rd = rank_at(c, delta, n, colour)
            assert rf + rank_at(c, delta, n+1, colour) == signature(a)[(n, colour)]
            assert rf + rq == signature(b)[(n, colour)]
            assert rq + rd == signature(c)[(n, colour)]
    return rank_delta


def main():
    seed = read_seed_declarations()
    labels = dict(zip('ABCD', range(4)))
    cycles = {name: tuple((labels[p.source], labels[p.target]) for p in packets)
              for name, packets in seed.items()}
    assert cycles == {'left': ((0, 1), (1, 2), (2, 0)),
                      'right': ((1, 0), (0, 3), (3, 1))}
    faces = {'012': cycles['left'], '013': cycles['right'],
             '023': ((0, 2), (2, 3), (3, 0)),
             '123': ((1, 3), (3, 2), (2, 1))}
    total_boundary = Counter()
    for cycle in faces.values(): total_boundary.update(boundary(cycle))
    assert all(n == 0 for n in total_boundary.values())
    for packets in seed.values():
        C = cycle_from_packets(packets)
        assert mm(mm(C, C), C) == I

    # Integral K0 already sees the oriented face relations.
    vertex_classes = ((0, 0), (1, 0), (0, 1), (1, 1))
    classes = {(i, j): minus(vertex_classes[j], vertex_classes[i])
               for i, j in combinations(range(4), 2)}
    for cycle in faces.values():
        value = (0, 0)
        for i, j in cycle: value = add(value, minus(vertex_classes[j], vertex_classes[i]))
        assert value == (0, 0)
    mod2 = {edge: tuple(c % 2 for c in value) for edge, value in classes.items()}
    fibers = {}
    for edge, value in mod2.items(): fibers.setdefault(value, []).append(edge)
    assert {tuple(v) for v in fibers.values()} == {
        ((0, 1), (2, 3)), ((0, 2), (1, 3)), ((0, 3), (1, 2))}
    assert minus(classes[(0, 3)], classes[(1, 2)]) == (2, 0)

    # Lawful stable counterexample: X and Y are independent coloured simples, f=0.
    X = (('x', 0, 'X'),)
    Y = (('y', 0, 'Y'),)
    cone = Y + shift(X)
    objects = {(0, 1): X, (0, 2): Y, (0, 3): X+Y,
               (1, 2): cone, (1, 3): X+cone, (2, 3): X}
    assert all(euler(obj) == classes[edge] for edge, obj in objects.items())
    assert signature(objects[(0, 1)]) == signature(objects[(2, 3)])
    assert signature(objects[(0, 2)]) != signature(objects[(1, 3)])
    assert signature(objects[(0, 3)]) != signature(objects[(1, 2)])
    triangles = {'012': ((0, 1), (0, 2), (1, 2)),
                 '013': ((0, 1), (0, 3), (1, 3)),
                 '023': ((0, 2), (0, 3), (2, 3)),
                 '123': ((1, 2), (1, 3), (2, 3))}
    actual_triangles = {'012': zero_arrow_triangle(X, Y),
                        '013': zero_arrow_triangle(X, X+Y),
                        '023': coordinate_inclusion_triangle(Y, X+Y),
                        '123': coordinate_inclusion_triangle(cone, X+cone)}
    connecting = {}
    for name, (a, b, c) in triangles.items():
        assert actual_triangles[name][:3] == (objects[a], objects[b], objects[c])
        assert euler(objects[b]) == add(euler(objects[a]), euler(objects[c]))
        connecting[name] = verify_homology_exactness(actual_triangles[name])
    assert connecting == {'012': 1, '013': 1, '023': 0, '123': 0}
    # Suspension signs are integral data erased by mod 2.
    assert euler(shift(X)) == (-1, 0) != euler(X)
    assert tuple(v % 2 for v in euler(shift(X))) == tuple(v % 2 for v in euler(X))

    # Actual coordinate-support model: explicit delta bases and complement sections.
    window = tuple(product((-1, 0, 1), repeat=4))
    subsets = (frozenset(), frozenset({0}), frozenset({0, 1}), frozenset({0, 1, 2}))
    spaces = [{v for v in window if all(i in S or v[i] == 0 for i in range(4))}
              for S in subsets]
    quotient_bases = {(i, j): spaces[j]-spaces[i] for i, j in combinations(range(4), 2)}
    assert [len(S) for S in spaces] == [1, 3, 9, 27]
    for a, b, c in triangles.values():
        left, middle, right = (quotient_bases[k] for k in (a, b, c))
        assert not left & right and left | right == middle
        # Quotient projection kills left and is identity on right; its section
        # includes the same delta labels, so connecting maps are zero.
        section = {v: v for v in right}
        assert all(section[v] in middle and section[v] not in left for v in right)
    support_dims = {''.join(map(str, e)): len(v) for e, v in quotient_bases.items()}
    assert all(dim % 2 == 0 for dim in support_dims.values())
    all_subsets = [frozenset(c) for n in range(5) for c in combinations(range(4), n)]
    nested_triples = sum(A <= B <= C for A in all_subsets for B in all_subsets for C in all_subsets)
    nested_quadruples = sum(A <= B <= C <= D for A in all_subsets for B in all_subsets
                            for C in all_subsets for D in all_subsets)
    assert nested_triples == 256 and nested_quadruples == 625

    inputs = [Path(__file__).resolve(), SEED, HELPER, TORUS]
    report = {
        'schema': 'marici.nima.s3-filtration-seed-faces.v1',
        'status': 'passed',
        'disposition': 'integral_oriented_incidence_matches; stable_seed_comparison_not_supplied; faithful_identification_with_split_support_model_refuted_in_general',
        'source_assumption': 'K0 classes of X and Y independent; chosen filtration 0,X,Y,X+Y',
        'actual_seed_cycles': cycles,
        'oriented_face_signs': {'012': 1, '013': -1, '023': 1, '123': -1},
        'integral_edge_classes': {''.join(map(str, e)): v for e, v in classes.items()},
        'mod2_edge_fibers': {str(k): v for k, v in fibers.items()},
        'integral_face_relations_checked': len(faces),
        'counterexample_category': 'Perf(Q) x Perf(Q), independent simples X,Y and f=0',
        'connecting_map_ranks': connecting,
        'equal_mod2_pair_objects_can_be_inequivalent': True,
        'coordinate_support_quotient_dimensions': support_dims,
        'coordinate_support_connecting_maps': 'all zero in underlying derived vector-space model',
        'coordinate_support_scalar_mod2_classes': 'all zero at this finite window',
        'legacy_checker_scope': {'nested_triples': nested_triples,
                                 'four_stage_chains_not_enumerated_by_legacy_checker': nested_quadruples,
                                 'only_dimensions_and_subset_rotation_tested': True},
        'residual': 'No specified comparison sending the seed TwoPacket cycles and coefficient rotation to stable objects, connecting morphisms and suspension isomorphisms.',
        'not_claimed': ['No exact functor exists', 'Splitness forbids a separate cyclic coefficient action',
                        'Universal stable source has been identified', 'Physical interpretation'],
        'source_sha256': {str(p.relative_to(ROOT)).replace('\\', '/'): hashlib.sha256(p.read_bytes()).hexdigest()
                          for p in inputs},
    }
    dest = ROOT/'research/nima/results/s3-filtration-seed-faces.json'
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(json.dumps(report, indent=2)+'\n', encoding='utf-8')
    print('PASS: actual seed cycles, four integral signed face relations, and mod-2 opposite pairs.')
    print('COUNTEREXAMPLE: connecting ranks 1,1,0,0; equal mod-2 classes do not identify cofibers.')
    print('SUPPORT MODEL: four split faces, scalar mod-2 quotient classes all zero.')
    print('OPEN: comparison preserving seed morphisms, coefficient operation and suspension.')


if __name__ == '__main__':
    main()
