"""Count successor choices without constructing a cycle; compare every subset of inherited marks."""
from functools import lru_cache
from itertools import combinations
from collections import Counter
from pathlib import Path
import json
from ramsey_inherited_swap_selector import run

@lru_cache(None)
def count_cycles(W,blue):
    req=[e for e in combinations(W,2) if e[1]-e[0]==1];usable=[e for e in combinations(W,2) if e[1]-e[0]!=2 and e not in blue];short=[i for i in W if sum(i in e for e in usable)<2]
    if short or not set(req)<=set(usable):return 0,short
    deficit=tuple(2-sum(i in e for e in req) for i in W);dp={deficit:1}
    for e in usable:
        if e in req:continue
        i,j=map(W.index,e);old=dp.copy()
        for d,n in old.items():
            if d[i] and d[j]:
                v=list(d);v[i]-=1;v[j]-=1;t=tuple(v);dp[t]=dp.get(t,0)+n
    return dp.get((0,)*5,0),short

def run_test():
    counts=Counter();examples=[]
    def audit(sq,path,marks,children):
        U=set().union(*sq);W=tuple(sorted(set(range(1,11))-U));mov=U-set.intersection(*map(set,sq));labels={}
        for m in marks:
            a,b=map(set,m);A=a-U;B=b-U;blue=frozenset(tuple(sorted(e)) for e in (A,B));ok=True
            if A!=B:
                z,=a&U;p,=[i for i in mov-{z} if not any({i,z}<=set(s) for s in sq)];ok=any(abs(i-p)==1 for i in set(W)-A-B)
            labels[m]=ok,blue
        def pred(ms):
            if not all(labels[m][0] for m in ms):return 0,[]
            return count_cycles(W,frozenset().union(*(labels[m][1] for m in ms)))
        for n in range(len(marks)+1):
            for ms in combinations(sorted(marks),n):
                v,short=pred(ms);assert v==sum(set(ms)<=s for c,s in children);counts['collections_checked']+=1
                if len(ms)>=2 and v==0 and all(pred(ms[:i]+ms[i+1:])[0] for i in range(n)):
                    counts['minimal_joint_conflicts']+=1;examples.append(dict(old_path=path,marks=ms,W=W,short=short,required_blue=sorted(set().union(*(labels[m][1] for m in ms)))))
    run(audit);assert len(examples)==3 and all(x['short']==[8] for x in examples);out=dict(counts=counts,examples=examples);print(out);(Path(__file__).resolve().parents[1]/'results/ramsey_inherited_joint_degree.json').write_text(json.dumps(out,indent=2)+'\n')
if __name__=='__main__':run_test()
