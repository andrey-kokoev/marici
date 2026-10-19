"""Compare exchange mismatch algebra to existing occupation/contact algebra.

Global linear intertwiner obstruction, independent of a chosen assignment of
source ports to target operators within the fixed-control mediator algebra.
Does not test endpoint-dependent maps or added spin/position controls.
"""
from contextlib import redirect_stdout
from pathlib import Path
import hashlib
import io
import json
import sympy as S
from check_predictive_pair_exchange_residual import main as build

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]


def main():
    checks = []
    def check(name, condition):
        if not condition:
            raise AssertionError(name)
        checks.append(name)
    with redirect_stdout(io.StringIO()):
        binding = build()
    updates = tuple(binding['updates'].values())
    K = binding['exchange']['K']
    # Products of the six rank-one defects span the entire mismatch algebra.
    defects = [S.eye(6)-t for t in updates]
    check('source/K-invertible', K.det() != 0)
    check('source/all-K-entries-nonzero', all(x != 0 for x in K))
    products = []
    for i in range(6):
        for j in range(6):
            product = defects[i]*defects[j]
            check(f'source/matrix-unit-product/{i}/{j}',
                  product == K[i,j]*K[:,i]*S.eye(6)[j,:])
            products.append(product.reshape(36,1))
    check('source/full-matrix-algebra', S.Matrix.hstack(*products).rank() == 36)
    # Consequently this six-dimensional module has no proper invariant
    # subspace, over either real or complex scalars.
    p = S.zeros(4)
    p[1,1] = p[2,2] = S.Rational(1,2)
    p[1,2] = p[2,1] = -S.Rational(1,2)
    n = S.diag(0,1)
    x = S.Matrix([[0,1],[1,0]])
    i2, i4 = S.eye(2), S.eye(4)
    N = S.kronecker_product(i4,n)
    V = S.kronecker_product(p,x)
    check('target/noncommuting-generators', N*V != V*N)
    basis = [S.kronecker_product(i4,i2), N, S.kronecker_product(p,i2),
             S.kronecker_product(p,n), V, S.kronecker_product(p,n*x)]
    columns = S.Matrix.hstack(*(b.reshape(64,1) for b in basis))
    check('target/six-dimensional-basis', columns.rank() == 6)
    for i,a in enumerate(basis):
        for j,b in enumerate(basis):
            check(f'target/algebra-closure/{i}/{j}',
                  columns.row_join((a*b).reshape(64,1)).rank() == 6)
    check('target/generated-P', V*V == basis[2])
    check('target/generated-Pn', V*V*N == basis[3])
    check('target/generated-nX', N*V == basis[5])
    # Rational pair basis: singlet, triplet 00, triplet 01+10, triplet 11.
    pair_frame = S.Matrix.hstack(S.Matrix([0,1,-1,0]), S.Matrix([1,0,0,0]),
                                 S.Matrix([0,1,1,0]), S.Matrix([0,0,0,1]))
    frame = S.kronecker_product(pair_frame,i2)
    inverse = frame.inv()
    check('target/complete-channel-frame', frame*inverse == S.eye(8))
    for i,b in enumerate(basis):
        moved = inverse*b*frame
        check(f'target/four-invariant-doublets/{i}', all(
            moved[r,c] == 0 for r in range(8) for c in range(8) if r//2 != c//2))
        check(f'target/triplet-occupation-lines/{i}', all(
            moved[r,c] == 0 for r in range(2,8) for c in range(2,8) if r != c))
    # Channel projections have rank two and jointly recover the full target.
    projections = [inverse[2*i:2*i+2,:] for i in range(4)]
    check('target/projections-jointly-faithful', S.Matrix.vstack(*projections).rank() == 8)
    check('target/projection-rank-bound', all(c.rank() == 2 for c in projections))
    paths = [Path(__file__), HERE/'check_predictive_pair_exchange_residual.py',
             HERE.parent/'results/predictive-pair-exchange-residual.json',
             ROOT/'research/voevodsky/checkers/check_proton_electron_contact_binding.py']
    result = {'schema':'marici.nima.exchange-full-mediator-algebra.v1','status':'pass',
              'checks':checks,'source_module_dimension':6,'source_algebra_dimension':36,
              'target_module_dimension':8,'target_algebra_dimension':6,
              'target_invariant_channels':[2,1,1,1,1,1,1],
              'conclusion':'No nonzero single global linear intertwiner from the irreducible '
                           'six-dimensional mismatch module into this fixed-contact occupation/flip '
                           'representation, regardless of the assignment of source ports to its algebra.',
              'argument':'Each target channel projection composed with an intertwiner has invariant '
                         'kernel. Source irreducibility makes it zero or injective, but channel '
                         'dimension at most two excludes injectivity. Jointly faithful projections '
                         'then force the original intertwiner to vanish.',
              'scope':'Fixed contact projector, logical pair times one mediator. Includes words, '
                      'linear combinations and finite-dimensional functions of occupation/contact '
                      'operators. Excludes position kinetics, independent spin rotations, varying '
                      'projectors, endpoint-dependent maps and nonlinear encodings. '
                      'Not a no-go for the full spatial contact model or interaction physics.',
              'input_sha256':{str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest()
                               for p in paths}}
    out = HERE.parent/'results/exchange-full-mediator-algebra.json'
    out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(f'PASS: {len(checks)} exact full-mediator algebra checks')
    print('Source mismatch generates M6; fixed-contact mediator algebra has dimension 6 on 8 states.')
    print('All target invariant channels have dimension at most 2: global linear intertwiner must vanish.')
    print('Endpoint-dependent maps, spin controls and spatial dynamics remain outside this result.')


if __name__ == '__main__':
    main()
