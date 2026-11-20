"""Exact stabilizer of the labeled A/B scopes from ramsey_interface_index_probe.
Root 0 and singleton 1 differ by their number of neighbors in B (5 and 0).
Every witness is identified by its distinct pair of singleton neighbors.
"""
from itertools import permutations,combinations
from collections import Counter
from ramsey_37_pair_rotation_rule import build

def main():
    g=build(); A=(0,1); B=tuple(range(2,7)); W=tuple(range(7,22)); S=(1,)+B
    assert [sum(g[v]>>b&1 for b in B) for v in A]==[5,0]
    pair={w:tuple(v for v in S if g[w]>>v&1) for w in W}
    inv={p:w for w,p in pair.items()};assert set(inv)==set(combinations(S,2))
    stats=Counter();invol=Counter()
    for b in permutations(B):
        p=dict(zip((0,)+S,(0,1)+b));p.update({w:inv[tuple(sorted(p[v] for v in pair[w]))] for w in W})
        if all((g[i]>>j&1)==(g[p[i]]>>p[j]&1) for i,j in combinations(range(22),2)):
            fixed=sum(p[w]==w for w in W);stats[fixed]+=1
            if all(p[p[w]]==w for w in W):invol[fixed]+=1
    print('all by fixed witness count:',sorted(stats.items()),'self-inverse:',sorted(invol.items()));assert not invol[1]

if __name__=='__main__':main()
