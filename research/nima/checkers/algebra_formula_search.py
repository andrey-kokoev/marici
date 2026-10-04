"""Target-blind enumeration of single identities over one binary operation.

Cost counts binary-operation occurrences across BOTH sides. Variables are
alpha-normalized in first-occurrence order across the complete equation.
There is no fixed variable bound, rewrite quotient, or seeded formula.
"""
from functools import lru_cache
from itertools import product
import argparse
import hashlib
import json
from pathlib import Path


@lru_cache(None)
def shapes(cost):
    if cost == 0:
        return (None,)
    return tuple((a, b) for i in range(cost) for a in shapes(i) for b in shapes(cost - 1 - i))


def patterns(length):
    def go(prefix, largest):
        if len(prefix) == length:
            yield tuple(prefix)
        else:
            for x in range(largest + 2):
                yield from go(prefix + [x], max(largest, x))
    yield from go([0], 0)


def label(shape, labels):
    return next(labels) if shape is None else (label(shape[0], labels), label(shape[1], labels))


def candidates(cost):
    pats = tuple(patterns(cost + 2))
    for left_cost in range(cost + 1):
        for left in shapes(left_cost):
            for right in shapes(cost - left_cost):
                for pat in pats:
                    labels = iter(pat)
                    yield label(left, labels), label(right, labels), max(pat) + 1


@lru_cache(None)
def coordinates(size, variables):
    # One bit for each assignment; one bit plane for each possible value.
    planes = [[0] * size for _ in range(variables)]
    for row, assignment in enumerate(product(range(size), repeat=variables)):
        for i, value in enumerate(assignment):
            planes[i][value] |= 1 << row
    return tuple(map(tuple, planes))


def nand_value(term, variables):
    mask = (1 << (1 << variables)) - 1
    def evaluate(t):
        if type(t) is int:
            return coordinates(2, variables)[t][1]
        return mask ^ (evaluate(t[0]) & evaluate(t[1]))
    return evaluate(term)


def satisfies(left, right, variables, size, table):
    groups = [[] for _ in range(size)]
    for i, z in enumerate(table):
        groups[z].append(divmod(i, size))
    def evaluate(t):
        if type(t) is int:
            return coordinates(size, variables)[t]
        a, b = evaluate(t[0]), evaluate(t[1])
        out = []
        for pairs in groups:
            value = 0
            for i, j in pairs:
                value |= a[i] & b[j]
            out.append(value)
        return tuple(out)
    return evaluate(left) == evaluate(right)


def obstruction(size, table):
    """A failed necessary Boolean-NAND law; not a heuristic non-Boolean label."""
    op = lambda x, y: table[size * x + y]
    for x, y in product(range(size), repeat=2):
        if op(x, y) != op(y, x):
            return {'law': 'commutativity', 'assignment': [x, y]}
        if op(op(x, x), op(x, x)) != x:
            return {'law': 'double-negation', 'assignment': [x]}
        if op(op(x, x), op(x, op(y, y))) != x:
            return {'law': 'absorption', 'assignment': [x, y]}
        if op(x, op(x, x)) != op(y, op(y, y)):
            return {'law': 'top-independence', 'assignment': [x, y]}
    return None


@lru_cache(None)
def countermodels(size):
    return tuple((t, failure) for t in product(range(size), repeat=size * size)
                 if (failure := obstruction(size, t)) is not None)


def text(term):
    return f'x{term}' if type(term) is int else f'({text(term[0])}|{text(term[1])})'


def search(max_cost=6, max_model=3, discovery_cost=5):
    if (type(max_cost) is not int or not 0 <= max_cost <= 6
            or type(max_model) is not int or max_model not in (2, 3)
            or type(discovery_cost) is not int or not -1 <= discovery_cost <= 5):
        raise ValueError('registered search bound exceeded')
    catalogue = [(n, t, failure) for n in range(2, max_model + 1) for t, failure in countermodels(n)]
    used, levels, survivors, rejections = [], [], [], []
    for cost in range(max_cost + 1):
        counts = {'cost': cost, 'enumerated': 0, 'boolean_invalid': 0, 'countermodel_rejected': 0, 'open': 0}
        for ordinal, (left, right, variables) in enumerate(candidates(cost)):
            counts['enumerated'] += 1
            if nand_value(left, variables) != nand_value(right, variables):
                counts['boolean_invalid'] += 1
                continue
            witness = next((i for i, (n, t, _) in enumerate(used)
                            if satisfies(left, right, variables, n, t)), None)
            if witness is None and cost <= discovery_cost:
                for model in catalogue:
                    n, table, _ = model
                    if satisfies(left, right, variables, n, table):
                        if model not in used:
                            used.append(model)
                        witness = used.index(model)
                        break
            if witness is not None:
                counts['countermodel_rejected'] += 1
                rejections.append([cost, ordinal, witness])
            else:
                counts['open'] += 1
                survivors.append({'cost': cost, 'ordinal': ordinal, 'left': left, 'right': right,
                                  'variables': variables, 'display': f'{text(left)} = {text(right)}',
                                  'status': 'finite-model-survivor-not-yet-adequate'})
        levels.append(counts)
        print(json.dumps(counts), flush=True)
    return {'schema': 'marici.algebra-formula-search.v1',
            'grammar': 'one binary operation; arbitrary terms on both sides; unrestricted alpha-normalized variables',
            'cost': 'total binary operation occurrences', 'max_cost': max_cost, 'max_countermodel_size': max_model,
            'countermodel_discovery_through_cost': discovery_cost,
            'levels': levels, 'survivors': survivors,
            'countermodels': [{'size': n, 'table': t, 'obstruction': failure} for n, t, failure in used],
            'rejections': rejections,
            'generator_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--max-cost', type=int, default=6)
    parser.add_argument('--max-model', type=int, default=3)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    result = search(args.max_cost, args.max_model)
    args.output.write_text(json.dumps(result, separators=(',', ':')) + '\n', encoding='utf-8')
    args.output.with_suffix('.survivors.json').write_text(json.dumps(result['survivors'], indent=2) + '\n', encoding='utf-8')
