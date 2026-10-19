"""Test the conditional seam completion under the surviving source rotation.

Spatial covariance of the candidate orphan is explicit; it is not a newly
admitted primitive operation on that orphan. Compare fixed and moving seams.
"""
from pathlib import Path
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
        return S.simplify((points[a]+points[b]+points[c])/3+omega*points[a]+S.conjugate(omega)*points[b])
    def adj(m): return m.conjugate().T
    def zero(m): return S.simplify(m) == S.zeros(*m.shape)
    edge = points['B']-points['A']
    results = []
    bindings = []
    for deleted in ('BC','CA','AD','DB'):
        report,_ = assemble({**source,'arrows':[e for e in source['arrows'] if ''.join(e)!=deleted]})
        cycle = report['derived_cycles'][0]
        mapping = {k:k for k in points}
        mapping.update(dict(zip(cycle,cycle[1:]+cycle[:1])))
        rotation = sum((points[mapping[k]]*points[k].T for k in points),S.zeros(3))/4
        check('source/proper-order-three/'+deleted, rotation.det()==1 and rotation**3==S.eye(3)
              and rotation.T*rotation==S.eye(3))
        rows = report['triangles_and_transports']
        labels = [''.join(row['outer_arrow']) for row in rows]
        orphan = next(k for k in ('AB','BA') if k not in labels)
        surviving = next(k for k in ('AB','BA') if k in labels)
        vectors = []
        for row in rows:
            a,b = row['outer_arrow']
            c = next(k for k in row['triangle'][0].split('_')[1:] if k not in (a,b))
            vectors.append(mode(a,b,c))
        native = S.zeros(9)
        for j,label in enumerate(labels):
            target = labels.index(''.join(mapping[k] for k in label))
            native[3*target:3*target+3,3*j:3*j+3] = rotation
        old = S.Matrix.vstack(*vectors)
        check('source/old-common-mode-fixed/'+deleted, zero(native*old-old))
        # Declared candidate extension: transform orphan spatial coordinates
        # by the same source isometry. The orphan's endpoint marking moves too.
        U = S.diag(native,rotation)
        check('extension/unitary-return/'+deleted, adj(U)*U == S.eye(12) and U**3 == S.eye(12))
        vc,vd = mode(*orphan,'C'),mode(*orphan,'D')
        E = S.Matrix.vstack(old,-(vc+vd)/2).row_join(S.Matrix.vstack(S.zeros(9,1),(vc-vd)/2))
        G = S.simplify(adj(E)*E)
        decoder = S.simplify(G.inv()*adj(E))
        N = S.simplify(E*decoder)
        leakage = S.simplify((S.eye(12)-N)*U*E)
        check('fixed-frame/not-closed/'+deleted, leakage.rank() > 0)
        orbit = S.Matrix.hstack(E,U*E,U**2*E)
        check('fixed-frame/minimal-linear-closure-four/'+deleted, orbit.rank() == 4)
        chosen = orbit.rref()[1]
        W = orbit[:,list(chosen)]
        WG = S.simplify(adj(W)*W)
        decodeW = S.simplify(WG.inv()*adj(W))
        T = S.simplify(decodeW*U*W)
        check('closure/intertwiner/'+deleted, zero(U*W-W*T))
        check('closure/return/'+deleted, zero(T**3-S.eye(4)))
        check('closure/metric/'+deleted, zero(adj(T)*WG*T-WG))
        # Fixed seam equality on raw vectors, versus the fully transported
        # seam at each source-rotation stage.
        fixed = S.zeros(1,12)
        index = labels.index(surviving)
        fixed[:,3*index:3*index+3] = edge.T
        fixed[:,9:12] = -edge.T
        check('fixed-frame/initial-seam-matches/'+deleted, zero(fixed*E))
        check('fixed-frame/next-seam-defect/'+deleted, not zero(fixed*U*E))
        mark = surviving
        for k in range(3):
            transported = S.zeros(1,12)
            index = labels.index(mark)
            d = rotation**k*edge
            transported[:,3*index:3*index+3] = d.T
            transported[:,9:12] = -d.T
            check('moving-frame/seam-matches/'+deleted+'/'+str(k), zero(transported*U**k*E))
            check('moving-frame/coordinates-recovered/'+deleted+'/'+str(k),
                  zero(decoder*adj(U**k)*U**k*E-S.eye(2)))
            mark = ''.join(mapping[c] for c in mark)
        check('moving-frame/mark-returns/'+deleted, mark == surviving)
        bindings.append({'deleted':deleted, 'encoding':W, 'update':T,
                         'metric':WG, 'seam_reader':fixed*W})
        results.append({'deleted':deleted,'source_cycle':cycle,
                        'fixed_two_coordinate_leakage_rank':int(leakage.rank()),
                        'fixed_observer_closure_dimension':4,
                        'first_fixed_seam_defect':[[str(x) for x in row] for row in S.simplify(fixed*U*E).tolist()],
                        'closure_update':[[str(x) for x in row] for row in T.tolist()],
                        'closure_metric':[[str(x) for x in row] for row in WG.tolist()]})
    files = [Path(__file__),source_path,HERE/'assemble_triangle_arrow_source.py',
             HERE/'check_joint_seam_transverse_residual.py']
    result = {'schema':'marici.nima.joint-seam-residual-transport.v1','status':'pass','checks':checks,
              'cases':results,
              'conclusion':'The fixed two-coordinate joint space is not invariant under the '
                           'surviving source rotation with covariant orphan transport. Its smallest '
                           'invariant linear span has dimension four. A transported seam instead '
                           'retains two fiber coordinates and a three-stage moving frame.',
              'scope':'Conditional extension of the actual source isometry to candidate orphan '
                      'spatial records. No source-authorized orphan dynamics, preparation, '
                      'relaxation, physical event time or interaction selection inferred. '
                      'Minimal closure concerns a linear state space containing the full initial '
                      'two-mode subspace, not arbitrary nonlinear encodings or scalar observability.',
              'input_sha256':{str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in files}}
    out = HERE.parent/'results/joint-seam-residual-transport.json'
    out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(f'PASS: {len(checks)} exact residual-transport checks')
    print('Fixed two-mode space leaks; exact invariant linear closure has four dimensions.')
    print('Moving seam preserves two coordinates with retained three-stage frame.')
    print('Conditional covariance test, not selection of physical orphan dynamics.')
    return bindings


if __name__ == '__main__':
    main()
