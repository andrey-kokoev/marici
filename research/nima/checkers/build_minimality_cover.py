"""Build universally quantified prefix refutations; the kernel will check coverage.
This planner is untrusted. It reads only explicit countermodels, not TARGET.
"""
from collections import Counter
from itertools import product
from pathlib import Path
import json
from algebra_formula_search import shapes, label, nand_value, satisfies

BASE = Path(__file__).resolve().parents[1]


def templates(shape, prefix, used):
    leaves = leaf_count(shape)
    labels = iter(tuple(prefix) + tuple(range(used, used + leaves - len(prefix))))
    eq = label(shape, labels)
    return eq[0], eq[1], used + leaves - len(prefix)


def leaf_count(shape):
    return 1 if shape is None else leaf_count(shape[0]) + leaf_count(shape[1])


def build():
    source = json.loads((BASE / 'results/algebra-formula-search.json').read_text())
    extra = json.loads((BASE / 'results/algebra-finite-sat.json').read_text())
    models = []
    for model in source['countermodels'] + [r['model'] for r in extra['reports']]:
        if model not in models:
            models.append(model)
    records, statistics = [], Counter()
    for cost in range(6):
        for index, shape in enumerate(shapes(cost + 1)):
            count = leaf_count(shape)
            leaves = []
            # Constant assignments are independent of all variable labels.
            closed = label(shape, iter([0] * count))
            bits = nand_value(closed[0], 1) ^ nand_value(closed[1], 1)
            constant = next((x for x in range(2) if bits & (1 << x)), None)

            def visit(prefix, used):
                statistics['visited'] += 1
                left, right, variables = templates(shape, prefix, used)
                remaining = count - len(prefix)
                if constant is not None:
                    leaves.append({'prefix': prefix, 'kind': 'constant', 'value': constant})
                    statistics['constant'] += 1
                    return
                delta = nand_value(left, variables) ^ nand_value(right, variables)
                width = 1 << remaining
                mask = (1 << width) - 1
                for fixed in range(1 << used):
                    if ((delta >> (fixed * width)) & mask) == mask:
                        values = [(fixed >> (used - 1 - i)) & 1 for i in range(used)]
                        leaves.append({'prefix': prefix, 'kind': 'boolean', 'values': values})
                        statistics['boolean'] += 1
                        statistics['boolean_cases_upper_bound'] += 2 ** remaining
                        return
                for i, model in enumerate(models):
                    if satisfies(left, right, variables, model['size'], model['table']):
                        leaves.append({'prefix': prefix, 'kind': 'model', 'model': i})
                        statistics['model'] += 1
                        statistics['model_cases_upper_bound'] += model['size'] ** variables
                        return
                if remaining == 0:
                    raise RuntimeError(('unresolved closed candidate', cost, index, prefix))
                for x in range(used + 1):
                    visit(prefix + [x], max(used, x + 1))
                # All greater natural labels violate the exact normal predicate.
                leaves.append({'prefix': prefix, 'kind': 'noncanonical', 'bound': used})
                statistics['noncanonical'] += 1

            visit([], 0)
            records.append({'cost': cost, 'shape_index': index, 'shape': shape, 'leaves': leaves})
    return {'schema': 'marici.synthesis.minimum-prefix-cover.v1', 'models': models,
            'records': records, 'statistics': dict(statistics)}


if __name__ == '__main__':
    result = build()
    (BASE / 'results/minimality-prefix-cover.json').write_text(json.dumps(result, separators=(',', ':')) + '\n')
    print(json.dumps(result['statistics']))
