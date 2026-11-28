"""Project the five outside degrees onto flank-edge counts; no pentagon input to predict()."""
from itertools import combinations,product
from collections import Counter
from ramsey_pentagon_selector import charts
from ramsey_two_repairs_edge_count import count
from ramsey_inherited_swap_selector import D
import json


def ways(W,red,blue):
    edges=list(combinations(W,2));red=red|{e for e in edges if e[1]-e[0]==1};blue=blue|{e for e in edges if e[1]-e[0]==2}
    if red&blue:return 0
    deg=tuple(2-sum(i in e for e in red) for i in W)
    if min(deg)<0:return 0
    states=Counter({deg:1})
    for e in edges:
        if e in red|blue:continue
        i,j=map(W.index,e)
        for d,n in list(states.items()):
            if d[i] and d[j]:
                v=list(d);v[i]-=1;v[j]-=1;states[tuple(v)]+=n
    return states[(0,)*5]


def predict(sq):
    U=set().union(*sq);W=sorted(set(range(1,11))-U);f,=set.intersection(*map(set,sq));mov=U-{f};edges=[];blocks=[]
    for x,z in combinations(sorted(mov),2):
        e=x-1,z+1;Y=mov-{x,z}
        if any({x,z}<=set(r) for r in sq) or not set(e)<=set(W) or any(abs(y-i)==1 for y in Y for i in e):continue
        edges.append(e);options=[(0,{e},set())];K=sorted(set(W)-set(e))
        for ab in combinations(K,2):
            n=sum(abs(i-j)==1 for i in ab for j in Y);m=2 if n==0 else 1;k=2*m+(all(abs(f-i)!=1 for i in e))*(m+2*(2-n));options.append((k,{ab},{e}))
        blocks.append(options)
    vectors=Counter()
    for flags in product(*blocks):
        n=ways(W,set().union(*(r for k,r,b in flags)),set().union(*(b for k,r,b in flags)))
        if n:vectors[tuple(k for k,r,b in flags)]+=n
    return edges,vectors


def audit():
    hist=Counter();profiles=Counter();examples={};records=[]
    for sq,_,cycles in charts():
        edges,v=predict(sq);assert v==Counter(tuple(0 if e in c else count(sq,c,e) for e in edges) for c in cycles)
        if len(cycles)==1:continue
        totals=Counter()
        for vec,n in v.items():totals[sum(vec)]+=n
        label='variable' if len(totals)>1 else 'fixed positive' if max(totals)>0 else 'fixed zero';hist[label]+=1;profiles[tuple(sorted(totals))]+=1
        row=dict(square=sq,edges=edges,counts=[dict(vector=k,ways=n) for k,n in sorted(v.items())],totals=totals);records.append(row);examples.setdefault(label,row)
    from ramsey_two_repairs_opposite import run
    keys=run();fixed_labels=[]
    for row in records:
        if len(row['totals'])==1 and max(row['totals'])>0:
            groups={}
            for s,c,r in keys:
                if s==row['square']:groups.setdefault(c,set()).add(r)
            fixed_labels.append(dict(square=row['square'],shared_quartets=len(set.intersection(*groups.values()))))
    result=dict(fixed_positive_label_checks=fixed_labels,hist=hist,profiles={str(k):n for k,n in profiles.items()},examples=examples,squares=records);print(hist,profiles,examples);(D/'ramsey_square_repair_counts.json').write_text(json.dumps(result,indent=2)+'\n')
if __name__=='__main__':audit()
