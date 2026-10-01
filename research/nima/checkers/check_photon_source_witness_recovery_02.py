"""Recover the native composable-pair span; audit its phase/spatial readers.

Uses existing registered prefix extension, not a new edge transport policy.
The source constructors supply seam proofs and retained families, not S4 edge
fillers or rational summation. Addition belongs to the declared coefficient
realization. Formal sources are inspected, not elaborated by this checker.
"""
from contextlib import redirect_stdout
from fractions import Fraction as F
from io import StringIO
from pathlib import Path
import hashlib
import json
import re

# This legacy module runs its finite path checks on import. Retain their output
# separately so stdout remains one SCC-readable JSON object.
IMPORT_LOG = StringIO()
with redirect_stdout(IMPORT_LOG):
    from retained_path_successor import RetainedSuccessorLedger, apply, identity
from photon_native_spatial_step import (
    REGISTRY, U, W, PLANE_STEP, ClockedHistory, VERTICES, continuation_matrix,
)
from check_triangle_half_phase import mm, transpose, zmul
from check_collective_four_state_identity import rank

ROOT = Path(__file__).resolve().parents[3]
DEST = ROOT / 'research/nima/results/photon-source-witness-recovery-02.json'
SOURCES = (
    'research/nima/agda/ActualSeedEndpointTable.agda',
    'research/nima/agda/TableFibrationCycle.agda',
    'research/nima/agda/IndexedConstructorTables.agda',
    'research/nima/agda/NativeTableRules.agda',
    'research/nima/agda/NativeTableResolution.agda',
    'research/nima/agda/SeedSeamPathComparisonBoundary.agda',
    'research/nima/checkers/retained_path_successor.py',
    'research/nima/checkers/check_indexed_path_synthesis.py',
    'research/nima/checkers/photon_native_spatial_step.py',
    'research/nima/checkers/check_natural_tower_return.py',
    'research/nima/checkers/check_triangle_half_phase.py',
    'research/nima/checkers/check_collective_four_state_identity.py',
    'research/nima/two-triangle-cycle-consolidation-and-stop.md',
    'research/nima/prior-seed-semantics-recovery-after-matrix-domain-gate.md',
    'research/chatgpt/marici_native_spatial_three_extension.md',
)


def sub(a, b):
    return tuple(tuple(x - y for x, y in zip(r, s)) for r, s in zip(a, b))


def zero(rows, columns):
    return tuple((F(0),) * columns for _ in range(rows))


def power(a, n):
    out = identity(len(a))
    for _ in range(n):
        out = mm(a, out)
    return out


def rejects(fn):
    try:
        fn()
    except ValueError:
        return
    raise AssertionError('Off-image or malformed retained payload admitted')


def main():
    DEST.unlink(missing_ok=True)
    raw = {name: (ROOT / name).read_bytes() for name in SOURCES}
    texts = {Path(name).name: value.decode('utf-8') for name, value in raw.items()}
    source = texts['ActualSeedEndpointTable.agda']
    sources = dict(re.findall(r'^source ([A-Z]+) = ([A-D])$', source, re.M))
    targets = dict(re.findall(r'^target ([A-Z]+) = ([A-D])$', source, re.M))
    packets = tuple((p.label, sources[p.label], targets[p.label]) for p in REGISTRY)
    assert packets == tuple((p.label, p.source, p.target) for p in REGISTRY)
    assert 'seed = T.table Occurrence (λ e → e) source target' in source
    explicit_seams = re.findall(r'^([\w-]+) : target ([A-Z]+) ≡ source ([A-Z]+)$', source, re.M)
    assert len(explicit_seams) == 6
    for name, a, b in explicit_seams:
        assert targets[a] == sources[b] and f'{name} = refl' in source
    # Recover the native types and their actual arguments, not a permutation
    # inferred from the graphical arrow notation.
    for file, equation in (
        ('TableFibrationCycle.agda', 'fibrate {E = E} p b = Σ E (λ e → p e ≡ b)'),
        ('TableFibrationCycle.agda', 'Iso.fun (unpack-fibers p) (b , e , witness) = e'),
        ('IndexedConstructorTables.agda', 'Result (E-header I F) = Σ I F'),
        ('IndexedConstructorTables.agda', 'Result (P-header I F) = (i : I) → F i'),
        ('IndexedConstructorTables.agda', 'Result (paths-header A x y) = x ≡ y'),
        ('NativeTableRules.agda', 'Filler a b = Σ (Ty a ≃ Ty b) (λ e → equivFun e (value a) ≡ value b)'),
        ('NativeTableRules.agda', 'Iso.fun law v = (λ i → fst (v i)) , (λ i → snd (v i))'),
        ('NativeTableRules.agda', 'generator v = comparison-package (left , v) (right , Iso.fun law v) (isoToEquiv law) refl'),
        ('NativeTableResolution.agda', 'module Target = Transport.Theory G.Package N.Rule N.Arity N.input N.output Admit'),
        ('SeedSeamPathComparisonBoundary.agda', '→ Path (target e) t → Path (source e) t'),
    ):
        assert equation in texts[file], (file, equation)

    ledger = RetainedSuccessorLedger(packets)
    root = ledger.root
    first = ledger.successor(root)
    byword = {tuple(e[2] for e in p): p for p in first.paths}
    assert len(first.paths) == 10
    expected = {(a, b) for a in sources for b in sources if targets[a] == sources[b]}
    assert set(byword) == expected
    assert len(expected - {(a, b) for _, a, b in explicit_seams}) == 4
    # Prefix and final projections both have nontrivial fibers. The native
    # group/unpack equivalence is ten grouped rows <-> ten rows, NOT six <-> ten.
    assert byword['AB', 'BC'][0] == byword['AB', 'BA'][0]
    assert byword['AB', 'BC'] != byword['AB', 'BA']
    assert byword['CA', 'AB'][-1] == byword['BA', 'AB'][-1]
    for direction in ('source', 'target'):
        assert ledger.deconstruct_family(ledger.family(first, direction)) == first.paths
    L, A, K = first.step_lift, first.summary, continuation_matrix()
    assert mm(A, L) == K == ledger.continuation
    assert (rank(L), rank(A), rank(K)) == (6, 6, 4)
    assert tuple(sum(row[i] for row in L) for i in range(6)) == (2, 1, 2, 2, 1, 2)
    assert mm(first.step_decoder, L) == identity(6)
    assert mm(L, first.step_decoder) != identity(10)
    # The existing bilinear path rule supplies exactly this unchanged-copy
    # extension when its RIGHT INPUT is all ones; it is not an E/P type law.
    for i in range(6):
        x = tuple(F(i == j) for j in range(6))
        assert ledger.compose_primitive_payloads(first, x, (F(1),) * 6) == apply(L, x)
    assert ledger.compose_primitive_payloads(first, U, U) != apply(L, U)

    E = transpose((U, W))
    # Existing coordinates(): a=x_AB, b=2*x_CA-x_AB. This is a membership
    # test for the declared plane, not a new inner product or physical projector.
    D = ((F(1), 0, 0, 0, 0, 0), (F(-1), 0, 2, 0, 0, 0))
    assert mm(D, E) == identity(2)
    P = mm(E, D)
    assert mm(K, E) == mm(E, PLANE_STEP)
    assert power(PLANE_STEP, 3) == identity(2)
    pair_leakage = []
    for (a, b), path in byword.items():
        i = next(i for i, p in enumerate(REGISTRY) if p.label == a)
        j = next(j for j, p in enumerate(REGISTRY) if p.label == b)
        atom = tuple(tuple(F(r == j and c == i) for c in range(6)) for r in range(6))
        image = mm(atom, E)
        residual = sub(image, mm(P, image))
        assert rank(image) == 1 and residual != zero(6, 2)
        pair_leakage.append([a, b])
    for j in range(6):
        edge = tuple(row if r == j else (F(0),) * 6 for r, row in enumerate(K))
        image = mm(edge, E)
        assert rank(image) == 1 and sub(image, mm(P, image)) != zero(6, 2)
    # On the complex eigenvector v=U+i*sqrt(3)*W, individual children COPY
    # v_parent, whereas only the final-occurrence sum has eigenphase omega.
    omega = (F(-1, 2), F(1, 2))
    v = tuple(zip(U, W))
    for path in first.paths:
        i = next(i for i, p in enumerate(REGISTRY) if p.label == path[0][2])
        assert v[i] != zmul(omega, v[i])

    stage, clocked = root, ClockedHistory.initial()
    rows = []
    for depth in range(4):
        values = ledger.encode(root, stage, U)
        expected_coefficients = {tuple((p.source, p.target, p.label) for p in h.packets): h.coefficient
                                 for h in clocked.paths}
        assert dict(zip(stage.paths, values)) == expected_coefficients
        assert ledger.summarize(stage, values) == clocked.summary()
        assert ledger.decode(root, stage, values) == U
        assert mm(stage.summary, mm(stage.origin_lift, E)) == mm(E, power(PLANE_STEP, depth))
        assert rank(mm(stage.summary, mm(stage.origin_lift, E))) == 2
        rows.append({'extensions': depth, 'paths': len(stage.paths),
                     'attached_clock_over_pi': str(clocked.clock_over_pi),
                     'summary_rank_on_origin_photon_plane': 2})
        if depth < 3:
            stage, clocked = ledger.successor(stage), clocked.advance()
    assert len(stage.paths) == 26 and clocked.summary() == U

    # Hostile to spatial-displacement descent through the final-occurrence
    # summary on ARBITRARY retained payloads. Do not misapply it to im(L_n E).
    words = {tuple(e[2] for e in p): i for i, p in enumerate(stage.paths)}
    a = words[('AB', 'BC', 'CA', 'AB')]
    b = words[('CA', 'AB', 'BA', 'AB')]
    detail = tuple(F(i == a) - F(i == b) for i in range(26))
    displacements = tuple(tuple(VERTICES[p[-1][1]][k] - VERTICES[p[0][1]][k] for k in range(3))
                          for p in stage.paths)
    spatial_reader = transpose(displacements)
    assert apply(stage.summary, detail) == (F(0),) * 6
    assert displacements[a] == (0, 0, 0) and displacements[b] == (0, -2, -2)
    assert apply(spatial_reader, detail) == (0, 2, 2)
    rejects(lambda: ledger.decode(root, stage, detail))
    # The sibling-detail control is a permitted arbitrary payload, not claimed
    # to be dynamically produced by unchanged copying from the photon seed.
    arbitrary = ledger.retain_payload(stage, detail)
    assert arbitrary.values == detail
    assert sum(d == (0, 0, 0) for d in displacements) == 10
    assert all(sum(x*x for x in d) <= 8 for d in displacements)

    report = {
        'passed': True,
        'classification': 'native_seam_span_recovered_but_its_coarse_phase_is_not_a_primitive_transport_witness',
        'admitted_scope': 'finite source-type audit and exact retained-span linearization; no new transport policy',
        'obligation': 'forward realization of the composable-pair carrier, then readout descent',
        'source_recovery': {
            'row_type': 'Sigma e:Occurrence. Sigma f:Occurrence. target(e)=source(f)',
            'primitive_occurrences': 6, 'composable_pair_rows': 10,
            'explicit_triangle_seam_proofs': 6, 'other_definitionally_matching_seams': 4,
            'native_grouping_equivalence': 'grouped ten-row carrier <-> same ten-row carrier',
            'comparison_fillers_not_supplied_by_seams': True,
            'pairs': [{'first': a, 'last': b, 'seam_vertex': targets[a]} for a, b in sorted(expected)],
        },
        'declared_linearization': {'equation': 'K = final_sum * prefix_pullback',
                                  'ranks': {'copy': 6, 'sum': 6, 'coarse': 4},
                                  'bilinear_right_input': 'all ones, as already declared by unchanged-copy extension',
                                  'summation_is_not_native_E_constructor': True},
        'phase_locality_test': {'pair_channels_failing_plane_preservation': len(pair_leakage),
                               'primitive_final_channels_failing_plane_preservation': 6,
                               'aggregate_preserves_plane': True,
                               'branch_phase': 'coefficient copied unchanged; omega occurs after summation'},
        'retained_phase_square': rows,
        'spatial_descent_hostile': {'domain': 'arbitrary rational payloads on the 26-word carrier',
                                    'same_final_occurrence': 'AB',
                                    'closed_word': ['AB', 'BC', 'CA', 'AB'],
                                    'open_word': ['CA', 'AB', 'BA', 'AB'],
                                    'summary_of_difference': [0] * 6,
                                    'displacement_reader_of_difference': [0, 2, 2],
                                    'difference_in_unchanged_copy_image': False,
                                    'summary_faithful_on_fixed_depth_origin_photon_image': True},
        'residuals': ['Seam proofs certify composition, not an action on phase/spatial payloads.',
                      'No recovered map sends this retained coefficient process to the larger spatial realization or selects physical evolution.'],
        'conclusion': 'The demand for six S4 fillers belongs to an extra adapter, not the native seed. Stop that recovery branch rather than inventing its missing physical response.',
        'reopening_condition': 'An independently supplied response/realization map on retained path packages, with primitive action and compatibility with the existing phase-summary square.',
        'formal_verification': 'Source equations inspected; this Python checker does not run Agda. See packet for separate failed fresh compiler launch.',
        'legacy_import_checks': IMPORT_LOG.getvalue().splitlines(),
        'source_sha256': {name: hashlib.sha256(data).hexdigest() for name, data in raw.items()},
        'checker_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    }
    DEST.parent.mkdir(parents=True, exist_ok=True)
    DEST.write_text(json.dumps(report, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    main()
