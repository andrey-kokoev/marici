"""Concrete candidate Berry cut of the existing marked table-fibration tower.
Reads the owner's stored coefficients without rewriting or rerunning its producer.
"""
from pathlib import Path
from itertools import combinations, product
import hashlib
import json
import sympy as s

ROOT = Path(__file__).resolve().parents[3]
STORE = 'research/voevodsky/results/electron_tetrahedral_spinor_store.json'


def decode(z):
    real, imag = z
    def d(v):
        return s.Rational(v[0]) + s.sqrt(3)*s.Rational(v[1])
    return s.simplify(d(real) + s.I*d(imag))


def canonical(rows):
    return tuple(sorted(rows, key=lambda r: (r[1], r[2])))


def fibrate(rows, selector, domain):
    # label/from/to columns; retain empty fibers and the selector.
    rest = [k for k in range(3) if k != selector]
    return (selector, tuple((key, tuple(tuple(r[k] for k in rest) for r in rows if r[selector] == key)) for key in domain))


def restore(marked):
    selector, fibers = marked
    rest = [k for k in range(3) if k != selector]
    rows = []
    for key, children in fibers:
        for child in children:
            r = [None]*3
            r[selector] = key
            for k, value in zip(rest, child):
                r[k] = value
            rows.append(tuple(r))
    return canonical(rows)


def cut(grouped, vertices):
    # Source-index cut: union of the requested projector fibers, with IDs retained.
    selector, fibers = grouped
    if selector != 1:
        raise ValueError('Expected projector-index grouping')
    return canonical((coefficient, i, entry) for i, children in fibers if i in vertices for coefficient, entry in children)


def read_face(rows, face):
    # Independent table contraction, not matrix decoding followed by old readout.
    entries = {(i, ab): value for value, i, ab in rows}
    i, j, k = face
    if any((v, (a, b)) not in entries for v in face for a, b in product(range(2), repeat=2)):
        raise ValueError('Incomplete face projector')
    return s.simplify(sum(entries[i, (a,b)]*entries[j, (b,c)]*entries[k, (c,a)] for a,b,c in product(range(2), repeat=3)))


def phase(b):
    if b == 0:
        raise ValueError('Undefined overlap phase')
    return s.simplify(b/s.sqrt(s.simplify(b*s.conjugate(b))))


def main():
    stored = json.loads((ROOT/STORE).read_text(encoding='utf-8-sig'))
    P = [s.Matrix([[decode(z) for z in row] for row in p]) for p in stored['face_projectors']]
    sigma = [s.Matrix([[0,1],[1,0]]), s.Matrix([[0,-s.I],[s.I,0]]), s.diag(1,-1)]
    signs = [(1,1,-1),(1,-1,1),(-1,1,1),(-1,-1,-1)]
    for p, sign in zip(P, signs):
        expected = (s.eye(2)-sum((sign[k]*sigma[k]/s.sqrt(3) for k in range(3)), s.zeros(2)))/2
        assert (p-expected).applyfunc(s.simplify) == s.zeros(2)
    q = canonical((P[i][a,b], i, (a,b)) for i in range(4) for a,b in product(range(2), repeat=2))
    assert len(q) == len({(i,ab) for _,i,ab in q}) == 16
    domains = [tuple(dict.fromkeys(r[0] for r in q)), tuple(range(4)), tuple(product(range(2), repeat=2))]
    # Actual marked fibrate/restore operations at every column.
    for selector, domain in enumerate(domains):
        assert restore(fibrate(q, selector, domain)) == q
    grouped = fibrate(q, 1, domains[1])
    q2 = canonical((value, ab, i) for i, children in grouped[1] for value, ab in children)
    grouped2 = fibrate(q2, 1, domains[2])
    q4 = canonical((value, i, ab) for ab, children in grouped2[1] for value, i in children)
    assert q4 == q
    faces, records = {}, []
    for face in combinations(range(4), 3):
        rows = cut(grouped, face)
        complement = cut(grouped, set(range(4))-set(face))
        assert len(rows) == 12 and len(complement) == 4
        assert canonical(rows+complement) == q
        matrix_b = s.simplify(s.trace(P[face[0]]*P[face[1]]*P[face[2]]))
        native_b = read_face(rows, face)
        assert s.simplify(native_b-matrix_b) == 0
        for selector, domain in enumerate(domains):
            assert restore(fibrate(rows, selector, domain)) == rows
            assert s.simplify(read_face(restore(fibrate(rows, selector, domain)), face)-native_b) == 0
        assert read_face(cut(fibrate(q4, 1, domains[1]), face), face) == native_b
        key = ''.join(map(str, face))
        faces[key] = phase(native_b)
        records.append({'face': list(face), 'selected_rows': 12, 'complement_rows': 4, 'bargmann': str(native_b), 'phase': str(faces[key])})
    assert s.simplify(faces['123']/faces['023']*faces['013']/faces['012']) == 1
    # Full complex coefficients matter: conjugate sources have the same entry
    # magnitudes and pair overlaps but opposite face phases.
    conjugated = canonical((s.conjugate(v),i,ab) for v,i,ab in q)
    assert all(s.simplify(v*s.conjugate(v)-w*s.conjugate(w)) == 0 for (v,i,ab),(w,j,cd) in zip(q,conjugated))
    assert phase(read_face(q,(0,1,2))) != phase(read_face(conjugated,(0,1,2)))
    # Transposing matrix-entry ports without the required orientation metadata
    # is not an innocent readout change: it conjugates the Berry loop.
    wrong = canonical((v,i,(b,a)) for v,i,(a,b) in q)
    assert phase(read_face(wrong,(0,1,2))) == -faces['012']
    incomplete = cut(grouped, (0,1,2))[1:]
    try:
        read_face(incomplete, (0,1,2))
    except ValueError:
        pass
    else:
        raise AssertionError('Missing coefficient accepted')
    sources = [STORE, 'research/nima/agda/TableFibrationCycle.agda', 'research/nima/native-table-equivalence.md', str(Path(__file__).relative_to(ROOT)).replace('\\','/')]
    result = {
        'status': 'pass', 'source': STORE,
        'binding': 'Candidate cut at group-from of the actual coefficient table; selected triple of source-index fibers.',
        'source_rows': len(q), 'faces': records,
        'marked_column_roundtrips': 3, 'face_column_roundtrips': 12,
        'four_step_recovery': True, 'independent_row_readout_commutes': True,
        'geometry': 'Bloch normals recovered as -Tr(P_i sigma); equals the existing regular tetrahedral source.',
        'hostiles': ['complex-conjugate source has same coefficient magnitudes but opposite Berry phases', 'matrix-entry transpose reverses phase', 'missing coefficient rejected'],
        'boundary': 'Finite four-line geodesic domain. Source coefficients, Pauli structure and face query are supplied; no arbitrary continuum Berry domain or uniquely selected cut claimed.',
        'sha256': {p: hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in sources},
    }
    # Explicit geometry recovery, rather than merely matching four vertices.
    for i,p in enumerate(P):
        assert all(s.simplify(-s.trace(p*sigma[k])-signs[i][k]/s.sqrt(3)) == 0 for k in range(3))
    output = ROOT/'research/strominger/results/berry-fibration-cut/verification.json'
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))


if __name__ == '__main__':
    main()
