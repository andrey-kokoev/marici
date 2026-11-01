"""Exact whole-assembly cloning of a regular 4-simplex.

Coordinates x=(u,v,s,t) mean v0+u(v1-v0)+v(v2-v0)+s(v3-g)+t(v4-g),
where vi=ei-(1,1,1,1,1)/5 and g=(v0+v1+v2)/3. The last two
basis vectors are orthogonal to the working triangular plane.
"""
from dataclasses import dataclass
from fractions import Fraction as Q
from itertools import combinations

ZERO = (Q(0),) * 4
IDENTITY = tuple(tuple(Q(i == j) for j in range(4)) for i in range(4))
GRAM = ((Q(2), Q(1), Q(0), Q(0)), (Q(1), Q(2), Q(0), Q(0)),
        (Q(0), Q(0), Q(4, 3), Q(1, 3)), (Q(0), Q(0), Q(1, 3), Q(4, 3)))
SEED = ((Q(0), Q(0), Q(0), Q(0)), (Q(1), Q(0), Q(0), Q(0)),
        (Q(0), Q(1), Q(0), Q(0)), (Q(1, 3), Q(1, 3), Q(1), Q(0)),
        (Q(1, 3), Q(1, 3), Q(0), Q(1)))


def add(x, y):
    return tuple(a + b for a, b in zip(x, y))


def sub(x, y):
    return tuple(a - b for a, b in zip(x, y))


def mv(a, x):
    return tuple(sum(v * w for v, w in zip(row, x)) for row in a)


def mm(a, b):
    return tuple(tuple(sum(a[i][k] * b[k][j] for k in range(len(b)))
                       for j in range(len(b[0]))) for i in range(len(a)))


def transpose(a):
    return tuple(zip(*a))


def inner(x, y):
    return sum(a * b for a, b in zip(x, mv(GRAM, y)))


def embed5(x):
    u, v, s, t = x
    return (Q(4, 5) - u - v - (s + t) / 3,
            Q(-1, 5) + u - (s + t) / 3,
            Q(-1, 5) + v - (s + t) / 3,
            Q(-1, 5) + s, Q(-1, 5) + t)


@dataclass(frozen=True)
class Affine:
    linear: tuple = IDENTITY
    offset: tuple = ZERO

    def __call__(self, x):
        return add(mv(self.linear, x), self.offset)

    def after(self, other):
        """self composed with other, including its translation."""
        return Affine(mm(self.linear, other.linear), add(mv(self.linear, other.offset), self.offset))

    def isometry(self):
        return mm(mm(transpose(self.linear), GRAM), self.linear) == GRAM

    def cell(self):
        return tuple(self(x) for x in SEED)


def planar(linear, offset=(Q(0), Q(0))):
    a = [list(row) for row in IDENTITY]
    for i in range(2):
        for j in range(2):
            a[i][j] = Q(linear[i][j])
    return Affine(tuple(map(tuple, a)), tuple(map(Q, offset)) + (Q(0), Q(0)))


def rotation(center=(Q(0), Q(0))):
    r = ((Q(-1), Q(-1)), (Q(1), Q(0)))
    return planar(r, sub(center, mv(r, center)))


def reflection(normal, level):
    """Reflect in n.u=h, extended identically on the orthogonal complement."""
    n = tuple(map(Q, normal))
    inv_g = ((Q(2, 3), Q(-1, 3)), (Q(-1, 3), Q(2, 3)))
    z = mv(inv_g, n)
    denominator = sum(a * b for a, b in zip(n, z))
    assert denominator > 0
    a = tuple(tuple(Q(i == j) - 2 * z[i] * n[j] / denominator for j in range(2)) for i in range(2))
    return planar(a, tuple(2 * Q(level) * v / denominator for v in z))


@dataclass(frozen=True)
class Copy:
    id: str
    parent: str | None
    word: tuple
    frame: Affine

    @property
    def vertices(self):
        return self.frame.cell()


def clone_all(copies, operation, name):
    old = tuple(copies)
    children = tuple(Copy('c' + str(len(old) + i), c.id, c.word + (name,), operation.after(c.frame))
                     for i, c in enumerate(old))
    return old + children


def supporting_edge(copies, normal=(Q(1), Q(1))):
    def height(p):
        return sum(a * b for a, b in zip(normal, p[:2]))
    h = max(height(p) for c in copies for p in c.vertices)
    edges = []
    for c in copies:
        for i, j in combinations(range(5), 2):
            if height(c.vertices[i]) == h == height(c.vertices[j]):
                edges.append({'copy': c.id, 'labels': (i, j), 'vertices': (c.vertices[i], c.vertices[j])})
    if not edges:
        raise ValueError('The supporting hyperplane meets no actual simplex edge')
    return h, edges


def construct(first_center=(Q(0), Q(0)), second_center=(Q(0), Q(0))):
    copies = (Copy('c0', None, (), Affine()),)
    stages = [copies]
    w = reflection((0, 1), 0)
    r1 = rotation(first_center)
    copies = clone_all(copies, w, 'white-reflection')
    stages.append(copies)
    copies = clone_all(copies, r1, 'first-rotation')
    stages.append(copies)
    h, edges = supporting_edge(copies)
    red = reflection((1, 1), h)
    copies = clone_all(copies, red, 'outer-red-reflection')
    stages.append(copies)
    r2 = rotation(second_center)
    copies = clone_all(copies, r2, 'second-rotation')
    stages.append(copies)
    return stages, {'white': w, 'rotation1': r1, 'red': red, 'rotation2': r2}, h, edges


def geometry_groups(copies):
    groups = {}
    for c in copies:
        groups.setdefault(tuple(sorted(c.vertices)), []).append(c)
    return list(groups.values())


def cross(a, b):
    return a[0] * b[1] - a[1] * b[0]


def halfplanes(triangle):
    points = list(triangle)
    if cross(sub(points[1], points[0]), sub(points[2], points[0])) < 0:
        points.reverse()
    result = []
    for a, b in zip(points, points[1:] + points[:1]):
        delta = sub(b, a)
        n = (-delta[1], delta[0])
        result.append((n, sum(x * y for x, y in zip(n, a))))
    return result


def triangle_intersection(a, b):
    """Vertices of the exact intersection of two closed projected triangles."""
    inequalities = halfplanes(a) + halfplanes(b)
    vertices = set()
    for (n, h), (m, k) in combinations(inequalities, 2):
        det = cross(n, m)
        if not det:
            continue
        x = ((h * m[1] - n[1] * k) / det, (n[0] * k - h * m[0]) / det)
        if all(sum(u * v for u, v in zip(q, x)) >= t for q, t in inequalities):
            vertices.add(x)
    return tuple(sorted(vertices))


def dimension(vertices):
    if not vertices:
        return -1
    if len(vertices) == 1:
        return 0
    a, b = vertices[:2]
    return 2 if any(cross(sub(b, a), sub(c, a)) for c in vertices[2:]) else 1


def contact_analysis(copies):
    groups = geometry_groups(copies)
    cells = [g[0].vertices for g in groups]
    # Each hidden vertex projects strictly inside the working triangle.
    # Consequently a boundary intersection of projected triangles can only
    # contain zero-hidden-coordinate points of either full simplex.
    for vs in cells:
        for p in vs[3:]:
            assert all(sum(n[i] * p[i] for i in range(2)) > h for n, h in halfplanes([v[:2] for v in vs[:3]]))
    adjacency = {i: [] for i in range(len(cells))}
    intersections, contacts = [], []
    for i, j in combinations(range(len(cells)), 2):
        points = triangle_intersection([v[:2] for v in cells[i][:3]], [v[:2] for v in cells[j][:3]])
        dim = dimension(points)
        assert dim < 2, 'Distinct projected interiors overlap: full intersection analysis needed'
        full = tuple(p + (Q(0), Q(0)) for p in points)
        intersections.append({'cells': (i, j), 'dimension': dim, 'vertices': full})
        if dim != 1:
            continue
        assert len(full) == 2
        assert all(v in cells[i] and v in cells[j] for v in full), 'Contact is not a complete shared edge'
        a, b = points
        delta = sub(b, a)
        n = (-delta[1], delta[0])
        h = sum(x * y for x, y in zip(n, a))
        seam = reflection(n, h)
        assert seam.isometry() and seam.after(seam) == Affine()
        assert all(seam(p) == p for p in full)
        assert set(map(seam, cells[i])) == set(cells[j]), 'Seam does not match all five vertices'
        permutation = tuple(cells[j].index(seam(v)) for v in cells[i])
        edge = {'cells': (i, j), 'vertices': full, 'map': seam, 'labelPermutation': permutation}
        contacts.append(edge)
        adjacency[i].append(j)
        adjacency[j].append(i)
    return groups, intersections, contacts, adjacency


def core_cycle(adjacency):
    remaining = set(adjacency)
    while True:
        leaves = {v for v in remaining if sum(w in remaining for w in adjacency[v]) < 2}
        if not leaves:
            break
        remaining -= leaves
    assert remaining and all(sum(w in remaining for w in adjacency[v]) == 2 for v in remaining)
    start = min(remaining)
    cycle = [start]
    previous = None
    while True:
        choices = sorted(w for w in adjacency[cycle[-1]] if w in remaining and w != previous)
        nxt = choices[0]
        if nxt == start:
            break
        assert nxt not in cycle
        previous = cycle[-1]
        cycle.append(nxt)
    assert set(cycle) == remaining
    return cycle
