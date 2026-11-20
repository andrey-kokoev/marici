"""Color opposite-preserving moves by the untouched block of the reference partition. Prove computationally that these are three commuting free bit flips on eight opposite partitions."""
from itertools import product,combinations
from ramsey_strip_opposite_partition_transport import T,moves
for i,A in enumerate(T):
    colors=sorted(A);op=[j for j,B in enumerate(T) if not A&B];F={}
    for j in op:
        for d in T[j]:
            a,=[a for a in colors if set(a).isdisjoint(d)];F[j,colors.index(a)]=moves[i,j,d]
    assert len(F)==24
    for j in op:
        for c in range(3):assert F[F[j,c],c]==j
        for c,e in combinations(range(3),2):assert F[F[j,c],e]==F[F[j,e],c]
    origin=min(op);chart={}
    for bits in product((0,1),repeat=3):
        j=origin
        for c,b in enumerate(bits):
            if b:j=F[j,c]
        chart[bits]=j
    assert len(set(chart.values()))==8
    if i==1:print('literal entry partition 16: reference block colors',colors,'cube chart (partition vertex IDs)',{b:j+15 for b,j in chart.items()});print('29 -> 22 color',[c for c in range(3) if F[14,c]==7])
print('all 15 references give an exact three-bit cube with canonically block-labeled directions')
