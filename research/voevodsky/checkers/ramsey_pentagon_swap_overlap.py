"""Classify coexistence of individually legal one-swap probes by source incidence."""
from ramsey_pentagon_selector import charts,ind,coexists,combinations,Counter,Path,json


def run():
    counts=Counter();bins={};example=None
    for sq,qs,cycles in charts():
        U=set().union(*sq);W=set(range(1,11))-U;moving=U-set.intersection(*map(set,sq));probes={tuple(sorted((*e,z))):set(e) for e in qs for z in moving if ind({*e,z})}
        for a,b in combinations(sorted(probes),2):
            if sum(abs(i-j) for i,j in zip(a,b))!=1:continue
            A,B=probes[a],probes[b];miss=W-A-B
            if A!=B:
                z,=set(a)&U;partner,=[t for t in moving-{z} if not any({z,t}<=set(row) for row in sq)]
            for cycle in cycles:
                if tuple(sorted(A)) in cycle or tuple(sorted(B)) in cycle:continue
                if A==B:pred=True;reason='same outside pair'
                else:pred=any(abs(partner-i)==1 for i in miss);reason='different outside pairs'
                actual=coexists(sq,(a,b),cycle);assert pred==actual;counts[reason,pred]+=1
                key=(sq,tuple(sorted(cycle)),tuple(sorted(miss)));d=bins.setdefault(key,{});d.setdefault(pred,dict(probes=(a,b),partner=(partner if A!=B else None)))
                if len(d)==2 and example is None:example=dict(square=sq,cycle=sorted(cycle),missed=sorted(miss),cases=d.copy())
    out=dict(decisions={str(k):v for k,v in counts.items()},mixed_same_missed=sum(len(d)==2 for d in bins.values()),example=example);print(out);(Path(__file__).resolve().parents[1]/'results/ramsey_pentagon_swap_overlap.json').write_text(json.dumps(out,indent=2)+'\n')
if __name__=='__main__':run()
