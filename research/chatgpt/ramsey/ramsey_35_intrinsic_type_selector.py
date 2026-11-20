"""Select types using only maximum-set incidence. Check vertex correspondence afterward."""
from collections import Counter
from itertools import combinations


def select(rows):
    sets=[0]
    for i,row in enumerate(rows):
        sets += [s | (1<<i) for s in sets if not s&row]
    alpha=max(s.bit_count() for s in sets)
    types=[s for s in sets if s.bit_count()==alpha]
    scores={s:sum(not s&t for t in types) for s in types}
    top=max(scores.values());return Counter(scores.values()),{s for s,d in scores.items() if d==top}

if __name__=='__main__':
    rows=[sum(1<<((i+d)%13) for d in (1,-1,5,-5)) for i in range(13)]
    hist,selected=select(rows);assert len(set(rows))==len(rows) and selected==set(rows)
    assert all(bool(rows[i]>>j&1)==(not (rows[i]&rows[j])) for i,j in combinations(range(13),2))
    print('disjointness counts -> number of types:',sorted(hist.items()));print('selected types equal the 13 distinct positive neighborhoods; all 78 mutual signs match')
