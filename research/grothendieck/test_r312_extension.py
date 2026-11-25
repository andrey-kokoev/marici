"""Exact one-vertex extension gate for the 48-vertex cyclic witness."""
n = 48
full = (1 << n) - 1
dist = {2,3,8,14,15,24}
compatible = [sum(1 << w for w in range(n) if w != v and min((v-w)%n,(w-v)%n) not in dist) for v in range(n)]

def maximal(r,p,x):
    # Bron-Kerbosch on the complement: each maximal independent set once.
    if not (p|x):
        yield r
        return
    pivot = ((p|x) & -(p|x)).bit_length()-1
    todo = p & ~compatible[pivot]
    while todo:
        bit = todo & -todo
        c = compatible[bit.bit_length()-1]
        yield from maximal(r|bit,p&c,x&c)
        p ^= bit
        x |= bit
        todo ^= bit

if __name__ == '__main__':
    sets = list(maximal(0,full,0))
    assert max(s.bit_count() for s in sets)==11
    large = [s for s in sets if s.bit_count()==11]
    # For each vertex, bitset of 11-sets it hits.
    hits = [sum(1<<i for i,s in enumerate(large) if s>>v&1) for v in range(n)]
    def missed(s):
        h=0
        while s:
            b=s&-s; s ^= b; h |= hits[b.bit_length()-1]
        return len(large)-h.bit_count()
    score,best=min((missed(s),s) for s in sets)
    print('maximal neighborhoods',len(sets),'independent 11-sets',len(large),'minimum missed',score,'best neighborhood',[i for i in range(n) if best>>i&1])
