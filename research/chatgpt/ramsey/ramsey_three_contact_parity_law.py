"""Three-birth orientation obstruction from antipodal contact parity.

Standard library only.  A = graph adjacency, B = nonadjacency.
Carrier: Cayley(F_2^6; 1,2,4,8,16,32,63).
Three births edit six distinct <1,2>-squares in the lower 32 vertices.

Run:
    python ramsey_three_contact_parity_law.py
    python ramsey_three_contact_parity_law.py --audit

Default: derive the contact-parity decision, construct every predicted
23-vertex B-witness, and count all 420*8 oriented arrangements.
--audit: independently compute all link capacities for 56 symmetry orbits,
covering the entire 3,360-arrangement family. No external Ramsey catalogue,
numerical optimizer, or third-party package is used.
"""
from itertools import combinations, permutations, product
from functools import lru_cache
from collections import Counter
import argparse
import json
from pathlib import Path

GEN = (1, 2, 4, 8, 16, 32, 63)
BASE = ((3, 6), (7, 5), (0, 1))


def quotient(c):
    """Antipodal square-cell class: {c,c xor 7}."""
    return min(c, c ^ 7)


def parity_assignment(pairs):
    """No common-link calculation: only six binary assignments."""
    p = {}
    for a, b in pairs:
        for cell, value in ((a, 0), (b, 1)):
            c = quotient(cell)
            if c in p and p[c] != value:
                return None
            p[c] = value
    return tuple(p.get(c, 0) for c in range(4))


def old_graph(pairs):
    assert len(pairs) == 3
    assert len({x for pair in pairs for x in pair}) == 6
    assert all(0 <= x < 8 for pair in pairs for x in pair)
    edges = {frozenset((v, v ^ s)) for v in range(64) for s in GEN}
    ports = []
    for a, b in pairs:
        x, y = 4*a, 4*b
        for u, v in ((x, x ^ 1), (x ^ 2, x ^ 3),
                     (y, y ^ 2), (y ^ 1, y ^ 3)):
            edges.remove(frozenset((u, v)))
        for u, v in ((x, x ^ 3), (y ^ 1, y ^ 2)):
            edges.add(frozenset((u, v)))
        ports.append({x ^ 1, x ^ 2, y, y ^ 3})
    return edges, ports


def direct_witness(pairs):
    """Construct 20 old mutually B-connected vertices using parity only."""
    p = parity_assignment(pairs)
    if p is None:
        return None
    # One selected vertex in each of the eight lower-half squares.
    # Its first low bit is parity(c); its second is parity(c) xor p_[c].
    left = set()
    for c in range(8):
        r = c.bit_count() % 2
        t = r + 2*(r ^ p[quotient(c)])
        left.add(4*c + t)
    assert len(left) == 8
    assert {v ^ 31 for v in left} == left
    # An intact parity class in the upper Q5, excluding cross-neighbors.
    right = {32 + v for v in range(32)
             if v.bit_count() % 2 == 0 and v not in left}
    assert len(right) == 12
    W = left | right
    edges, ports = old_graph(pairs)
    assert all(W.isdisjoint(P) for P in ports)
    assert not any(e <= W for e in edges)
    assert len(W) == 20
    # Three mutually B-connected newborns produce a 23-node B-clique.
    return W | {64, 65, 66}


def pairings(vertices):
    if not vertices:
        yield ()
        return
    a = vertices[0]
    for j in range(1, len(vertices)):
        b = vertices[j]
        rest = vertices[1:j] + vertices[j+1:]
        for tail in pairings(rest):
            yield ((a, b),) + tail


def matchings():
    for selected in combinations(range(8), 6):
        yield from pairings(selected)


def oriented_arrangements():
    for base in matchings():
        for eps in product((0, 1), repeat=3):
            yield tuple(p[::-1] if e else p for p, e in zip(base, eps))


# Independent capacity check: exact matching on the intact upper half.
# Identify antipodes v,v xor 31 in Q5; quotient is a 16-cell folded 5-cube.
idx = lambda v: min(v, v ^ 31)
EVEN = tuple(v if v.bit_count() % 2 == 0 else v ^ 31 for v in range(16))
CLEBSCH = tuple(sum(1 << idx(v ^ (1 << j)) for j in range(5)) for v in EVEN)


@lru_cache(None)
def upper_independence(U):
    """Kőnig: alpha of the surviving bipartite upper half is |V|-matching."""
    matched = [-1]*16

    def augment(v, visited):
        rest = CLEBSCH[v] & U & ~visited[0]
        while rest:
            bit = rest & -rest
            rest ^= bit
            w = bit.bit_length() - 1
            visited[0] |= bit
            if matched[w] < 0 or augment(matched[w], visited):
                matched[w] = v
                return True
        return False

    size = sum(augment(v, [0]) for v in range(16) if U >> v & 1)
    return 2*U.bit_count() - size


def link_capacities(pairs):
    edges, ports = old_graph(pairs)
    lower_adj = [0]*32
    for edge in edges:
        u, v = tuple(edge)
        if u < 32 and v < 32:
            lower_adj[u] |= 1 << v
            lower_adj[v] |= 1 << u
    port_mask = [sum(1 << i for i, P in enumerate(ports) if v in P)
                 for v in range(32)]
    best = [-1]*8

    def visit(available, selected, occupied_cells, contacted):
        if not available:
            score = selected.bit_count() + upper_independence(65535 ^ occupied_cells)
            best[contacted] = max(best[contacted], score)
            return
        bit = available & -available
        v = bit.bit_length() - 1
        visit(available ^ bit, selected, occupied_cells, contacted)
        visit((available ^ bit) & ~lower_adj[v], selected | bit,
              occupied_cells | (1 << idx(v)), contacted | port_mask[v])

    visit((1 << 32) - 1, 0, 0, 0)
    return [max(best[t] for t in range(8) if not t & s) for s in range(8)]


def cube_maps():
    return [tuple(shift ^ sum(((v >> i) & 1) << perm[i] for i in range(3))
                  for v in range(8))
            for perm in permutations(range(3)) for shift in range(8)]


MAPS = cube_maps()


def orbit(pairs):
    # Permutations/translations of the three high coordinates preserve carrier,
    # halves, and edits. Simultaneous birth reversal is the low-coordinate
    # map (bit0,bit1) -> (bit1 xor 1,bit0), preserving the same data.
    return {tuple(sorted((f[b], f[a]) if reverse else (f[a], f[b])
                         for a, b in pairs))
            for f in MAPS for reverse in (False, True)}


def audit(output):
    remaining = {tuple(sorted(pairs)) for pairs in oriented_arrangements()}
    assert len(remaining) == 3360
    results = []
    counts = Counter()
    while remaining:
        pairs = min(remaining)
        O = orbit(pairs)
        assert O <= remaining
        remaining -= O
        beta = link_capacities(pairs)
        assert beta[0] == 22
        assert all(beta[s] == 21 for s in (1, 2, 4))
        assert all(beta[s] in (20, 21) for s in (3, 5, 6))
        assert beta[7] in (19, 20)
        pair_ok = all(beta[s] == 20 for s in (3, 5, 6))
        predicted = parity_assignment(pairs) is not None
        actual_genuine = pair_ok and beta[7] == 20
        assert predicted == actual_genuine, (pairs, beta, predicted)
        counts['pair-obstructed' if not pair_ok else
               'genuine-three-way' if beta[7] == 20 else 'fully-admissible'] += len(O)
        results.append(dict(pairs=pairs, orbit_size=len(O), beta=beta,
                            parity_predicted=predicted, pairwise_admissible=pair_ok))
    assert len(results) == 56
    assert dict(counts) == {'pair-obstructed': 816,
                           'fully-admissible': 1968,
                           'genuine-three-way': 576}
    output.write_text(json.dumps(results, indent=2) + '\n')
    print('Independent exhaustive audit: 56 symmetry orbits, 3,360 arrangements.')
    print('Exact classification:', dict(counts))
    print('Counterexamples to genuine-obstruction parity criterion: 0.')
    print('Audit output:', output)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--audit', action='store_true')
    parser.add_argument('--output', type=Path,
                        default=Path(__file__).with_name('ramsey_three_contact_parity_audit.json'))
    args = parser.parse_args()
    print('Original contact arrangement:')
    for eps in product((0, 1), repeat=3):
        pairs = tuple(p[::-1] if e else p for p, e in zip(BASE, eps))
        W = direct_witness(pairs)
        assert (W is not None) == (eps[0] == eps[1] == eps[2])
        print('orientation', eps, 'parity witness', '23-node B-clique' if W else 'none')
    print('Aligned example B23:', sorted(direct_witness(BASE)))
    histogram = Counter()
    witness_count = 0
    for base in matchings():
        count = 0
        for eps in product((0, 1), repeat=3):
            pairs = tuple(p[::-1] if e else p for p, e in zip(base, eps))
            W = direct_witness(pairs)
            count += W is not None
        histogram[count] += 1
        witness_count += count
    assert dict(histogram) == {2: 192, 4: 48, 0: 180}
    assert witness_count == 576
    print('Unoriented arrangements by number of obstructing orientations:', dict(histogram))
    print('All 576 predicted 23-node witnesses checked directly against generators and edits.')
    if args.audit:
        audit(args.output)


if __name__ == '__main__':
    main()
