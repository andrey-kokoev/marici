"""A mark costs one paired-position query (possibly two distinct incidence observations). Compare all frozen closure decoders under identification against the entire Hall dictionary, and explicitly audit what happens when the observed cycle is promised to be alternating. The true matching is not used to choose follow-up when two possibilities remain."""
from ramsey_strip_three_readings import rows,profiles,tables,bits,full,H
from collections import Counter
import json
rules=json.loads((H/'ramsey_strip_incidence_decoders.json').read_text())['fits'];results=[];prior=Counter()
for reading in rules:
    rule=set(map(tuple,reading['rule']));counts=Counter();cost=Counter();unknown=0
    for row,p in zip(rows,profiles):
        C=row['cycle'];T=[i for i in range(1,11) if p[i-1] in rule];alternating=full
        for i,u in enumerate(C):alternating &= bits[u,C[i-1]]|bits[u,C[(i+1)%22]]
        for parity in (0,1):
            def obs(i):return bits[C[i],C[(i+(1 if i%2==parity else -1))%22]]
            if reading is rules[0]:prior[alternating.bit_count(),(alternating&obs(1)).bit_count()]+=1
            m=full
            for i in T:m &= obs(i)&obs(22-i)
            n=m.bit_count();counts[n]+=1
            if n==1:cost[len(T)]+=1
            elif n==2:
                cand=[tab for j,tab in enumerate(tables) if m>>j&1];q=next(i for i in range(1,11) if cand[0][C[i]]!=cand[1][C[i]] or cand[0][C[-i]]!=cand[1][C[-i]]);assert q not in T and (m&obs(q)&obs(22-q)).bit_count()==1;cost[len(T)+1]+=1
            else:unknown+=1
    results.append(dict(rule=sorted(rule),marks=len(T),remaining=dict(counts),read_cost=dict(cost),more_than_two=unknown))
print('promise',prior);print('marks,remaining,cost,rule count',Counter((r['marks'],str(sorted(r['remaining'].items())),str(sorted(r['read_cost'].items()))) for r in results));(H/'ramsey_strip_read_cost.json').write_text(json.dumps(dict(promise={str(k):v for k,v in prior.items()},results=results),indent=2)+'\n')
