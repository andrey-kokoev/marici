"""Thin quartet constraints, never attachment candidates. Counts unordered triples."""
from itertools import combinations,combinations_with_replacement
from collections import Counter


def main():
    reps=[(0,2,4,6),(0,2,6,9),(0,3,6,9)]
    Q=[sum(1<<((x+d)%13) for x in r) for r in reps for d in range(13)]
    blue=[sum(1<<x for x in t) for n in range(14) for t in combinations(range(13),n) if all((y-x)%13 not in {1,5,8,12} for x,y in combinations(t,2))]
    assert set(Q)=={b for b in blue if b.bit_count()==4} and all(any(b&q==b for q in Q) for b in blue)
    miss=[sum(1<<j for j,q in enumerate(Q) if not a&q) for a in Q]; counts=Counter();private={};residual=[set(),set()]
    for i,j,k in combinations_with_replacement(range(39),3):
        x,y,z=miss[i],miss[j],miss[k]; bad=x&y|x&z|y&z
        counts[sum(1<<a for a in range(3) if bad&(8191<<(13*a)))]+=1
        if not bad&(8191<<13):
            a=bad&8191;c=bad>>26
            assert bool(a)!=bool(c) # each survivor needs only one kind of test
            residual[bool(c)].add(a or c)
        if bad.bit_count()==1:private[bad.bit_length()-1]=(i,j,k)
    for t in range(1,8):print('keep', ''.join('ABC'[i] for i in range(3) if t>>i&1),'survivors',sum(c for s,c in counts.items() if not s&t))
    print('individually necessary',len(private),'representative private triples',{q:private[q] for q in (0,13,26) if q in private})
    assert counts[0]==0 and set(private)==set(range(13,26))
    for group,clauses in zip('AC',residual):
        best=min((m for m in range(8192) if all(m&v for v in clauses)),key=int.bit_count)
        print(group,'minimum extra shifts',[d for d in range(13) if best>>d&1])

if __name__=='__main__':main()
