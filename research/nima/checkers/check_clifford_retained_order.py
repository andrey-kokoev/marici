"""Exact Clifford lift of the source square and its recursive sign rule.
No claim of a complete higher-source or physical readout derivation.
"""
from fractions import Fraction
from itertools import product
from pathlib import Path
import hashlib
import json
import re

OWNER = Path(__file__).resolve().parents[1]
I = (1, 0, 0, 1)
E1 = (1, 0, 0, -1)
E2 = (0, 1, 1, 0)
ZERO = (0, 0, 0, 0)


def mul(a, b):
    return (a[0]*b[0]+a[1]*b[2], a[0]*b[1]+a[1]*b[3],
            a[2]*b[0]+a[3]*b[2], a[2]*b[1]+a[3]*b[3])


def scale(k, a):
    return tuple(k*x for x in a)


def subtract(a, b):
    return tuple(x-y for x, y in zip(a,b))


def reverse(a):
    return (a[0], a[2], a[1], a[3])


def scalar(a):
    return Fraction(a[0]+a[3], 2)


def norm(a):
    return scalar(mul(reverse(a), a))


J = mul(E1, E2)
BASIS = (I, E1, E2, J)


def normal_product(g, h):
    sign, a, b = g
    other, c, d = h
    return (sign*other*(-1)**(b*c), a ^ c, b ^ d)


def normal_reverse(g):
    sign, a, b = g
    return (sign*(-1)**(a*b), a, b)


def realize(g):
    sign, a, b = g
    return scale(sign, mul(E1 if a else I, E2 if b else I))


def evaluate(word):
    value = (1,0,0)
    for letter in word:
        value = normal_product(value, (1,1,0) if letter == 1 else (1,0,1))
    return value


def bracketings(word):
    if not word:
        return [I]
    if len(word) == 1:
        return [E1 if word[0] == 1 else E2]
    return [mul(a,b) for split in range(1,len(word))
            for a in bracketings(word[:split]) for b in bracketings(word[split:])]


def main():
    assert mul(E1,E1) == mul(E2,E2) == I
    assert mul(E2,E1) == scale(-1,J) and mul(J,J) == scale(-1,I)
    k = subtract(mul(E1,E2), mul(E2,E1))
    assert k == scale(2,J) and scalar(k) == 0 and norm(k) == 4
    assert subtract(mul(J,scale(-1,J)),mul(scale(-1,J),J)) == ZERO
    # Adjoint actions commute on the WHOLE Clifford algebra, by linearity.
    ad = lambda unit, q: mul(mul(unit,q),reverse(unit))
    for q in BASIS:
        assert ad(E1,ad(E2,q)) == ad(E2,ad(E1,q)) == ad(J,q)
        assert ad(E1,ad(E1,q)) == ad(E2,ad(E2,q)) == q

    # Intertwine the actual source's independent swap actions on its active
    # four-dimensional sector. This is an algebraic intertwiner; unnormalized
    # odd vectors are used, so no isometry is claimed.
    source_path = OWNER/'agda/RetainedComparisonSeries.agda'
    source_text = source_path.read_text(encoding='utf-8')
    match = re.search(r'^swap-image-codes : .* ≡ \((\d+) , (\d+) , (\d+) , (\d+)\)$', source_text, re.M)
    image = tuple(map(int,match.groups()))
    anchor, odd = (1,0,0,0), (0,1,-1,0)
    tensor = lambda v,w: tuple(x*y for x in v for y in w)
    source_basis = (tensor(anchor,anchor), tensor(anchor,odd), tensor(odd,anchor), tensor(odd,odd))
    def coefficients(m):
        return (Fraction(m[0]+m[3],2), Fraction(m[0]-m[3],2),
                Fraction(m[1]+m[2],2), Fraction(m[1]-m[2],2))
    def source_realization(m):
        return tuple(sum(c*v[i] for c,v in zip(coefficients(m),source_basis)) for i in range(16))
    for q in BASIS:
        v = source_realization(q)
        left = tuple(v[4*image[x]+y] for x in range(4) for y in range(4))
        right = tuple(v[4*x+image[y]] for x in range(4) for y in range(4))
        assert source_realization(ad(E1,q)) == left
        assert source_realization(ad(E2,q)) == right

    grades = list(product((0,1),repeat=2))
    signs = [(sign,a,b) for sign in (1,-1) for a,b in grades]
    xor = lambda g,h: (g[0]^h[0],g[1]^h[1])
    cocycle = lambda g,h: (-1)**(g[1]*h[0])
    for g,h,t in product(grades,repeat=3):
        assert cocycle(g,h)*cocycle(xor(g,h),t) == cocycle(h,t)*cocycle(g,xor(h,t))
    for g,h,t in product(signs,repeat=3):
        assert normal_product(normal_product(g,h),t) == normal_product(g,normal_product(h,t))
    for g,h in product(signs,repeat=2):
        assert realize(normal_product(g,h)) == mul(realize(g),realize(h))
        assert normal_reverse(normal_product(g,h)) == normal_product(normal_reverse(h),normal_reverse(g))
    for g in signs:
        assert normal_reverse(normal_reverse(g)) == g
        assert normal_product(g,normal_reverse(g)) == normal_product(normal_reverse(g),g) == (1,0,0)

    # Forward/reverse parenthesization and their mixed comparison, through six
    # letters. The universal finite cocycle identity above supplies associativity.
    word_count = tree_count = 0
    for length in range(7):
        for word in product((1,2),repeat=length):
            word_count += 1
            normal = evaluate(word)
            trees = bracketings(word)
            tree_count += len(trees)
            assert all(value == realize(normal) for value in trees)
            rev_normal = evaluate(word[::-1])
            assert rev_normal == normal_reverse(normal)
            assert all(reverse(value) == realize(rev_normal) for value in trees)
            assert all(value == realize(rev_normal) for value in bracketings(word[::-1]))
            # Keep history independently of its normal form: appending records
            # the whole old word, recoverable even when the scalar reading is 1.
            for letter in (1,2):
                packet = {'previous': word, 'word': word+(letter,),
                          'normal':normal_product(normal,evaluate((letter,)))}
                assert packet['word'][:-1] == packet['previous']
                assert packet['normal'] == evaluate(packet['word'])
    assert evaluate(()) == evaluate((1,1)) and () != (1,1)
    # Real residues can already arise between longer histories with the same
    # adjoint action. Grade, not an asserted coherence depth, controls this.
    assert realize(evaluate((1,2,1,2))) == scale(-1,I)
    assert subtract(realize(evaluate((1,2,1,2))),realize(evaluate(()))) == scale(-2,I)
    # Replacing retention by ordinary squaring can erase a nonzero element.
    nilpotent = tuple(a+b for a,b in zip(E1,J))
    assert nilpotent != ZERO and mul(nilpotent,nilpotent) == ZERO and norm(nilpotent) == 2

    result = {
        'schema':'marici.nima.clifford-retained-order.v1',
        'classification':'clifford_sign_recursion_realizes_a_commuting_source_sector_with_retained_lift_phase',
        'source_swap_images':image,
        'normal_product':'(s,a,b)*(t,c,d)=(s*t*(-1)^(b*c),a xor c,b xor d)',
        'source_action':'L=Ad(e1), R=Ad(e2); intertwines the actual active source product sector',
        'lift_difference':'e1*e2-e2*e1=2J', 'positive_readout':4,
        'nested_product_commutator':0,
        'cocycle_cases':64,'signed_associativity_cases':512,
        'word_controls':word_count,'parenthesization_controls':tree_count,
        'source_sha256':hashlib.sha256(source_path.read_bytes()).hexdigest(),
        'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'scope':'Exact finite algebra and retained-history prototype. Algebraic checks of forward/reverse word coherence; not a construction of every higher witness of the full retained source, a uniquely selected Clifford lift, or a derived physical amplitude.'
    }
    out = OWNER/'results/clifford-retained-order.json'
    out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result))


if __name__ == '__main__':
    main()
