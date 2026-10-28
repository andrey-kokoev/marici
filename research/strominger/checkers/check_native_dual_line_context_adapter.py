"""Read-only exact adapter test in the existing native five-slot grammar.
The window-to-sector contrast binding remains an inherited candidate assumption.
No producer with top-level writes is imported.
"""
from pathlib import Path
from fractions import Fraction as F
from hashlib import sha256
import json
import re
import sys
from exact_multiradical import Radical as R, sqrt, mm, adj, identity, serialize

ROOT = Path(__file__).resolve().parents[3]
BASE = ROOT/'research/strominger/results'


def restore(a):
    return [[R({int(k): F(v) for k, v in x.items()}) for x in row] for row in a]


def permutation(p):
    return [[R(int(j == p[i])) for j in range(len(p))] for i in range(len(p))]


def minus(a, b):
    return [[x-y for x, y in zip(row, other)] for row, other in zip(a, b)]


def frame(z):
    a, b = z[0][0], z[1][0]
    return [[a, -b.conj()], [b, a.conj()]]


def det(a):
    return a[0][0]*a[1][1]-a[0][1]*a[1][0]


def run():
    paths = [ROOT/'research/nima/generative-phase-assembly.mjs',
             ROOT/'research/strominger/demos/particle-overlap-tetrahedron/phase-advance-model.mjs',
             BASE/'neutron-contrast-electron-transport/verification.json',
             BASE/'full-five-channel-candidate/verification.json',
             ROOT/'research/voevodsky/results/electron_tetrahedral_spinor_store.json']
    before = {p: sha256(p.read_bytes()).hexdigest() for p in paths}
    assembly, phase = [p.read_text() for p in paths[:2]]
    pne = json.loads(re.search(r'\bNE=(\[[^]]+\])', assembly)[1])
    pnn = json.loads(re.search(r'neutron:Object.freeze\((\[[^]]+\])\)', phase)[1])
    active = re.search(r'activePhaseSlots=([^;]+)', phase)[1]
    slots = {s: json.loads(re.search(s+r':(\[[^]]+\])', active)[1]) for s in ('neutron', 'electron')}
    NE, NN = permutation(pne), permutation(pnn)
    q = [[sqrt(F(1, 2)), sqrt(F(1, 6))], [-sqrt(F(1, 2)), sqrt(F(1, 6))], [R(), -sqrt(F(2, 3))]]
    def chart(indices):
        D = [[R() for _ in range(5)] for _ in range(2)]
        for j in range(2):
            for i, slot in enumerate(indices):
                D[j][slot] = q[i][j]
        outside = sorted(set(range(5))-set(indices))
        rows = [[R(int(i == outside[0])) for i in range(5)],
                [sqrt(F(1, 3)) if i in indices else R() for i in range(5)],
                [R(int(i == outside[1])) for i in range(5)]]
        T = D+rows
        assert mm(T, adj(T)) == mm(adj(T), T) == identity(5)
        return D, T
    DN, TN = chart(slots['neutron'])
    DE, TE = chart(slots['electron'])
    reflection = mm(mm(DE, NE), adj(DN))
    assert mm(DE, NE) == mm(reflection, DN)
    assert mm(adj(reflection), reflection) == identity(2)
    assert det(reflection) == -1
    ne_block = mm(mm(TE, NE), adj(TN))
    assert ne_block == [[reflection[i][j] if i < 2 and j < 2 else R(int(i == j and i >= 2)) for j in range(5)] for i in range(5)]

    candidate = json.loads(paths[2].read_text())
    full = json.loads(paths[3].read_text())
    K, EF, S = [restore(candidate[k]) for k in ('contrastFrame', 'electronFrame', 'NEcandidateMatrix')]
    assert reflection == restore(candidate['fiveCoefficientTest']['activeContrastReflection'])
    BN, Bout = [restore(full[k]) for k in ('neutronFiveEmbedding', 'postNEJointEmbedding')]
    store = json.loads(paths[4].read_text())
    def complex_value(v):
        return R(F(v[0][0]))+F(v[0][1])*sqrt(3)+F(v[1][0])*sqrt(-1)+F(v[1][1])*sqrt(-3)
    J = [[sqrt(F(1, 2))*complex_value(x) for x in row] for face in store['face_projectors'] for row in face]
    assert mm(adj(J), J) == identity(2)
    W = mm(adj(J), EF)
    assert mm(adj(W), W) == identity(2) and mm(J, W) == EF
    # The candidate raw electron output is exactly the original logical source
    # encoder applied to W DN, with no phase chosen to fix the determinant.
    assert mm(S, BN) == mm(EF, DN) == mm(J, mm(W, DN))
    assert mm(Bout[36:], NE) == mm(J, mm(W, DN))
    assert mm(mm(W, adj(reflection)), mm(DE, NE)) == mm(W, DN)

    nn_block = mm(mm(TN, NN), adj(TN))
    assert mm(adj(nn_block), nn_block) == identity(5)
    assert any(x != 0 for row in nn_block[:2] for x in row[2:])
    assert any(x != 0 for row in nn_block[2:] for x in row[:2])
    witness = [[R(int(i == 4))] for i in range(5)]
    assert mm(DN, witness) == [[R()], [R()]]
    outgoing = mm(DN, mm(NN, witness))
    assert mm(adj(outgoing), outgoing) == [[R(F(2, 3))]]
    # If A DN = DN NN existed, it would send this zero input to nonzero.
    carried_chart = mm(TN, adj(NN))
    assert mm(carried_chart, NN) == TN
    assert mm(mm(carried_chart, adj(NN)), mm(NN, NN)) == TN
    # Returning coefficient frames is not returning absolute native history.
    histories = [[], ['NN', 'NN']]
    assert histories[0] != histories[1]

    seeds = [[[R(int(i == j))] for i in range(5)] for j in range(5)]
    seeds += [[[R(i+1)+sqrt(-1)*R(5-i)] for i in range(5)]]
    for v in seeds:
        packet = mm(TN, v)
        assert mm(adj(TN), packet) == v
        assert mm(nn_block, packet) == mm(TN, mm(NN, v))
        assert mm(ne_block, packet) == mm(TE, mm(NE, v))
        assert mm(adj(packet), packet) == mm(adj(v), v)
        z = mm(DN, v)
        # U(2) reader correction is on the right of the paired frame.
        assert frame(mm(reflection, z)) == mm(mm(reflection, frame(z)), [[R(1), R()], [R(), det(reflection).conj()]])
        assert mm(mm(W, adj(reflection)), mm(DE, mm(NE, v))) == mm(W, z)
    assert all(sha256(p.read_bytes()).hexdigest() == before[p] for p in paths)
    evidence = {str(p.relative_to(ROOT)): digest for p, digest in before.items()}
    for p in [Path(__file__), Path(__file__).with_name('exact_multiradical.py'), ROOT/'research/strominger/native-dual-line-context-adapter-v1.md']:
        evidence[str(p.relative_to(ROOT))] = sha256(p.read_bytes()).hexdigest()
    return {'schema': 'native-dual-line.context-adapter.v1', 'constructionAdmitted': False,
            'signedPairBindingAdmitted': False, 'status': 'NE contrast adapter passes; fixed two-channel NN transport rejected; retained five-channel transport passes',
            'sourceActiveSlots': slots, 'NE': pne, 'NN': pnn,
            'NEcontrastReflection': serialize(reflection), 'reflectionDeterminant': det(reflection).record(),
            'NEpacketOperator': serialize(ne_block), 'NNpacketOperator': serialize(nn_block),
            'electronSourceAlignment': serialize(W), 'originalElectronEncoderIntertwines': True,
            'NNcounterexample': {'sourceFiveVector': serialize(witness), 'incomingContrast': serialize(mm(DN, witness)), 'outgoingContrast': serialize(outgoing), 'outgoingContrastNormSquared': '2/3'},
            'retainedChannels': {'contrast': 2, 'complement': 3}, 'matrixIdentitiesExact': True,
            'zeroContrastHasNoInventedHopfRay': True, 'sourceStoresUnchanged': True,
            'scope': 'Uses actual native five-slot permutations and the existing conditional window-to-sector/NE field binding. This does not identify the operator signed P/E pair with the five-slot packet, derive that geometric binding, admit inverse NE execution, or close global native overlaps/boundaries. The pair frame retains the extracted contrast, not all five coefficients.',
            'sourceHashes': evidence}


if __name__ == '__main__':
    report = run()
    if '--record' in sys.argv:
        path = BASE/'native-dual-line-context-adapter-v1/verification.json'
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(report, indent=2)+'\n')
    print(json.dumps({k: report[k] for k in ('status', 'constructionAdmitted', 'signedPairBindingAdmitted', 'retainedChannels', 'originalElectronEncoderIntertwines', 'sourceStoresUnchanged')}, indent=2))
