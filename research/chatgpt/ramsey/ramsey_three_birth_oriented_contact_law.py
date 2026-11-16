"""Exact oriented-contact classification of three births in the folded-7-cube.

No graph independent-set optimizer, matching algorithm, or Ramsey catalogue.
Pure eight-square incidence law for pair obstructions; four-bit contact-parity
law for genuinely ternary obstructions. Uses only the Python standard library.

Run: python ramsey_three_birth_oriented_contact_law.py
Optional independent cross-check (separately computed link audit):
     python ramsey_three_birth_oriented_contact_law.py --compare
"""
from itertools import combinations, permutations, product
from collections import Counter
from pathlib import Path
import argparse, json

# Square cells c are three-bit elements. Their low labels t are two-bit.
Q5 = (1, 2, 4, 8, 15)  # the five-generator Clebsch quotient
CNEIGH = tuple(sum(1 << (q ^ s) for s in Q5) for q in range(16))
assert len(set(CNEIGH)) == 16

# In-same-square A edges, after orientation-specific half-square moves.
LOCAL_A = {
    0: {(0, 1), (0, 2), (1, 3), (2, 3)}, # unedited 4-cycle
    1: {(0, 2), (1, 3), (0, 3)},         # first-contact edit
    2: {(0, 1), (2, 3), (1, 2)},         # second-contact edit
}
OPTIONS = {
    kind: tuple((t,) for t in range(4)) + tuple(
        (u, v) for u, v in combinations(range(4), 2)
        if (u, v) not in LOCAL_A[kind]
    )
    for kind in (0, 1, 2)
}
assert [len(OPTIONS[k]) for k in (0, 1, 2)] == [6, 7, 7]


def antipode_class(c, t):
    v = 4*c + t
    return min(v, v ^ 31)


def first_second_tags(pairs):
    assert len(pairs) in (3, 4)
    assert all(0 <= a < 8 and 0 <= b < 8 and a != b for a, b in pairs)
    assert len({c for ab in pairs for c in ab}) == 2*len(pairs)
    tags = {}
    for i, (a, b) in enumerate(pairs):
        tags[a] = (1, i)
        tags[b] = (2, i)
    return tags


def pair_obstruction_witness(pairs, i, j):
    """Pure contact/square test; returns explicit forbidden B23 or None.

    Lower witness: 11 vertices distributed across eight squares (three
    doubled), exactly nine touched antipodal quotient classes. Five untouched
    quotient classes must form the entire neighborhood of a quotient vertex q.
    Both upper representatives of each of those five classes then give B10.
    """
    tags = first_second_tags(pairs)
    chosen_births = {i, j}
    candidate = []
    for c in range(8):
        kind, owner = tags.get(c, (0, None))
        if owner in chosen_births:
            opts = ((0,), (3,)) if kind == 1 else ((1,), (2,))
        else:
            opts = OPTIONS[kind]
        candidate.append(tuple(
            (sum(1 << t for t in ls),
             sum(1 << antipode_class(c, t) for t in ls),
             len(ls))
            for ls in opts))

    labels = [0]*8
    def dfs(c, touched, doubled):
        if c == 8:
            if doubled != 3 or touched.bit_count() != 9:
                return None
            # All maximum independent 5-sets of the Clebsch quotient are the
            # 16 neighborhoods of individual quotient vertices.
            q = next((q for q in range(16) if not (touched & CNEIGH[q])), None)
            if q is None:
                return None
            lower = {4*k+t for k in range(8) for t in range(4)
                     if labels[k] >> t & 1}
            assert len(lower) == 11
            upper = set()
            for x in range(16):
                if CNEIGH[q] >> x & 1:
                    p = x if x.bit_count()%2 == 0 else x ^ 31
                    upper.add(32+p)
                    upper.add(32+(p^31))
            assert len(upper) == 10
            return lower | upper
        if doubled > 3 or doubled+8-c < 3:
            return None
        for low, touch, size in candidate[c]:
            if doubled+(size==2)>3:
                continue
            # An intersquare A-step flips one high-bit square coordinate and
            # leaves the two-bit low label unchanged.
            if any(c^d in (1,2,4) and (low & labels[d])
                   for d in range(c)):
                continue
            labels[c] = low
            W = dfs(c+1, touched|touch, doubled+(size==2))
            if W is not None:
                return W
        labels[c] = 0
        return None
    return dfs(0,0,0)


def triple_parity_witness(pairs):
    """Construct B23 when each antipodal square class is consistently typed."""
    tags = first_second_tags(pairs)
    p={}
    for a,b in pairs:
        for c,val in ((a,0),(b,1)):
            q=min(c,c^7)
            if q in p and p[q]!=val:
                return None
            p[q]=val
    lower=set()
    for c in range(8):
        e=c.bit_count()%2
        t=e+2*(e^p.get(min(c,c^7),0))
        lower.add(4*c+t)
    assert len(lower)==8 and {v^31 for v in lower}==lower
    upper={32+v for v in range(32) if v.bit_count()%2==0 and v not in lower}
    assert len(upper)==12
    return lower | upper


def verify_witness(pairs, births, W):
    """Independent verification using the full 64-vertex A graph and ports."""
    assert len(W)==23
    assert len(W&set(range(64)))+len(births)==23
    edges={frozenset((v,v^s)) for v in range(64)
           for s in (1,2,4,8,16,32,63)}
    ports=[]
    for a,b in pairs:
        x,y=4*a,4*b
        for u,v in ((x,x^1),(x^2,x^3),(y,y^2),(y^1,y^3)):
            edges.remove(frozenset((u,v)))
        for u,v in ((x,x^3),(y^1,y^2)):
            edges.add(frozenset((u,v)))
        ports.append({x^1,x^2,y,y^3})
    old={v for v in W if v<64}
    assert all(not e<=old for e in edges)
    assert all(old.isdisjoint(ports[i]) for i in births)
    return True


def unordered_matchings(cells):
    if not cells:
        yield ()
    else:
        a=cells[0]
        for j in range(1,len(cells)):
            b=cells[j]
            for tail in unordered_matchings(cells[1:j]+cells[j+1:]):
                yield ((a,b),)+tail


def orientations():
    for cells in combinations(range(8),6):
        for matching in unordered_matchings(cells):
            for eps in product((0,1), repeat=3):
                yield tuple(sorted((b,a) if e else (a,b)
                                   for (a,b),e in zip(matching,eps)))


def maps():
    return [tuple(shift ^ sum(((v>>k)&1)<<p[k] for k in range(3))
                  for v in range(8))
            for p in permutations(range(3)) for shift in range(8)]

MAPS=maps()

def orbit(pairs):
    return {tuple(sorted((m[b],m[a]) if flip else (m[a],m[b])
                         for a,b in pairs))
            for m in MAPS for flip in (False,True)}


def main(compare):
    remaining=set(orientations())
    assert len(remaining)==3360
    classes=Counter()
    examples={}
    records=[]
    while remaining:
        pairs=min(remaining)
        orb=orbit(pairs)
        assert orb<=remaining
        remaining-=orb
        blocked=[]
        witnesses={}
        for i,j in combinations(range(3),2):
            W=pair_obstruction_witness(pairs,i,j)
            if W is not None:
                blocked.append((i,j))
                witnesses[(i,j)]=W|{64+i,64+j}
                verify_witness(pairs,(i,j),W|{64+i,64+j})
        if len(blocked)==0:
            triple=triple_parity_witness(pairs)
            if triple is not None:
                verify_witness(pairs,(0,1,2),triple|{64,65,66})
                kind='triple'
            else:
                kind='none'
        elif len(blocked)==1:
            kind='pair'
        elif len(blocked)==2:
            kind='two_pairs'
        else:
            raise AssertionError((pairs,blocked))
        classes[kind]+=len(orb)
        examples.setdefault(kind,(pairs,blocked))
        records.append({'pairs':pairs,'orbit_size':len(orb),
                        'blocked_pairs':blocked,'kind':kind})
    assert len(records)==56
    assert classes==Counter({'none':1968,'pair':624,'triple':576,
                             'two_pairs':192}),classes
    print('Pure oriented-incidence classifier: 56 orbits / 3360 assemblies')
    print('No maximum-independent-set optimization or bipartite matching')
    print('Missing face types:',dict(classes))
    print('Examples:',examples)
    if compare:
        ref=Path(__file__).with_name('ramsey_three_contact_parity_audit.json')
        data=json.loads(ref.read_text())
        ground={tuple(map(tuple,r['pairs'])):r for r in data}
        assert len(ground)==56
        for rec in records:
            r=ground[rec['pairs']]
            blocked=[(i,j) for i,j in combinations(range(3),2)
                     if r['beta'][(1<<i)|(1<<j)]==21]
            assert rec['blocked_pairs']==blocked
            if not blocked:
                assert (rec['kind']=='triple') == (r['beta'][7]==20)
        print('All 56 predictions independently match the full link-capacity audit')

if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--compare',action='store_true')
    args=parser.parse_args()
    main(args.compare)
