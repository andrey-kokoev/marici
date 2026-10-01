"""Exact integration and hostile checks for the retained-successor interface."""
from dataclasses import replace
from fractions import Fraction as F
from pathlib import Path
import json

import check_whole_seed_occurrence_spectrum as prior
import check_natural_tower_return as algebra
from retained_path_successor import (
    RetainedSuccessorLedger, SpectralDescriptor, identity, zero, apply,
)


def rejects(fn):
    try:
        fn()
    except ValueError:
        return
    raise AssertionError('Invalid interface operation was accepted')


def main():
    fixture = prior.main()  # fresh headless closure of all preceding audit gates
    names = ('phi', 'omega', 'psi', 'omega_conjugate')
    descriptors = tuple(SpectralDescriptor(name, d, eigenvalue, projector)
                        for name, (d, eigenvalue, projector) in zip(names, fixture['nonzero_modes']))
    descriptors += (SpectralDescriptor('zero_sector', 5, (F(0), F(0)),
                                       (fixture['zero_projector'], zero(6))),)
    ledger = RetainedSuccessorLedger(fixture['packets'], descriptors)
    root = ledger.root
    assert ledger.continuation == fixture['continuation']
    assert ledger.deconstruct(root) == fixture['packets']
    stages = [root]
    for _ in range(3):
        stages.append(ledger.successor(stages[-1]))
    assert [len(s.paths) for s in stages] == [6, 10, 16, 26]
    x = tuple(F(i - 2, 7) for i in range(6))
    summaries = []
    K_power = identity(6)
    all_modes = []
    for stage in stages:
        n = len(stage.paths)
        for direction in ('source', 'target'):
            family = ledger.family(stage, direction)
            assert ledger.deconstruct_family(family) == stage.paths
            rejects(lambda family=family: ledger.deconstruct_family(replace(family)))
        assert ledger.transition(root, stage) == (stage.origin_lift, stage.origin_decoder)
        encoded = ledger.encode(root, stage, x)
        assert ledger.decode(root, stage, encoded) == x
        assert ledger.summarize(stage, encoded) == apply(K_power, x)
        assert algebra.mm(stage.summary, stage.origin_lift) == K_power
        if stage is not root:
            parent, decomposition = ledger.deconstruct(stage)
            assert tuple(prefix + (edge,) for prefix, edge in decomposition) == stage.paths
            assert tuple(parent.paths[i] for i in stage.parent_slots) == tuple(p[:-1] for p in stage.paths)
        modes = tuple(ledger.inherit(stage, descriptor.name) for descriptor in descriptors)
        all_modes.append(modes)
        sums, weighted = {}, {}
        for mode in modes:
            d = mode.descriptor.radicand
            E = ledger.inherited_projector(mode)
            assert mode.origin == root.label and mode.ordered_occurrences == ledger.labels
            assert algebra.rmul(E, E, d) == E
            reading = ledger.read_mode(mode, encoded)
            assert reading == tuple(apply(part, encoded) for part in E)
            # The lifted action and origin descriptor commute with encoding.
            assert tuple(algebra.mm(part, stage.origin_lift) for part in E) == tuple(
                algebra.mm(stage.origin_lift, part) for part in mode.descriptor.projector)
            sums[d] = algebra.radd(sums.get(d, (zero(n), zero(n))), E)
            weighted[d] = algebra.radd(weighted.get(d, (zero(n), zero(n))),
                                       algebra.rscale(E, *mode.descriptor.eigenvalue, d))
            rejects(lambda mode=mode: ledger.resolve_mode(replace(mode)))
        total, reconstructed = zero(n), zero(n)
        for d in sums:
            assert sums[d][1] == weighted[d][1] == zero(n)
            total = algebra.add(total, sums[d][0])
            reconstructed = algebra.add(reconstructed, weighted[d][0])
        image = algebra.mm(stage.origin_lift, stage.origin_decoder)
        transported_K = algebra.mm(stage.origin_lift, algebra.mm(ledger.continuation, stage.origin_decoder))
        assert total == image and reconstructed == transported_K
        assert apply(total, encoded) == encoded
        assert reconstructed == algebra.mm(image, algebra.mm(reconstructed, image))
        assert algebra.mm(stage.summary, reconstructed) == algebra.mm(ledger.continuation, algebra.mm(stage.summary, image))
        if stage is not root:
            assert total != identity(n)  # no ambient spectral completeness claim
        summaries.append({'word_length': stage.word_length, 'paths': n,
                          'inherited_image_rank': prior.rank(image),
                          'projector_sum_is_image_not_full_identity': stage is not root,
                          'spectral_coarse_summary_square': True})
        K_power = algebra.mm(ledger.continuation, K_power)

    # Spectral descriptors commute with the actual successive extension maps,
    # with no independent spectral phase advancement being inserted.
    for i, (parent, child) in enumerate(zip(stages, stages[1:])):
        for left, right in zip(all_modes[i], all_modes[i + 1]):
            E, Fp = ledger.inherited_projector(left), ledger.inherited_projector(right)
            assert tuple(algebra.mm(child.step_lift, part) for part in E) == tuple(
                algebra.mm(part, child.step_lift) for part in Fp)
    # Matrix-level compositional laws apply on arbitrary intermediate payloads,
    # not only on those copied from primitive inputs.
    for i in range(len(stages)):
        for j in range(i, len(stages)):
            for k in range(j, len(stages)):
                Lij, Dij = ledger.transition(stages[i], stages[j])
                Ljk, Djk = ledger.transition(stages[j], stages[k])
                Lik, Dik = ledger.transition(stages[i], stages[k])
                assert Lik == algebra.mm(Ljk, Lij)
                assert Dik == algebra.mm(Dij, Djk)
    intermediate = tuple(F(i + 1, 11) for i in range(10))
    extended = ledger.encode(stages[1], stages[3], intermediate)
    assert ledger.decode(stages[1], stages[3], extended) == intermediate
    rejects(lambda: ledger.decode(root, stages[1], intermediate))
    rejects(lambda: ledger.read_mode(all_modes[1][0], intermediate))
    rejects(lambda: ledger.read_mode(all_modes[3][0], extended))
    assert ledger.summarize(stages[1], intermediate) == apply(stages[1].summary, intermediate)

    # Explicit inherited zero sector survives on path records but not summary.
    for stage, modes in zip(stages[1:], all_modes[1:]):
        contrast = tuple(F(label == 'CA') - F(label == 'BA') for label in ledger.labels)
        payload = ledger.encode(root, stage, contrast)
        zero_mode = modes[-1]
        assert ledger.read_mode(zero_mode, payload) == (payload, (F(0),) * len(payload))
        assert payload != (F(0),) * len(payload)
        assert ledger.summarize(stage, payload) == (F(0),) * 6

    # Identity-bound authority: copied records and other-ledger lookalikes do
    # not count as this ledger's constructors or ancestors.
    foreign = RetainedSuccessorLedger(fixture['packets'], descriptors)
    sibling = ledger.successor(root)
    rejects(lambda: ledger.successor(replace(root)))
    rejects(lambda: ledger.successor(foreign.root))
    rejects(lambda: ledger.transition(sibling, stages[2]))
    rejects(lambda: ledger.transition(stages[2], root))
    rejects(lambda: ledger.family(root, 'unregistered-index'))
    rejects(lambda: ledger.inherit(root, 'invented-phase'))
    rejects(lambda: ledger.resolve_mode(foreign.inherit(foreign.root, 'phi')))
    rejects(lambda: ledger.encode(root, stages[1], (F(0),) * 5))
    rejects(lambda: ledger.encode(root, stages[1], (0.1,) * 6))
    rejects(lambda: RetainedSuccessorLedger(fixture['packets'], descriptors[:-1]))
    rejects(lambda: RetainedSuccessorLedger(fixture['packets'],
                                            (replace(descriptors[0], eigenvalue=(F(7), F(0))),) + descriptors[1:]))
    rejects(lambda: RetainedSuccessorLedger(fixture['packets'] + (fixture['packets'][0],)))
    sink = RetainedSuccessorLedger((('AB', 'A', 'B'),))
    rejects(lambda: sink.successor(sink.root))
    # A true parallel-ID registry remains lossless because the family interface
    # stores word IDs, unlike endpoint-profile aggregation.
    parallel = RetainedSuccessorLedger(fixture['packets'] + (('AB:second', 'A', 'B'),))
    parallel_next = parallel.successor(parallel.root)
    parallel_input = tuple(F(i == 0) - F(i == 6) for i in range(7))
    parallel_output = parallel.encode(parallel.root, parallel_next, parallel_input)
    assert parallel.decode(parallel.root, parallel_next, parallel_output) == parallel_input
    assert parallel_output != (F(0),) * len(parallel_output)
    for direction in ('source', 'target'):
        assert parallel.deconstruct_family(parallel.family(parallel_next, direction)) == parallel_next.paths

    report = {
        'status': 'passed',
        'interface': 'retained_path_successor.RetainedSuccessorLedger',
        'stages': summaries,
        'source_target_families_recover_ordered_words': True,
        'successive_transition_maps_and_decoders_compose': True,
        'arbitrary_intermediate_payloads_supported': True,
        'inherited_spectral_reads_restricted_to_origin_image': True,
        'inherited_spectral_intertwining_with_extension': True,
        'parallel_occurrence_provenance_preserved': True,
        'rejected_controls': ['forged stage/family/mode', 'cross-ledger stage/mode', 'non-ancestor transition',
                              'unknown index/mode', 'wrong dimension', 'inexact float payload',
                              'off-origin spectral payload', 'missing zero sector', 'wrong eigenvalue',
                              'duplicate primitive ID', 'sink with no retained extension'],
        'scope': 'finite registered rational coefficient interface; quadratic inherited descriptors; no physical dynamics or native higher-cell promotion',
        'spectral_boundary': 'sum inherited E = image projector, not ambient identity beyond the root',
    }
    dest = Path(__file__).resolve().parents[1] / 'results' / 'retained-path-successor-interface.json'
    dest.write_text(json.dumps(report, indent=2) + '\n', encoding='utf-8')
    print('PASS: registered successor stages, indexed family deconstruction, and compositional encode/decode.')
    print('PASS: inherited spectra intertwine with extension and reconstruct only the registered origin image.')
    print('PASS: hostile identity, scope, missing-mode, sink and parallel-occurrence controls.')
    print('Report: research/nima/results/retained-path-successor-interface.json')


if __name__ == '__main__':
    main()
