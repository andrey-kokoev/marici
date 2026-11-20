"""Eight square frames. Exhaust all inverse-closed offset sets, not colorings of 39 vertices."""
from itertools import combinations

# q^i s^f, with s q s = q^-1.
G=[(i,f) for f in range(2) for i in range(4)]
def mul(g,h):
    i,f=g;j,k=h
    return ((i+(-1)**f*j)%4,f^k)
def inv(g):
    i,f=g;return ((-(-1)**f*i)%4,f)
def tests(S):
    def edge(g,h):return mul(inv(g),h) in S
    assert all(edge(g,h)==edge(h,g) for g in G for h in G)
    return tuple(sum(all(edge(g,h)==v for g,h in combinations(t,2)) for t in combinations(G,k)) for k,v in ((3,True),(4,False)))

def main():
    orbits={tuple(sorted({g,inv(g)})) for g in G[1:]};orbits=sorted(orbits);valid=[]
    for m in range(1<<len(orbits)):
        S={g for n,o in enumerate(orbits) if m>>n&1 for g in o}
        if tests(S)==(0,0):valid.append(S)
    print('tested',1<<len(orbits),'valid',len(valid));print('valid offsets',valid)
    tour=[(0,0),(1,0),(2,0),(3,0),(3,1),(2,1),(1,1),(0,1)]
    assert set(tour)==set(G)
    # Delete the frame bit, and require an ordinary loop-free base graph:
    # each pair of positions has just one color, irrespective of its frames.
    pos_only=[]
    for S in valid:
        if all((mul(inv(g),h) in S)==(mul(inv((g[0],0)),(h[0],0)) in S) for g,h in combinations(G,2)):pos_only.append(S)
    print('valid position-only readouts',len(pos_only))
if __name__=='__main__':main()
