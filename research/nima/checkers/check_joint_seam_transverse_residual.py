"""Retain the parent-face ambiguity of the conditional edge interface.

The complementary edge gives a geometric diagnostic, not a physically selected
measurement. Use the true raw-vector metric; candidate modes are not orthogonal
independent registers. This enlarges the prior conditional interface only.
"""
from pathlib import Path
from itertools import permutations
import hashlib
import json
import sympy as S
from assemble_triangle_arrow_source import assemble

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]


def main():
    checks = []
    def check(name, condition):
        if not condition: raise AssertionError(name)
        checks.append(name)
    source_path = HERE.parent/'inputs/proton-six-arrows.json'
    source = json.loads(source_path.read_text())
    points = {k:S.Matrix(v) for k,v in source['vertices'].items()}
    omega = (-1+S.I*S.sqrt(3))/2
    def mode(a,b,c):
        return S.simplify((points[a]+points[b]+points[c])/3 + omega*points[a]+S.conjugate(omega)*points[b])
    def adj(m): return m.conjugate().T
    edge = points['B']-points['A']
    transverse = points['C']-points['D']
    check('geometry/orthogonal-complementary-edges', (edge.T*transverse)[0] == 0)
    results = []
    for deleted in ('BC','CA','AD','DB'):
        report,_ = assemble({**source,'arrows':[e for e in source['arrows'] if ''.join(e)!=deleted]})
        rows = report['triangles_and_transports']
        labels = [''.join(r['outer_arrow']) for r in rows]
        orphan = next(a for a in ('AB','BA') if a not in labels)
        raw = []
        for row in rows:
            a,b = row['outer_arrow']
            c = next(k for k in row['triangle'][0].split('_')[1:] if k not in (a,b))
            raw.append(mode(a,b,c))
        vc,vd = mode(*orphan,'C'),mode(*orphan,'D')
        check('ambiguity/exact-difference/'+deleted, S.simplify(vc-vd) == transverse/3)
        check('reader/transverse-separation/'+deleted,
              S.simplify((transverse.T*vc)[0]) == S.Rational(4,3)
              and S.simplify((transverse.T*vd)[0]) == -S.Rational(4,3))
        average, difference = (vc+vd)/2,(vc-vd)/2
        check('metric/candidates-not-orthogonal/'+deleted, S.simplify((adj(vc)*vd)[0]) == S.Rational(56,9))
        # w=c vc+d vd; seam matching imposes c+d=-a. Retain r=c-d.
        a_column = S.Matrix.vstack(*raw,-average)
        r_column = S.Matrix.vstack(S.zeros(9,1),difference)
        encoding = a_column.row_join(r_column)
        gram = S.simplify(adj(encoding)*encoding)
        check('joint/actual-induced-metric/'+deleted, gram == S.diag(S.Rational(238,9),S.Rational(2,9)))
        decoder = S.simplify(gram.inv()*adj(encoding))
        projector = S.simplify(encoding*decoder)
        check('joint/two-coordinate-recovery/'+deleted, S.simplify(decoder*encoding) == S.eye(2))
        check('joint/orthogonal-projector/'+deleted,
              S.simplify(projector*projector-projector) == S.zeros(12)
              and S.simplify(adj(projector)-projector) == S.zeros(12))
        old_vector = S.Matrix.vstack(*raw)
        old_projector = S.simplify(old_vector*adj(old_vector)/20)
        check('joint/old-compression/'+deleted,
              S.simplify(projector[:9,:9]-S.Rational(90,119)*old_projector) == S.zeros(9))
        check('retention/full-complement/'+deleted, projector+(S.eye(12)-projector) == S.eye(12))
        for residual,candidate in ((-1,vc),(1,vd)):
            branch = S.Matrix.vstack(*raw,-candidate)
            check('prior/both-candidate-branches-retained/'+deleted+str(residual),
                  S.simplify(encoding*S.Matrix([1,residual])-branch) == S.zeros(12,1))
        # Two source-geometric readers recover the orphan's coefficients on
        # its two-mode span. They are not tomography of arbitrary C^3 inputs.
        read = edge.T.col_join(transverse.T)
        mode_frame = vc.row_join(vd)
        response = S.simplify(read*mode_frame)
        check('reader/two-mode-invertible/'+deleted, response.det() != 0)
        check('reader/two-mode-decoder/'+deleted,
              S.simplify(response.inv()*read*mode_frame) == S.eye(2))
        check('reader/general-raw-kernel-remains/'+deleted, read.rank() == 2)
        # Swapping C and D changes r's coordinate sign, not the encoded vector.
        swapped = a_column.row_join(-r_column)
        check('frame/parent-swap-covariance/'+deleted,
              swapped*S.diag(1,-1) == encoding)
        results.append({'deleted':deleted,'orphan':orphan,
                        'joint_coordinate_metric':[[str(x) for x in row] for row in gram.tolist()],
                        'old_compression_factor':'90/119',
                        'two_reader_matrix':[[str(x) for x in row] for row in response.tolist()]})
    # Covariance of the geometric readout under every tetrahedral orthogonal
    # relabelling; this does not declare all relabellings admitted dynamics.
    vertices = tuple(points[k] for k in 'ABCD')
    for perm in permutations(range(4)):
        rotation = sum((vertices[perm[k]]*vertices[k].T for k in range(4)),S.zeros(3))/4
        check('frame/orthogonality/'+str(perm), rotation.T*rotation == S.eye(3))
        check('frame/readout-covariance/'+str(perm),
              (rotation*transverse).T*rotation == transverse.T)
    files = [Path(__file__),source_path,HERE/'assemble_triangle_arrow_source.py',
             HERE/'check_joint_seam_edge_reconstruction.py']
    report = {'schema':'marici.nima.joint-seam-transverse-residual.v1','status':'pass','checks':checks,
              'cases':results,'joint_dimension':2,
              'coordinate_law':'old amplitudes=(a,a,a); orphan= -a*(vC+vD)/2 + r*(vC-vD)/2',
              'norm_law':'238/9 |a|^2 + 2/9 |r|^2',
              'scope':'Conditional edge-matching completion retaining both parent candidates in their '
                      'actual overlapping raw span. Complementary-edge readout is a geometric '
                      'diagnostic, not a source-authorized physical instrument. No residual '
                      'preparation, dynamics, physical coupling or face-selection rule supplied.',
              'input_sha256':{str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in files}}
    out = HERE.parent/'results/joint-seam-transverse-residual.json'
    out.write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    print(f'PASS: {len(checks)} exact transverse-residual checks')
    print('Complementary-edge reading distinguishes both parent faces; retain a two-coordinate joint state.')
    print('True metric retained; no face choice, residual dynamics or physical instrument selected.')


if __name__ == '__main__':
    main()
