"""Read the same forbidden rectangle from its five-core and three-port boundaries."""
from itertools import combinations
from collections import Counter
from ramsey_retention_slice import decode,check,D
import json
P=D.parent/'ramsey_joint_constraint_transfer_k7.json'

def run():
    trial=json.loads(P.read_text());a=decode(trial['core_graph6']);w=trial['witness'];S=list(map(set,w['shared']));q=set(w['missed_clique']);V=set(range(len(a)));blue=lambda b:all(not(a[i]>>j&1) for i,j in combinations(b,2));Q=[set(c) for c in combinations(sorted(V),5) if blue(c)];forced=[c for c in Q if sum(not c&s for s in S)>=2];print('forward',len(Q),len(forced));out=dict(blue_fives=len(Q),required_fives=len(forced),panels={})
    for label in ('legal','illegal'):
        rows=S+[set(w[label])];miss=[sorted(c) for c in forced if not c&rows[3]];triples={};rects=Counter();
        for ids in combinations(range(4),3):
            common=V-set.union(*(rows[p] for p in ids));qs=[sorted(c) for c in Q if c<=common];triples[str(ids)]=dict(common_blue=sorted(common),blue_fives=qs);rects.update(map(tuple,qs))
        assert set(map(tuple,miss))==set(rects);out['panels'][label]=dict(missed=miss,triples=triples);print(label,'missed',miss,'triples',[(t,len(v['blue_fives'])) for t,v in triples.items()])
    rows=S+[set(w['illegal'])];g=a.copy()+[0]*5
    for p,s in enumerate(rows,len(a)):
        g[p]=sum(1<<x for x in s)|1<<26;g[26]|=1<<p
        for x in s:g[x]|=1<<p
    pairs=list(combinations(sorted(q),2));block={str(e):[x for x in range(27) if (g[e[0]]&g[e[1]])>>x&1] for e in pairs};print('triangle blockers',block)
    winners=[]
    for mask in range(1<<len(pairs)):
        G=g.copy();edges=[]
        for j,(x,y) in enumerate(pairs):
            if mask>>j&1:G[x]|=1<<y;G[y]|=1<<x;edges.append((x,y))
        if check(G,(1<<27)-1,3,8):winners.append(edges)
    out['reverse_fixed_exterior']=dict(q=sorted(q),triangle_blockers=block,assignments=2**len(pairs),legal=winners);print('legal fillings',len(winners),winners[:2]);dest=D.parent/'ramsey_joint_constraint_reverse.json';s=json.dumps(out,indent=2)+'\n';assert not dest.exists() or dest.read_text()==s;dest.write_text(s)
if __name__=='__main__':run()
