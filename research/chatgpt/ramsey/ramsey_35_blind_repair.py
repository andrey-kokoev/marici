"""List all minimum repairs using only the endpoint word and the (3,5) rules."""
from itertools import combinations


def solve(word):
    vs=range(1,len(word));pairs=set(combinations(vs,2))
    joins={(i,j) for i,j in pairs if word[i]==word[j-1] or word[j]==word[i-1]}
    triangles=[set(combinations(t,2)) for t in combinations(vs,3)]
    assert not any(t<=joins for t in triangles)
    threats=[set(combinations(t,2)) for t in combinations(vs,5) if joins.isdisjoint(combinations(t,2))]
    candidates=sorted(e for e in pairs-joins if not any(t<=joins|{e} for t in triangles) and any(e in t for t in threats))
    for size in range(len(candidates)+1):
        sols=[]
        for repair in combinations(candidates,size):
            r=set(repair)
            if all(t&r for t in threats) and not any(t<=joins|r for t in triangles):sols.append(repair)
        if sols:
            print('joins, threats, candidates:',len(joins),len(threats),len(candidates));print('minimum, repairs:',size,sols);return sols
    return []

if __name__=='__main__':solve('ABCDEFACBDGEGF')
