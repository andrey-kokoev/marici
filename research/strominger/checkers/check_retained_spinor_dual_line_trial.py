"""Exact read-only reuse of the retained spinor source; no spatial ray assignment.
No producer main() is called and no other-owner store is written.
The complementary column is derived from z, not a new independent partner.
"""
from pathlib import Path
import sys
import json
from hashlib import sha256
from fractions import Fraction as F
from itertools import product, combinations

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / 'research/voevodsky/checkers'))
import check_spinor_potential_link_bridge as source
from check_electron_tetrahedral_spinor import D, G0, G1, adj, ident, sm, trace, pos


def complement(z):
    return (source.neg(source.gc(z[1])), source.gc(z[0]))


def frame(z):
    if source.norm(z) == 0:
        raise ValueError('Zero state has no phase frame')
    w = complement(z)
    return tuple((z[i], w[i]) for i in range(2))


def determinant(a):
    return source.ga(source.gm(a[0][0], a[1][1]), source.neg(source.gm(a[0][1], a[1][0])))


def diagonal(a, b):
    return ((a, G0), (G0, b))


def run():
    contract_path = ROOT / 'research/voevodsky/inputs/spinor-potential-link-bridge-v1.json'
    contract = json.loads(contract_path.read_text())
    paths = [contract_path, *(ROOT / contract[k] for k in ('electron', 'potential', 'proton'))]
    before = {str(p.relative_to(ROOT)): sha256(p.read_bytes()).hexdigest() for p in paths}
    electron = json.loads((ROOT / contract['electron']).read_text())
    potential = json.loads((ROOT / contract['potential']).read_text())
    source.verify_atlas(potential)
    p0, normal, recovery = source.parameters(potential['source'])
    p = tuple(tuple((D(a), D(0, b)) for a, b in row) for row in p0)
    projectors = tuple(tuple(tuple(source.decode(x) for x in row) for row in face) for face in electron['face_projectors'])
    encoder = tuple(row for face in projectors for row in face)
    ell = encoder[0]
    assert source.gmm(adj(encoder), encoder) == sm(2, ident(2))
    stages = {s: [[G0]*8 for _ in range(8)] for s in 'LGN'}
    for arrow in electron['arrows']:
        stages[arrow['stage']][arrow['target']][arrow['source']] = source.decode(arrow['weight'])
    for stage in stages.values():
        assert source.gmm(stage, encoder) == encoder

    dark = (source.neg(ell[1]), ell[0])
    hosts = [(D(F(1, 3)),)*3, (D(F(1, 2)), D(F(1, 4)), D(F(1, 4)))]
    phases = [G1, (D(), D(1)), (D(-1), D()), (D(F(3, 5)), D(F(4, 5)))]
    seeds = [(G1, (D(F(k, 2)), D(F(l, 2)))) for k in range(-2, 3) for l in range(-2, 3)]
    seeds += [(G0, G1), dark, tuple(source.gm(phases[1], x) for x in dark)]
    records_checked = phase_checks = 0
    for z in seeds:
        n = source.norm(z)
        U = frame(z)
        # Exact unnormalized frame: U/sqrt(n) is SU(2). No extra sqrt field.
        assert source.gmm(adj(U), U) == sm(n, ident(2))
        assert determinant(U) == (n, D())
        assert complement(complement(z)) == tuple(source.neg(x) for x in z)
        records = []
        for host in hosts:
            record = source.construct(z, host, ell, p)
            recovered = source.reconstruct(record, ell, p)
            recovered_mode, _ = source.reconstruct_from_mode(record, ell, p, normal, recovery)
            assert recovered == recovered_mode == z
            assert frame(recovered) == U
            assert source.reconstruct(source.unser(json.loads(json.dumps(source.ser(record)))), ell, p) == z
            records.append(record)
            records_checked += 1
        for field in ('potential', 'mode', 'norm_squared', 'link', 'dark_phase_witness'):
            assert records[0][field] == records[1][field]
        for g in phases:
            changed = tuple(source.gm(g, x) for x in z)
            assert frame(changed) == source.gmm(U, diagonal(g, source.gc(g)))
            assert determinant(diagonal(g, source.gc(g))) == G1
            phase_checks += 1

    dark_record = source.construct(dark, hosts[0], ell, p)
    assert dark_record['link'] == G0
    assert source.rejects(lambda: source.reconstruct(dict(dark_record, dark_phase_witness=None), ell, p))
    rotated_dark = source.construct(tuple(source.gm(phases[1], x) for x in dark), hosts[0], ell, p)
    assert dark_record['potential'] == rotated_dark['potential']
    assert dark_record['dark_phase_witness'] != rotated_dark['dark_phase_witness']
    assert source.rejects(lambda: frame((G0, G0)))
    # Common spinor phase -1 is not discarded by the paired frame.
    assert frame(tuple(source.neg(x) for x in dark)) != frame(dark)

    quaternions = set()
    for k in range(4):
        for sign in (-1, 1):
            quaternions.add(tuple(F(sign if i == k else 0) for i in range(4)))
    quaternions.update(tuple(F(sign, 2) for sign in signs) for signs in product((-1, 1), repeat=4))
    equivariance_checks = 0
    for q in quaternions:
        action = source.spin(q)
        for z in seeds:
            assert frame(source.act(action, z)) == source.gmm(action, frame(z))
            equivariance_checks += 1

    # Actual stored tetrahedral projectors, not spatial cell-centre rays.
    I = ident(2)
    duals = tuple(tuple(tuple(source.ga(I[i][j], source.neg(P[i][j])) for j in range(2)) for i in range(2)) for P in projectors)
    for P, Q in zip(projectors, duals):
        assert source.gmm(Q, Q) == Q and adj(Q) == Q and trace(Q) == G1
        assert source.gmm(P, Q) == sm(0, I)
    loops = []
    for indices in combinations(range(4), 3):
        i, j, k = indices
        B = trace(source.gmm(source.gmm(projectors[i], projectors[j]), projectors[k]))
        C = trace(source.gmm(source.gmm(duals[i], duals[j]), duals[k]))
        assert C == source.gc(B)
        assert B[0] == 0 and B[1] != 0  # exact source tetrahedron: phases +/-i
        phase = (D(), D(1 if pos(B[1]) else -1))
        holonomy = diagonal(phase, source.gc(phase))
        assert determinant(holonomy) == G1
        assert holonomy != I and trace(holonomy) == G0
        assert determinant(diagonal(phase, phase)) != G1
        loops.append({'face': list(indices), 'line_bargmann': source.encode(B), 'dual_bargmann': source.encode(C), 'line_phase': source.encode(phase), 'determinant': source.encode(determinant(holonomy)), 'matrix_is_identity': False})

    after = {str(p.relative_to(ROOT)): sha256(p.read_bytes()).hexdigest() for p in paths}
    assert before == after
    # Pin imported implementation evidence as well as the retained stores.
    files = [Path(__file__), ROOT/'research/strominger/retained-spinor-dual-line-trial-v1.md']
    for module in list(sys.modules.values()):
        filename = getattr(module, '__file__', None)
        if filename:
            path = Path(filename).resolve()
            if path.parent == ROOT/'research/voevodsky/checkers' and path.suffix == '.py':
                files.append(path)
    evidence = dict(before)
    evidence.update({str(p.relative_to(ROOT)): sha256(p.read_bytes()).hexdigest() for p in sorted(set(files))})
    return {'schema': 'retained-spinor.dual-line-trial.v1', 'constructionAdmitted': False,
            'nativePENBindingAdmitted': False, 'status': 'exact retained-electron-source frame test passed',
            'sourceSeeds': len(seeds), 'retainedRecordRoundTrips': records_checked,
            'phaseFrameChecks': phase_checks, 'binaryActions': len(quaternions),
            'equivarianceChecks': equivariance_checks, 'sourceFaceLoops': loops,
            'darkPhaseRetained': True, 'hostIndependentInternalState': True,
            'sourceStoresUnchanged': True, 'newIndependentPartnerAdded': False,
            'scope': 'Complement Jz is derived from one existing logical spinor. This does not encode independent P and E inputs, extend a rank-one baryon source, bind N adjacent-face readers, or prove the octahedral boundary law. Zero determinant winding retains nontrivial two-channel holonomy.',
            'sourceHashes': evidence}


if __name__ == '__main__':
    report = run()
    if '--record' in sys.argv:
        out = ROOT/'research/strominger/results/retained-spinor-dual-line-trial-v1/verification.json'
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(json.dumps(report, indent=2)+'\n')
    print(json.dumps({k: v for k, v in report.items() if k not in ('sourceHashes', 'sourceFaceLoops')}, indent=2))
