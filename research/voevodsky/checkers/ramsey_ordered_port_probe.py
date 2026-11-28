"""First displayed row with asymmetric overlap; choose the row before graph evaluation."""
from itertools import product,combinations
from collections import Counter
from ramsey_cube_diagonal_pairs import analyze,profile,D
import json


def audit():
    t=analyze(10);upper=sorted(list(map(tuple,t['leftover']))+[tuple(r) for p in t['pieces'] for r in p['new']]);flip=lambda r:tuple(11-i for i in reversed(r));starts=[tuple(p['start']) for p in t['pieces']];hist=Counter();cases=Counter();records=[]
    for rec in json.loads((D/'ramsey_cube_diagonal_colors.json').read_text())['records']:
        upper_half=rec['half']=='upper';sheet=upper if upper_half else [flip(r) for r in reversed(upper)];order=starts if upper_half else [tuple(10-i for i in reversed(r)) for r in reversed(starts)];sq=tuple(map(tuple,rec['square']));ds=[tuple(map(tuple,d)) for d in rec['diagonals']];opp=set(ds[0]+ds[1]);later=sheet[1+max(sheet.index(r) for r in opp|set(sq)):];marks=[]
        for a in order[order.index(tuple(rec['start']))+1:]:
            shared=opp&set(product(*[(v,v+1) for v in a]));
            if len(shared)!=2 or len(set.intersection(*map(set,shared)))!=2:continue
            targets=[next(r for r in d if r in shared) for d in ds];pool=[r for r in later if sum(set(r).isdisjoint(s) for s in targets)==1];first=pool[0] if pool else None
            # The chosen row is now fixed, independently of the following graph checks.
            ms=[profile(sq,d,set(map(tuple,rec['cycle'])),later)[1] for d in ds]
            def score(r):return [any(m&(1<<(15+d.index(s))) for m in opts.get(r,())) for d,s,opts in zip(ds,targets,ms)]
            works=[r for r in pool if len(set(score(r)))==2];immediate=bool(later and len(set(score(later[0])))==2);hit=bool(first and len(set(score(first)))==2);hist['marks']+=1;hist['has_candidate']+=bool(first);hist['first_hit']+=hit;hist['immediate']+=immediate;hist['any_hit']+=bool(works)
            if first:
                hist['candidate_rejected_both']+=all(first not in opts for opts in ms)
                hist['candidate_contains_red_site_pair']+=any(list(e) in rec['cycle'] for e in combinations(first,2))
            marks.append(dict(successor=a,targets=targets,candidate=first,candidate_legal=[first in opts for opts in ms],first_hit=hit,immediate=immediate,first_working=works[:1],working_rank=pool.index(works[0])+1 if works else None,pool_size=len(pool)))
        for key in ('candidate','first_hit','immediate','first_working'):cases[key]+=any(m[key] for m in marks)
        records.append(dict(half=rec['half'],square=sq,start=rec['start'],marks=marks))
    out=dict(trials=hist,cases=cases,records=records);print(hist,cases);print(next((r for r in records if any(m['first_working'] for m in r['marks'])),None));(D/'ramsey_ordered_port_probe.json').write_text(json.dumps(out,indent=2)+'\n')
if __name__=='__main__':audit()
