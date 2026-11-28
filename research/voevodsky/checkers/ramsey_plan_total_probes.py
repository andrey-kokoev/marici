"""Plan the total readout from square degree constraints, before reading any attachment verdict."""
from itertools import combinations
from collections import Counter
from ramsey_pentagon_selector import charts
from ramsey_square_repair_counts import predict,count
from ramsey_inherited_swap_selector import D,evaluate
import json


def plan(sq):
    flank,vectors=predict(sq);U=set().union(*sq);W=set(range(1,11))-U;f,=set.intersection(*map(set,sq));mov=U-{f};totals={sum(v) for v in vectors}
    def convert(edges):
        return [tuple(sorted((*e,min(z for z in mov if all(abs(z-i)>1 for i in e))))) for e in edges]
    for size in range(len(flank)+1):
        for ids in combinations(range(len(flank)),size):
            reads={}
            for v in vectors:reads.setdefault(tuple(v[i]>0 for i in ids),set()).add(sum(v))
            if all(len(t)==1 for t in reads.values()):
                edges=[flank[i] for i in ids];return edges,convert(edges),{k:next(iter(t)) for k,t in reads.items()},'flank' if edges else 'constant'
    # Only remaining case in the width-ten census: one always-blue flank,
    # and exactly one of the other three sites touches the other movable axis.
    e,=flank;assert totals=={5,10};X={e[0]+1,e[1]-1};Y=mov-X;K=W-set(e);z,=[i for i in K if any(abs(i-j)==1 for j in Y)];inner=tuple(sorted(K-{z}));return [inner],convert([inner]),{(True,):5,(False,):10},'inner'


def audit():
    counts=Counter();result=[]
    for sq,_,cycles in charts():
        edges,rows,read,kind=plan(sq);counts[kind,len(rows)]+=1
        for c in cycles:
            if rows:ok={s for s, in evaluate(10,sq,c,[(r,) for r in rows])};bits=tuple(r in ok for r in rows)
            else:bits=()
            W=set(range(1,11))-set().union(*sq);n=sum(count(sq,c,e) for e in combinations(sorted(W),2) if e not in c);assert read[bits]==n
        assert len(rows)==(len(set(read.values()))-1).bit_length()
        result.append(dict(square=sq,kind=kind,edges=edges,rows=rows,read=[dict(bits=k,total=v) for k,v in read.items()]))
    out=dict(counts={str(k):v for k,v in counts.items()},plans=result);print(counts);print([r for r in result if r['kind']=='inner']);(D/'ramsey_plan_total_probes.json').write_text(json.dumps(out,indent=2)+'\n')
if __name__=='__main__':audit()
