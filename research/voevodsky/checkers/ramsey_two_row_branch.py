"""Keep two installed ports; test third moves that extend to a minimum-two quartet."""
from itertools import combinations
from collections import Counter,defaultdict
from ramsey_quartet_live_probe import configs,decode,independent_sets,D,path
from ramsey_two_repairs_opposite import run
import json


def can(sq,cs,prefix,old,r,links):
    rs=prefix+(r,);g=path|set(cs)|{(i,11+j) for j,s in enumerate(sq+rs) for i in s}|{(11+i,15+j) for i,s in enumerate(sq) for j,t in enumerate(rs) if set(s).isdisjoint(t)}|{(15+i,17) for i in links}
    if old:g.add((15,16))
    return not any(all(e in g for e in combinations(t,2)) for t in combinations(range(1,18),3)) and not independent_sets(17,g,7)


def audit():
    index=defaultdict(list)
    for sq,c,rs in run():index[sq,c].append(rs)
    records=[];hist=Counter()
    for item in json.loads((D/'ramsey_quartet_terminal.json').read_text()):
        if item['choice']!='matching':continue
        sq=tuple(map(tuple,item['square']));orig=tuple(map(tuple,item['rows']));cs=decode(sq,orig)[3];es,={tuple(st[1]) for c in cs for st in configs(sq,orig,c)}
        for i,j in combinations(range(4),2):
            prefix=(orig[i],orig[j]);old=(15+i,15+j) in es;plans=[];potential=set()
            for pi,c in enumerate(cs):
                for rs in sorted(index[sq,c]):
                    if not set(prefix)<=set(rs):continue
                    for _,full,_,_ in configs(sq,rs,c):
                        red={frozenset((rs[a-15],rs[b-15])) for a,b in full}
                        if (frozenset(prefix) in red)!=old:continue
                        for r in sorted(set(rs)-set(prefix)):
                            links=tuple(k for k,p in enumerate(prefix) if frozenset((p,r)) in red);potential.add((pi,rs))
                            if can(sq,cs[1-pi],prefix,old,r,links):continue
                            other=any(can(sq,cs[1-pi],prefix,old,r,l) for n in range(3) for l in combinations(range(2),n));plans.append(dict(accept=c,probe=r,red_to=[prefix[k] for k in links],accept_final=rs,accept_links=[(rs[a-15],rs[b-15]) for a,b in full],support_alone_distinguishes=not other,reject_final=orig))
            states=len({p['accept'] for p in plans});hist[states]+=1;records.append(dict(square=sq,original=orig,prefix=prefix,old_link_red=old,completion_counts=[sum(i==k for i,r in potential) for k in range(2)],plans=plans))
    print(hist);print(next((r for r in records if r['plans']),None));print(Counter(tuple(sorted(r['completion_counts'])) for r in records));(D/'ramsey_two_row_branch.json').write_text(json.dumps(dict(by_accepting_directions=hist,records=records),indent=2)+'\n')
if __name__=='__main__':audit()
