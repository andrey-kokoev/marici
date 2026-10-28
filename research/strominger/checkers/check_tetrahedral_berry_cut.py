"""Exact Berry face test of the existing four-face Pauli source.
Not a proof identifying this source with a Marici tower cut.
"""
from pathlib import Path
import hashlib
import itertools
import json
import sympy as s

ROOT = Path(__file__).resolve().parents[3]


def main():
    # Same ordered normals and negative-polarization projectors as the owner source.
    signs = [(1, 1, -1), (1, -1, 1), (-1, 1, 1), (-1, -1, -1)]
    sigma = [s.Matrix([[0, 1], [1, 0]]), s.Matrix([[0, -s.I], [s.I, 0]]), s.diag(1, -1)]
    normals = [s.Matrix(v) / s.sqrt(3) for v in signs]
    projectors = [(s.eye(2) - sum((n[k]*sigma[k] for k in range(3)), s.zeros(2))) / 2 for n in normals]
    simp = s.simplify
    for p in projectors:
        assert (p*p-p).applyfunc(simp) == s.zeros(2)
        assert simp(s.trace(p)) == 1
    for i, j in itertools.combinations(range(4), 2):
        assert simp(s.trace(projectors[i]*projectors[j])) == s.Rational(1, 3)

    def bargmann(i, j, k):
        return simp(s.trace(projectors[i]*projectors[j]*projectors[k]))

    def phase(i, j, k):
        b = bargmann(i, j, k)
        return simp(b / s.sqrt(simp(b*s.conjugate(b))))

    faces = {''.join(map(str, f)): phase(*f) for f in itertools.combinations(range(4), 3)}
    assert all(h in (s.I, -s.I) for h in faces.values())
    # Boundary orientation: [123]-[023]+[013]-[012].
    boundary = simp(faces['123'] / faces['023'] * faces['013'] / faces['012'])
    assert boundary == 1
    assert simp(faces['012']*faces['023'] - faces['013']*faces['123']) == 0
    for i, j, k in itertools.permutations(range(4), 3):
        assert simp(phase(i, k, j)-s.conjugate(phase(i, j, k))) == 0

    # Frame rephasing cannot alter any loop. Explicit normalized eigenvectors
    # come from a nonzero projector column, not from the desired holonomy.
    vectors = []
    for p in projectors:
        v = p[:, 0]
        vectors.append((v/s.sqrt(simp((v.conjugate().T*v)[0]))).applyfunc(simp))
    gauges = [s.Integer(1), s.I, (3+4*s.I)/5, -s.I]
    def loop(vs, i, j, k):
        g = simp((vs[i].conjugate().T*vs[j])[0] *
                 (vs[j].conjugate().T*vs[k])[0] *
                 (vs[k].conjugate().T*vs[i])[0])
        return simp(g/s.sqrt(simp(g*s.conjugate(g))))
    moved = [g*v for g, v in zip(gauges, vectors)]
    for f in itertools.combinations(range(4), 3):
        assert simp(loop(vectors, *f)-phase(*f)) == 0
        assert simp(loop(moved, *f)-phase(*f)) == 0
    # Hostiles: making each face a strict transport equality predicts phase 1;
    # deleting one nontrivial face breaks the tetrahedral boundary identity.
    strict_residuals = {k: simp(h-1) for k, h in faces.items()}
    assert all(r != 0 for r in strict_residuals.values())
    deleted_boundary = simp(faces['123']/faces['023']*faces['013'])
    assert deleted_boundary != 1
    sources = [
        'research/voevodsky/checkers/check_electron_tetrahedral_spinor.py',
        'research/benincasa/complex-kernel-berry-curvature.md',
        'research/nima/agda/RetainedTetrahedralPackage.agda',
        str(Path(__file__).relative_to(ROOT)).replace('\\', '/'),
    ]
    result = {
        'status': 'pass',
        'source_method': 'Explicit transcription of ordered normals and P=(I-n.sigma)/2; owner producer not rerun.',
        'pairwise_projector_overlap': '1/3',
        'bargmann_invariants': {''.join(map(str, f)): str(bargmann(*f)) for f in itertools.combinations(range(4), 3)},
        'face_phases': {k: str(v) for k, v in faces.items()},
        'oriented_boundary_phase': str(boundary),
        'frame_gauge_invariance': True,
        'strict_face_residuals': {k: str(v) for k, v in strict_residuals.items()},
        'deleted_012_boundary_phase': str(deleted_boundary),
        'scope': 'Finite Pancharatnam/Bargmann phases; interpreted as Berry phases for shortest projective geodesic edges with the stated sign convention.',
        'tower_cut_binding_established': False,
        'native_FCC_equivalence_established': False,
        'sha256': {p: hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in sources},
    }
    out = ROOT/'research/strominger/results/tetrahedral-berry-cut/verification.json'
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(result, indent=2)+'\n', encoding='utf-8')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
