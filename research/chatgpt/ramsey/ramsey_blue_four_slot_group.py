"""Role permutations from incidence transport, not graph automorphisms."""
from collections import deque
from itertools import combinations, permutations
from ramsey_blue_pair_transport import blue


def main():
    start = (0, 2, 4, 6)
    seen = {start}; q = deque([start])
    while q:
        state = q.popleft()
        for i in range(4):
            retained = state[:i] + state[i+1:]
            x, = [v for v in range(13) if v != state[i] and all(blue(v,y) for y in retained)]
            nxt = state[:i] + (x,) + state[i+1:]
            if nxt not in seen:
                seen.add(nxt); q.append(nxt)
    loops = set(permutations(start)) & seen
    all_sets = {t for t in combinations(range(13),4) if all(blue(i,j) for i,j in combinations(t,2))}
    assert len(loops)==24 and len(all_sets)==39 and len(seen)==24*len(all_sets)
    print('ordered states',len(seen),'unordered states',len(all_sets),'return permutations',len(loops))
    for a,b in combinations(start,2):
        if sum(blue(x,a) and blue(x,b) for x in range(13))==5:
            print('retain',a,b,'swap',sorted(set(start)-{a,b}))

if __name__=='__main__':main()
