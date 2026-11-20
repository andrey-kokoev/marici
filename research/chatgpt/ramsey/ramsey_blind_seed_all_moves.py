"""Exhaust all unrestricted extensions of the first target-only seeds. No order cap."""
from collections import Counter
from ramsey_blind_start_formulas import blue, check, seed


def audit(k, form):
    rows, _, _ = seed(k, form)
    visits, leaves = Counter(), Counter()

    def visit(rows):
        n = len(rows)
        visits[n] += 1
        sets = blue(rows)
        targets = [s for s in sets if s.bit_count() == k-1]
        cols = [p for p in sets if all(p & s for s in targets)]
        if not cols:
            leaves[n] += 1
        for p in cols:
            child = [r | (((p >> i) & 1) << n) for i,r in enumerate(rows)] + [p]
            assert check(child, k)
            visit(child)

    visit(rows)
    print(k, form, 'labeled histories by size', dict(sorted(visits.items())),
          'terminal histories', dict(sorted(leaves.items())), flush=True)

if __name__ == '__main__':
    for k in (7, 8):
        for form in ('double', 'array'):
            audit(k, form)
