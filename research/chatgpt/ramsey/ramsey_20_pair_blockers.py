"""One certificate per rejected sign of every pair (including repeated columns)."""
from itertools import combinations, combinations_with_replacement
from pathlib import Path
import json
from ramsey_difference_next_round import run, add, ids, build
from ramsey_delayed_address_move import moves


def main():
    rows=[r&((1<<20)-1) for r in build()[:20]]
    _,cols,retained=run(rows)
    fives=[sum(1<<i for i in f) for f in combinations(range(20),5)
           if all(not (rows[i]>>j&1) for i,j in combinations(f,2))]
    results=[]; wins=[]
    for i,j in combinations_with_replacement(range(len(cols)),2):
        p,q=cols[i],cols[j]; shared=ids(p&q); missed=next((s for s in fives if not s&(p|q)),None)
        legal=moves(add(rows,p))[2]
        assert (q in legal)==(missed is None) and ((q|(1<<20)) in legal)==(not shared)
        results.append(dict(pair=[i,j],plus_blocker=shared[0] if shared else None,minus_blocker=ids(missed) if missed else None))
        if missed is None or not shared:wins.append((i,j))
    doc=dict(labels='old addresses 0..19; null means the sign is allowed',columns=list(map(ids,cols)),retained=[p in retained for p in cols],negative_five_sets=len(fives),pairs=results)
    Path(__file__).with_suffix('.json').write_text(json.dumps(doc,indent=2)+'\n');print(len(fives),wins,results[1],results[4]);print('common to all:',[v for v in range(20) if all(p>>v&1 for p in cols)])

if __name__=='__main__':main()
