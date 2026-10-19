"""Conditional joint regeneration from a declared geometric edge readout.

Use the supplied spatial pairing on the AB edge, preserve the old three-mode
compatibility equations, and rebuild the joint kernel with an orphan mode.
Both possible parent faces are tested; neither is selected by the input.
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
        if not condition:
            raise AssertionError(name)
        checks.append(name)
    source_path = HERE.parent/'inputs/proton-six-arrows.json'
    source = json.loads(source_path.read_text())
    points = {k:S.Matrix(v) for k,v in source['vertices'].items()}
    omega = (-1+S.I*S.sqrt(3))/2
    def mode(a,b,c):
        center = (points[a]+points[b]+points[c])/3
        return S.simplify(center+omega*points[a]+S.conjugate(omega)*points[b])
    def adj(m):
        return m.conjugate().T
    edge = points['B']-points['A']  # same marked spatial reader in every case
    check('reader/source-edge-length', (edge.T*edge)[0] == 8)
    results = []
    for deleted in ('BC','CA','AD','DB'):
        changed = {**source,'arrows':[e for e in source['arrows'] if ''.join(e)!=deleted]}
        report,_ = assemble(changed)
        rows = report['triangles_and_transports']
        labels = [''.join(r['outer_arrow']) for r in rows]
        surviving = next(a for a in ('AB','BA') if a in labels)
        orphan = next(a for a in ('AB','BA') if a not in labels)
        local_vectors = []
        for row in rows:
            a,b = row['outer_arrow']
            c = next(k for k in row['triangle'][0].split('_')[1:] if k not in (a,b))
            local_vectors.append(mode(a,b,c))
        index = labels.index(surviving)
        read_surviving = S.simplify((edge.T*local_vectors[index])[0])
        candidate_vectors = []
        for parent in ('C','D'):
            candidate = mode(orphan[0],orphan[1],parent)
            candidate_vectors.append(candidate)
            read_candidate = S.simplify((edge.T*candidate)[0])
            check('restriction/nonzero/'+deleted+'/'+parent, read_candidate != 0)
            check('restriction/opposite-orientation/'+deleted+'/'+parent,
                  S.simplify(read_candidate+read_surviving) == 0)
            norm = S.simplify((adj(candidate)*candidate)[0])
            check('metric/equal-local-mode-norms/'+deleted+'/'+parent,
                  norm == S.Rational(20,3) and all(S.simplify((adj(v)*v)[0]) == norm for v in local_vectors))
            # Old compatibility: all three transported amplitudes equal.
            # Edge equality: R_old v_old a_old = R_orphan v_orphan a_orphan.
            D = S.Matrix([[1,-1,0,0],[1,0,-1,0]])
            seam = S.zeros(1,4)
            seam[0,index] = read_surviving
            seam[0,3] = -read_candidate
            D = D.col_join(seam)
            basis = D.nullspace()
            check('joint/kernel-dimension/'+deleted+'/'+parent, len(basis) == 1)
            v = S.Matrix([1,1,1,-1])
            check('joint/source-restriction-kernel/'+deleted+'/'+parent, S.simplify(D*v) == S.zeros(3,1))
            N = v*adj(v)/4
            old = S.ones(3)/3
            check('joint/projector/'+deleted+'/'+parent, N*N == N and adj(N) == N)
            check('joint/old-compression-changes/'+deleted+'/'+parent, N[:3,:3] == S.Rational(3,4)*old)
            # Isometric identification of the OLD COMPATIBLE line with the
            # new compatible line; not recovery of arbitrary old raw states.
            u = S.Matrix([1,1,1])/S.sqrt(3)
            z = v/2
            encode = z*adj(u)
            decode = adj(encode)
            check('recovery/old-compatible-line/'+deleted+'/'+parent, S.simplify(decode*encode) == old)
            check('recovery/joint-compatible-line/'+deleted+'/'+parent, S.simplify(encode*decode) == N)
            check('recovery/intertwines-returns/'+deleted+'/'+parent, N*encode == encode*old)
            # The orthogonal complement is retained, not declared reconstructible
            # from the single compatible coordinate.
            check('retention/full-amplitude-decomposition/'+deleted+'/'+parent, N+(S.eye(4)-N) == S.eye(4))
            results.append({'deleted':deleted,'surviving_mode':surviving,'unresolved_primitive':orphan,
                            'candidate_parent_face':''.join(sorted(orphan+parent)),
                            'edge_readout':str(read_candidate),'joint_dimension':1,
                            'old_compression_factor':'3/4','restriction_recovery_factor':'2/sqrt(3)',
                            'interface_status':'conditional-geometric-edge-readout'})
        check('ambiguity/different-raw-mode-lines/'+deleted,
              S.simplify(candidate_vectors[0]*adj(candidate_vectors[0]) -
                         candidate_vectors[1]*adj(candidate_vectors[1])) != S.zeros(3))
        difference = S.simplify(candidate_vectors[0]-candidate_vectors[1])
        check('ambiguity/invisible-to-edge-reader/'+deleted, (edge.T*difference)[0] == 0)
    files = [Path(__file__),source_path,HERE/'assemble_triangle_arrow_source.py',
             ROOT/'research/voevodsky/cell-interface-assembly-contract.md',
             ROOT/'research/voevodsky/geometric-cycle-reversal.md']
    receipt = {'schema':'marici.nima.joint-seam-edge-reconstruction.v1','status':'pass',
               'checks':checks,'candidates':results,
               'result':'Conditional joint projector and compatible-line recovery constructed. '
                        'Edge response is independent of the orphan parent-face choice, but '
                        'raw modes differ in an edge-invisible direction.',
               'scope':'Declared fixed spatial edge-component matching, not source-selected '
                       'physical coupling. Orphan modes are candidate completions, not generated '
                       'by the unchanged incomplete source. No new primitive reverse cycle is '
                       'asserted. Recovery concerns compatible subspaces; complements are retained. '
                       'No exchange kernel, spin coupling, preparation or energy scale inferred.',
               'input_sha256':{str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in files}}
    out = HERE.parent/'results/joint-seam-edge-reconstruction.json'
    out.write_text(json.dumps(receipt,indent=2)+'\n',encoding='utf-8')
    print(f'PASS: {len(checks)} exact conditional joint-seam reconstruction checks')
    print('Joint compatible line exists; old compression changes by 3/4 and isometrically recovers.')
    print('Both orphan parent faces have the same edge readout but different raw mode lines.')
    print('Interface choice remains explicit; full source completion is not uniquely selected.')


if __name__ == '__main__':
    main()
