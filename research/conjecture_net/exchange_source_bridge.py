"""Faithful retained exchange-to-metric-spectral structural bridge.

Uses live pinned source receipts, exact rational matrices and actual typed ports.
The analytic spectral extension is declared mathematics, not physical actuation.
"""
import ast
from fractions import Fraction as F
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[2]
SOURCE = 'research/nima/results/predictive-pair-exchange-residual.json'
BINDING = 'research/nima/results/seed-port-exchange-binding.json'


def zeros(rows, columns=None):
    return [[F(0) for _ in range(rows if columns is None else columns)] for _ in range(rows)]


def identity(n):
    result = zeros(n)
    for i in range(n):
        result[i][i] = F(1)
    return result


def decode(rows):
    return [[F(value) for value in row] for row in rows]


def add(a, b):
    return [[x + y for x, y in zip(row, other)] for row, other in zip(a, b)]


def scale(c, a):
    return [[c * value for value in row] for row in a]


def transpose(a):
    return [list(row) for row in zip(*a)]


def mul(a, b):
    if not a or not b or len(a[0]) != len(b):
        raise ValueError('matrix domain mismatch')
    result = zeros(len(a), len(b[0]))
    for i, row in enumerate(a):
        for k, coefficient in enumerate(row):
            if coefficient:
                for j, value in enumerate(b[k]):
                    if value:
                        result[i][j] += coefficient * value
    return result


def outer(column, row):
    return [[a * b for b in row] for a in column]


def block_diagonal(a, b):
    return [row + [F(0)] * len(b) for row in a] + [[F(0)] * len(a) + row for row in b]


def invert(a):
    n = len(a)
    rows = [list(row) + list(unit) for row, unit in zip(a, identity(n))]
    for column in range(n):
        pivot = next((r for r in range(column, n) if rows[r][column]), None)
        if pivot is None:
            raise ValueError('singular matrix')
        rows[column], rows[pivot] = rows[pivot], rows[column]
        divisor = rows[column][column]
        rows[column] = [value / divisor for value in rows[column]]
        for r in range(n):
            if r != column and rows[r][column]:
                factor = rows[r][column]
                rows[r] = [x - factor * y for x, y in zip(rows[r], rows[column])]
    return [row[n:] for row in rows]


def ldl(a):
    if transpose(a) != a:
        raise ValueError('metric is not symmetric')
    n = len(a)
    lower = identity(n)
    diagonal = []
    for j in range(n):
        pivot = a[j][j] - sum(lower[j][k] ** 2 * diagonal[k] for k in range(j))
        if pivot <= 0:
            raise ValueError('metric is not positive definite')
        diagonal.append(pivot)
        for i in range(j + 1, n):
            lower[i][j] = (a[i][j] - sum(lower[i][k] * lower[j][k] * diagonal[k] for k in range(j))) / pivot
    return lower, diagonal


def actual_ports():
    # Read the primary literal without importing its producer/dependencies or
    # executing a SymPy/NumPy proof pipeline in this audit.
    path = ROOT / 'research/nima/checkers/check_natural_tower_return.py'
    tree = ast.parse(path.read_text(encoding='utf-8'))
    for node in tree.body:
        if isinstance(node, ast.Assign) and any(isinstance(target, ast.Name) and target.id == 'PACKETS' for target in node.targets):
            return {label: (source, target) for label, source, target in ast.literal_eval(node.value)}
    raise ValueError('actual source port registry not found')


def validate_word(word, ports):
    if not word or any(label not in ports for label in word):
        raise ValueError('nonempty actual port word required')
    if any(ports[a][1] != ports[b][0] for a, b in zip(word, word[1:])):
        raise ValueError('unmatched source port seam')
    return ports[word[0]][0], ports[word[-1]][1]


def word_matrix(word, operators, ports):
    validate_word(word, ports)
    result = identity(len(next(iter(operators.values()))))
    for label in word:
        result = mul(operators[label], result)
    return result


def execute(word, state, operators, ports, batch_id, source_vertex):
    start, _ = validate_word(word, ports)
    if source_vertex != start:
        raise ValueError('state/source vertex attachment mismatch')
    if not isinstance(batch_id, str) or not batch_id:
        raise ValueError('explicit occurrence batch identity required')
    n = len(next(iter(operators.values())))
    if len(state) != n:
        raise ValueError('state/source domain mismatch')
    current = tuple(F(value) for value in state)
    records = []
    for index, label in enumerate(word):
        before = current
        current = tuple(row[0] for row in mul(operators[label], [[value] for value in current]))
        records.append({'occurrence_id': (batch_id, index), 'port': label, 'endpoints': ports[label],
                        'before': before, 'after': current})
    return current, tuple(records)


class ExecutionLedger:
    """Batch-scoped occurrence allocator; rejected requests reserve no IDs."""
    def __init__(self):
        self.used_batches = set()

    def execute(self, word, state, operators, ports, batch_id, source_vertex):
        if not isinstance(batch_id, str) or not batch_id:
            raise ValueError('explicit occurrence batch identity required')
        if batch_id in self.used_batches:
            raise ValueError('execution batch identity already used')
        output, records = execute(word, state, operators, ports, batch_id, source_vertex)
        self.used_batches.add(batch_id)
        return output, records


def source_model():
    source = json.loads((ROOT / SOURCE).read_text())
    binding = json.loads((ROOT / BINDING).read_text())
    if source['status'] != 'pass' or binding['status'] != 'pass':
        raise ValueError('source receipt did not pass')
    decomposition = source['decomposition']
    ports = actual_ports()
    reduced = {label: decode(matrix) for label, matrix in decomposition['port_updates'].items()}
    labels = tuple(reduced)
    if set(labels) != set(ports):
        raise ValueError('source ports differ from exported updates')
    g4 = [[F(10 * int(i == j) + 1) for j in range(4)] for i in range(4)]
    h = [[g4[i // 4][j // 4] * g4[i % 4][j % 4] for j in range(16)] for i in range(16)]
    features = zeros(16, 6)
    for column, label in enumerate(labels):
        a, b = ports[label]
        slot = 4 * 'ABCD'.index(a) + 'ABCD'.index(b)
        if binding['port_binding'][label] != 121 + slot:
            raise ValueError('source feature/port binding mismatch')
        features[slot][column] = F(1, 11)
    metric = block_diagonal(h, identity(6))
    raw = {}
    for index, label in enumerate(labels):
        f = [[features[row][index]] for row in range(16)]
        dual = scale(-1, mul(transpose(f), h))[0] + identity(6)[index]
        direction = [row[0] for row in f] + [-value for value in identity(6)[index]]
        raw[label] = add(identity(22), outer(direction, dual))
    return {'source_receipt': source, 'ports': ports, 'labels': labels, 'raw': raw, 'raw_metric': metric,
            'encoder': decode(decomposition['encoder']), 'decoder': decode(decomposition['decoder']),
            'reduced': reduced, 'mismatch_metric': decode(decomposition['mismatch_metric'])}


def spectral(operator, real_phase, imaginary_phase):
    q = scale(F(1, 2), add(identity(len(operator)), scale(-1, operator)))
    return add(identity(len(operator)), scale(real_phase - 1, q)), scale(imaginary_phase, q)


def complex_mul(a, b):
    return add(mul(a[0], b[0]), scale(-1, mul(a[1], b[1]))), add(mul(a[0], b[1]), mul(a[1], b[0]))


def adjoint(a):
    return transpose(a[0]), scale(-1, transpose(a[1]))


def realification(a):
    real, imag = a
    return [x + [-v for v in y] for x, y in zip(real, imag)] + [y + x for x, y in zip(real, imag)]
