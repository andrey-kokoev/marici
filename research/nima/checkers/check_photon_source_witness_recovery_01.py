"""Recover concrete source operations before identifying photon continuation.

Exact finite audit, not Agda elaboration or a physical-time theorem. The seed
is parsed from SeedAttachedObserver.agda. No per-edge S4 policy is selected.
"""
from dataclasses import fields
from fractions import Fraction as F
from itertools import permutations, product
from pathlib import Path
import hashlib
import json
import re

from photon_native_spatial_step import (
    ClockedHistory, RetainedPath, REGISTRY, U, W, PLANE_STEP,
    continuation_matrix, coordinates, contrast_reader, target_reader, mv,
)
from check_twenty_four_triangle_shared_seed import proper, rotation, POINTS, det, mean
from check_triangle_half_phase import mm, transpose

ROOT = Path(__file__).resolve().parents[3]
DEST = ROOT / 'research/nima/results/photon-source-witness-recovery-01.json'
SOURCES = (
    'research/nima/agda/SeedAttachedObserver.agda',
    'research/nima/agda/ObserverCoherenceCube.agda',
    'research/nima/agda/DependentSigmaPiCoherence.agda',
    'research/nima/agda/ProofRelevantCoherenceClosure.agda',
    'research/nima/agda/WholePackageSigmaPiInstance.agda',
    'research/nima/agda/BoundaryGeneratedQuestions.agda',
    'research/nima/agda/RetainedComparisonSeries.agda',
    'research/nima/agda/NativeTableRegression.agda',
    'research/nima/checkers/photon_native_spatial_step.py',
    'research/nima/checkers/check_triangle_half_phase.py',
    'research/nima/checkers/check_natural_tower_return.py',
    'research/nima/checkers/check_twenty_four_triangle_shared_seed.py',
    'research/nima/checkers/check_twelve_triangle_positive_geometry.py',
)


def identity(n):
    return tuple(tuple(F(i == j) for j in range(n)) for i in range(n))


def difference(a, b):
    return tuple(tuple(x - y for x, y in zip(r, s)) for r, s in zip(a, b))


def neg(a):
    return tuple(tuple(-x for x in row) for row in a)


def power(a, n):
    result = identity(len(a))
    for _ in range(n):
        result = mm(a, result)
    return result


def det2(a):
    return a[0][0] * a[1][1] - a[0][1] * a[1][0]


def permutation_matrix(image):
    return tuple(tuple(F(i == image[j]) for j in range(len(image))) for i in range(len(image)))


def rejects(fn):
    try:
        fn()
    except ValueError:
        return
    raise AssertionError('Out-of-plane candidate accepted as photon phase transport')


def main():
    DEST.unlink(missing_ok=True)
    raw = {name: (ROOT / name).read_bytes() for name in SOURCES}
    text = {Path(name).name: data.decode('utf-8') for name, data in raw.items()}
    source = text['SeedAttachedObserver.agda']
    labels = 'ABCD'
    declared = re.findall(r'^\s+([A-Z]+(?: [A-Z]+)*) : Out ([A-D])$', source, re.M)
    outgoing = {v: tuple(names.split()) for names, v in declared}
    targets = dict(re.findall(r'^target ([A-Z]+) = ([A-D])$', source, re.M))
    source_of = {edge: v for v, edges in outgoing.items() for edge in edges}
    assert set(outgoing) == set(labels)
    assert {(p.label, p.source, p.target) for p in REGISTRY} == {
        (e, source_of[e], targets[e]) for e in source_of}
    assert tuple(f.name for f in fields(type(REGISTRY[0]))) == ('label', 'source', 'target')
    # The actual unit-family adapter has four source sections, not four seed
    # vertices masquerading as four Boolean points.
    assert '(λ _ _ → Unit) (λ _ _ _ → Unit) (λ _ _ _ _ → Unit)' in source
    sections = tuple(product(*(outgoing[v] for v in labels)))
    assert len(sections) == 4
    named_sections = {}
    for name in ('cycle', 'other'):
        choices = dict(re.findall(rf'^{name} ([A-D]) = ([A-Z]+) ,', source, re.M))
        named_sections[name] = tuple(choices[v] for v in labels)
        assert named_sections[name] in sections
    assert named_sections['cycle'] == ('AD', 'BC', 'CA', 'DB')
    assert named_sections['other'] == ('AB', 'BC', 'CA', 'DB')

    # Recover the specific equivalence actually passed to compare-rule.
    assert 'package-comparison x = comparison-package (source x) (target x) R.recordLift refl' in text['WholePackageSigmaPiInstance.agda']
    assert '(invEquiv (isoToEquiv routeA))' in text['DependentSigmaPiCoherence.agda']
    assert 'route-comparison x = refl' in text['DependentSigmaPiCoherence.agda']
    retained = text['ProofRelevantCoherenceClosure.agda']
    for equation in (
        'recordLift = Σ-cong-equiv-snd (λ q → Σ-cong-equiv-snd (λ t → pathLift e))',
        'source-retained r = refl', 'trace-retained r = refl',
        'witness-transported r = refl',
    ):
        assert equation in retained
    # The seed observer expansion is source projection on canonical traces,
    # not execution of the next directed edge.
    assert 'Iso.fun traceIso = fst' in text['ObserverCoherenceCube.agda']
    assert 'recover-attachments s = refl' in text['ObserverCoherenceCube.agda']
    # Encoding in native tables does not manufacture a different filler.
    assert 'actual-filler-equivalence a b = idEquiv _' in text['NativeTableRegression.agda']
    assert 'Iso.fun swap-iso (x , y) = y , x' in text['BoundaryGeneratedQuestions.agda']
    assert 'swap-filler : Filler fourQ fourQ' in text['BoundaryGeneratedQuestions.agda']
    certificate = re.search(r'^swap-image-codes : .* ≡ \((\d+) , (\d+) , (\d+) , (\d+)\)$',
                            text['RetainedComparisonSeries.agda'], re.M)
    assert certificate and tuple(map(int, certificate.groups())) == (0, 2, 1, 3)

    # Any reader of the retained (q,trace) factors through an unchanged pair.
    # The source proofs therefore give identity there, whereas K-I is invertible
    # on the entire nonzero photon plane. This is not just a sampled phase test.
    embedding = transpose((U, W))
    K = continuation_matrix()
    C = PLANE_STEP
    assert mm(K, embedding) == mm(embedding, C)
    assert power(C, 3) == identity(2)
    assert det2(difference(C, identity(2))) == 3
    assert det2(difference(C, neg(identity(2)))) == 1
    assert mv(K, U) != U

    # Exhaust the actual seed's relabelling symmetries, without identifying
    # Bool x Bool with its vertex set or forgetting the directed incidence.
    edges = {(p.source, p.target) for p in REGISTRY}
    autos = tuple(g for g in permutations(range(4))
                  if {(labels[g[labels.index(s)]], labels[g[labels.index(t)]]) for s, t in edges} == edges)
    assert autos == ((0, 1, 2, 3), (1, 0, 3, 2))
    g = autos[1]
    by_ends = {(p.source, p.target): p for p in REGISTRY}
    renamed = {p: by_ends[(labels[g[labels.index(p.source)]], labels[g[labels.index(p.target)]])]
               for p in REGISTRY}
    slot_image = tuple(REGISTRY.index(renamed[p]) for p in REGISTRY)
    S = permutation_matrix(slot_image)
    assert slot_image == (3, 4, 5, 0, 1, 2)
    assert mm(S, K) == mm(K, S)
    assert mm(S, embedding) == neg(embedding)
    assert all(power(C, n) != neg(identity(2)) for n in range(3))
    H = target_reader()
    assert mm(H, S) == mm(permutation_matrix(g), H)
    xyz = transpose(tuple(POINTS[v] for v in labels))
    assert mm(xyz, permutation_matrix(g)) == mm(rotation(g), xyz)
    assert proper(g) == rotation(g) == ((1, 0, 0), (0, -1, 0), (0, 0, -1))
    assert mm(contrast_reader(), S) == mm(proper(g), contrast_reader())
    assert mean(tuple(mv(proper(g), POINTS[v]) for v in labels)) == (0, 0, 0)

    def transport(history):
        return ClockedHistory(history.updates, tuple(
            RetainedPath(tuple(renamed[p] for p in path.packets), path.coefficient)
            for path in history.paths))

    def coefficients_on_words(history):
        # Retain the entire word; ignore only enumeration order, not prefixes.
        return {tuple(p.label for p in path.packets): path.coefficient for path in history.paths}

    history = ClockedHistory.initial()
    history_tests = []
    for depth in range(4):
        moved = transport(history)
        assert moved.clock_over_pi == history.clock_over_pi
        assert moved.updates == history.updates
        assert transport(moved) == history
        assert moved.summary() == mv(S, history.summary())
        assert coefficients_on_words(transport(history.advance())) == coefficients_on_words(moved.advance())
        assert moved.spatial_contrast() == mv(proper(g), history.spatial_contrast())
        history_tests.append({'depth': depth, 'retained_paths': len(history.paths),
                              'clock_over_pi': str(history.clock_over_pi), 'transport_advances_clock': False})
        history = history.advance()
    # Only AB and BA have their endpoints transported by this source symmetry.
    covered = [p.label for p in REGISTRY if g[labels.index(p.source)] == labels.index(p.target)]
    assert covered == ['AB', 'BA']

    # Test the actual source sections as deterministic routings, not as an
    # invented S4 edge policy. A choice at every source keeps four of six edges.
    section_rows = []
    for section in sections:
        image = tuple(labels.index(targets[e]) for e in section)
        selected = set(section)
        operator = tuple(row if p.label in selected else (F(0),) * 6
                         for p, row in zip(REGISTRY, K))
        output = mv(operator, U)
        rejects(lambda: coordinates(output))
        omitted = [p.label for p in REGISTRY if p.label not in selected]
        assert len(omitted) == 2
        assert all(output[i] == 0 and U[i] != 0 for i, p in enumerate(REGISTRY) if p.label in omitted)
        section_rows.append({'section': list(section), 'target_map': list(image),
                             'bijective_vertex_map': len(set(image)) == 4,
                             'omitted_packets': omitted, 'one_step_coefficients': list(map(str, output)),
                             'photon_plane_preserved': False})
    bijective = [row for row in section_rows if row['bijective_vertex_map']]
    assert len(bijective) == 1 and tuple(bijective[0]['section']) == named_sections['cycle']
    cycle = tuple(bijective[0]['target_map'])
    assert cycle == (3, 2, 0, 1) and cycle not in autos
    cycle_space = proper(cycle)
    assert det(rotation(cycle)) == -1
    assert power(cycle_space, 4) == identity(3)
    assert all(power(cycle_space, n) != identity(3) for n in (1, 2, 3))
    assert mean(tuple(mv(cycle_space, POINTS[v]) for v in labels)) == (0, 0, 0)
    # Bare Boolean-point swap, vertex symmetry, and selected section have
    # different types AND different finite image certificates.
    assert (0, 2, 1, 3) != g != cycle

    report = {
        'status': 'passed',
        'passed': True,
        'classification': 'concrete_source_comparisons_and_routings_do_not_supply_the_six_edge_photon_update',
        'admitted_scope': 'source-equation audit and exact finite joint relabelling tests; not physical evolution or fresh Agda elaboration',
        'obligation': 'attachment transport: recover typed source operations before joint phase-space identification',
        'stratum': 'exact six-arrow seed and declared two-dimensional phase plane; no physical-time or Agda-elaboration promotion',
        'source_record_comparison': {
            'witness': 'WholePackageSigmaPiInstance.R.recordLift',
            'action': '(q,t,p) -> (q,t,cong(e,p)), e=inverse(routeA)',
            'retained_pair_reader_action': 'identity',
            'native_table_bridge': 'idEquiv on the entire supplied filler',
            'det_phase_step_minus_identity': '3',
            'first_step_seed': list(map(str, mv(K, U))),
        },
        'boolean_swap': {'images': [0, 2, 1, 3], 'carrier': 'Bool x Bool pointed at (false,false)',
                         'vertex_or_packet_identification_supplied': False},
        'seed_symmetry': {
            'vertex_images': list(g), 'packet_images': list(slot_image),
            'phase_plane_action': '-I', 'det_phase_step_plus_identity': '1',
            'area_matrix': [[str(x) for x in row] for row in proper(g)],
            'body_centre': [0, 0, 0], 'endpoint_tasks_covered': covered,
            'full_word_naturality_checks': history_tests,
            'interpretation': 'compatible relabelling, not continuation or a phase-clock increment',
        },
        'source_sections': section_rows,
        'explicit_cycle': {'vertex_images': list(cycle), 'spatial_order': 4,
                           'area_matrix': [[str(x) for x in row] for row in cycle_space],
                           'seed_automorphism': False, 'omitted_packets': ['AB', 'BA']},
        'residuals': ['No inspected source operation supplies six primitive comparison witnesses compatible with the current branching phase update.'],
        'next_falsifier': 'Audit the native E/P and composition constructors for the actual composable-pair span (six <- ten -> six), rather than assuming each continuation must be a four-vertex bijection.',
        'unsupported': ['identifying Boolean points, seed sections, and seed vertices by cardinality',
                        'using the selected four-edge cycle as full six-edge continuation',
                        'a physical per-edge clock or translation', 'fresh Agda compilation'],
        'source_sha256': {name: hashlib.sha256(data).hexdigest() for name, data in raw.items()},
        'checker_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
    }
    DEST.parent.mkdir(parents=True, exist_ok=True)
    DEST.write_text(json.dumps(report, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    main()
