"""Can a distinguishing permanent fourth move itself finish a new minimum-two quartet?"""
from itertools import combinations
from collections import Counter
from ramsey_quartet_prefix_read import moves
from ramsey_quartet_live_probe import configs,decode,independent_sets,D,path
import json


def minimum(sq,rows,c):
    E=path|set(c)|{(i,11+j) for j,r in enumerate(sq+rows) for i in r}|{(11+i,15+j) for i,r in enumerate(sq) for j,s in enumerate(rows) if set(r).isdisjoint(s)}
    opts=[(15+i,15+j) for i,j in combinations(range(4),2) if set(rows[i]).isdisjoint(rows[j]) and all(set(s)&set(rows[i]+rows[j]) for s in sq)]
    for n in range(len(opts)+1):
        for links in combinations(opts,n):
            g=E|set(links)
            if not any(all(e in g for e in combinations(t,2)) for t in combinations(range(15,19),3)) and not independent_sets(18,g,7):return n
    raise ValueError('expected a legal attachment')


def audit():
    from ramsey_two_repairs_opposite import run
    keys=run();hist=Counter();records=[]
    for item in json.loads((D/'ramsey_quartet_terminal.json').read_text()):
        if item['choice']!='matching':continue
        sq=tuple(map(tuple,item['square']));rs=tuple(map(tuple,item['rows']));cs=decode(sq,rs)[3];es,={tuple(st[1]) for c in cs for st in configs(sq,rs,c)}
        for keep in combinations(range(4),3):
            prefix=tuple(rs[i] for i in keep);choices=[moves(sq,rs,c,es,keep) for c in cs];options=[]
            for i in (0,1):
                for r,links in sorted(choices[i]-choices[1-i]):
                    n=minimum(sq,prefix+(r,),cs[i]);solo=all(s!=r for s,l in choices[1-i]);hist[solo,n]+=1;options.append(dict(row=r,red_to=[rs[j-15] for j in links],cycle=cs[i],support_distinguishes=solo,minimum=n))
            completions=[{g for s,z,g in keys if s==sq and z==c and set(prefix)<=set(g)} for c in cs]
            assert completions==[{rs},{rs}]
            records.append(dict(square=sq,original=rs,prefix=prefix,only_minimum_two_completion=rs,options=options))
    out=dict(by_support_distinguishes_and_minimum={str(k):v for k,v in hist.items()},records=records);print(hist);print(Counter(tuple(sorted({o['minimum'] for o in t['options']})) for t in records));print(records[0]);(D/'ramsey_quartet_prefix_replacement.json').write_text(json.dumps(out,indent=2)+'\n')
if __name__=='__main__':audit()
