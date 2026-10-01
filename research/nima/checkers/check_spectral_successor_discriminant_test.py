"""Historical prototype: hardcoded endpoint/pairing flags do not prove admission.

The '7 surviving conjectures' and promotability interpretation below are
superseded; see spectral-successor-collective-test-synthesis.md. Same-mode
acceptance is an input policy here, not evidence selecting that policy.
Use check_spectral_successor_many_many.py for exact reconstruction checks.

Original scope: vary eigenvalue (same vs different) and check promotability.

The key questions that separate the 7 surviving conjectures:
1. Does the successor require same eigenvalue? (YES -> 2,6,10; NO -> 1,4,7,9)
2. Does the successor have concrete source/target for re-promotion? (YES -> 1,10; NO -> 4,6,7,9)
3. Does swapping input order change the successor? (YES -> 1,9,7; NO -> 4,6,10; mixed -> 2)
4. Can two promotions from the SAME triangle form a non-trivial successor? (YES -> 1,4; NO -> 2,6,7,9,10)

Each test records whether the construction was possible and what it produced.
"""
from dataclasses import dataclass, fields as dc_fields
from fractions import Fraction as F
from itertools import product
import check_record4_spectral_promotion as sp
import check_recursive_independent_comparison as rc

# ---------------------------------------------------------------------------
# 1. Setup: two triangles, all modes promoted
# ---------------------------------------------------------------------------
ledger = sp.SpectralLedger()
left_pkts = tuple(sp.TwoPacket(e,e[0],e[1]) for e in ('AB','BC','CA'))
right_pkts = tuple(sp.TwoPacket(e,e[0],e[1]) for e in ('BA','AD','DB'))
left_root = ledger.record4(left_pkts)
right_root = ledger.record4(right_pkts)
all_modes = {m: (ledger.promote(left_root, m), ledger.promote(right_root, m))
             for m in sp.MODES}

# Seed symmetry intertwiner
T0, T1 = ledger.validate_root(left_root), ledger.validate_root(right_root)
J = sp.I
assert sp.mm(J, T0) == sp.mm(T1, J)

def transport_projector(E, direction='to_left'):
    """Transports a 3x3 projector between the two triangle basises."""
    if direction == 'to_left':
        return sp.zmm(sp.zreal(sp.transpose(J)),
                      sp.zmm(E, sp.zreal(J)))
    else:
        return sp.zmm(sp.zreal(J),
                      sp.zmm(E, sp.zreal(sp.transpose(J))))

# ---------------------------------------------------------------------------
# 2. Construction strategies — each returns (ok, info)
# ---------------------------------------------------------------------------

def strut_promotable(record_like):
    """Check if an object can be grouped by target and promoted."""
    return (hasattr(record_like, 'source') and hasattr(record_like, 'target')
            and record_like.source is not None and record_like.target is not None)

# --- Strategy 1: recover occurrences, build Records, all-pairs comparison
def try_occurrence_product(ids_a, ids_b):
    pkts_a = ledger.deconstruct(ids_a)
    pkts_b = ledger.deconstruct(ids_b)
    records = {}
    for tp in pkts_a + pkts_b:
        records[(tp.label,)] = rc.Record(source=(tp.source,), target=(tp.target,))
    try:
        next_recs, _ = rc.compare_families(records, level=10)
    except Exception as e:
        return False, {'error': str(e)}
    return True, {'count': len(next_recs), 'promotable': True,
                  'sample_source': next(iter(next_recs.values())).source,
                  'sample_target': next(iter(next_recs.values())).target}

# --- Strategy 2: combined projector P = (Ea + transported(Eb)) / 2
def try_combined_projector(ids_a, ids_b):
    Ea = ids_a.projector
    Eb = transport_projector(ids_b.projector, 'to_left')
    P = sp.zmscale(sp.zmadd(Ea, Eb), (F(1,2), F(0)))
    ok = sp.zmm(P, P) == P
    src = dst = '3x3_matrix_no_endpoints'
    return ok, {'idempotent': ok, 'trace': str(sp.ztrace(P)),
                'source': src, 'target': dst,
                'promotable': False}

# --- Strategy 3: symmetry identification (requires same eigenvalue)
def try_symmetry_identification(ids_a, ids_b):
    if ids_a.eigenvalue != ids_b.eigenvalue:
        return False, {'error': 'different eigenvalues — symmetry does not identify them'}
    Ea = ids_a.projector
    Eb_t = transport_projector(ids_b.projector, 'to_left')
    return Ea == Eb_t, {'identified': Ea == Eb_t,
                         'source': 'symmetry_class', 'target': 'symmetry_class',
                         'promotable': False}

# --- Strategy 4: structural concatenation (trivially ok)
def try_concatenation(ids_a, ids_b):
    return True, {'count': 2, 'source': None, 'target': None, 'promotable': False}

# --- Strategy 5: projector difference as connector
def try_connector(ids_a, ids_b):
    Ea = ids_a.projector
    Eb_t = transport_projector(ids_b.projector, 'to_left')
    C = sp.zmadd(Ea, sp.zmscale(Eb_t, (F(-1), F(0))))
    return True, {'shape': f'{len(C)}x{len(C[0])}',
                  'is_zero': C == sp.zreal(sp.ZERO),
                  'source': 'im(Ea)', 'target': 'im(Eb)',
                  'promotable': False}

# --- Strategy 6: endpoint-compatibility pairing (requires same eigenvalue, endpoints A->A)
def try_endpoint_pairing(ids_a, ids_b):
    if ids_a.eigenvalue != ids_b.eigenvalue:
        return False, {'error': 'different eigenvalues — no compatible pairing'}
    # Make a minimal promotable record: source=A, target=A, parents=both IDs
    rec = rc.Record(source=('A',), target=('A',), parents=(ids_a.label, ids_b.label))
    return True, {'count': 1, 'source': rec.source, 'target': rec.target,
                  'promotable': True, 'parents': rec.parents}

# --- Strategy 7: same-triangle double promotion (non-triviality check)
def try_same_triangle_double(ids_a, ids_b_from_same_root):
    """Both identities promoted from the same root."""
    if ids_a.window.root != ids_b_from_same_root.window.root:
        return False, {'error': 'different roots'}
    # Try occurrence product — should give pairs within one triangle
    return try_occurrence_product(ids_a, ids_b_from_same_root)

# ---------------------------------------------------------------------------
# 3. Test matrix
# ---------------------------------------------------------------------------
tests = []

# Conditions
conditions = [
    ('same-positive',    all_modes['positive'][0], all_modes['positive'][1]),
    ('same-common',      all_modes['common'][0],   all_modes['common'][1]),
    ('same-negative',    all_modes['negative'][0], all_modes['negative'][1]),
    ('cross-pos-common', all_modes['positive'][0], all_modes['common'][1]),
    ('cross-pos-neg',    all_modes['positive'][0], all_modes['negative'][1]),
    ('cross-common-neg', all_modes['common'][0],   all_modes['negative'][1]),
]

strategies = [
    ('occurrence_product',  try_occurrence_product),
    ('combined_projector',  try_combined_projector),
    ('symmetry_id',         try_symmetry_identification),
    ('concatenation',       try_concatenation),
    ('connector_diff',      try_connector),
    ('endpoint_pairing',    try_endpoint_pairing),
]

# Triples promoting both from the SAME root
same_root_variants = [
    ('same-root-pos-pos', ledger.promote(left_root, 'positive'),
                          ledger.promote(left_root, 'positive')),
    ('same-root-pos-com', ledger.promote(left_root, 'positive'),
                          ledger.promote(left_root, 'common')),
]

print('='*72)
print('HISTORICAL POLICY PROTOTYPE -- NOT A CONJECTURE SELECTION TEST')
print('='*72)
print()
print(f'{"Condition":24s}', end='')
for sname, _ in strategies:
    print(f'{sname:20s}', end='')
print()
print('-'*24 + '-'*20*len(strategies))

for cname, id_a, id_b in conditions:
    print(f'{cname:24s}', end='')
    for sname, strat in strategies:
        ok, info = strat(id_a, id_b)
        tag = 'OK' if ok else 'XX'
        print(f'{tag:20s}', end='')
    print()

print()
print('--- Same-root (both promoted from left triangle) ---')
for cname, id_a, id_b in same_root_variants:
    print(f'{cname:24s}', end='')
    ok, info = try_occurrence_product(id_a, id_b)
    tag = 'OK' if ok else 'XX'
    print(f'occurrence_prod: {tag:12s} count={info.get("count","?")}')
    
    # Combined projector for same-root
    Ea, Eb = id_a.projector, id_b.projector
    P = sp.zmscale(sp.zmadd(Ea, Eb), (F(1,2), F(0)))
    print(f'{"":24s} combined_proj:   idempotent={sp.zmm(P,P)==P} trace={sp.ztrace(P)}')

print()
print('--- Order swap test (positive mode) ---')
a, b = all_modes['positive']
for label, first, second in [('normal', a, b), ('swapped', b, a)]:
    print(f'{label:24s}', end='')
    ok, info = try_occurrence_product(first, second)
    tag = f'occ_prod count={info.get("count","?")}'
    print(f'{tag}')
    _, info_conn = try_connector(first, second)
    conn_zero = info_conn.get('is_zero', '?')
    print(f'{"":24s} connector_diff is_zero={conn_zero}')

print()
print('='*72)
print('INTERPRETATION')
print('='*72)
print()
print('Columns: OK=construction succeeded, XX=construction failed.')
print()
print('Rows labelled "same-*" test same-eigenvalue inputs;')
print('rows labelled "cross-*" test different-eigenvalue inputs.')
print()
print('Key discriminant axes:')
print('  A. Does the construction require same eigenvalue?')
print('     (compare same-positive vs cross-pos-common rows)')
print('  B. Is the output promotable (has concrete source/target)?')
print('     (check promotable field in each strategy)')
print('  C. Is the construction non-trivial?')
print('     (check connector is zero, combined proj is not just E, etc.)')
print('  D. Can it produce non-trivial output from one triangle alone?')
print('     (see same-root section)')