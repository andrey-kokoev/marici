"""Exhaust cross signs for four doubled witnesses. No catalogue or target host."""
from itertools import permutations, combinations

def main():
    t=4;arcs=list(permutations(range(t),2));accepted=0
    # 0,1: positive endpoints; 2+i: witness; 6+i: left; 10+i: right.
    for m in range(1<<len(arcs)):
        pos={(0,1)}
        for i in range(t):pos.update(((0,6+i),(1,10+i),(2+i,6+i),(2+i,10+i)))
        D={arc for j,arc in enumerate(arcs) if m>>j&1}
        pos.update((6+i,10+j) for i,j in D)
        I=[0];tri=False
        for j in range(14):
            p=sum(1<<i for i in range(j) if (i,j) in pos)
            if p not in I:tri=True
            I += [s|1<<j for s in I if not s&p]
        valid=not tri and max(s.bit_count() for s in I)<6
        rule=all((i,j) in D or (j,i) in D for i,j in combinations(range(t),2))
        assert valid==rule;accepted+=valid
    print(accepted,'valid out of',1<<len(arcs))
if __name__=='__main__':main()
