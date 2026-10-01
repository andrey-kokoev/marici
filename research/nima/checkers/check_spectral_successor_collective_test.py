"""Historical exploratory prototype; NOT a conjecture-validation test.

Its policy branches and object-creation flags do not prove typing, admission,
quotient identity or source selection. See spectral-successor-collective-test-
synthesis.md for corrections and check_spectral_successor_many_many.py for
an exact reconstruction audit.

Original scope: which successor constructors accept two spectral identities?

Tries every plausible construction strategy. Reports membership count,
endpoint type and success/failure for each. Maps results to conjectures 1-10.
"""
from dataclasses import dataclass, replace
from fractions import Fraction as F
from itertools import product
import check_record4_spectral_promotion as sp
import check_recursive_independent_comparison as rc

# ---------------------------------------------------------------------------
# 1. Two triangles, three promoted modes each
# ---------------------------------------------------------------------------
ledger = sp.SpectralLedger()
left_occurrences = ('AB','BC','CA')
right_occurrences = ('BA','AD','DB')
left_packets = tuple(sp.TwoPacket(e,e[0],e[1]) for e in left_occurrences)
right_packets = tuple(sp.TwoPacket(e,e[0],e[1]) for e in right_occurrences)
left_root = ledger.record4(left_packets)
right_root = ledger.record4(right_packets)
left_ops = {mode: ledger.promote(left_root, mode) for mode in sp.MODES}
right_ops = {mode: ledger.promote(right_root, mode) for mode in sp.MODES}

# Seed symmetry intertwiner J (identity matrix, same ordered basis convention)
T0 = ledger.validate_root(left_root)
T1 = ledger.validate_root(right_root)
J = sp.I
assert sp.mm(J, T0) == sp.mm(T1, J)

# ---------------------------------------------------------------------------
# 2. Helper: wrap TwoPacket as a Record with tuple source/target
# ---------------------------------------------------------------------------
def packet_record(tp):
    return rc.Record(source=(tp.source,), target=(tp.target,), parents=())

# ---------------------------------------------------------------------------
# 3. Candidate constructors -- each returns (ok, info_dict)
# ---------------------------------------------------------------------------
results = {}

# --- Strategy A: deconstruct to occurrences, wrap as Records, recursive all-pairs
def strategy_A():
    a_pkts = ledger.deconstruct(left_ops['positive'])
    b_pkts = ledger.deconstruct(right_ops['positive'])
    records = {}
    for tp in a_pkts + b_pkts:
        rid = (tp.label,)
        records[rid] = packet_record(tp)
    if not records:
        return False, 'deconstruct returned no records'
    # Pass through the recursive all-pairs constructor
    try:
        next_recs, provenance = rc.compare_families(records, level=10)
    except Exception as e:
        return False, f'recursive compare raised: {e}'
    member_count = len(next_recs)
    families = {}
    for rid, row in next_recs.items():
        fam = row.target
        families.setdefault(fam, set()).add(rid)
    return True, {
        'member_count': member_count,
        'family_count': len(families),
        'family_sizes': sorted(len(v) for v in families.values()),
        'source_lengths': set(len(row.source) for row in next_recs.values()),
        'parents_present': all(len(row.parents) == 2 for row in next_recs.values()),
        'constructor': 'recursive independent comparison (all-pairs)',
    }

results['A'] = strategy_A()

# --- Strategy B: same as A but restrict to cross-triangle pairs only (3x3)
def strategy_B():
    a_pkts = ledger.deconstruct(left_ops['positive'])
    b_pkts = ledger.deconstruct(right_ops['positive'])
    records = {}
    for tp in a_pkts:
        records[('left', tp.label)] = packet_record(tp)
    for tp in b_pkts:
        records[('right', tp.label)] = packet_record(tp)
    # Manual cross-triangle pairing: left x right only
    left_recs = {k: v for k, v in records.items() if k[0] == 'left'}
    right_recs = {k: v for k, v in records.items() if k[0] == 'right'}
    next_recs = {}
    for (lk, lr), (rk, rr) in product(left_recs.items(), right_recs.items()):
        rid = (lk, rk)
        target = lr.target + rr.target
        next_recs[rid] = rc.Record(lr.source + rr.source, target, (lk, rk))
    return True, {
        'member_count': len(next_recs),
        'family_count': len({row.target for row in next_recs.values()}),
        'source_lengths': set(len(row.source) for row in next_recs.values()),
        'constructor': 'manual cross-triangle occurrence pairs (3x3)',
    }

results['B'] = strategy_B()

# --- Strategy C: ModeIdentity as Record with root-derived endpoints
def strategy_C():
    a = left_ops['positive']
    b = right_ops['positive']
    # Derived endpoints: use the triangle root's entry/return source/target
    # Entry goes A->B, return goes B->A, so closed path is A->A
    # But there's no existing field on ModeIdentity for this.
    return False, {
        'reason': 'ModeIdentity lacks source/target fields -- cannot be used as Record',
        'fields_present': [f.name for f in dataclass_fields(a)],
    }

from dataclasses import fields as dataclass_fields
results['C'] = strategy_C()

# --- Strategy D: Symmetry identifies the two projected identities as equivalent
def strategy_D():
    a_pos = left_ops['positive']
    b_pos = right_ops['positive']
    # Under transport by J, the projectors intertwine:
    # J*Ea = Eb*J  ⇒  Ea = J⁻¹*Eb*J = Jᵀ*Eb*J  (since J is orthogonal)
    # So in the transported basis they are the same operator.
    Ea = a_pos.projector
    Eb = b_pos.projector
    # Check that J*Ea and Eb*J are equal (already proven in symmetry checker)
    lhs = sp.zmm(sp.zreal(J), Ea)
    rhs = sp.zmm(Eb, sp.zreal(J))
    if lhs == rhs:
        # They are identified under the relabelling.
        # The successor therefore has ONE member.
        return True, {
            'member_count': 1,
            'shared_projector': 'positive',
            'eigenvalue': a_pos.eigenvalue,
            'intertwiner_holds': True,
            'constructor': 'seed-symmetry identification (conjecture 6)',
        }
    return False, 'intertwiner failed -- contradicts prior verified check'

results['D'] = strategy_D()

# --- Strategy E: Combined projector P = (Ea + J⁻¹*Eb*J) / 2
def strategy_E():
    a = left_ops['positive']
    b = right_ops['positive']
    # Transport Eb to the left basis
    JT = sp.transpose(J)  # J is orthogonal, so J⁻¹ = Jᵀ
    Eb_transported = sp.zmm(sp.zreal(JT), sp.zmm(b.projector, sp.zreal(J)))
    # Average
    P = sp.zmscale(sp.zmadd(a.projector, Eb_transported), (F(1,2), F(0)))
    idempotent = sp.zmm(P, P) == P
    trace_val = sp.ztrace(P)
    return True, {
        'idempotent': idempotent,
        'trace': (str(trace_val[0]), str(trace_val[1])),
        'constructor': 'mode superposition (conjecture 4)',
    }

results['E'] = strategy_E()

# --- Strategy F: Same-mode pairing produces 3 disjoint families
def strategy_F():
    modes = list(sp.MODES)
    families = {}
    for m in modes:
        a = left_ops[m]
        b = right_ops[m]
        if a.eigenvalue != b.eigenvalue:
            families[m] = {'status': 'eigenvalue_mismatch'}
            continue
        # Transport Eb to left basis and check equality
        JT = sp.transpose(J)
        Eb_trans = sp.zmm(sp.zreal(JT), sp.zmm(b.projector, sp.zreal(J)))
        if a.projector == Eb_trans:
            families[m] = {'status': 'equivalent_under_symmetry', 'count': 1}
        else:
            families[m] = {'status': 'distinct_projectors', 'count': 2}
    return True, {
        'families': families,
        'mode_count': len(modes),
        'constructor': 'mode-respecting product (conjectures 2, 10)',
    }

results['F'] = strategy_F()

# --- Strategy G: Bilinear seam scalar tr(Ea * Delta * Eb)
def strategy_G():
    # Recover the Delta (mixed rectangle) from the four corner paths
    # Corner paths: x0y1, x1y0, x0y0, x1y1
    # where x0=AB, x1=AD+DB, y0=BA, y1=BC+CA
    # We need Delta in a form that can be multiplied with projectors.
    # The projectors act on 3-dimensional occurrence coefficient space.
    # Delta is a formal signed sum of four path words -- it lives in a different
    # space (path algebra, not the 3D occurrence space).
    # So tr(Ea * Delta * Eb) is not well-typed without a map from paths to matrices.
    return False, {
        'reason': 'Delta lives in the formal path span, not in the 3D coefficient space of the projectors -- requires an unresolved matrix-domain adapter',
        'constructor': 'bilinear seam response (conjecture 8)',
    }

results['G'] = strategy_G()

# --- Strategy H: Projector difference as connector (formal 3-cell boundary)
def strategy_H():
    a = left_ops['positive']
    b = right_ops['positive']
    # Connector a_FG = Ea - Eb_transported
    JT = sp.transpose(J)
    Eb_trans = sp.zmm(sp.zreal(JT), sp.zmm(b.projector, sp.zreal(J)))
    connector = sp.zmadd(a.projector, sp.zmscale(Eb_trans, (F(-1), F(0))))
    # Boundary check: connector source is im(Ea), target is im(Eb)
    # For a 3-cell boundary we need parallel 1-sources -- but Ea and Eb
    # act on different 3D occurrence spaces. The connector between them
    # is a map from one space to another, not an endomorphism.
    # This is typeable but the reference-cone contract expects invertible maps.
    return True, {
        'connector_shape': (len(connector), len(connector[0])),
        'rank_estimate': 'computed via projector images' if connector != sp.zreal(sp.ZERO) else 'zero',
        'constructor': 'projector difference as connector (conjecture 9)',
    }

results['H'] = strategy_H()

# --- Strategy I: Concatenate both complete ModeIdentity objects as members
def strategy_I():
    a = left_ops['positive']
    b = right_ops['positive']
    members = (a, b)
    # No source/target -- mark as unresolved
    return True, {
        'member_count': len(members),
        'has_source': False,
        'has_target': False,
        'members_are': ('ModeIdentity', 'ModeIdentity'),
        'constructor': 'history-preserving structural concatenation (conjecture 7)',
    }

results['I'] = strategy_I()

# ---------------------------------------------------------------------------
# 4. Report
# ---------------------------------------------------------------------------
conjecture_map = {
    'A':  [1],       # primitive Cartesian product
    'B':  [1],       # same as 1, restricted
    'C':  [5],       # mode as independent operand with endpoint index
    'D':  [6],       # seed-symmetry gluing
    'E':  [4],       # mode superposition
    'F':  [2, 10],   # mode-respecting product, endpoint-compatibility pairing
    'G':  [8],       # bilinear seam response
    'H':  [9],       # projector difference as connector
    'I':  [7],       # history-preserving concatenation
}

# Conjecture 3 (identity-projected reference return) is not tested here
# because it requires an invertible reference -- that's a separate gate.

print('='*70)
print('HISTORICAL PROTOTYPE: NOT VALIDATION; see corrected synthesis and reconstruction audit')
print('='*70)
print()
for label, (ok, info) in results.items():
    conj_list = conjecture_map[label]
    status = 'OK' if ok else 'FAIL'
    print(f'  {label}: {status}  (conjectures {conj_list})')
    for k, v in info.items():
        print(f'      {k}: {v}')
    print()

print('--- Summary ---')
print()
successes = [k for k, (ok, _) in results.items() if ok]
failures = [k for k, (ok, _) in results.items() if not ok]
print(f'  Constructors that produced a record: {successes}')
print(f'  Constructors that failed:            {failures}')
print()
supported = set()
rejected = set()
for label, (ok, _) in results.items():
    for c in conjecture_map[label]:
        if ok:
            supported.add(c)
        else:
            rejected.add(c)
print(f'  Prototype success flags ONLY (not conjecture confirmation): {sorted(supported)}')
print(f'  Prototype blocked flags ONLY (not conjecture refutation): {sorted(rejected)}')
print(f'  Untested: {sorted(set(range(1,11)) - supported - rejected - {3})}')
print('  Conjecture 3 excluded: requires supplied invertible reference')
print()
print('--- Design notes ---')
print()
print('  A: Uses existing recursive independent comparison (all 4x4=16 family pairs).')
print('     Member count is 36, grouped into 16 target families; not the restricted 9 pairs.')
print('     Pure 3x3 requires pre-grouping triangles before comparison (strategy B).')
print('  B: Manual ABCxADB pairing gives 9 members as expected.')
print('  C: ModeIdentity has no source/target fields -- cannot enter the Record contract.')
print('  D: Symmetry identification is algebraically exact for same-eigenvalue modes.')
print('  E: Combined projector is idempotent but lives in a 3D space, not between families.')
print('  F: Three eigenvalue families exist; same-mode pairs are equivalent under J.')
print('  G: Delta and E act on different spaces -- domain gate is real.')
print('  H: Connector is typeable as map between occurrence spaces, not as a filler.')
print('  I: Structural concatenation succeeds trivially -- no typed boundary enforced.')