"""Test the four orientations left by cutting both bridges, keeping old signs fixed."""
from itertools import combinations, product
from ramsey_37_pair_rotation_rule import build
from pauli_realization_audit import independent_witness


def main():
    base=build(); n=len(base); assert n==22
    for flip20,flip21 in product((0,1),repeat=2):
        g=base.copy()
        for j,flip in ((20,flip20),(21,flip21)):
            if flip:
                for i in range(j):
                    g[i]^=1<<j; g[j]^=1<<i
        tri=next((t for t in combinations(range(n),3) if all(g[a]>>b&1 for a,b in combinations(t,2))),None)
        seven=independent_witness(g,7)
        print(flip20,flip21,'positive triangle',tri,'negative seven-set',seven)
        assert (tri is None and seven is None)==(not flip20 and not flip21)

if __name__=='__main__':main()
