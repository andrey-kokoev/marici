"""One exact relative geometric constructor; no particle cases or target imports.

Generate point orbits under supplied affine isometries. Derive supporting facets
from the generated points, reserve marked orbit facets for external attachment,
and cone every other facet to the mean of the generated vertices.

The source metric, generators and orbit roles are mathematical inputs. This
constructs geometry; it does not assign coefficient operators or arrow counts.
"""
from fractions import Fraction as Q
from itertools import combinations
from pathlib import Path
import argparse
import hashlib
import json


def determinant(matrix):
    a = [list(row) for row in matrix]
    out = Q(1)
    for j in range(len(a)):
        p = next((i for i in range(j, len(a)) if a[i][j]), None)
        if p is None:
            return Q(0)
        if p != j:
            a[j], a[p] = a[p], a[j]
            out = -out
        v = a[j][j]
        out *= v
        for i in range(j+1, len(a)):
            q = a[i][j]/v
            for k in range(j+1, len(a)):
                a[i][k] -= q*a[j][k]
    return out


def dot_metric(a, b, G):
    return sum(a[i]*G[i][j]*b[j] for i in range(len(G)) for j in range(len(G)))


def subtract(a, b):
    return tuple(x-y for x, y in zip(a, b))


def apply(generator, point):
    matrix, translation = generator
    return tuple(sum(row[j]*point[j] for j in range(len(point)))+translation[i]
                 for i, row in enumerate(matrix))


def assemble(source, max_orbit_points=256):
    # Reject cell/face lists and unknown instruction fields rather than quietly
    # carrying a finished target through the input interface.
    if set(source) != {'metric', 'generators', 'seeds'}:
        raise ValueError('Source must contain exactly metric, generators and seeds')
    G = tuple(tuple(Q(x) for x in row) for row in source['metric'])
    d = len(G)
    if d < 1 or any(len(row) != d for row in G):
        raise ValueError('Metric must be a nonempty square matrix')
    if any(G[i][j] != G[j][i] for i in range(d) for j in range(d)):
        raise ValueError('Metric must be symmetric')
    if any(determinant([row[:k] for row in G[:k]]) <= 0 for k in range(1, d+1)):
        raise ValueError('Metric must be positive definite')
    generators = []
    for raw in source['generators']:
        if set(raw) != {'matrix', 'translation'}:
            raise ValueError('A generator requires only a matrix and translation')
        matrix = tuple(tuple(Q(x) for x in row) for row in raw['matrix'])
        translation = tuple(Q(x) for x in raw['translation'])
        if len(matrix) != d or any(len(row) != d for row in matrix) or len(translation) != d:
            raise ValueError('Generator dimension does not match metric')
        columns = list(zip(*matrix))
        if any(dot_metric(columns[i], columns[j], G) != G[i][j] for i in range(d) for j in range(d)):
            raise ValueError('Generator does not preserve the source metric')
        if determinant(matrix) != 1:
            raise ValueError('Generator is not orientation preserving')
        generators.append((matrix, translation))
    if not source['seeds']:
        raise ValueError('At least one seed is required')
    orbits = []
    for seed in source['seeds']:
        if set(seed) != {'point', 'role'} or seed['role'] not in {'carrier', 'external_interface', 'attachment_pole'}:
            raise ValueError('Seed must contain point and a declared geometric role')
        point = tuple(Q(x) for x in seed['point'])
        if len(point) != d:
            raise ValueError('Seed dimension does not match metric')
        orbit, frontier = {point}, [point]
        while frontier:
            p = frontier.pop()
            for generator in generators:
                q = apply(generator, p)
                if q not in orbit:
                    orbit.add(q)
                    frontier.append(q)
                    if len(orbit) > max_orbit_points:
                        raise ValueError('Point orbit exceeded the finite-construction resource bound')
        orbits.append((seed['role'], orbit))
    points = sorted(set().union(*(orbit for _, orbit in orbits)))
    if len(points) > max_orbit_points:
        raise ValueError('Combined orbits exceeded resource bound')
    if len(points) <= d or not any(determinant([subtract(p, points[0]) for p in chosen])
                                   for chosen in combinations(points[1:], d)):
        raise ValueError('Generated points do not span the supplied metric dimension')
    ids = {point: i for i, point in enumerate(points)}
    facets = set()
    for chosen in combinations(range(len(points)), d):
        base = points[chosen[0]]
        rows = [subtract(points[i], base) for i in chosen[1:]]
        sides = [determinant(rows+[subtract(p, base)]) for p in points]
        if not any(sides):
            continue
        if all(s >= 0 for s in sides) or all(s <= 0 for s in sides):
            facets.add(tuple(i for i, s in enumerate(sides) if s == 0))
    if not facets or any(len(f) != d for f in facets):
        raise ValueError('This constructor requires simplicial supporting facets')
    external_orbits = [{ids[p] for p in orbit} for role, orbit in orbits if role == 'external_interface']
    reserved = {f for f in facets if any(set(f) <= mark for mark in external_orbits)}
    for mark in external_orbits:
        if not any(set(f) <= mark for f in reserved):
            raise ValueError('An external-interface orbit contains no supporting facet')
    retained = set()
    for seed in source['seeds']:
        if seed['role'] == 'attachment_pole':
            pole = ids[tuple(Q(x) for x in seed['point'])]
            opposite = {f for f in facets if pole not in f}
            if len(opposite) != 1:
                raise ValueError('Attachment pole does not select a unique opposite facet')
            retained |= opposite
    if retained & reserved:
        raise ValueError('A facet cannot be both retained and omitted as external')
    admitted = facets-reserved
    if not admitted:
        raise ValueError('No internal carrier facets remain')
    center = tuple(sum(p[k] for p in points)/len(points) for k in range(d))
    oriented, cone_determinants = [], []
    for f in sorted(admitted):
        order = list(f)
        value = determinant([subtract(points[i], center) for i in order])
        if value == 0:
            raise ValueError('Degenerate center-to-facet cone')
        if value < 0:
            order[0], order[1] = order[1], order[0]
        oriented.append(order)
        cone_determinants.append(str(abs(value)))
    distances = [[dot_metric(subtract(a, b), subtract(a, b), G) for b in points] for a in points]
    result = {
        'dimension': d, 'vertices': [list(map(str, p)) for p in points],
        'metric': [list(map(str, row)) for row in G],
        'squared_distances': [list(map(str, row)) for row in distances],
        'seed_orbits': [{'role': role, 'vertices': sorted(ids[p] for p in orbit)} for role, orbit in orbits],
        'supporting_facets': [list(f) for f in sorted(facets)],
        'external_interfaces': [list(f) for f in sorted(reserved)],
        'retained_attachment_interfaces': [list(f) for f in sorted(retained)],
        'carrier_facets': oriented, 'center': list(map(str, center)),
        'center_vertex_id': len(points),
        'cone_cells': [[len(points)]+f for f in oriented],
        'positive_cone_determinants_in_source_coordinates': cone_determinants,
        'counts': {'vertices': len(points), 'supporting_facets': len(facets),
                   'external_interfaces': len(reserved), 'carrier_facets': len(admitted),
                   'cone_cells': len(admitted)},
    }
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source', required=True)
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    raw = Path(args.source).read_bytes()
    result = assemble(json.loads(raw))
    result['source_sha256'] = hashlib.sha256(raw).hexdigest()
    result['constructor_sha256'] = hashlib.sha256(Path(__file__).read_bytes()).hexdigest()
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(result['counts']))


if __name__ == '__main__':
    main()
