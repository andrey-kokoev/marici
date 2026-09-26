"""Coherence versus selection of a central phase on the actual source action."""
from itertools import product
from pathlib import Path
import hashlib
import json
import re
import sympy as s

OWNER = Path(__file__).resolve().parents[1]
G = range(4)  # bit 0 = first swap, bit 1 = second swap
PAIRS = tuple(product(G, repeat=2))
TRIPLES = tuple(product(G, repeat=3))
NONZERO_PAIRS = tuple(product(range(1,4), repeat=2))


def entry(c,g,h):
    return c[4*g+h]


def add_cochains(a,b):
    return tuple(x^y for x,y in zip(a,b))


def orbits(cocycles,boundaries):
    remaining = set(cocycles)
    answer = []
    while remaining:
        c = min(remaining)
        orbit = {add_cochains(c,b) for b in boundaries}
        assert orbit <= set(cocycles)
        answer.append(orbit)
        remaining -= orbit
    return answer


def main():
    out = OWNER/'results/phase-selection.json'
    out.unlink(missing_ok=True)
    cocycles = []
    for values in product((0,1),repeat=9):
        c = [0]*16
        for (g,h),v in zip(NONZERO_PAIRS,values):
            c[4*g+h] = v
        c = tuple(c)
        if all(entry(c,g,h)^entry(c,g^h,k) == entry(c,h,k)^entry(c,g,h^k) for g,h,k in TRIPLES):
            cocycles.append(c)
    assert len(cocycles) == 16
    sign_boundaries = set()
    for values in product((0,1),repeat=3):
        f = (0,)+values
        sign_boundaries.add(tuple(f[g]^f[h]^f[g^h] for g,h in PAIRS))
    assert len(sign_boundaries) == 2
    assert len(orbits(cocycles,sign_boundaries)) == 8
    unit_lifts = [c for c in cocycles if entry(c,1,1) == entry(c,2,2) == 0]
    assert len(unit_lifts) == 4
    assert len(orbits(unit_lifts,sign_boundaries)) == 2
    # Complete U(1) gauge comparison between sign-valued normalized cocycles:
    # each f(g)^2 must be a sign, so f(g) must be a fourth root of unity.
    complex_boundaries = set()
    for values in product(range(4),repeat=3):
        f = (0,)+values
        delta = tuple((f[g]+f[h]-f[g^h])%4 for g,h in PAIRS)
        if all(x%2 == 0 for x in delta):
            complex_boundaries.add(tuple(x//2 for x in delta))
    assert len(complex_boundaries) == 8
    complex_orbits = orbits(cocycles,complex_boundaries)
    assert len(complex_orbits) == 2
    trivial = (0,)*16
    clifford = tuple(((g>>1)&1)*(h&1) for g,h in PAIRS)
    assert trivial in unit_lifts and clifford in unit_lifts
    assert not any(trivial in orbit and clifford in orbit for orbit in complex_orbits)
    assert entry(trivial,1,2)^entry(trivial,2,1) == 0
    assert entry(clifford,1,2)^entry(clifford,2,1) == 1

    signed = tuple(product((0,1),G))
    def multiply(c,x,y):
        phase,g = x
        other,h = y
        return phase^other^entry(c,g,h), g^h
    def inverse(c,x):
        phase,g = x
        return phase^entry(c,g,g),g
    for c in cocycles:
        commutator_bit = entry(c,1,2)^entry(c,2,1)
        # Extending this basis multiplication linearly gives a commutative
        # algebra exactly in the trivial commutator class. Its inner actions
        # are identities, unlike the actual nontrivial source swaps.
        assert all(multiply(c,x,y) == multiply(c,y,x) for x,y in product(signed,repeat=2)) == (commutator_bit == 0)
        for x,y,z in product(signed,repeat=3):
            assert multiply(c,multiply(c,x,y),z) == multiply(c,x,multiply(c,y,z))
        for x,y in product(signed,repeat=2):
            assert inverse(c,multiply(c,x,y)) == multiply(c,inverse(c,y),inverse(c,x))
        for x in signed:
            assert inverse(c,inverse(c,x)) == x
            assert multiply(c,x,inverse(c,x)) == multiply(c,inverse(c,x),x) == (0,0)

    # Both extensions cover EXACTLY the same concrete source permutations.
    source_path = OWNER/'agda/RetainedComparisonSeries.agda'
    match = re.search(r'^swap-image-codes : .* ≡ \((\d+) , (\d+) , (\d+) , (\d+)\)$', source_path.read_text(encoding='utf-8'),re.M)
    p = tuple(map(int,match.groups()))
    actions = [tuple(4*(p[x] if g&1 else x)+(p[y] if g&2 else y)
                     for x in range(4) for y in range(4)) for g in G]
    assert len(set(actions)) == 4
    for g,h in PAIRS:
        assert tuple(actions[g][actions[h][i]] for i in range(16)) == actions[g^h]
    for c in (trivial,clifford):
        for length in range(7):
            for word in product((1,2),repeat=length):
                value = (0,0)
                for letter in word:
                    value = multiply(c,value,(0,letter))
                for letter in (1,2):
                    packet = (word,word+(letter,),multiply(c,value,(0,letter)))
                    assert packet[1][:-1] == packet[0]
                    assert actions[packet[2][1]] == tuple(actions[value[1]][actions[letter][i]] for i in range(16))

    # Fixed-Clifford-algebra implementation is a STRONGER condition.
    E1, E2 = s.diag(1,-1), s.Matrix([[0,1],[1,0]])
    J = E1*E2
    basis = (s.eye(2),E1,E2,J)
    variables = s.symbols('u00 u01 u10 u11')
    U = s.Matrix(2,2,variables)
    for generator in (E1,E2):
        equations = [component for q in basis for component in (U*q-(generator*q*generator)*U)]
        matrix,_ = s.linear_eq_to_matrix(equations,variables)
        kernel = matrix.nullspace()
        assert len(kernel) == 1
        candidate = s.Matrix(2,2,kernel[0])
        assert s.Matrix.hstack(s.Matrix(list(candidate)),s.Matrix(list(generator))).rank() == 1
    assert E1*E2*E1*E2 == -s.eye(2)
    # Direct actions on the four observable coordinates give a commuting lift
    # in a different representation space, not inner implementers in Mat_2.
    directL = s.diag(1,1,-1,-1)
    directR = s.diag(1,-1,1,-1)
    assert directL*directR == directR*directL

    # Continuum exponent: every rate, including zero, satisfies the same laws.
    q,p0,r,t,u,v,rate = s.symbols('q p r t u v rate')
    omega = lambda a,b: a[0]*b[1]-a[1]*b[0]
    add = lambda a,b: (a[0]+b[0],a[1]+b[1])
    negate = lambda a: (-a[0],-a[1])
    x,y,z = (q,p0),(r,t),(u,v)
    assert s.expand(rate*(omega(x,y)+omega(add(x,y),z)-omega(y,z)-omega(x,add(y,z)))) == 0
    assert s.expand(rate*(omega(negate(y),negate(x))+omega(x,y))) == 0
    assert (rate*omega(x,y)).subs(rate,0) == 0
    # A nonzero source-independent value is possible but not selected.
    assert omega((1,0),(0,1)) == 1

    receipt_path = OWNER/'results/agda-PhaseLiftCocycle.json'
    receipt = json.loads(receipt_path.read_text(encoding='utf-8-sig'))
    assert receipt['passed'] and receipt['ignore_interfaces']
    formal_path = OWNER/'agda/PhaseLiftCocycle.agda'
    assert hashlib.sha256(formal_path.read_bytes()).hexdigest() == receipt['source_sha256'].lower()
    source_receipt_path = OWNER/'results/agda-ComparisonKineticReadout.json'
    source_receipt = json.loads(source_receipt_path.read_text(encoding='utf-8-sig'))
    assert source_receipt['passed'] and source_receipt['ignore_interfaces']
    checked_source_modules = set()
    def audit_source(module):
        path = OWNER/'agda'/(module.replace('.', '/')+'.agda')
        if not path.exists() or module in checked_source_modules:
            return
        checked_source_modules.add(module)
        assert hashlib.sha256(path.read_bytes()).hexdigest() == source_receipt['owner_source_inventory_sha256'][path.name].lower(), module
        for dependency in re.findall(r'^\s*(?:open\s+)?import\s+([\w.]+)', path.read_text(encoding='utf-8'),re.M):
            audit_source(dependency)
    audit_source('RetainedComparisonSeries')
    result = {
        'schema':'marici.nima.phase-selection.v1',
        'classification':'coherence_allows_both_phase_classes_clifford_inner_implementation_selects_nontrivial',
        'normalized_sign_cocycles':16,'classes_under_sign_rephasing':8,
        'unit_generator_lift_cocycles':4,'unit_generator_classes_under_sign_rephasing':2,
        'classes_under_complex_rephasing':2,
        'source_action':'same faithful V4 action from the actual independent swap maps',
        'retention':'both trivial and Clifford extensions retain identical full word histories',
        'inner_implementation':'inside fixed Mat_2 Clifford algebra every implementer is a scalar multiple of e1 or e2; relative commutator phase is -1',
        'extra_selection_condition':'requiring the nontrivial source actions to be inner in the twisted four-dimensional algebra excludes the commutative class; this condition is not derived from source coherence',
        'continuum':'exp(i*rate*omega) coherent for every real rate, including zero; Weyl rate=1/(2*hbar) is an additional calibration',
        'source_sha256':{str(path.relative_to(OWNER)):hashlib.sha256(path.read_bytes()).hexdigest()
                         for path in (source_path,formal_path,receipt_path,source_receipt_path,Path(__file__))},
        'current_source_imports_bound_to_prior_fresh_receipt':len(checked_source_modules),
        'scope':'Exact finite central-extension classification and linear intertwiner test; fresh generic ring proof of continuum exponent identities. Neither full native higher-witness integration nor selection of the Clifford algebra, Hilbert-state interpretation, or physical phase scale is derived.'
    }
    out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({key:result[key] for key in ('classification','normalized_sign_cocycles','unit_generator_classes_under_sign_rephasing','classes_under_complex_rephasing')}))


if __name__ == '__main__':
    main()
