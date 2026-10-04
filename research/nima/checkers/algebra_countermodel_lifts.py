"""Search four-element lifts of a two-element NAND quotient, not a solver wrapper."""
from itertools import product
from pathlib import Path
import json
import argparse
from algebra_formula_search import obstruction, satisfies


def lifted_tables():
    # Elements are (quotient bit, fiber bit); the quotient operation is NAND.
    high = [2 * (1 - ((a // 2) & (b // 2))) for a, b in product(range(4), repeat=2)]
    for bits in range(1 << 16):
        yield tuple(h | ((bits >> i) & 1) for i, h in enumerate(high))


def extend(packet):
    models = list(packet['countermodels'])
    remaining = []
    for candidate in packet['survivors']:
        left, right, variables = candidate['left'], candidate['right'], candidate['variables']
        found = next((i for i, m in enumerate(models)
                      if satisfies(left, right, variables, m['size'], m['table'])), None)
        if found is None:
            for table in lifted_tables():
                failure = obstruction(4, table)
                if failure is not None and satisfies(left, right, variables, 4, table):
                    models.append({'size': 4, 'table': table, 'obstruction': failure})
                    found = len(models) - 1
                    break
        if found is None:
            remaining.append(candidate)
        print(json.dumps({'cost': candidate['cost'], 'ordinal': candidate['ordinal'], 'countermodel': found}), flush=True)
    return {'schema': 'marici.algebra-countermodel-bank.v1', 'models': models, 'unresolved': remaining,
            'scope': 'Known necessary-law violations; explicit four-element quotient lifts only.'}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('source', type=Path)
    parser.add_argument('output', type=Path)
    args = parser.parse_args()
    result = extend(json.loads(args.source.read_text(encoding='utf-8')))
    args.output.write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
