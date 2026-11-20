"""Blue-fibre substitution on the 35-circle, exact at (3,10). No external libraries."""
from itertools import combinations
from collections import Counter


def layers(rows):
    sets=[0]
    for j,r in enumerate(rows):
        sets += [s|1<<j for s in sets if not s&r]
    return sets

def main():
    n=35;steps={1,7,11,16,19,24,28,34};rows=[sum(1<<((v+d)%n) for d in steps) for v in range(n)]
    old=layers(rows);eight=[s for s in old if s.bit_count()==8];assert max(map(int.bit_count,old))==8
    # Every blue pair is jointly saturated: it already lies on a depth-8 path.
    coverage=Counter(pair for s in eight for pair in combinations([j for j in range(n) if s>>j&1],2));blue={(i,j) for i,j in combinations(range(n),2) if not rows[i]>>j&1};assert set(coverage)==blue and all(any(s>>i&1 for s in eight) for i in range(n));print('blue eights',len(eight),'all',len(blue),'blue pairs covered; minimum witnesses',min(coverage.values()))
    assert all(r in old for r in rows)  # red triangle-free => <=2 mutually red duplicate sites.
    parent=list(range(n))+[0,1];new=[sum(1<<j for j,w in enumerate(parent) if rows[v]>>w&1) for v in parent];b=layers(new);r=layers([((1<<len(new))-1)^x^(1<<i) for i,x in enumerate(new)]);print('order',len(new),'red layers',sorted(Counter(map(int.bit_count,r)).items()),'blue (depth 9,10)',sum(x.bit_count()==9 for x in b),sum(x.bit_count()==10 for x in b));assert max(map(int.bit_count,r))==2 and max(map(int.bit_count,b))==9
if __name__=='__main__':main()
