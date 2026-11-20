"""Count global square choices on K(3,n) for direct two-link substitutions only.
A square is unrooted: the same filler applies at both opposite endpoint pairs.
"""
from itertools import combinations
from math import comb


def counts(n):
    # After every right pair passes, each right pair has 4 choices: omit
    # none of its three squares, or omit exactly one. For one fixed left
    # pair its edge has one absent and three present choices.
    total=lambda k:4**comb(k,2)
    conn=[0]*(n+1)
    for k in range(1,n+1):
        conn[k]=total(k)-sum(comb(k-1,s-1)*conn[s]*total(k-s) for s in range(1,k))
    bad=total(n)-conn[n]
    return 2**(3*comb(n,2)), total(n)-3*bad


def brute(n):
    pairs=list(combinations(range(n),2)); good=0
    for mask in range(1<<(3*len(pairs))):
        graphs=[[set() for _ in range(n)] for _ in range(3)]
        for j,(a,b) in enumerate(pairs):
            col=(mask>>(3*j))&7
            if col.bit_count()<2:break
            for i in range(3):
                if col>>i&1:graphs[i][a].add(b);graphs[i][b].add(a)
        else:
            for g in graphs:
                seen={0};stack=[0]
                while stack:
                    for v in g[stack.pop()]-seen:seen.add(v);stack.append(v)
                if len(seen)<n:break
            else:good+=1
    return good

if __name__=='__main__':
    for n in (2,3,4):assert brute(n)==counts(n)[1]
    print(counts(7))
