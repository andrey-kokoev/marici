"""For tied successors, also retain every individually legal old separated triple."""
from collections import Counter
from itertools import combinations
import json
from ramsey_inherited_swap_selector import D, evaluate, run


def audit():
    counts = Counter()
    examples = {}
    failures = []
    def compare(square, path, swaps, children):
        tied = [edges for edges, marks in children if swaps <= marks]
        if len(tied) < 2:
            return
        # A one-element tuple asks evaluate to test exactly one extra port.
        queries = [(s,) for s in combinations(range(1, 10), 3)
                   if s not in square and min(s[1]-s[0], s[2]-s[1]) >= 2]
        old_edges = {tuple(sorted(p)) for p in zip(path, path[1:])}
        old = evaluate(9, square, old_edges, queries)
        losses = [sorted(s for (s,) in old - evaluate(10, square, c, queries)) for c in tied]
        n = losses.count([])
        counts[n] += 1
        if n == 0:
            common = set.intersection(*map(set, losses))
            residual = [set(l) - common for l in losses]
            witnesses = []
            if all(residual):
                pool = sorted(set.union(*residual))
                for size in range(2, len(tied)+1):
                    witnesses = [g for g in combinations(pool, size)
                                 if all(set(g) & l for l in residual)]
                    if witnesses:
                        break
                assert witnesses
            failures.append(dict(square=square, old_path=path, common=sorted(common),
                                 minimum_residual_conflicts=witnesses,
                                 candidates=[dict(edges=sorted(c), lost_rows=l) for c,l in zip(tied, losses)]))
        examples.setdefault(n, dict(square=square, old_path=path, old_rows=len(old),
                                    candidates=[dict(edges=sorted(c), lost_rows=l) for c,l in zip(tied, losses)]))
    run(compare)
    assert sum(counts.values()) == 28
    assert len(failures) == 15
    result = dict(by_survivor_count=dict(sorted(counts.items())), examples=examples,
                  failed_cases=failures)
    (D/'ramsey_inherited_single_rows.json').write_text(json.dumps(result, indent=2)+'\n')
    print(counts)
    for k,v in examples.items(): print(k,v)

if __name__ == '__main__':
    audit()
