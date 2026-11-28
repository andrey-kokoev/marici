"""Does preservation of old row decisions imply preservation of cyclic order?"""
import json
from itertools import combinations,pairwise
from collections import Counter
from ramsey_inherited_swap_selector import evaluate,run,D
from ramsey_inherited_endpoint_splice import splices


def audit():
    hist=Counter();example={};reads=Counter()
    def inspect(sq,path,swaps,children):
        tied=[c for c,v in children if swaps<=v]
        queries=[(s,) for s in combinations(range(1,10),3) if s not in sq and min(s[1]-s[0],s[2]-s[1])>=2]
        old=evaluate(9,sq,{tuple(sorted(e)) for e in pairwise(path)},queries);rings=list(splices(path).values())
        U=set().union(*sq);W=set(range(1,10))-U;mov=U-set.intersection(*map(set,sq));red={tuple(sorted(e)) for e in pairwise(path)}
        for e in combinations(sorted(W),2):
            if e in red:continue
            witnesses=[s for (s,) in old if set(e)<=set(s) and set(s)&mov];reads[bool(witnesses)]+=1
        if len(tied)<2:return
        for c in tied:
            new=evaluate(10,sq,c,queries);key=(old<=new,old==new,c in rings);hist[key]+=1
            example.setdefault(key,dict(square=sq,path=path,cycle=sorted(c),old_rows=len(old),lost=sorted(s for (s,) in old-new),gained=sorted(s for (s,) in new-old)))
    run(inspect);print(hist);print(example.get((True,True,False)));print(example.get((True,False,False)));print(reads);out=dict(old_blue_edges_with_witness={str(k):v for k,v in reads.items()},counts={str(k):v for k,v in hist.items()},key=['keeps_old_legal_rows','same_old_row_decisions','keeps_cyclic_order'],examples={str(k):v for k,v in example.items()});(D/'ramsey_inherited_order_necessity.json').write_text(json.dumps(out,indent=2)+'\n')
if __name__=='__main__':audit()
