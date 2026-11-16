"""Check Hall identity and tight-face structure for the seven 17-node
R(3,6)-critical A graphs. Standard library only.
"""
from itertools import combinations
from collections import Counter
from ramsey36_four_birth_probe import G6, parse, independent_masks


def local_hall(G,L):
    n=len(G); Lmask=sum(1<<v for v in L)
    H=[v for v in range(n) if not (Lmask>>v&1)]
    supports=[sum(1<<i for i,v in enumerate(L) if G[u]>>v&1)
              for u in H]
    adj=[sum(1<<j for j,w in enumerate(H) if w!=v and G[u]>>w&1)
         for v,u in enumerate(H)]
    Tbest=-99; tght=Counter(); first=[]; independent_count=0
    for T in range(1<<len(H)):
        if any((T>>i&1) and (T&adj[i]) for i in range(len(H))):
            continue
        independent_count+=1
        nbrs=0
        for i,s in enumerate(supports):
            if T>>i&1:nbrs|=s
        gap=T.bit_count()-nbrs.bit_count()
        Tbest=max(Tbest,gap)
        if T and not gap:
            tght[T.bit_count()]+=1
            if len(first)<3:first.append(([H[i] for i in range(len(H)) if T>>i&1],
                                           [L[j] for j in range(len(L)) if nbrs>>j&1]))
    return Tbest,independent_count,dict(tght),first


def main():
    for gi,s in enumerate(G6,1):
        G=parse(s)
        independent5=[S for S,k in independent_masks(G,5) if k==5]
        L=[v for v in range(17) if independent5[0]>>v&1]
        deficit,nind,tight,examples=local_hall(G,L)
        assert deficit==0
        print(f'graph {gi}: B5={L}, B-independent exterior faces={nind},'
              f' Hall-tight faces by size={tight}')
    print('Every graph obeys exact independent-set Hall expansion.')

if __name__=='__main__':main()
