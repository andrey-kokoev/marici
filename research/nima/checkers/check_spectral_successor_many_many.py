"""Exact reconstruction audit replacing the earlier incorrect weight experiment.

Nine occurrence-pair coordinates form a tensor coefficient space. All nine
mode-pair projectors resolve it; three same-mode channels are a restriction.
Provenance is retained explicitly, never inferred from numerical coefficients.
No successor endpoints, native admission or physical interpretation are added.
"""
from dataclasses import dataclass, replace
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import json
import check_record4_spectral_promotion as sp

Z = (F(0), F(0))
ONE = (F(1), F(0))
MODES = tuple(sp.MODES)
KEYS = tuple(product(MODES, repeat=2))
N = 9
ZERO = tuple(tuple(Z for _ in range(N)) for _ in range(N))
IDENTITY = tuple(tuple(ONE if i == j else Z for j in range(N)) for i in range(N))


def kron(a, b):
    return tuple(tuple(sp.zmul(a[i][j], b[k][l])
                       for j in range(len(a[0])) for l in range(len(b[0])))
                 for i in range(len(a)) for k in range(len(b)))


def apply(matrix, vector):
    return tuple(row[0] for row in sp.zmm(matrix, tuple((v,) for v in vector)))


def vector_sum(vectors):
    out = (Z,) * N
    for vector in vectors:
        out = tuple(sp.zadd(x, y) for x, y in zip(out, vector))
    return out


def subtract(a, b):
    return tuple(sp.zadd(x, sp.zscale(y, -1)) for x, y in zip(a, b))


def norm2(vector):
    return sum((sp.znorm(z) for z in vector), F(0))


def matrix_sum(matrices):
    out = ZERO
    for matrix in matrices:
        out = sp.zmadd(out, matrix)
    return out


def reject(action):
    try:
        action()
    except ValueError:
        return
    raise AssertionError('Malformed retained decomposition was accepted')


@dataclass(frozen=True)
class Decomposition:
    # IDs point to complete registered spectral records, not just projectors.
    parent_modes: tuple
    pair_manifest: tuple
    components: tuple


def main():
    ledger = sp.SpectralLedger()
    words = (('AB', 'BC', 'CA'), ('BA', 'AD', 'DB'))
    roots = tuple(ledger.record4(tuple(sp.TwoPacket(e, e[0], e[1]) for e in word))
                  for word in words)
    ports = tuple(tuple(ledger.promote(root, mode) for mode in MODES) for root in roots)
    parent_ids = tuple(tuple(port.label for port in side) for side in ports)
    manifest = tuple(product(*words))
    projectors = {(left.mode, right.mode): kron(left.projector, right.projector)
                  for left in ports[0] for right in ports[1]}

    # Exact matrix identities establish all-input linear reconstruction.
    assert matrix_sum(projectors.values()) == IDENTITY
    for key, projector in projectors.items():
        assert sp.dagger(projector) == projector
        assert sp.zmm(projector, projector) == projector
        assert sp.ztrace(projector) == ONE
        for other, other_projector in projectors.items():
            if key != other:
                assert sp.zmm(projector, other_projector) == ZERO

    same = matrix_sum(projectors[key] for key in KEYS if key[0] == key[1])
    residual = matrix_sum(projectors[key] for key in KEYS if key[0] != key[1])
    for projector, rank in ((same, 3), (residual, 6)):
        assert sp.zmm(projector, projector) == projector
        assert sp.dagger(projector) == projector
        assert sp.ztrace(projector) == (F(rank), F(0))
    assert sp.zmm(same, residual) == ZERO
    assert sp.zmadd(same, residual) == IDENTITY

    def encode(vector):
        return Decomposition(parent_ids, manifest,
                             tuple((key, apply(projectors[key], vector)) for key in KEYS))

    def decode(packet):
        # Decoder scoped to this fixed, ordered pair of retained root families.
        if packet.parent_modes != parent_ids:
            raise ValueError('Unbound or reordered spectral parents')
        recovered = []
        for side in packet.parent_modes:
            side_words = []
            for mode, label in zip(MODES, side):
                identity = ledger.identities[label]
                if identity.mode != mode:
                    raise ValueError('Mode-parent mismatch')
                side_words.append(tuple(p.label for p in ledger.deconstruct(identity)))
            if len(set(side_words)) != 1:
                raise ValueError('Mode family lost its common root history')
            recovered.append(side_words[0])
        if packet.pair_manifest != tuple(product(*recovered)):
            raise ValueError('Missing, reordered or forged occurrence-pair provenance')
        if tuple(key for key, _ in packet.components) != KEYS:
            raise ValueError('Incomplete or reordered spectral component family')
        for key, vector in packet.components:
            if len(vector) != N or apply(projectors[key], vector) != vector:
                raise ValueError('Component is not in its declared spectral image')
        return vector_sum(vector for _, vector in packet.components), packet.pair_manifest

    energies = []
    for i in range(N):
        basis = tuple(ONE if j == i else Z for j in range(N))
        packet = encode(basis)
        recovered, provenance = decode(packet)
        assert recovered == basis and provenance == manifest
        channel_norms = tuple(norm2(v) for _, v in packet.components)
        assert channel_norms == (F(1, 9),) * N
        assert sum(channel_norms) == norm2(basis) == 1
        selected, omitted = apply(same, basis), apply(residual, basis)
        assert selected != basis
        assert norm2(selected) == F(1, 3)
        assert norm2(omitted) == F(2, 3)
        assert vector_sum((selected, omitted)) == basis
        assert subtract(basis, selected) == omitted
        energies.append({'pair': manifest[i], 'each_mode_pair_norm2': '1/9',
                         'same_mode_norm2': '1/3', 'residual_norm2': '2/3'})

    # Single-occurrence weights use |a+i*sqrt(3)*b|^2=a^2+3*b^2,
    # not sums of absolute real parts (the old calculation was incorrect).
    for side in ports:
        for port in side:
            for i in range(3):
                basis3 = tuple(ONE if j == i else Z for j in range(3))
                assert norm2(apply(port.projector, basis3)) == F(1, 3)

    # Strong hostile: an entire nonzero cross-mode state is invisible to same-mode reading.
    basis0 = (ONE,) + (Z,) * (N - 1)
    hidden = apply(projectors['positive', 'common'], basis0)
    assert norm2(hidden) == F(1, 9)
    assert apply(same, hidden) == (Z,) * N
    assert apply(residual, hidden) == hidden
    assert decode(encode(hidden))[0] == hidden
    # Conversely the three-channel representation is complete ON its admitted image.
    visible = apply(same, basis0)
    assert apply(same, visible) == visible
    assert apply(residual, visible) == (Z,) * N

    # Exact complex linear-combination regression in addition to basis identities.
    mixed = tuple((F(i - 4, 7), F(i % 3 - 1, 5)) for i in range(N))
    assert decode(encode(mixed))[0] == mixed
    assert sum(norm2(v) for _, v in encode(mixed).components) == norm2(mixed)
    assert norm2(apply(same, mixed)) + norm2(apply(residual, mixed)) == norm2(mixed)

    # Intensities alone are not a reversible change of representation.
    minus_basis = tuple(sp.zscale(v, -1) for v in basis0)
    a, b = encode(basis0), encode(minus_basis)
    assert a.components != b.components
    assert tuple(norm2(v) for _, v in a.components) == tuple(norm2(v) for _, v in b.components)
    # Even two distinct labelled coordinate states share these nine intensities.
    basis1 = (Z, ONE) + (Z,) * (N - 2)
    assert tuple(norm2(v) for _, v in a.components) == tuple(norm2(v) for _, v in encode(basis1).components)

    reject(lambda: decode(replace(a, components=a.components[:-1])))
    reject(lambda: decode(replace(a, pair_manifest=tuple(reversed(manifest)))))
    reject(lambda: decode(replace(a, parent_modes=())))
    reject(lambda: decode(replace(a, components=tuple((key, basis0) for key in KEYS))))

    # Same projector but fresh identity/root: provenance cannot be recovered from numbers.
    repeat_root = ledger.record4(tuple(sp.TwoPacket(e + ':repeat', e[0], e[1]) for e in words[0]))
    repeat = ledger.promote(repeat_root, 'positive')
    original = ports[0][MODES.index('positive')]
    assert repeat.projector == original.projector
    assert repeat.window != original.window and repeat.label != original.label

    report = {
        'status': 'passed',
        'scope': 'Declared complex occurrence-pair coefficient representation; not native successor admission',
        'coefficient_dimension': 9,
        'full_mode_pair_channels': 9,
        'full_reconstruction': True,
        'same_mode_rank': 3,
        'omitted_cross_mode_rank': 6,
        'basis_checks': energies,
        'checks': ['Hermitian orthogonal projector resolution', 'exact complex reconstruction',
                   'Hermitian norm preservation', 'same-mode plus residual recovery',
                   'nonzero cross-mode hostile annihilated by same-mode reading',
                   'intensity-only ambiguity', 'complete ledger parent/window recovery',
                   'missing-channel, wrong-image and provenance rejection'],
        'bookkeeping': {'same_mode_by_occurrence_pairs': 27,
                        'full_mode_pairs_by_occurrence_pairs': 81,
                        'independent_dimensions': 9},
        'corrections': ['Old 3/7,2/7,2/7 single-mode weights were invalid',
                        'Old common-versus-complex pair weight disparity was invalid',
                        '27 membership slots are not 27 independent amplitudes',
                        'Same-mode components do not reconstruct unrestricted pair states',
                        'Source/target A->A and next-level admission were not established'],
    }
    destination = Path(__file__).resolve().parents[1] / 'results' / 'spectral-successor-reconstruction.json'
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(json.dumps(report, indent=2) + '\n', encoding='utf-8')
    print('PASS: all 9 spectral channels reconstruct the 9-dimensional pair coefficient space.')
    print('PASS: same-mode rank 3; omitted rank 6; each basis keeps 1/3 and loses 2/3 squared norm.')
    print('PASS: residual restores state; retained windows restore provenance; intensities alone do neither.')
    print('BOUNDARY: 27/81 association slots are bookkeeping, not new dimensions or admitted successors.')
    print('Report: research/nima/results/spectral-successor-reconstruction.json')


if __name__ == '__main__':
    main()
