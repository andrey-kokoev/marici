"""Can reuse of endpoints alone explain the sign? Enumerate all words modulo renaming."""
from itertools import combinations
from collections import Counter
from ramsey_34_chain_joins import completions


def words(w=(0,)):
    if len(w)==9:
        yield w
        return
    for v in range(max(w)+2):yield from words(w+(v,))


def readings(w):
    return tuple(sum(1<<i for i in range(j) if w[i+1]==w[j] or w[j+1]==w[i]) for j in range(8))

if __name__=='__main__':
    legal=set(completions());circle=tuple(sum(1<<i for i in range(j) if j-i in (1,4,7)) for j in range(8));counts=Counter();sample={};total=0
    for w in words():
        total+=1;r=readings(w)
        if r in legal:
            counts[r]+=1
            if r not in sample or len(set(w))>len(set(sample[r])):sample[r]=w
    print('tested',total,'words; represented',len(counts),'of',len(legal),'legal matrices; valid words',sum(counts.values()),'circle',circle in counts)
    if counts:
        r=max(sample,key=lambda r:len(set(sample[r])));w=sample[r];print('example',w,'extra positive links',[(i+1,j+1) for i,j in combinations(range(8),2) if j>i+1 and r[j]>>i&1]);print('words without loops or repeated arrows',sum(1 for w in words() if readings(w) in legal and all(a!=b for a,b in zip(w,w[1:])) and len(set(zip(w,w[1:])))==8))
