"""Exact Cardano branch-sensitive Merkle reassembly for x^3-3x-1.
Uses Q[t]/(t^6-t^3+1), the primitive eighteenth-root cyclotomic field,
and Q[h]/(h^3-3h-1), its real cubic subfield. Standard library only.
"""
from fractions import Fraction as Q
from hashlib import sha256
from pathlib import Path
import json

BASE = Path(__file__).resolve().parents[1]
MOD6 = (-1, 0, 0, 1, 0, 0)  # t^6 = t^3 - 1
MOD3 = (1, 3, 0)             # h^3 = 3h + 1

def constant(value, n): return (Q(value),) + (Q(0),) * (n - 1)
def plus(a, b): return tuple(x + y for x, y in zip(a, b))
def scale(a, c): return tuple(x * c for x in a)
def product(a, b, modulus):
    n = len(modulus)
    out = [Q(0)] * (2 * n - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b): out[i + j] += x * y
    for k in range(len(out) - 1, n - 1, -1):
        for j, c in enumerate(modulus): out[k - n + j] += out[k] * c
        out[k] = 0
    return tuple(out[:n])
def power(a, n, modulus=MOD6):
    out = constant(1, len(modulus))
    for _ in range(n): out = product(out, a, modulus)
    return out

def encoded(a): return [str(q) for q in a]
def decoded(a): return tuple(Q(q) for q in a)

zero, one = constant(0, 6), constant(1, 6)
t = (Q(0), Q(1), Q(0), Q(0), Q(0), Q(0))
zeta = power(t, 6)
alpha = plus(t, power(t, 17))
real_basis_images = [one, alpha, power(alpha, 2)]
def embed(real):
    result = zero
    for c, basis in zip(real, real_basis_images): result = plus(result, scale(basis, c))
    return result

def rank(columns):
    rows = [list(row) for row in zip(*columns)]
    r = 0
    for col in range(len(columns)):
        pivot = next((i for i in range(r, len(rows)) if rows[i][col]), None)
        if pivot is None: continue
        rows[r], rows[pivot] = rows[pivot], rows[r]
        divisor = rows[r][col]
        rows[r] = [x / divisor for x in rows[r]]
        for i in range(len(rows)):
            if i != r:
                c = rows[i][col]
                rows[i] = [x - c * y for x, y in zip(rows[i], rows[r])]
        r += 1
    return r

checks = {
    'primitive_eighteenth_root': power(t, 18) == one and all(power(t, n) != one for n in (1, 2, 3, 6, 9)),
    'alpha_solves_cubic': plus(plus(power(alpha, 3), scale(alpha, -3)), scale(one, -1)) == zero,
    'cubic_has_no_rational_root': all(n**3 - 3*n - 1 != 0 for n in (-1, 1)),
    'real_embedding_injective': rank(real_basis_images) == 3,
}
real_basis = [tuple(Q(i == j) for i in range(3)) for j in range(3)]
checks['real_embedding_preserves_all_basis_products'] = all(
    embed(product(a, b, MOD3)) == product(embed(a), embed(b), MOD6)
    for a in real_basis for b in real_basis)
checks['real_embedding_preserves_unit'] = embed(constant(1, 3)) == one

# Three real roots in one cubic field, obtained from paired cyclotomic branches.
real_roots = [(Q(0), Q(1), Q(0)), (Q(2), Q(0), Q(-1)), (Q(-2), Q(-1), Q(1))]
checks['three_real_normal_forms_are_distinct'] = len(set(real_roots)) == 3
checks['all_three_normal_forms_solve_cubic'] = all(
    plus(plus(power(r, 3, MOD3), scale(r, -3)), constant(-1, 3)) == constant(0, 3)
    for r in real_roots)
checks['paired_radicals_match_real_normal_forms'] = all(
    plus(power(t, (1 + 6*k) % 18), power(t, (-1 - 6*k) % 18)) == embed(real_roots[k])
    for k in range(3))
def conjugate(v):
    result = zero
    for i, coefficient in enumerate(v): result = plus(result, scale(power(t, (-i) % 18), coefficient))
    return result
checks['all_roots_fixed_by_complex_conjugation'] = all(conjugate(embed(r)) == embed(r) for r in real_roots)

STORE = {}
def digest(rec):
    return sha256(b'marici.cardano-merkle.v1\0' + json.dumps(rec, sort_keys=True, separators=(',', ':'), allow_nan=False).encode()).hexdigest()
def put(rec):
    key = digest(rec)
    STORE[key] = rec
    return key
def get(key, store=None):
    store = STORE if store is None else store
    if key not in store or digest(store[key]) != key: raise ValueError('hash mismatch')
    return store[key]
def value_node(value, typ): return put({'kind': 'value', 'type': typ, 'coefficients': encoded(value)})
def add_node(a, b): return put({'kind': 'add', 'type': 'Cyclotomic18', 'inputs': [a, b]})
def embedded_node(a): return put({'kind': 'embed-real', 'type': 'Cyclotomic18', 'input': a})

def evaluate(key, store=None):
    rec = get(key, store)
    if rec['kind'] == 'value':
        if rec['type'] not in ('Cyclotomic18', 'RealCubic'): raise ValueError('unknown field')
        v = decoded(rec['coefficients'])
        if len(v) != (6 if rec['type'] == 'Cyclotomic18' else 3) or encoded(v) != rec['coefficients']:
            raise ValueError('noncanonical field coordinates')
        return rec['type'], v
    if rec['kind'] == 'add':
        if len(rec['inputs']) != 2: raise ValueError('arity')
        a, b = [evaluate(ref, store) for ref in rec['inputs']]
        if rec['type'] != 'Cyclotomic18' or a[0] != rec['type'] or b[0] != rec['type']: raise ValueError('typed addition')
        return rec['type'], plus(a[1], b[1])
    if rec['kind'] == 'embed-real':
        a = evaluate(rec['input'], store)
        if rec['type'] != 'Cyclotomic18' or a[0] != 'RealCubic': raise ValueError('typed embedding')
        return rec['type'], embed(a[1])
    raise ValueError('not an algebraic expression')

def make_boundary(u, v, s):
    return put({'kind': 'CardanoBoundary', 'p': -3, 'q': -1,
                'u': value_node(u, 'Cyclotomic18'), 'v': value_node(v, 'Cyclotomic18'),
                's': value_node(s, 'Cyclotomic18'),
                'equations': ['s^2=-3/4', 'u^3=1/2+s', 'v^3=1/2-s', 'uv=1']})

def verify_boundary(key, store=None):
    rec = get(key, store)
    if set(rec) != {'kind', 'p', 'q', 'u', 'v', 's', 'equations'} or rec['kind'] != 'CardanoBoundary' or rec['p'] != -3 or rec['q'] != -1 or rec['equations'] != ['s^2=-3/4', 'u^3=1/2+s', 'v^3=1/2-s', 'uv=1']:
        raise ValueError('wrong or incomplete boundary')
    terms = [evaluate(rec[name], store) for name in ('u', 'v', 's')]
    if any(typ != 'Cyclotomic18' for typ, _ in terms): raise ValueError('boundary types')
    u, v, s = [v for _, v in terms]
    if not (power(s, 2) == scale(one, Q(-3, 4)) and power(u, 3) == plus(scale(one, Q(1, 2)), s)
            and power(v, 3) == plus(scale(one, Q(1, 2)), scale(s, -1)) and product(u, v, MOD6) == one):
        raise ValueError('Cardano attachment fails')
    return u, v, s

def package(boundary, term):
    witness = put({'kind': 'RootAndAssemblyWitness', 'boundary': boundary, 'term': term,
                   'method': 'exact cyclotomic arithmetic; x=u+v and x^3-3x-1=0'})
    return put({'kind': 'WitnessedCardanoRoot', 'boundary': boundary, 'term': term, 'witness': witness})
def verify_package(key, store=None):
    rec = get(key, store)
    if set(rec) != {'kind', 'boundary', 'term', 'witness'} or rec['kind'] != 'WitnessedCardanoRoot': raise ValueError('package shape')
    u, v, _ = verify_boundary(rec['boundary'], store)
    typ, value = evaluate(rec['term'], store)
    if typ != 'Cyclotomic18' or value != plus(u, v) or plus(plus(power(value, 3), scale(value, -3)), scale(one, -1)) != zero:
        raise ValueError('root/assembly equation fails')
    expected = {'kind': 'RootAndAssemblyWitness', 'boundary': rec['boundary'], 'term': rec['term'],
                'method': 'exact cyclotomic arithmetic; x=u+v and x^3-3x-1=0'}
    if get(rec['witness'], store) != expected: raise ValueError('witness attachment mismatch')
    return value

def certificate(before, after): return put({'kind': 'BranchPreservingEquivalence', 'from': before, 'to': after})
def verify_certificate(key, store=None):
    rec = get(key, store)
    if set(rec) != {'kind', 'from', 'to'} or rec['kind'] != 'BranchPreservingEquivalence': raise ValueError('certificate shape')
    left, right = get(rec['from'], store), get(rec['to'], store)
    if left['boundary'] != right['boundary']: raise ValueError('branch boundary changed')
    if verify_package(rec['from'], store) != verify_package(rec['to'], store): raise ValueError('root changed')
    return True

def swap_certificate(before, after): return put({'kind': 'EndpointSwapEquivalence', 'from': before, 'to': after})
def verify_swap(key, store=None):
    rec = get(key, store)
    if set(rec) != {'kind', 'from', 'to'} or rec['kind'] != 'EndpointSwapEquivalence': raise ValueError('swap certificate shape')
    left, right = get(rec['from'], store), get(rec['to'], store)
    u, v, s = verify_boundary(left['boundary'], store)
    uu, vv, ss = verify_boundary(right['boundary'], store)
    if (uu, vv, ss) != (v, u, scale(s, -1)): raise ValueError('missing endpoint-swap transport')
    if verify_package(rec['from'], store) != verify_package(rec['to'], store): raise ValueError('swap changed root')
    return True

def rejected(action):
    try: action()
    except (ValueError, KeyError): return True
    return False

branches = []
for k in range(3):
    u, v = power(t, 1 + 6*k), power(t, (-1 - 6*k) % 18)
    s = scale(plus(power(u, 3), scale(power(v, 3), -1)), Q(1, 2))
    for orientation in (1, -1):
        uu, vv, ss = (u, v, s) if orientation == 1 else (v, u, scale(s, -1))
        boundary = make_boundary(uu, vv, ss)
        rec = get(boundary)
        before = package(boundary, add_node(rec['u'], rec['v']))
        after = package(boundary, embedded_node(value_node(real_roots[k], 'RealCubic')))
        cert = certificate(before, after)
        branches.append({'branch': k, 'orientation': orientation, 'source': before, 'normalized': after,
                         'certificate': cert, 'real_coordinates': encoded(real_roots[k])})
checks['six_branch_preserving_normalizations_verified'] = all(verify_certificate(b['certificate']) for b in branches)
checks['opposite_endpoint_orders_same_root_value'] = all(verify_package(branches[2*k]['source']) == verify_package(branches[2*k+1]['source']) for k in range(3))
checks['opposite_endpoint_orders_keep_distinct_package_hashes'] = all(branches[2*k]['normalized'] != branches[2*k+1]['normalized'] for k in range(3))
checks['equal_value_does_not_authorize_branch_erasure'] = rejected(lambda: verify_certificate(certificate(branches[0]['normalized'], branches[1]['normalized'])))
checks['different_valid_root_not_same_solution'] = verify_package(branches[0]['source']) != verify_package(branches[2]['source'])
swaps = [swap_certificate(branches[2*k]['normalized'], branches[2*k+1]['normalized']) for k in range(3)]
checks['explicit_attachment_swap_certifies_equal_value_presentations'] = all(verify_swap(c) for c in swaps)
restored = []
for k in range(3):
    left, right = branches[2*k]['normalized'], branches[2*k+1]['normalized']
    verify_swap(swap_certificate(right, left))
    u, v, s = verify_boundary(get(right)['boundary'])
    restored.append(make_boundary(v, u, scale(s, -1)) == get(left)['boundary'])
checks['reverse_swap_restores_original_boundary'] = all(restored)

u, v = t, power(t, 17)
s = scale(plus(power(u, 3), scale(power(v, 3), -1)), Q(1, 2))
wrong_v = product(v, zeta, MOD6)
checks['independent_cube_choice_preserves_individual_cubes'] = power(wrong_v, 3) == power(v, 3)
checks['independent_cube_choice_breaks_product'] = product(u, wrong_v, MOD6) != one
checks['independent_cube_choice_not_a_root'] = plus(plus(power(plus(u, wrong_v), 3), scale(plus(u, wrong_v), -3)), scale(one, -1)) != zero
checks['honestly_hashed_bad_branch_rejected'] = rejected(lambda: verify_boundary(make_boundary(u, wrong_v, s)))
missing = dict(get(get(branches[0]['source'])['boundary']))
missing['equations'] = missing['equations'][:-1]
checks['deleted_product_constraint_rejected'] = rejected(lambda: verify_boundary(put(missing)))
# Valid but different algebraic root substituted under the old source boundary.
old_boundary = get(branches[0]['source'])['boundary']
checks['different_root_with_old_attachment_rejected'] = rejected(lambda: verify_package(package(old_boundary, embedded_node(value_node(real_roots[1], 'RealCubic')))))

valid = {}
def retain(key):
    if key in valid: return
    rec = get(key); valid[key] = rec
    if rec['kind'] == 'add': refs = rec['inputs']
    elif rec['kind'] == 'embed-real': refs = [rec['input']]
    elif rec['kind'] == 'CardanoBoundary': refs = [rec[n] for n in ('u', 'v', 's')]
    elif rec['kind'] == 'WitnessedCardanoRoot': refs = [rec[n] for n in ('boundary', 'term', 'witness')]
    elif rec['kind'] == 'RootAndAssemblyWitness': refs = [rec['boundary'], rec['term']]
    elif rec['kind'] in ('BranchPreservingEquivalence', 'EndpointSwapEquivalence'): refs = [rec['from'], rec['to']]
    else: refs = []
    for ref in refs: retain(ref)
for b in branches: retain(b['certificate'])
for c in swaps: retain(c)
artifact = {'schema': 'marici.cardano-merkle-store.v1', 'branches': branches, 'swap_certificates': swaps, 'objects': valid}
serialized = json.loads(json.dumps(artifact))
checks['serialized_artifact_reverifies'] = (all(verify_certificate(b['certificate'], serialized['objects']) for b in serialized['branches'])
    and all(verify_swap(c, serialized['objects']) for c in serialized['swap_certificates']))
result = {'schema': 'marici.voevodsky.cardano-merkle-branches.v1', 'passed': all(checks.values()), 'checks': checks,
          'problem': 'x^3-3x-1=0; discriminant=-3/4', 'complex_field': 'Q[t]/(t^6-t^3+1)',
          'real_field': 'Q[h]/(h^3-3h-1)', 'embedding_h': encoded(alpha),
          'distinct_roots': 3, 'retained_branch_presentations': 6, 'branches': branches,
          'stored_objects': len(valid), 'checker_sha256': sha256(Path(__file__).read_bytes()).hexdigest(),
          'scope': 'Exact algebraic identities for this irreducible cubic and its six endpoint-order presentations. No floating-point sampling, global radical-branch selector, minimal circuit theorem, or geometric 2-Segal claim.'}
(BASE / 'results' / 'cardano_merkle_store.json').write_text(json.dumps(artifact, indent=2) + '\n', encoding='utf-8')
(BASE / 'results' / 'cardano_merkle_branches.json').write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
print(json.dumps({k: v for k, v in result.items() if k != 'branches'}, indent=2))
if not result['passed']: raise SystemExit(1)
