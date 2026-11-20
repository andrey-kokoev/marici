"""R(3,3) one-vertex extension. Cache modulo global color reversal in SQLite."""
import sqlite3
from itertools import combinations

edges = list(combinations(range(4), 2))

def extends(prefix, star=None):
    colors = dict(zip(edges, ((prefix >> i) & 1 for i in range(6))))
    if star is not None:
        colors.update({(v, 4): (star >> v) & 1 for v in range(4)})
    return all(len({colors[e] for e in combinations(t, 2)}) == 2
               for t in combinations(range(4 + int(star is not None)), 3))

def run():
    db = sqlite3.connect(':memory:')
    db.execute('CREATE TABLE futures (k INTEGER PRIMARY KEY, legal INTEGER NOT NULL)')
    answers = {}; checks = hits = 0
    for p in range(64):
        if not extends(p): continue
        k = min(p, p ^ 63)
        row = db.execute('SELECT legal FROM futures WHERE k=?', (k,)).fetchone()
        if row is None:
            legal = sum(1 << s for s in range(16) if extends(k, s)); checks += 16
            db.execute('INSERT INTO futures VALUES (?,?)', (k, legal))
        else:
            legal, = row; hits += 1
        answers[p] = {s for s in range(16) if legal >> (s if p == k else s ^ 15) & 1}
    # Exhaustive labeled reference, separate from the cached-search counts.
    assert all(ss == {s for s in range(16) if extends(p,s)} for p,ss in answers.items())
    print(f'{len(answers)} prefixes; {hits} hits; {checks} cached vs {16*len(answers)} direct candidate checks')

if __name__ == '__main__': run()
