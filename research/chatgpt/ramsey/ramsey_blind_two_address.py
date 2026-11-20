"""Blind recovery of two unordered labeled-neighborhood columns, plus their shared bit.
Solve hitting and incompatibility constraints jointly; no single-column candidate list.
"""
from itertools import combinations
from collections import Counter
from random import Random
from ramsey_37_pair_rotation_rule import build
from ramsey_delayed_address_move import moves
from ramsey_difference_next_round import add

def recover(rows):
    n=len(rows); m=(1<<n)-1; blue=[0]
    for i,r in enumerate(rows):blue += [s|1<<i for s in blue if not s&r]
    five=[s for s in blue if s.bit_count()==5]; six=[s for s in blue if s.bit_count()==6]; out=set()
    for sign in (0,1):
        clauses=six+[s<<n for s in six]+([] if sign else [s|(s<<n) for s in five]);bad=[(r<<(j*n))|((1<<(i+(1-j)*n)) if sign else 0) for j in range(2) for i,r in enumerate(rows)]
        def dfs(chosen,free,need):
            if need:
                options=min((s&free for s in need),key=int.bit_count)
                while options:
                    bit=options&-options;options-=bit;free^=bit
                    dfs(chosen|bit,free&~bad[bit.bit_length()-1],[s for s in need if not s&bit])
            else:
                a,b=sorted((chosen&m,chosen>>n));out.add((a,b,sign))
                while free:
                    bit=free&-free;free^=bit
                    dfs(chosen|bit,free&~bad[bit.bit_length()-1],[])
        dfs(0,m|(m<<n),clauses)
    return out

def main():
    g=build(); rng=Random(37);hist=Counter();examples={}
    for u,v in combinations(range(22),2):
        labels=[i for i in range(22) if i not in (u,v)];rng.shuffle(labels)
        project=lambda r:sum((r>>i&1)<<j for j,i in enumerate(labels))
        rows=[project(g[i]) for i in labels];out=recover(rows)
        truth=(*sorted((project(g[u]),project(g[v]))),g[u]>>v&1);assert truth in out
        # Independent exhaustive check on first example of each multiplicity.
        if len(out) not in examples:
            check={(*sorted((a,b&((1<<20)-1))),b>>20) for a in moves(rows)[2] for b in moves(add(rows,a))[2]};assert out==check
            examples[len(out)]=(u,v)
        hist[len(out)]+=1
    print('completions -> deletion count:',sorted(hist.items()));print('example deletions:',examples)
if __name__=='__main__':main()
