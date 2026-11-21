"""Construct decision trees from exact-one constraints only. Each disjoint-duad link xy corresponds to flag (partition xyz, middle z); blue selects that flag. No list of legal wirings in decoder."""
from itertools import combinations
from functools import lru_cache
from collections import Counter
from pathlib import Path
import json
P=list(combinations(range(6),2));T=[t for t in combinations(range(15),3) if len(set().union(*(P[i] for i in t)))==6];E=[e for e in combinations(range(15),2) if set(P[e[0]]).isdisjoint(P[e[1]])];F=(1<<45)-1
rows=[0]*30
for i,(x,y) in enumerate(E):
    t=next(t for t in T if x in t and y in t);z,=set(t)-{x,y};rows[T.index(t)]|=1<<i;rows[15+z]|=1<<i
assert all(r.bit_count()==3 for r in rows)
@lru_cache(None)
def close(on,off):
    while True:
        before=(on,off)
        for r in rows:
            a=r&on;b=r&~off
            if not b or a.bit_count()>1 or on&off:return None
            if a:off|=r^a
            elif b&(b-1)==0:on|=b
        if before==(on,off):return before

def tree(order,failed_literal=False):
    H=Counter();dead=0;leaves=set()
    def visit(on,off,pos,depth):
        nonlocal dead
        state=close(on,off)
        if state is None:dead+=1;return
        on,off=state
        while pos<45:
            b=1<<order[pos];pos+=1
            if (on|off)&b:continue
            if failed_literal:
                left=close(on|b,off);right=close(on,off|b)
                if left is None or right is None:
                    if left is None and right is None:dead+=1;return
                    on,off=left or right;continue
            visit(on|b,off,pos,depth+1);visit(on,off|b,pos,depth+1);return
        assert on|off==F and all((on&r).bit_count()==1 for r in rows);leaves.add(F^on);H[depth]+=1
    visit(0,0,0,0);return H,dead,leaves
if __name__=='__main__':
    # Independent full list used only to audit constructed leaves and compare ideal costs.
    from ramsey_transport_order_bits import group,j,a,b,Q,score,total
    import random
    out={};base=list(range(45));rng=random.Random(7308);orders=[base[:]]
    for _ in range(100):rng.shuffle(base);orders.append(base[:])
    for probe in (False,True):
        dif=[];oracle_gaps=[];fixed={}
        for it,base in enumerate(orders):
            costs=[]
            for name,gens in [('plain',[]),('row',[j])]+([('square',[a,b,j])] if it==0 else []):
                order=group(base,gens);h,d,L=tree(order,probe);assert L==set(Q);costs.append(total(h));ideal=score(order);oracle_gaps.append(total(h)-total(ideal));
                if it==0:fixed[name]=dict(hist=dict(h),dead_branches=d,mean=total(h)/288,worst=max(h),extra_over_ideal=total(h)-total(ideal))
            if it:dif.append(costs[1]-costs[0])
        out[str(probe)]=dict(fixed=fixed,random_orders=len(dif),row_minus_plain=sum(dif)/(288*len(dif)),better=sum(x<0 for x in dif),tied=dif.count(0),worse=sum(x>0 for x in dif),max_aggregate_oracle_gap=max(oracle_gaps));print(probe,out[str(probe)],flush=True)
    (Path(__file__).parent/'ramsey_local_transport_decoder.json').write_text(json.dumps(out)+'\n')
