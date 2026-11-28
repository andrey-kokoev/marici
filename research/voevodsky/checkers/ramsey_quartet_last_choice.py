"""Decode a known minimum quartet, without looking up candidate cycles of its square."""
from itertools import combinations,permutations
from collections import Counter,defaultdict
from ramsey_two_repairs_opposite import run
from ramsey_inherited_swap_selector import D,evaluate
import json


def decode(sq,rs):
    edge=lambda i,j:tuple(sorted((i,j)))
    U=set().union(*sq);W=set(range(1,11))-U;u,v=sorted(W-set().union(*rs));x,z=u+1,v-1;K=W-{u,v};singles=sorted((set(r)&U,set(r)&W) for r in rs if len(set(r)&W)==2);(_,A),(_,B)=singles
    diff=A!=B;opposite=singles[0][0]!=singles[1][0];possible=[]
    for a,b in combinations(sorted(K),2):
        if diff and {a,b}!=A^B or not diff and {a,b}==A:continue
        h,=K-{a,b}
        for left,right in permutations((a,b)):
            c={edge(a,b),edge(u,h),edge(v,h),edge(u,left),edge(v,right)}
            if any(((i,j) not in c and j-i==1) or ((i,j) in c and j-i==2) for i,j in combinations(sorted(W),2)):continue
            if diff and opposite:
                Sx=next(s for m,s in singles if x in m)
                if right not in Sx:continue
            possible.append(((a,b),tuple(sorted(c))))
    assert 1<=len(possible)<=2
    label='known';probe=None;queried=None
    if len(possible)==2:
        if possible[0][0]!=possible[1][0]:label='inner edge';queried=possible[0][0]
        else:label='matching';queried=edge(u,possible[0][0][0])
        movable=U-set.intersection(*map(set,sq));p=min(i for i in movable if all(abs(i-j)>1 for j in queried));probe=sorted((*queried,p));assert len({queried in c for _,c in possible})==2
    return label,queried,probe,[c for _,c in possible]


def audit():
    index=defaultdict(set)
    for sq,c,rs in run():index[sq,rs].add(c)
    hist=Counter();examples={}
    for (sq,rs),truth in sorted(index.items()):
        tag,e,r,cycles=decode(sq,rs);assert set(cycles)==truth
        if r:
            query=(tuple(r),)
            for c in cycles:assert (query in evaluate(10,sq,set(c),[query]))==(e not in c)
        hist[tag]+=1;examples.setdefault(tag,dict(square=sq,quartet=rs,edge=e,probe=r,cycles=cycles))
    out=dict(labeled_quartets=hist,examples=examples);print(out);(D/'ramsey_quartet_last_choice.json').write_text(json.dumps(out,indent=2)+'\n')
if __name__=='__main__':audit()
