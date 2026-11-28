"""Count attachments per labeled blue edge from path adjacencies, without generating a row."""
from collections import Counter
from itertools import combinations
import json
from ramsey_pentagon_selector import charts
from ramsey_inherited_swap_selector import D


def count(sq,cycle,edge):
    u,v=edge;f,=set.intersection(*map(set,sq));mov=set().union(*sq)-{f};X={u+1,v-1}
    if v-u!=3 or not X<=mov or any(X<=set(r) for r in sq):return 0
    Y=mov-X
    if any(abs(i-j)==1 for i in Y for j in edge):return 0
    K=set(range(1,11))-set().union(*sq)-{u,v};ab,=[e for e in combinations(sorted(K),2) if e in cycle]
    n=sum(abs(i-j)==1 for i in Y for j in ab);m=2 if n==0 else 1
    return 2*m+(min(abs(f-u),abs(f-v))!=1)*(m+2*(2-n))


def audit():
    ref=json.loads((D/'ramsey_construct_two_repairs.json').read_text());lookup={(tuple(map(tuple,t['square'])),tuple(map(tuple,t['cycle'])),tuple(t['missed'])):sum(s['outputs'] for s in t['flanks']) for t in ref['edge_report']};hist=Counter();by_cycle=Counter();examples={}
    for sq,_,cycles in charts():
        W=set(range(1,11))-set().union(*sq)
        for cycle in cycles:
            subtotal=0
            for edge in combinations(sorted(W),2):
                if edge in cycle:continue
                k=count(sq,cycle,edge);assert k==lookup.pop((sq,tuple(sorted(cycle)),edge));hist[k]+=1;subtotal+=k;examples.setdefault(k,dict(square=sq,cycle=sorted(cycle),edge=edge))
            by_cycle[subtotal]+=1
    assert not lookup and sum(k*v for k,v in hist.items())==276
    out=dict(edges_by_count=hist,cycles_by_total=by_cycle,examples=examples);print(hist,by_cycle);(D/'ramsey_two_repairs_edge_count.json').write_text(json.dumps(out,indent=2)+'\n')
if __name__=='__main__':audit()
