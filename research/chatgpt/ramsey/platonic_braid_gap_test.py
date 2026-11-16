"""Exact R/B gap criterion; no FCC or embedding assumptions.

The integers U,V represent Artin braid generators in SL(2,Z).
For true B3 equality, additionally record exponent sum (both have +1).
The map (rho, exponent): B3 -> SL(2,Z) x Z is faithful.
"""
from itertools import combinations

I = ((1, 0), (0, 1))
U = ((1, -1), (0, 1))  # R
V = ((1, 0), (1, 1))   # B


def mul(A, B):
    return tuple(tuple(sum(A[i][k]*B[k][j] for k in range(2))
                       for j in range(2)) for i in range(2))


def power(A, n):
    out = I
    for _ in range(n):
        out = mul(out, A)
    return out


def matrix(word):
    out = I
    for letter in word:
        out = mul(out, U if letter == "R" else V)
    return out


def canonical(word):
    return min(word[i:] + word[:i] for i in range(len(word)))


def gap_lengths(word):
    assert word[0] == "B" and word.count("B") == 3
    blocks = word[1:].split("B")
    assert len(blocks) == 3
    return tuple(map(len, blocks))


def classes(reds, no_BB):
    length = reds + 3
    out = set()
    for bs in combinations(range(length), 3):
        w = ''.join('B' if i in bs else 'R' for i in range(length))
        if no_BB and 'BB' in w + w[0]:
            continue
        out.add(canonical(w))
    return sorted(out)


def order(A, max_order=12):
    return next((n for n in range(1,max_order+1) if power(A,n)==I), None)


def verify(reds, no_BB):
    words = classes(reds, no_BB)
    print(f"{reds}R/3B, no_BB={no_BB}: {len(words)} cyclic types")
    nfinite = 0
    for word in words:
        r,s,t = gap_lengths(word)
        W = matrix(word)
        trace = W[0][0] + W[1][1]
        assert r+s+t == reds
        assert trace == reds-6-(r-2)*(s-2)*(t-2)
        n = order(W)
        if n is not None:
            nfinite += 1
        print(f"  {word} : gaps={r,s,t}, trace={trace:>3}, order={n}")
    print("  Finite order types:", nfinite)
    return words

# Exact braid relations and central full twist identity.
assert mul(mul(U,V),U) == mul(mul(V,U),V)
full_twist = power(mul(V,U), 3)
assert full_twist == ((-1,0),(0,-1))
assert mul(full_twist,U) == mul(U,full_twist)
assert mul(full_twist,V) == mul(V,full_twist)
assert mul(mul(mul(V,power(U,2)),V),power(U,2)) == full_twist

# For any r+t=5, the full braid words (not just matrices) obey
# V U^r V U^2 V U^t = Delta^2 V U^3.
# Proof: V U^2 V U^2 = Delta^2, central in B3.
for r in range(6):
    t = 5-r
    word = 'B'+'R'*r+'B'+'R'*2+'B'+'R'*t
    A = matrix(word)
    normal = mul(full_twist, matrix('B'+'R'*3))
    assert A == normal
    assert order(A) == 6
    assert power(A,3) == full_twist

print('=== 7R+3B with exterior no-BB ===')
assert len(verify(7, True))==5
print('\n=== 7R+3B with BB permitted ===')
assert len(verify(7, False))==12
print('\n=== Next test: 8R+3B with no-BB ===')
assert len(verify(8, True))==7
print('\nAll assertions passed.')
