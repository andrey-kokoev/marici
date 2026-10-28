"""Bounded exact port/seed test; owner sources are read-only, no phase refitting."""
from pathlib import Path
from fractions import Fraction as F
from itertools import permutations
import hashlib
import json
import sys

ROOT = Path(__file__).resolve().parents[3]
for folder in ['research/voevodsky/checkers', 'research/strominger/checkers']:
    sys.path.insert(0, str(ROOT / folder))
from check_belt_local_field_lift import inner, mat, inv2, inv
from check_opposite_branch_canonical import (
    decode, conj, mul, norm, compose, identity, apply, Z, dump)
from exact_multiradical import Radical as MR, mm, adj, serialize

pins = {}
def load(path):
    raw = (ROOT / path).read_bytes()
    pins[path] = hashlib.sha256(raw).hexdigest()
    return json.loads(raw)

def restore(matrix):
    return [[MR({int(k): F(v) for k, v in x.items()}) for x in row] for row in matrix]

def radical(z):
    a, b = z
    return MR({1: a.a, 3: a.b, -1: b.a, -3: b.b})

def main():
    load('research/voevodsky/contracts/ramsey-based-port-readout-attempt.v1.json')
    reader = load('research/strominger/results/neutron-reader-field-interface/verification.json')
    seed = load('research/strominger/results/full-five-channel-candidate/verification.json')
    local = load('research/strominger/results/belt-local-field-lift/verification.json')
    native = load('research/voevodsky/results/belt_three_by_twelve_store.json')
    ambient = load('research/voevodsky/results/coupled_six_piece_belt_store.json')['record']
    protocol = load('research/strominger/results/common-three-carrier-protocol/neutron.json')
    seam = load('research/strominger/results/T-seam-transition/verification.json')
    # Check recorded direct inputs, not a transitive scientific replay.
    for report in [reader, seed, local]:
        for path, digest in report.get('sourceHashes', report.get('source_hashes', {})).items():
            actual = hashlib.sha256((ROOT / path).read_bytes()).hexdigest()
            assert actual == digest, path
            pins[path] = actual
    incoming, outgoing, Q = seam['incomingReference'], seam['outgoingReference'], seam['basisMap']
    assert Q == [4, 3, 2, 1, 0]
    occurrence = {'C0': 'M2', 'M0': 'C2', 'C1': 'M1', 'M1': 'C1', 'C2': 'M0', 'M2': 'C0'}
    assert [incoming.index(occurrence[x]) for x in outgoing] == Q
    marks = {'b': 'M0', 'u': 'C1', 'v': 'M1', 'c': 'C2'}
    invmarks = {v: k for k, v in marks.items()}
    T = {k: invmarks[occurrence[v]] for k, v in marks.items()}
    assert T == {'b': 'c', 'u': 'v', 'v': 'u', 'c': 'b'}
    patches = reader['charts'][0]['readerPatches']
    def transform(p):
        return ['F_' + ''.join(sorted(T[x] for x in p[0][2:])), T[p[1]], T[p[2]]]
    patch_map = [patches.index(transform(p)) for p in patches]
    assert patch_map == [3, 4, 5, 0, 1, 2]
    charts = [c['vertexMap'] for c in reader['charts']]
    sector_rows = []
    for sigma in permutations(range(3)):
        proposals = {}
        for s, chart in enumerate(charts):
            target_inverse = {v: k for k, v in charts[sigma[s]].items()}
            for vertex, mark in chart.items():
                proposals.setdefault(vertex, set()).add(target_inverse[T[mark]])
        consistent = all(len(values) == 1 for values in proposals.values())
        sector_rows.append({'sectorMap': list(sigma), 'consistentOnSharedVertices': consistent,
                            'vertexImages': {k: sorted(v) for k, v in proposals.items()}})
    # This selection tests the prior numerical seed ansatz; it is NOT an
    # independent source derivation of window-to-sector identification.
    sigma = [Q[1+s]-1 for s in range(3)]
    assert sigma == [2, 1, 0]
    selected = next(r for r in sector_rows if r['sectorMap'] == sigma)
    assert selected['consistentOnSharedVertices']
    assert sum(r['consistentOnSharedVertices'] for r in sector_rows) == 3
    order = native['triangle_order']
    coords = native['coordinates']
    d = [F(c['d']) for c in coords]
    z = [decode(c['selected_numerator']) for c in coords]
    metric = list(map(F, protocol['source']['metric']))
    assert metric == [1/x for x in d], 'coordinate metric mismatch'
    # Confirm the chart slot-to-native triangle binding rather than using
    # equal dimensions as identification.
    for s, chart in enumerate(charts):
        for p in range(6):
            centroid, a, b = ambient['triangles'][order[6*s+p]]
            mapped = ['F_' + ''.join(sorted(chart[x] for x in centroid[2:].split('_'))), chart[a], chart[b]]
            assert mapped == patches[p]
    route_ports = set(local['metric_port_loop'])
    U = [[MR() for _ in range(36)] for _ in range(36)]
    backward = [[MR() for _ in range(36)] for _ in range(36)]
    rows = []
    def port(a, b):
        wa, wb = z[2*a:2*a+2], z[2*b:2*b+2]
        da, db = d[2*a:2*a+2], d[2*b:2*b+2]
        ca, cb = inner(wa, tuple(map(conj, wa)), da), inner(wb, tuple(map(conj, wb)), db)
        na, nb = inner(wa, wa, da), inner(wb, wb, db)
        equal_norm = na == nb
        equal_shape = norm(ca) * norm(nb) == norm(cb) * norm(na)
        if not (equal_norm and equal_shape):
            return None, equal_norm, equal_shape
        q = mul(ca, inv(cb))
        assert norm(q) == 1
        B = compose(mat((wb, tuple(mul(q, conj(x)) for x in wb))), inv2(mat((wa, tuple(map(conj, wa))))))
        assert apply(B, wa, 2) == tuple(wb)
        dense = [[radical(B.get((i,j), Z)) for j in range(2)] for i in range(2)]
        sharp = [[dense[j][i].conj() * (da[i]/db[j]) for j in range(2)] for i in range(2)]
        assert mm(sharp, dense) == [[MR(int(i == j)) for j in range(2)] for i in range(2)]
        return B, equal_norm, equal_shape
    for s in range(3):
        for p in range(6):
            a, b = 6*s+p, 6*sigma[s]+patch_map[p]
            B, equal_norm, equal_shape = port(a,b)
            row = {'sourceSector': s, 'targetSector': sigma[s], 'sourcePatch': p, 'targetPatch': patch_map[p],
                   'sourceTriangle': order[a], 'targetTriangle': order[b],
                   'bothInExistingTwelvePortRoute': order[a] in route_ports and order[b] in route_ports,
                   'equalModeNorm': equal_norm, 'equalGramShape': equal_shape}
            if B is not None:
                Back, _, _ = port(b,a)
                assert compose(Back, B) == identity(2)
                row['independentlyBasedInversePasses'] = True
                row['map'] = dump(B)
                for (i,j), value in B.items(): U[2*b+i][2*a+j] = radical(value)
                for (i,j), value in Back.items(): backward[2*a+i][2*b+j] = radical(value)
            rows.append(row)
    all_planes = all(r.get('independentlyBasedInversePasses') for r in rows)
    binding = restore(seed['neutronFiveEmbedding'])
    result = {'schema': 'marici.ramsey-based-port-readout-test.v1', 'node': 'T-seam-based-port-readout-binding',
              'checkerStatus': 'passed', 'scientificStatus': 'open', 'readerInvolution': T, 'patchMap': patch_map,
              'sectorCandidates': sector_rows, 'QSelectedSectorMap': sigma, 'selectedSectorMapIsGeometricallyConsistent': selected['consistentOnSharedVertices'],
              'planeTests': rows, 'allRequiredPlaneMapsPass': all_planes,
              'extraPairsOutsidePriorTwelvePortRoute': sum(not r['bothInExistingTwelvePortRoute'] for r in rows),
              'interpretation': 'The prior pointed Gram formula is evaluated on the required pairs without phase refitting. Extra pairs are a fresh finite extension test, not prior route admission.'}
    if all_planes:
        eye = [[MR(int(i==j)) for j in range(36)] for i in range(36)]
        assert mm(backward, U) == eye
        sharp = [[U[j][i].conj() * (metric[j]/metric[i]) for j in range(36)] for i in range(36)]
        assert mm(sharp, U) == eye and sharp == backward
        # This port-exchange map differs from the opposite-branch converter;
        # compute its square rather than importing the latter's noninvolution.
        result['portExchangeSquaredIdentity'] = mm(U,U) == eye
        image, expected = mm(U, binding), [[row[i] for i in Q] for row in binding]
        differences = [{'fieldCoordinate': i, 'coefficientSlot': j, 'residual': (image[i][j]-expected[i][j]).record()}
                       for i in range(36) for j in range(5) if image[i][j] != expected[i][j]]
        result.update(fullFieldBasedInversePasses=True, numericFiveColumnSquarePasses=not differences,
                      numericColumnPasses=[all(image[i][j]==expected[i][j] for i in range(36)) for j in range(5)],
                      fiveColumnResiduals=differences, fullFieldMap=serialize(U))
        Pi = [[MR(int(j==Q[i])) for j in range(5)] for i in range(5)]
        assert mm(binding, Pi) == expected
        R = [[binding[j][i].conj()*metric[j] for j in range(36)] for i in range(5)]
        assert mm(R,binding) == [[MR(int(i==j)) for j in range(5)] for i in range(5)]
        readout_square = mm(R,U) == mm(Pi,R)
        assert readout_square == (not differences)
        result['full36ReadoutSquarePasses'] = readout_square
        # Negative controls separate inverse/norm success from the Q/readout task.
        assert binding != expected, 'identity incorrectly realizes Q on the seed'
        assert mm(R,U) != R, 'unchanged readout incorrectly realizes Q'
        erased = [row[:] for row in U]
        erased[0] = [MR() for _ in range(36)]
        assert mm(backward, erased) != eye, 'complement erasure accepted'
        bad_port, _, shape = port(0,1)
        assert bad_port is None and not shape, 'unequal-Gram plane accepted'
        result['negativeControls'] = ['identity field map fails seed Q square',
            'unchanged readout fails full-field square', 'coordinate erasure fails inverse',
            'unequal-Gram port pair rejected', 'literal outgoing basis fails native named reader']
    # Separate the actual native labels from a numerical outgoing-basis cast.
    native_active = [1,2,3]
    required = [incoming[i] for i in native_active]
    literal = [outgoing[i] for i in native_active]
    assert required == ['M0','C1','M1'] and literal == ['C1','M1','C2'] and required != literal
    result['namedReadout'] = {'nativeRequiredMarks': required, 'literalOutgoingMarksAtNativeSlots': literal,
                             'sameTypedReader': False, 'outgoingBasisAdapterSupplied': False}
    result['scientificStatus'] = 'numeric_field_lift_passes_typed_binding_open' if all_planes and not differences else 'blocked_for_tested_adapter'
    result['stopReason'] = ('Required plane Gram/norm compatibility fails' if not all_planes else
                            'Prior pointed port maps fail the fixed five-column Q square; no phase refit performed' if differences else
                            'Numeric square passes but no source-supplied native/outgoing named-readout adapter')
    result['scope'] = 'Finite fixed-seed/fixed-pointed-map test. The sector permutation is selected by the prior seed/Q ansatz, not independently source-selected. This uses Gram port transport, not the opposite-branch converter or its16-coordinate bank. Numeric full-field recovery does not identify incoming/outgoing reference labels. Not a no-go for a future typed adapter or a native-admission result. No PN/NE extension attempted.'
    # Bind local code and imported research modules as well as recorded inputs.
    for module in list(sys.modules.values()):
        filename = getattr(module, '__file__', None)
        if filename:
            p = Path(filename).resolve()
            if p.is_file() and p.is_relative_to(ROOT / 'research'):
                pins[p.relative_to(ROOT).as_posix()] = hashlib.sha256(p.read_bytes()).hexdigest()
    result['source_sha256'] = pins
    path = ROOT / 'research/voevodsky/results/ramsey-based-port-readout-v1.json'
    path.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({k: result[k] for k in ['checkerStatus','scientificStatus','patchMap','allRequiredPlaneMapsPass','extraPairsOutsidePriorTwelvePortRoute','stopReason']}))
    if all_planes: print(json.dumps({'numericColumnPasses': result['numericColumnPasses'], 'residualEntries': len(differences)}))

if __name__ == '__main__': main()
