"""Bounded finite countermodel search with SymPy's propositional SAT engine.

SAT results are decoded to explicit tables and independently replayed. UNSAT or
budget exhaustion never rejects a candidate's adequacy. This backend does not
use the held-out formula. Invoke with the admitted ephemeral SymPy environment.
"""
from functools import lru_cache
from itertools import combinations, product
from pathlib import Path
import argparse
import hashlib
import json
import time
from algebra_formula_search import obstruction
from check_algebra_synthesis import direct_holds, check_model


class BudgetExceeded(Exception):
    pass


class Encoding:
    def __init__(self, size):
        self.size = size
        self.last = 1
        self.clauses = [{1}]
        self.table = [self.onehot() for _ in range(size * size)]

    def fresh(self):
        self.last += 1
        return self.last

    def clause(self, literals):
        clause = set(literals)
        if 1 in clause or any(-x in clause for x in clause):
            return
        clause.discard(-1)
        self.clauses.append(clause)

    def onehot(self):
        values = tuple(self.fresh() for _ in range(self.size))
        self.clause(values)
        for a, b in combinations(values, 2):
            self.clause((-a, -b))
        return values

    def constant(self, x):
        return tuple(1 if i == x else -1 for i in range(self.size))

    @lru_cache(None)
    def operation(self, a, b):
        if 1 in a and 1 in b:
            return self.table[self.size * a.index(1) + b.index(1)]
        out = self.onehot()
        for i, left in enumerate(a):
            if left == -1:
                continue
            for j, right in enumerate(b):
                if right == -1 or (a == b and i != j):
                    continue
                for z, value in enumerate(self.table[self.size * i + j]):
                    self.clause((-left, -right, -value, out[z]))
        return out

    def evaluate(self, term, assignment):
        if type(term) is int:
            return self.constant(assignment[term])
        return self.operation(self.evaluate(term[0], assignment), self.evaluate(term[1], assignment))

    def equal(self, a, b):
        for x, y in zip(a, b):
            self.clause((-x, y))
            self.clause((-y, x))

    def distinct_flag(self, a, b):
        # If flag is true, onehot a and b cannot have the same value.
        flag = self.fresh()
        for x, y in zip(a, b):
            self.clause((-flag, -x, -y))
        return flag

    def demand_nonboolean(self):
        flags = []
        for x, y in product(range(self.size), repeat=2):
            a, b = self.constant(x), self.constant(y)
            xx, yy = self.operation(a, a), self.operation(b, b)
            for left, right in [
                (self.operation(a, b), self.operation(b, a)),
                (self.operation(xx, xx), a),
                (self.operation(xx, self.operation(a, yy)), a),
                (self.operation(a, xx), self.operation(b, yy)),
            ]:
                flags.append(self.distinct_flag(left, right))
        self.clause(flags)


def find_model(candidate, size, seconds):
    import sympy
    from sympy.logic.algorithms.dpll2 import SATSolver
    if sympy.__version__ != '1.14.0':
        raise RuntimeError('backend adapter tested only against SymPy 1.14.0')
    encoding = Encoding(size)
    for assignment in product(range(size), repeat=candidate['variables']):
        encoding.equal(encoding.evaluate(candidate['left'], assignment),
                       encoding.evaluate(candidate['right'], assignment))
    encoding.demand_nonboolean()
    # Family restriction only: search a labeled non-fixed diagonal point.
    # Failure in this family leaves the original adequacy obligation open.
    encoding.clause((encoding.table[0][1],))
    encoding.operation.cache_clear()
    started = time.monotonic()

    class BoundedSolver(SATSolver):
        def _assign_literal(self, *args, **kwargs):
            if time.monotonic() - started > seconds:
                raise BudgetExceeded()
            return super()._assign_literal(*args, **kwargs)

    report = {'cost': candidate['cost'], 'ordinal': candidate['ordinal'], 'size': size,
              'variables': encoding.last, 'clauses': len(encoding.clauses),
              'family': 'operation(0,0)=1 and violation of one checked necessary law'}
    print(json.dumps({'starting': report}), flush=True)
    try:
        solver = BoundedSolver(encoding.clauses, set(range(1, encoding.last + 1)), set())
        assignment = next(solver._find_model(), False)
    except BudgetExceeded:
        report['status'] = 'budget-exhausted-not-a-refutation'
        return report
    if assignment is False:
        report['status'] = 'no-model-in-declared-family-not-a-refutation'
        return report
    table = [next(i for i, literal in enumerate(row) if assignment.get(literal, False))
             for row in encoding.table]
    failure = obstruction(size, table)
    assert failure is not None
    model = {'size': size, 'table': table, 'obstruction': failure}
    check_model(model)
    assert direct_holds(candidate['left'], candidate['right'], candidate['variables'], size, table)
    report.update(status='countermodel-replayed', model=model)
    return report


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('source', type=Path)
    parser.add_argument('output', type=Path)
    parser.add_argument('--size', type=int, choices=(4, 5, 6), default=4)
    parser.add_argument('--seconds', type=int, choices=range(1, 61), default=15)
    parser.add_argument('--limit', type=int, choices=range(1, 33), default=1)
    args = parser.parse_args()
    source = json.loads(args.source.read_text(encoding='utf-8'))
    reports, known = [], []
    for candidate in [s for s in source['survivors'] if s['cost'] < 6][:args.limit]:
        cached = next((m for m in known if direct_holds(candidate['left'], candidate['right'],
                      candidate['variables'], m['size'], m['table'])), None)
        if cached is not None:
            report = {'cost': candidate['cost'], 'ordinal': candidate['ordinal'],
                      'status': 'countermodel-replayed', 'model': cached, 'backend': 'retained-model-replay'}
        else:
            report = find_model(candidate, args.size, args.seconds)
        reports.append(report)
        if 'model' in report:
            model = report['model']
            if model not in known:
                known.append(model)
            n, table = model['size'], model['table']
            opposite = [table[n * j + i] for i, j in product(range(n), repeat=2)]
            failure = obstruction(n, opposite)
            if failure is not None:
                reflected = {'size': n, 'table': opposite, 'obstruction': failure}
                check_model(reflected)
                if reflected not in known:
                    known.append(reflected)
        args.output.write_text(json.dumps({'schema': 'marici.finite-sat-countermodels.v1',
            'source_sha256': hashlib.sha256(args.source.read_bytes()).hexdigest(),
            'backend_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'dependency': 'sympy 1.14.0', 'reports': reports}, indent=2) + '\n', encoding='utf-8')
        print(json.dumps(report), flush=True)
