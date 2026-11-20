"""Find a small graph invariant distinguishing residual-fill outputs, independently of isomorphism search. Count common-neighbor multiplicities and four-cycles per vertex."""
from collections import Counter
from itertools import combinations
from ramsey_strip_short_output_isomorphism import G
for i,N in enumerate(G,1):
    pairhist=Counter(len(N[a]&N[b]) for a,b in combinations(range(22),2));pervertex=[]
    for v in range(22):
        count=sum(len((N[a]&N[b])-{v}) for a,b in combinations(N[v],2));pervertex.append(count)
    total=sum(pervertex)//4;assert sum(pervertex)%4==0
    assert total==sum(k*(k-1)//2*n for k,n in pairhist.items())//2
    print('output',i,'common neighbors',dict(sorted(pairhist.items())),'four-cycles',total,'four-cycles per vertex distribution',dict(sorted(Counter(pervertex).items())))
