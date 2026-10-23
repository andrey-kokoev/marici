"""Pure geometric channel producer/assembler. No census or fixture I/O.
Source rule: the ordered-chamber Freudenthal construction in
research/voevodsky/checkers/check_esd7_explicit_analytical_census.py.
Geometric incidence is constructed; analytical coherence is only an obligation.
"""
from itertools import combinations, permutations, product
from collections import Counter

SCHEMA = 'marici.esd-geometric-attachment-channel.v1'


def require(condition, message):
    if not condition:
        raise ValueError(message)


def valid(v, scale):
    return 0 <= v[0] <= v[1] <= v[2] <= scale


def simplex(base, order):
    vertices = [tuple(base)]
    for axis in order:
        p = list(vertices[-1]); p[axis] += 1
        vertices.append(tuple(p))
    return tuple(vertices)


def placements(scale):
    # A rule over lattice sites, not a stored cell list or a fitted schedule.
    for base in product(range(scale), repeat=3):
        for order in permutations(range(3)):
            vertices = simplex(base, order)
            if all(valid(v, scale) for v in vertices):
                yield base, order


def orientation(order):
    return (-1) ** sum(order[i] > order[j] for i in range(3) for j in range(i+1, 3))


def produce(scale=7):
    require(type(scale) is int and 1 <= scale <= 16, 'scale must be an integer in1..16')
    yield {'type': 'open', 'schema': SCHEMA, 'scale': scale}
    for index, (base, order) in enumerate(placements(scale)):
        yield {'type': 'attach', 'occurrence': f'attachment-{index}', 'base': list(base), 'order': list(order)}
    yield {'type': 'close'}


def boundary(cell):
    return [(cell[:i]+cell[i+1:], (-1)**i) for i in range(len(cell))] if len(cell) > 1 else []


class Assembler:
    def __init__(self):
        self.scale = None; self.closed = False; self.failed = False
        self.cells = [set() for _ in range(4)]
        self.tetra_signs = {}; self.occurrences = {}; self.log = []; self.prefixes = []
        self.face_degrees = Counter(); self.oriented_boundary = Counter()

    def feed(self, record):
        require(not self.failed, 'failed replay requires a fresh assembler')
        try:
            self._feed(record)
        except Exception:
            self.failed = True
            raise

    def _feed(self, r):
        import copy
        require(not self.closed and isinstance(r, dict), 'closed or malformed channel')
        kind = r.get('type')
        if self.scale is None:
            require(set(r) == {'type', 'schema', 'scale'} and kind == 'open', 'opening required')
            require(r['schema'] == SCHEMA, 'unknown schema')
            require(type(r['scale']) is int and 1 <= r['scale'] <= 16, 'invalid scale')
            self.scale = r['scale']
        elif kind == 'attach':
            require(set(r) == {'type', 'occurrence', 'base', 'order'}, 'attachment fields')
            occurrence, base, order = r['occurrence'], r['base'], r['order']
            require(isinstance(occurrence, str) and 0 < len(occurrence) <= 128, 'occurrence identity')
            require(occurrence not in self.occurrences, 'duplicate occurrence')
            require(isinstance(base, list) and len(base) == 3 and all(type(x) is int for x in base), 'integer base')
            require(isinstance(order, list) and all(type(x) is int for x in order) and sorted(order) == [0,1,2], 'axis permutation')
            t = simplex(base, order)
            require(all(valid(v, self.scale) for v in t), 'attachment outside chamber')
            require(t not in self.cells[3], 'duplicate geometric attachment')
            sign = orientation(order)
            for rank in range(1,5):
                self.cells[rank-1].update(combinations(t, rank))
            self.tetra_signs[t] = sign; self.occurrences[occurrence] = t
            for face, s in boundary(t):
                self.face_degrees[face] += 1; self.oriented_boundary[face] += sign*s
                require(self.face_degrees[face] <= 2, 'nonmanifold face')
                if self.face_degrees[face] == 2:
                    require(self.oriented_boundary[face] == 0, 'shared oriented face fails cancellation')
        elif kind == 'close':
            require(set(r) == {'type'}, 'closing fields')
            expected = {simplex(base, order) for base, order in placements(self.scale)}
            require(self.cells[3] == expected, 'unfilled source-rule attachment obligations')
            # No inferred analytical filler is installed at geometric closure.
            self.closed = True
        else:
            raise ValueError('unknown record or second opening')
        self.log.append(copy.deepcopy(r))
        self.prefixes.append({'records': len(self.log), 'cells': [len(c) for c in self.cells],
                              'exposedFaces': sum(n == 1 for n in self.face_degrees.values()), 'closed': self.closed})

    def finish(self):
        require(self.closed and not self.failed, 'unfinished or failed assembly')
        ids = [{cell: f'{prefix}{i:03d}' for i, cell in enumerate(sorted(cells))}
               for prefix, cells in zip('VEFT', self.cells)]
        rows = []
        for dim, cells in enumerate(self.cells):
            table = []
            for cell in sorted(cells):
                row = {'id': ids[dim][cell], 'vertices': [ids[0][(v,)] for v in cell],
                       'boundary': [{'cell': ids[dim-1][face], 'sign': sign} for face, sign in boundary(cell)]}
                if dim == 0:
                    a,b,c = cell[0]
                    row.update(cumulative=list(cell[0]), barycentric=[a,b-a,c-b,self.scale-c])
                if dim >= 2:
                    row['edges'] = [ids[1][e] for e in combinations(cell, 2)]
                if dim == 2:
                    row['incidence'] = self.face_degrees[cell]
                    row['homotopyObligation'] = {'composite': [ids[1][(cell[0],cell[1])], ids[1][(cell[1],cell[2])]],
                                                  'direct': ids[1][(cell[0],cell[2])], 'discharged': False}
                if dim == 3:
                    row['faces'] = [ids[2][f] for f in combinations(cell, 3)]
                    row['orientation'] = self.tetra_signs[cell]
                    abc,abd,acd,bcd = row['faces']
                    row['coherenceObligation'] = {'H_ABC': abc, 'H_ABD': abd, 'H_ACD': acd, 'H_BCD': bcd,
                                                  'equation': 'H_ACD (d_CD * H_ABC) = H_ABD (H_BCD * d_AB)',
                                                  'discharged': False}
                table.append(row)
            rows.append(table)
        return {'schema': SCHEMA, 'scale': self.scale, 'vertices': rows[0], 'edges': rows[1],
                'triangles': rows[2], 'tetrahedra': rows[3], 'records': self.log, 'prefixes': self.prefixes,
                'occurrences': {name: ids[3][t] for name,t in self.occurrences.items()},
                'geometricClosure': True, 'analyticalCoherenceDischarged': False,
                'full114ChannelEstablished': False, 'globalFieldTransportEstablished': False}


def decode(records):
    assembler = Assembler()
    for record in records:
        assembler.feed(record)
    return assembler.finish()
