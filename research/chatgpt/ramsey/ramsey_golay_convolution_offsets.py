"""A single Golay convolution as a symmetric offset table on Z/23. No dependencies."""
from collections import Counter
from itertools import combinations
N=23
G=sum(1<<i for i in (0,1,5,6,7,9,11))
def encode(m):
    v=0
    for i in range(12):
        if m>>i&1:v ^= G<<i
    return v

def main():
    counts=Counter();example=None
    words={encode(m) for m in range(4096)}
    assert len(words)==4096 and min(w.bit_count() for w in words if w)==7
    for w in sorted(words):
        D={i for i in range(1,N) if w>>i&1};
        if D!={-i%N for i in D}:continue
        # Ignore the diagonal; translation lets us root a certificate at zero.
        tri=next(((0,a,b) for a,b in combinations(sorted(D),2) if (b-a)%N in D),None)
        if tri:counts['triangle']+=1;continue
        seven=next((t for t in combinations(range(1,N),6) if all((b-a)%N not in D for a,b in combinations((0,)+t,2))),None)
        assert seven is not None;counts['no triangle, seven']+=1
        if D:example=(D,(0,)+seven)
    print('symmetric words by certificate',counts,'nonempty triangle-free example',example)
    w=encode(1);D={i for i in range(1,N) if w>>i&1};print('single pulse: offsets',sorted(D),'symmetric?',D=={-i%N for i in D})
if __name__=='__main__':main()
