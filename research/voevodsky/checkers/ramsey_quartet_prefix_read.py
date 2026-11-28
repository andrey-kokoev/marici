"""Test a probe with three installed ports; distinguish temporary tests from permanent additions."""
from itertools import combinations
from collections import Counter
import json
from ramsey_quartet_live_probe import independent_sets,configs,decode,D,path


def moves(sq,rs,c,es,keep):
    base=path|set(c)|{(i,11+j) for j,r in enumerate(sq) for i in r}|{(i,15+j) for j in keep for i in rs[j]}|{(11+i,15+j) for i,r in enumerate(sq) for j in keep if set(r).isdisjoint(rs[j])}|{(i,j) for i,j in es if i-15 in keep and j-15 in keep}
    # Site numbering keeps the absent port as a gap. Exclude its bit.
    gap,=set(range(4))-set(keep);sixes=[q for q in independent_sets(18,base,6) if not q&(1<<(15+gap))];valid=set()
    for r in combinations(range(1,11),3):
        if r in rs or r in sq or any(e in path for e in combinations(r,2)):continue
        fixed=set(r)|{11+j for j,s in enumerate(sq) if set(s).isdisjoint(r)};opt=[15+j for j in keep if set(r).isdisjoint(rs[j])]
        for k in range(len(opt)+1):
            for links in combinations(opt,k):
                red=fixed|set(links);mask=sum(1<<i for i in red)
                if not any(i in red and j in red for i,j in base) and all(mask&q for q in sixes):valid.add((r,links))
    return valid


def audit():
    records=[];hist=Counter()
    for t in json.loads((D/'ramsey_quartet_terminal.json').read_text()):
        if t['choice']!='matching':continue
        assert all(len(tree)==1 and not tree[0]['continuations'] for tree in t['trees']);sq=tuple(map(tuple,t['square']));rs=tuple(map(tuple,t['rows']));cs=decode(sq,rs)[3];es,={tuple(st[1]) for c in cs for st in configs(sq,rs,c)}
        for keep in combinations(range(4),3):
            a,b=[moves(sq,rs,c,es,keep) for c in cs];ar={r for r,l in a};br={r for r,l in b};diff=[(i,r,l) for i,(s,other) in enumerate(((a,br),(b,ar))) for r,l in sorted(s) if r not in other];hist[bool(ar^br),bool(a^b)]+=1
            example=next(iter(diff),None);records.append(dict(square=sq,rows=rs,installed=[rs[i] for i in keep],omitted=next(s for i,s in enumerate(rs) if i not in keep),distinct_rows=len(ar^br),distinct_colored_moves=len(a^b),example=dict(row=example[1],red_to=[rs[j-15] for j in example[2]],accepting_cycle=cs[example[0]]) if example else None))
    assert len(records)==16;out=dict(prefix_counts={str(k):v for k,v in hist.items()},records=records);print(hist);print(next((r for r in records if r['example']),None));(D/'ramsey_quartet_prefix_read.json').write_text(json.dumps(out,indent=2)+'\n')
if __name__=='__main__':audit()
