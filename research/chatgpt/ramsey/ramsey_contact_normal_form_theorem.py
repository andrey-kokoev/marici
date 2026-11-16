"""Normal-form and four-birth certificates for the declared folded-7-cube model.

Run: python ramsey_contact_normal_form_theorem.py
     python ramsey_contact_normal_form_theorem.py --audit

Standard library only. The companion Markdown file gives the structural proof.
Default checks the small quotient lemmas, every local-state type up to symmetry,
and an explicit pair-obstruction witness. --audit additionally checks all 1,680
oriented four-birth assemblies, reduced to 52 symmetry orbits. All edits are
fixed BEFORE any newborn subset is tested.
"""
from itertools import combinations, permutations, product
from collections import Counter
from functools import lru_cache
from pathlib import Path
import argparse
import json

GEN = (1, 2, 4, 8, 16, 32, 63)
ALL16 = (1 << 16) - 1
ALL32 = (1 << 32) - 1
idx = lambda v: min(v, v ^ 31)
EVEN = tuple(v if v.bit_count() % 2 == 0 else v ^ 31 for v in range(16))
C = tuple(sum(1 << idx(v ^ (1 << j)) for j in range(5)) for v in EVEN)
MAPS = [tuple(shift ^ sum(((v >> i) & 1) << p[i] for i in range(3))
              for v in range(8))
        for p in permutations(range(3)) for shift in range(8)]


def graph(pairs):
    k = len(pairs)
    assert k in (3, 4)
    assert len({v for pair in pairs for v in pair}) == 2*k
    edges = {tuple(sorted((v, v ^ s))) for v in range(64) for s in GEN}
    ports = []
    for a, b in pairs:
        x, y = 4*a, 4*b
        for u, v in ((x, x ^ 1), (x ^ 2, x ^ 3),
                     (y, y ^ 2), (y ^ 1, y ^ 3)):
            edges.remove(tuple(sorted((u, v))))
        edges.update((tuple(sorted((x, x ^ 3))), tuple(sorted((y ^ 1, y ^ 2)))))
        ports.append({x ^ 1, x ^ 2, y, y ^ 3})
    adj = [0]*32
    for u, v in edges:
        if v < 32:
            adj[u] |= 1 << v
            adj[v] |= 1 << u
    return edges, ports, adj


def parity_consistent(sources, targets):
    return not ({idx(4*c)//4 for c in sources} & {idx(4*c)//4 for c in targets})


def parity_witness(sources, targets):
    p = {}
    for cells, bit in ((sources, 0), (targets, 1)):
        for c in cells:
            h = min(c, c ^ 7)
            if h in p and p[h] != bit:
                return None
            p[h] = bit
    left = set()
    for c in range(8):
        e = c.bit_count() % 2
        low = e + 2*(e ^ p.get(min(c, c ^ 7), 0))
        left.add(4*c + low)
    right = {32+v for v in range(32)
             if v.bit_count() % 2 == 0 and v not in left}
    assert len(left) == 8 and {v ^ 31 for v in left} == left
    assert len(right) == 12
    return left | right


@lru_cache(None)
def upper_capacity(U):
    """Exact independent-set size of the intact bipartite upper link."""
    match = [-1]*16
    def aug(v, seen):
        rest = C[v] & U & ~seen[0]
        while rest:
            bit = rest & -rest
            rest ^= bit
            w = bit.bit_length()-1
            seen[0] |= bit
            if match[w] < 0 or aug(match[w], seen):
                match[w] = v
                return True
        return False
    size = sum(aug(v, [0]) for v in range(16) if U >> v & 1)
    return 2*U.bit_count()-size


def check_quotient():
    assert all(v.bit_count() == 5 for v in C)
    for i, j in combinations(range(16), 2):
        assert (C[i] & C[j]).bit_count() == (0 if C[i] >> j & 1 else 2)
    largest = 0
    for size in range(1, 7):
        for S in combinations(range(16), size):
            if any(C[i] >> j & 1 for i, j in combinations(S, 2)):
                continue
            largest = max(largest, size)
            nbr = 0
            for i in S:
                nbr |= C[i]
            if size >= 2:
                assert nbr.bit_count() >= size + 6
    assert largest == 5


def pattern_orbit(s, t):
    return {(tuple(sorted(f[c] for c in (t if rev else s))),
             tuple(sorted(f[c] for c in (s if rev else t))))
            for f in MAPS for rev in (False, True)}


def parallel_face_exception(s, t):
    free = set(range(8)) - set(s) - set(t)
    if len(free) != 2:
        return False
    c, d = sorted(free)
    bit = c ^ d
    return (bit in (1, 2, 4)
            and len({v & bit for v in s}) == 1
            and set(t) == {v ^ bit for v in s})


def local_states(s, t):
    pairs = tuple(zip(s, t))
    edges, ports, adj = graph(pairs)
    excluded = sum(1 << v for P in ports for v in P)
    def walk(free, selected, occupied):
        if not free:
            yield selected, occupied
            return
        bit = free & -free
        v = bit.bit_length()-1
        yield from walk(free ^ bit, selected, occupied)
        yield from walk((free ^ bit) & ~adj[v], selected | bit,
                        occupied | (1 << idx(v)))
    return walk(ALL32 ^ excluded, 0, 0)


def check_local_lemmas():
    state_count = 0
    case_counts = {}
    for k in (3, 4):
        remaining = {(s, t) for s in combinations(range(8), k)
                     for t in combinations(sorted(set(range(8))-set(s)), k)}
        cases = 0
        while remaining:
            s, t = min(remaining)
            remaining -= pattern_orbit(s, t)
            cases += 1
            consistent = parity_consistent(s, t)
            best = -1
            for selected, D in local_states(s, t):
                state_count += 1
                size = selected.bit_count()
                p = size-D.bit_count()
                U = ALL16 ^ D
                h = upper_capacity(U)-U.bit_count()
                score = 16+p+h
                best = max(best, score)
                assert size <= 16-2*k
                isolated = any((U >> v & 1) and not (C[v] & U) for v in range(16))
                if isolated:
                    assert p <= 5-k, (s, t, selected, p)
                if k == 3:
                    assert p <= 4
                    if p >= 4:
                        assert consistent
                    if score >= 20 and not consistent:
                        assert size == 10 and parallel_face_exception(s, t)
                else:
                    if not consistent:
                        assert score <= 18
                    assert score <= 20
            if consistent:
                W = parity_witness(s, t)
                edges, ports, _ = graph(tuple(zip(s, t)))
                assert len(W) == 20
                assert not any(u in W and v in W for u, v in edges)
                assert all(W.isdisjoint(P) for P in ports)
                assert best == 20
            if k == 4:
                assert best in (17, 18, 20)
                assert (best == 20) == consistent
        case_counts[k] = cases
    assert case_counts == {3: 13, 4: 6}
    return state_count


def check_pair_exception():
    sources, targets = (0, 1, 2), (4, 5, 6)
    W = {2, 3, 4, 8, 13, 14, 17, 22, 26, 28, 31,
         33, 38, 42, 44, 47, 48, 51, 53, 57, 62}
    assert len(W) == 21
    for t in permutations(targets):
        pairs = tuple(zip(sources, t))
        edges, ports, _ = graph(pairs)
        assert not any(u in W and v in W for u, v in edges)
        assert W.isdisjoint(ports[1]) and W.isdisjoint(ports[2])
        assert W & ports[0] == {2}


def link_profile(pairs):
    _, ports, adj = graph(pairs)
    k = len(pairs)
    contact = [sum(1 << i for i, P in enumerate(ports) if v in P) for v in range(32)]
    best = [-1]*(1 << k)
    def walk(free, selected, occupied, touched):
        if not free:
            score = selected.bit_count()+upper_capacity(ALL16 ^ occupied)
            best[touched] = max(best[touched], score)
            return
        bit = free & -free
        v = bit.bit_length()-1
        walk(free ^ bit, selected, occupied, touched)
        walk((free ^ bit) & ~adj[v], selected | bit,
             occupied | (1 << idx(v)), touched | contact[v])
    walk(ALL32, 0, 0, 0)
    return [max(best[c] for c in range(1 << k) if not (c & T)) for T in range(1 << k)]


def pairings(vertices):
    if not vertices:
        yield ()
        return
    a = vertices[0]
    for j in range(1, len(vertices)):
        b = vertices[j]
        for rest in pairings(vertices[1:j]+vertices[j+1:]):
            yield ((a, b),)+rest


def birth_orbit(pairs):
    return {tuple(sorted((f[b], f[a]) if rev else (f[a], f[b]) for a, b in pairs))
            for f in MAPS for rev in (False, True)}


def audit_four(output):
    remaining = {tuple(sorted((b, a) if flip else (a, b)
                              for (a, b), flip in zip(base, eps)))
                 for base in pairings(tuple(range(8))) for eps in product((0, 1), repeat=4)}
    assert len(remaining) == 1680
    records = []
    capacities = Counter()
    classes = Counter()
    while remaining:
        pairs = min(remaining)
        O = birth_orbit(pairs)
        assert O <= remaining
        remaining -= O
        beta = link_profile(pairs)
        assert beta[0] == 22
        consistent = parity_consistent([a for a,b in pairs], [b for a,b in pairs])
        assert (beta[15] == 20) == consistent
        assert consistent or beta[15] <= 18
        forbidden = [T for T in range(16) if beta[T]+T.bit_count() > 22]
        minimal = [T for T in forbidden if not any(U != T and not (U & ~T) for U in forbidden)]
        assert 15 not in minimal
        kind = tuple(sorted({T.bit_count() for T in minimal}))
        capacities[beta[15]] += len(O)
        classes[str(kind)] += len(O)
        records.append(dict(pairs=pairs, orbit_size=len(O), beta=beta,
                            minimal_forbidden=minimal, parity_consistent=consistent))
    assert len(records) == 52
    assert dict(capacities) == {17: 384, 18: 1152, 20: 144}
    output.write_text(json.dumps(dict(full_link_capacities=dict(capacities),
                                    minimal_obstruction_classes=dict(classes),
                                    orbits=records), indent=2)+'\n')
    print('Four births: 1,680 assemblies / 52 symmetry orbits.')
    print('Full-link capacities:', dict(capacities))
    print('Irreducible fourth-order obstructions: 0.')
    print('Audit saved to', output)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--audit', action='store_true')
    args = parser.parse_args()
    check_quotient()
    count = check_local_lemmas()
    check_pair_exception()
    print('Verified quotient neighborhood expansion and independence bound.')
    print('Verified local lemmas on', count, 'states in 13 three-birth and 6 four-birth types.')
    print('Verified explicit 21-old-vertex witness for the exceptional pair obstruction.')
    print('Three-birth normal form and four-birth gap agree with all local checks.')
    if args.audit:
        audit_four(Path(__file__).with_name('ramsey_contact_normal_form_four_audit.json'))


if __name__ == '__main__':
    main()
