"""Lift a 3x8 cell index by unrestricted sequential borders. Seed cores are obtained by puncturing valid cyclic order-26 graphs at every pair-distance; no catalogue. No cyclic constraint on new addresses."""
from pathlib import Path
import json
from collections import Counter
from ramsey_3k_target_free_prime import red_masks

def independent(A):
    ss=[0]
    for i,a in enumerate(A):ss.extend([s|1<<i for s in ss if not s&a])
    return ss

def visit(A,ss,left):
    if left==0:return A
    seven=[s for s in ss if s.bit_count()==7];opts=[r for r in ss if all(s&r for s in seven)]
    for r in opts:
        n=len(A);new=[a|((r>>i&1)<<n) for i,a in enumerate(A)]+[r];sv=ss+[s|1<<n for s in ss if not s&r];ans=visit(new,sv,left-1)
        if ans:return ans

def main():
    X=[[j>>i&1 for j in range(8)] for i in range(3)];seeds=red_masks(26,8);best=0;stats=Counter()
    for mask in sorted(seeds):
        for gap in range(1,14):
            ids=[j for j in range(26) if j not in (0,gap)];ds={i+1 for i in range(13) if mask>>i&1};red=lambda x,y:min((x-y)%26,(y-x)%26) in ds
            core=[sum(1<<j for j,y in enumerate(ids) if red(x,y)) for x in ids];ss=independent(core);assert max(map(int.bit_count,ss))==7
            a=visit(core,ss,3);stats['tested']+=1
            if a:stats['reached27']+=1
            if not a and not best:a=visit(core,ss,2)
            if a and len(a)>best:
                best=len(a);s=independent(a);assert max(map(int.bit_count,s))==7 and all(r in s for r in a);T=[[[a[3*j+i]>>w&1 for w in range(best)] for j in range(8)] for i in range(3)];Path(__file__).with_suffix('.json').write_text(json.dumps(dict(table=X,seed_offsets=sorted(ds),deleted=[0,gap],rows=a,tensor=T)));print('verified',best,'gap',gap,'offsets',sorted(ds),flush=True)
            if best==27:print(stats);return
    print('seeds',len(seeds),stats)
if __name__=='__main__':main()
