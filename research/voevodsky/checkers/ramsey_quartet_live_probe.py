"""Install the probe as a fifth port, not just as a separate read on the square."""
from itertools import combinations
from collections import Counter
from ramsey_quartet_last_choice import decode
from ramsey_two_repairs_opposite import run
from ramsey_inherited_swap_selector import evaluate,D
from ramsey_pentagon_selector import path
import json


def independent_sets(n,edges,k):
    nb=[0]*(n+1)
    for i,j in edges:nb[i]|=1<<j;nb[j]|=1<<i
    def extend(pool,need,t):
        if not need:yield t;return
        while pool.bit_count()>=need:
            b=pool&-pool;pool^=b;yield from extend(pool&~nb[b.bit_length()-1],need-1,t|b)
    return list(extend((1<<(n+1))-2,k,0))


def configs(sq,rs,c):
    supports=sq+rs;base=path|set(c)|{(i,11+j) for j,r in enumerate(supports) for i in r}|{(11+i,15+j) for i,r in enumerate(sq) for j,s in enumerate(rs) if set(r).isdisjoint(s)}
    options=[(15+i,15+j) for i,j in combinations(range(4),2) if set(rs[i]).isdisjoint(rs[j]) and all(set(r)&set(rs[i]+rs[j]) for r in sq)]
    for size in range(2,len(options)+1):
        for es in combinations(options,size):
            g=base|set(es)
            if any(all(e in g for e in combinations(q,2)) for q in combinations(range(15,19),3)) or independent_sets(18,g,7):continue
            yield size,es,[((1<<i)|(1<<j)) for i,j in g],independent_sets(18,g,6)


def attach(sq,rs,r,states):
    base=sum(1<<i for i in r)+sum(1<<(11+j) for j,s in enumerate(sq) if set(s).isdisjoint(r));opts=[15+j for j,s in enumerate(rs) if set(s).isdisjoint(r)]
    for size,es,red,sixes in states:
        for n in range(len(opts)+1):
            for links in combinations(opts,n):
                mask=base+sum(1<<i for i in links)
                if all(mask&e!=e for e in red) and all(mask&s for s in sixes):return dict(quartet_links=es,probe_links=links)
    return None


def audit():
    counts=Counter();examples={};records=[];coexist_counts=Counter()
    for sq,rs in sorted({(s,r) for s,c,r in run()}):
        tag,e,probe,cs=decode(sq,rs)
        if not probe:continue
        probe=tuple(probe);queries=[(r,) for r in combinations(range(1,11),3) if r not in sq+rs and all(p not in path for p in combinations(r,2))];legal=[{s for s, in evaluate(10,sq,set(c),queries)} for c in cs];choices=[]
        state_sets=[list(configs(sq,rs,c)) for c in cs]
        for i,c in enumerate(cs):
            states=state_sets[i];assert states and states[0][0]==2
            for r in sorted(legal[i]-legal[1-i]):
                act=attach(sq,rs,r,states)
                if act:choices.append(dict(row=r,cycle=c,**act))
        default=any(t['row']==probe for t in choices);same=any(set(e)<=set(t['row']) and set(t['row'])-set().union(*sq)==set(e) for t in choices);key=tag,default,same,bool(choices);counts[key]+=1
        joint_only=[];patterns=Counter()
        for r in sorted(legal[0]&legal[1]):
            acts=[attach(sq,rs,r,ss) for ss in state_sets];i=int(not acts[0]);patterns[sum(bool(a) for a in acts)]+=1
            if bool(acts[0])!=bool(acts[1]):joint_only.append(dict(row=r,cycle=cs[i],**acts[i]))
        coexist_counts[tag,bool(choices),bool(joint_only)]+=1
        item=dict(square=sq,quartet=rs,edge=e,probe=probe,canonical_joint=default,live=choices,joint_only=joint_only,common_single_rows_by_number_of_joint_passes=patterns);records.append(item);examples.setdefault(str(key),item)
    out=dict(counts={str(k):v for k,v in counts.items()},coexist_counts={str(k):v for k,v in coexist_counts.items()},records=records);print(counts);print([(k,v['quartet'],v['probe'],v['live'][:1]) for k,v in examples.items()]);(D/'ramsey_quartet_live_probe.json').write_text(json.dumps(out,indent=2)+'\n')
if __name__=='__main__':audit()
