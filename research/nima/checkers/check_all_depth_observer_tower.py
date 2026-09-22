"""Bounded-depth regressions for the all-depth saturated observer theorem.

The all-depth proof and the summable-source counterexample are analytical;
finite enumeration does not establish either infinite assertion.
"""
from pathlib import Path
from itertools import combinations, product
from collections import defaultdict
from functools import lru_cache
import runpy
import json

ROOT=Path(__file__).resolve().parents[3]
f=runpy.run_path(str(ROOT/'research/nima/checkers/check_seven_event_factorization_descent.py'))


def ordered(start,column,r):
    out=defaultdict(int)
    for (word,marks),coefficient in column.items():
        states=[start]
        for j in word:states.append(states[-1]|(1<<j))
        for positions in combinations(range(len(word)),r):
            seams=tuple(('e',states[i],states[i+1],marks[i]) for i in positions)
            cuts=(-1,)+positions+(len(word),)
            buffers=[f['record'](states[a+1],word[a+1:b],marks[a+1:b])
                     for a,b in zip(cuts,cuts[1:])]
            for entries in product(*(v.items() for v in buffers)):
                c=coefficient
                for _,value in entries:c*=value
                out[seams,tuple(key for key,_ in entries)]+=c
    return f['clean'](out)


def one(column):
    return {((('e',x,y,k),),(u,v)):c for (x,y,u,k,v),c in column.items()}


def join_key(a,b):
    sa,ba=a;sb,bb=b
    return sa+sb,ba[:-1]+(ba[-1]+bb[0],)+bb[1:]


def join(a,b):
    out=defaultdict(int)
    for ka,ca in a.items():
        for kb,cb in b.items():out[join_key(ka,kb)]+=ca*cb
    return f['clean'](out)


def factors(r):
    return [f['relation']((2*i,2*i+1),int(i<r-1)) for i in range(r)]


def selected(r):
    for choices in product((0,1),repeat=r-1):
        seams=[];weight=1
        for i,choice in enumerate(choices):
            start=(1<<(2*i))-1
            if choice:
                seams.append(('e',start|(1<<(2*i)),(1<<(2*i+2))-1,1))
                weight*=3*i+3
            else:
                seams.append(('e',start,start|(1<<(2*i)),1))
                weight*=-(3*i+1)
        start=(1<<(2*(r-1)))-1
        seams.append(('e',start,start|(1<<(2*(r-1))),0))
        yield (tuple(seams),((),)*(r+1)),weight


def score(image,r):return sum(weight*image.get(key,0) for key,weight in selected(r))


@lru_cache(None)
def trees(n,offset=0):
    if n==1:return (offset,)
    return tuple((a,b) for k in range(1,n)
                 for a in trees(k,offset) for b in trees(n-k,offset+k))


def eval_tree(tree,items,combine):
    if isinstance(tree,int):return items[tree]
    return combine(eval_tree(tree[0],items,combine),eval_tree(tree[1],items,combine))


def main():
    sources=[];full_trees=lower=sectors=0
    for r in range(1,7):
        fs=factors(r);source=f['chain_product'](fs)
        assert len(source)==2*4**(r-1)
        assert all(abs(c)==1 and len(word)==2*r and sum(marks)==r-1
                   for (word,marks),c in source.items())
        sources.append({'depth':r,'source_terms':len(source)})
        if r>4:continue
        ds=[one(f['derivative']((1<<(2*i))-1,col)) for i,col in enumerate(fs)]
        image=ordered(0,source,r)
        assert not f['balanced_boundary'](image)
        for tree in trees(r):
            assert eval_tree(tree,ds,join)==image
            full_trees+=1
        for k in range(1,r):
            assert not ordered(0,source,k)
            lower+=1
        assert not ordered(0,f['multiply'](source,f['relation']((2*r,2*r+1),0)),r)
        for key,weight in selected(r):
            assert image[key]==1
            sectors+=1
        assert score(image,r)==2**(r-1)
    # All finite tree routes on actual records, including nonvacuum buffers.
    record_trees=nonvac=0
    for r in range(1,8):
        ds=[one(f['derivative']((1<<(2*i))-1,col)) for i,col in enumerate(factors(r))]
        records=[next((k for k in d if any(k[1])),next(iter(d))) for d in ds]
        nonvac+=sum(any(key[1]) for key in records)
        seams=tuple(seam for key in records for seam in key[0])
        buffers=(records[0][1][0],)+tuple(records[i][1][-1]+records[i+1][1][0]
                    for i in range(r-1))+(records[-1][1][-1],)
        for tree in trees(r):
            assert eval_tree(tree,records,join_key)==(seams,buffers)
            record_trees+=1
    # A raw scalar coordinate cannot have trivial ideal action; its saturated
    # left-context coordinate evaluates the tail to the nonzero new detector.
    contexts=0
    for r in (2,3):
        fs=factors(r);a=fs[0];tail=f['chain_product'](fs[1:])
        whole=f['multiply'](a,tail)
        target=score(ordered(0,whole,r),r)
        assert target==2**(r-1)
        expanded=sum(c*score(ordered(0,f['multiply']({key:1},tail),r),r)
                     for key,c in a.items())
        assert expanded==target
        assert all(len(word)<2*r for word,marks in tail) # unsaturated row is zero
        contexts+=1
    result={'passed':True,'source_fixtures':sources,
        'independent_full_derivative_parenthesizations':full_trees,
        'lower_derivative_annihilations':lower,'selected_positive_sectors':sectors,
        'actual_record_reassociation_routes':record_trees,'nonvacuum_record_factors':nonvac,
        'nontrivial_ideal_action_context_checks':contexts,
        'scope':'Finite source/coherence regressions. General saturation, inverse-tower compatibility, derived nonvanishing and infinite source summability use the accompanying proofs.'}
    out=ROOT/'research/nima/results/all-depth-observer-tower.json'
    out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))


if __name__=='__main__':main()
