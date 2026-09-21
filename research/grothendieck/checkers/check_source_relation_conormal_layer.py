"""Local terminal relations and the first nonzero I^2 corner in four primes."""
from pathlib import Path
from itertools import combinations,permutations,product
from collections import defaultdict
import importlib.util
import json
import sympy as s
ROOT=Path(__file__).resolve().parents[3]
spec=importlib.util.spec_from_file_location('sig',ROOT/'research/grothendieck/theta_interval_signature.py')
a=importlib.util.module_from_spec(spec);spec.loader.exec_module(a)

def record(start,word,marks):
    result={():1};state=start
    for p,keep in zip(word,marks):
        target=state|1<<p
        if keep:
            result={w+(j,):c for w,c in result.items() for j in range(a.POSITION[state],a.POSITION[target])}
        state=target
    return result

def relations(pair):
    p,q=pair;out=[]
    for patterns in (((False,False),),((False,True),(True,False))):
        out.append({((p,q),m):1 for m in patterns}|{((q,p),m):-1 for m in patterns})
    return out

def evaluate(start,relation):
    out=defaultdict(int)
    for (word,marks),c in relation.items():
        for w,v in record(start,word,marks).items():out[w]+=c*v
    return {w:c for w,c in out.items() if c}

def terminal_rank(start,letters):
    cols=[record(start,w,m) for w in permutations(letters) for m in product((False,True),repeat=len(letters))]
    keys=sorted(set().union(*(set(c) for c in cols)))
    return s.Matrix([[c.get(k,0) for c in cols] for k in keys]).rank()

allpaths=[(w,m) for w in permutations(range(4)) for m in product((False,True),repeat=4)]
index={v:i for i,v in enumerate(allpaths)}
columns=[];local_checks=0
for pair in combinations(range(4),2):
    middle=sum(1<<j for j in pair)
    complement=tuple(j for j in range(4) if j not in pair)
    left,right=relations(pair),relations(complement)
    for start,letters,rels in ((0,pair,left),(middle,complement,right)):
        assert terminal_rank(start,letters)==6
        assert all(not evaluate(start,r) for r in rels)
        local_checks+=1
    for l,r in product(left,right):
        combined=defaultdict(int)
        for (u,mu),x in l.items():
            for (v,mv),y in r.items():combined[u+v,mu+mv]+=x*y
        assert combined and not evaluate(0,combined)
        col=s.zeros(len(allpaths),1)
        for key,c in combined.items():col[index[key]]=c
        columns.append(col)
products=s.Matrix.hstack(*columns)
assert products.cols==24 and products.rank()==24
rank3=terminal_rank(0,(0,1,2))
assert rank3==26
rank4=terminal_rank(0,(0,1,2,3))
assert rank4>0
result={'schema':'marici.grothendieck.source-relation-conormal-layer.v1','passed':True,
        'local_two_event_diamonds_checked':local_checks,
        'two_event_source_kernel_dimension':2,
        'three_event_terminal_rank':rank3,'three_event_source_kernel_dimension':48-rank3,
        'four_event_terminal_rank':rank4,'four_event_source_kernel_dimension':384-rank4,
        'four_event_conormal_dimension':(384-rank4)-24,
        'four_event_I_squared_corner_dimension':24,
        'checks':{'all_local_relations_vanish':True,'all_products_vanish':True,
                  'twenty_four_products_independent':True},
        'scope':'Exact coefficient source with independent chamber labels. Tor identification follows from the quotient-algebra theorem; four-event terminal rank and first I^2 layer are computed.'}
p=ROOT/'research/grothendieck/results/source-relation-conormal-layer.json'
p.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,indent=2))
