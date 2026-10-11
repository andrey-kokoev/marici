"""Source-driven version of the centroid-triangle / three-stage constructor.

Input supplies directed arrows and rational 3D vertex coordinates. Every complete
oriented three-cycle supplies a vertex permutation (fixing the other vertices).
The existing cyclic-sector, frame transport and dense-feedback rules are fixed.
No expected group order, triangle count or arrow count is input or asserted.
"""
from itertools import permutations
from pathlib import Path
from fractions import Fraction as F
import hashlib
import json

from check_twelve_triangle_positive_geometry import (
    I, C, ONE, ZERO, OMEGA, transpose, inv, mm, mv, det, mean, boundary,
    projector, zmv, zmm, zreal, zmul, zadd, znorm,
)


def assemble(source):
    labels = tuple(source['vertices'])
    points = {k: tuple(F(x) for x in source['vertices'][k]) for k in labels}
    if not labels or any(len(v) != 3 for v in points.values()):
        raise ValueError('Vertices must supply rational three-dimensional coordinates')
    edges = {tuple(e) for e in source['arrows']}
    if any(len(e) != 2 or any(k not in points for k in e) for e in edges):
        raise ValueError('Every arrow must have two registered endpoints')
    # Canonicalize rotations, not reversal: ABC and ACB are different cycles.
    cycles = sorted({min((t, t[1:]+t[:1], t[2:]+t[:2]))
                     for t in permutations(labels, 3)
                     if all((t[i], t[(i+1) % 3]) in edges for i in range(3))})
    if not cycles:
        raise ValueError('Source has no complete oriented triangle; no reference frame is available')
    identity = tuple(range(len(labels)))
    generators = []
    for cycle in cycles:
        mapping = dict(zip(cycle, cycle[1:]+cycle[:1]))
        generators.append(tuple(labels.index(mapping.get(k, k)) for k in labels))
    group = {identity}
    frontier = [identity]
    while frontier:
        q = frontier.pop()
        for g in generators:
            p = tuple(g[q[i]] for i in identity)
            if p not in group:
                group.add(p)
                frontier.append(p)
    ref = cycles[0]
    frame = transpose((mean([points[k] for k in ref]), points[ref[0]], points[ref[1]]))
    if det(frame) == 0:
        raise ValueError('Reference centroid-edge frame is singular')
    frame_inverse = inv(frame)
    coeff = (ONE, OMEGA, zmul(OMEGA, OMEGA))
    rotations, vectors, projectors, triangles, rows = [], [], [], [], []
    all_points = dict(points)
    for p in sorted(group):
        mapped = tuple(labels[p[labels.index(k)]] for k in ref)
        centre = 'F_' + '_'.join(sorted(mapped))
        all_points[centre] = mean([points[k] for k in mapped])
        tri = (centre, mapped[0], mapped[1])
        X = transpose(tuple(all_points[k] for k in tri))
        R = mm(X, frame_inverse)
        if det(R) != 1 or mm(transpose(R), R) != I:
            raise ValueError('Arrow-derived permutation is not a proper rotation of the supplied geometry')
        if any(mv(R, points[k]) != points[labels[p[i]]] for i, k in enumerate(labels)):
            raise ValueError('Arrow-derived permutation does not realize the supplied vertices')
        v = zmv(X, coeff)
        rotations.append(R)
        vectors.append(v)
        projectors.append(projector(v))
        triangles.append(tri)
        rows.append({'outer_arrow': list(mapped[:2]), 'triangle': list(tri)})
    m = len(rotations)
    dimension = 3*m
    local = tuple(tuple(projectors[i//3][i%3][j%3] if i//3 == j//3 else ZERO
                        for j in range(dimension)) for i in range(dimension))
    blocks = [[mm(R, transpose(S)) for S in rotations] for R in rotations]
    alignment = zreal(tuple(tuple(blocks[i//3][j//3][i%3][j%3]/m
                                  for j in range(dimension)) for i in range(dimension)))
    collective = zmm(alignment, local)
    assembled = tuple(z for v in vectors for z in v)
    if collective != zmm(local, alignment) or collective != projector(assembled):
        raise ValueError('Local and alignment maps do not yield the required collective eigenline')
    if zmm(collective, collective) != collective:
        raise ValueError('Collective map is not idempotent')
    stages = []
    for stage, matrix in enumerate((local, alignment, collective)):
        stages.append({((stage, i), ((stage+1) % 3, j)): matrix[j][i]
                       for i in range(dimension) for j in range(dimension)
                       if matrix[j][i] != ZERO})
    all_arrows = set().union(*(set(s) for s in stages))
    used, cycle_count, weight_sum = set(), 0, ZERO
    positive = True
    for closing, z in stages[2].items():
        k, i = closing[0][1], closing[1][1]
        for b in range(dimension):
            e0, e1 = ((0, i), (1, b)), ((1, b), (2, k))
            if e0 not in stages[0] or e1 not in stages[1]:
                continue
            weight = zmul(zmul(stages[0][e0], stages[1][e1]), z)
            positive &= weight[1] == 0 and weight[0] > 0
            weight_sum = zadd(weight_sum, weight)
            cycle_count += 1
            used.update((e0, e1, closing))
    if weight_sum != ONE:
        raise ValueError('Closed trace does not equal one')
    def port(v):
        stage, i = v
        return [('raw', 'local', 'aligned')[stage], ''.join(rows[i//3]['outer_arrow']), 'xyz'[i%3]]
    manifest = [{'source': port(src), 'target': port(dst),
                 'weight_real': str(weight[0]), 'weight_imag_sqrt3': str(weight[1])}
                for arrows in stages for (src, dst), weight in sorted(arrows.items())]
    surface_edges = {tuple(sorted((a, b))) for t in triangles for a, b in zip(t, t[1:]+t[:1])}
    report = {
        'input_arrows': [list(e) for e in sorted(edges)],
        'derived_cycles': [list(c) for c in cycles],
        'proper_rotations': len(group), 'triangles': len(triangles),
        'boundary_chain_zero': not boundary(triangles),
        'vertices': len(all_points), 'undirected_edges': len(surface_edges),
        'signed_volume': str(sum(det(transpose(tuple(all_points[k] for k in t)))/6 for t in triangles)),
        'arrows_per_stage': list(map(len, stages)),
        'unique_directed_arrows': len(all_arrows),
        'closed_three_step_cycles': cycle_count,
        'return_cycle_union_measure': len(used),
        'closed_walk_union_covers_every_arrow': used == all_arrows,
        'closed_cycle_weights_positive': positive,
        'closed_cycle_weight_sum': [str(x) for x in weight_sum],
        'triangles_and_transports': rows,
        'assembled_norm_squared': str(sum(znorm(z) for z in assembled)),
        'rule': 'complete directed triangle permutations; centroid-edge orbit; cyclic eigenline; local selection, alignment, dense collective feedback',
    }
    return report, manifest


def run(source_path, output_dir):
    raw = Path(source_path).read_bytes()
    report, manifest = assemble(json.loads(raw))
    report['source_sha256'] = hashlib.sha256(raw).hexdigest()
    dest = Path(output_dir)
    dest.mkdir(parents=True, exist_ok=True)
    (dest/'assembly.json').write_text(json.dumps(report, indent=2)+'\n')
    (dest/'arrows.json').write_text(json.dumps(manifest, indent=2)+'\n')
    print(json.dumps({k: report[k] for k in (
        'derived_cycles', 'triangles', 'boundary_chain_zero', 'arrows_per_stage',
        'return_cycle_union_measure', 'closed_walk_union_covers_every_arrow')}))
