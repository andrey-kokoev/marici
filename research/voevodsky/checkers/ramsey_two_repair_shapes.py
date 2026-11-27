"""Classify all optimal parent pairs and helper assignments (not only first optimum)."""
from itertools import combinations,product
from collections import Counter
from pathlib import Path
import json
from ramsey_corner_joint_repairs import run


def audit(k):
    hist=Counter();shapes=Counter();examples={};split_keys=set()
    def classify(ss,bad,opts):
        minimal=sorted(h for h in bad if not any(g!=h and g&h==g for g in bad));single=sum(h.bit_count()==1 for h in minimal)
        solutions=[((i,j),(a,b)) for i,j in combinations(range(3),2) if all(h&((1<<i)|(1<<j)) for h in minimal) for a,b in product(opts[i],opts[j])];assert solutions
        hub='/'.join(sorted({'shared' if a==b else 'split' for _,(a,b) in solutions}));hist[single,hub]+=1
        def name(h,swap):return ''.join(t for bit,t in zip((1,2,4),('C','E','D') if swap else ('C','D','E')) if h&bit)
        label=min('+'.join(sorted(name(h,swap) for h in minimal)) for swap in (False,True));shapes[label]+=1
        if hub=='split':split_keys.add((tuple(sorted(ss[:3])),tuple(sorted(ss[3:]))))
        if (single,hub) not in examples:
            def sites(m):return [i+1 for i in range(k) if m>>i&1]
            witnesses=[]
            for h in minimal:
                u=ss[3]|ss[4];v=[]
                for i in range(3):
                    if h>>i&1:u|=ss[i]
                for x in range(k):
                    if not u>>x&1 and (not v or v[-1]!=x):v.append(x+1)
                assert len(v)>=5-h.bit_count();witnesses.append([name(h,False),v[:5-h.bit_count()]])
            examples[single,hub]=dict(rows=list(map(sites,ss)),witnesses=witnesses,solutions=solutions)
    tally=run(k,classify)
    if split_keys:
        flip=lambda m:sum(1<<(k-1-i) for i in range(k) if m>>i&1)
        assert len(split_keys)==2 and all((tuple(sorted(map(flip,p))),tuple(sorted(map(flip,n)))) in split_keys and (tuple(sorted(map(flip,p))),tuple(sorted(map(flip,n))))!=(p,n) for p,n in split_keys)
    assert sum(hist.values())==tally['counts']['2'];encode=lambda d:{str(i):n for i,n in d.items()};out=dict(width=k,singletons_and_hubs=encode(hist),minimal_parent_witness_shapes=dict(shapes),examples=encode(examples));print(k,hist,shapes);return out
if __name__=='__main__':
    data=[audit(k) for k in (10,11)];(Path(__file__).resolve().parents[1]/'results/ramsey_two_repair_shapes.json').write_text(json.dumps(data,indent=2)+'\n')
