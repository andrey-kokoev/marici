"""Prediction-preserving joint completion: exact generic identities and hostiles.
uv run --with sympy python research/nima/checkers/check_joint_compatibility_free_completion.py
"""
from contextlib import redirect_stdout
from itertools import product
from pathlib import Path
import hashlib
import io
import json
import sympy as s
import check_native_square_controlled_hamiltonian as native

OWNER = Path(__file__).resolve().parents[1]
REPO = OWNER.parent.parent
OUT = OWNER/'results/joint-compatibility-free-completion.json'
CONTRACT = OWNER/'contracts/joint-compatibility-free-completion.v1.json'
CHECKS = []


def require(name, condition):
    if not bool(condition):
        raise AssertionError(name)
    CHECKS.append(name)


def reduce(M):
    return M.applyfunc(s.simplify)


def zero(M):
    return all(s.expand(x) == 0 for x in M)


def realify(M):
    A, B = M.applyfunc(s.re), M.applyfunc(s.im)
    return A.row_join(-B).col_join(B.row_join(A))


def hermitian(prefix):
    M = s.zeros(4)
    for i in range(4):
        M[i,i] = s.Symbol(f'{prefix}{i}{i}', real=True)
        for j in range(i+1,4):
            a,b = s.symbols(f'{prefix}r{i}{j} {prefix}i{i}{j}', real=True)
            M[i,j],M[j,i] = a+s.I*b,a-s.I*b
    return M


def norm2(M):
    return s.simplify(s.trace(M.H*M))


def clean(x):
    if isinstance(x,s.MatrixBase):
        return [[str(a) for a in row] for row in x.tolist()]
    if isinstance(x,s.Basic):
        return str(x)
    if isinstance(x,dict):
        return {k:clean(v) for k,v in x.items()}
    if isinstance(x,(tuple,list)):
        return [clean(v) for v in x]
    return x


def main():
    OUT.unlink(missing_ok=True)
    CHECKS.clear()
    contract = json.loads(CONTRACT.read_text())
    parent_path = REPO/contract['source']['predecessor_receipt']
    parent = json.loads(parent_path.read_text())
    source_paths = [OWNER/p for p in parent['source_sha256']]
    paths = [Path(__file__).resolve(),CONTRACT,parent_path,
             OWNER/'joint-compatibility-free-completion.md',
             OWNER/'scc-models/joint-compatibility-free-completion.json',
             OWNER/'results/native-square-controlled-hamiltonian.json',
             OWNER/'results/agda-NativeSquareHamiltonianSkeleton.json',*source_paths]
    before = {p:p.read_bytes() for p in paths}
    require('current-source-bound-predecessor', parent['status']=='pass' and all(
        hashlib.sha256((OWNER/p).read_bytes()).hexdigest()==h for p,h in parent['source_sha256'].items()))
    with redirect_stdout(io.StringIO()):
        source = native.main()
    require('predecessor-receipts-byte-preserved', all(p.read_bytes()==raw for p,raw in before.items()))
    I4,I8 = s.eye(4),s.eye(8)
    L,R,PL,PR = (s.Matrix(source[k]) for k in ('L','R','PL','PR'))
    swap = s.Matrix(source['swap'])
    joints = {key:s.Matrix(J) for key,J in source['joints'].items()}
    J = s.zeros(4).row_join(I4).col_join((-I4).row_join(s.zeros(4)))
    metric,omega = 2*I8,2*J
    H,Q = hermitian('h'),hermitian('q')
    RH,RQ = realify(H),realify(Q)
    A = J*RH
    require('all-16-Hermitian-parameters-retained', len(H.free_symbols)==16)
    require('Hermitian-realification-symmetric', zero(RH.T-RH))
    require('same-complex-structure', zero(J*RH-RH*J))
    require('generic-Hamiltonian-route', zero(-omega*A-2*RH))
    require('generic-metric-compatibility', zero(A.T*metric+metric*A))
    require('generic-symplectic-compatibility', zero(A.T*omega+omega*A))
    require('generic-energy-conservation', zero(A.T*RH+RH*A))
    observer_derivative = realify(s.I*(H*Q-Q*H))
    require('generic-state-effect-route', zero(A.T*RQ+RQ*A-observer_derivative))
    # This realification also transports pairwise commutation; the sign follows
    # from realify(-iH)=J realify(H).
    AQ = J*RQ
    require('generic-Lie-transport', zero(A*AQ-AQ*A+realify(H*Q-Q*H)))

    for ij,P in joints.items():
        require('source-projector', P*P==P and P.H==P and s.trace(P)==1)
        for kl,T in joints.items():
            if ij != kl:
                require('source-orthogonality', P*T==s.zeros(4))
    require('source-projectors-complete', sum(joints.values(),s.zeros(4))==I4)
    def E(k,z,w):
        return sum((z**(a+k*a*b)*w**(b+k*a*b)*P for (a,b),P in joints.items()),s.zeros(4))
    z,w,u,v = s.symbols('z w u v',nonzero=True)
    phase_pair = source['roots'][1]
    phase = s.Rational(phase_pair[0])+s.I*s.sqrt(3)*s.Rational(phase_pair[1])
    X = s.Matrix([[0,1],[1,0]])
    Y = s.Matrix([[0,-s.I],[s.I,0]])
    Z = s.diag(1,-1)
    paulis = {'X':X,'Y':Y,'Z':Z}
    effects = {a+b:[s.kronecker_product((s.eye(2)+p*A0)/2,(s.eye(2)+q*B0)/2)
                    for p,q in product((1,-1),repeat=2)] for a,A0 in paulis.items() for b,B0 in paulis.items()}
    basis = [s.kronecker_product(a,b) for a,b in product((s.eye(2),X,Y,Z),repeat=2)]
    for name,setting in effects.items():
        require('complete-fixed-effect-setting/'+name, sum(setting,s.zeros(4))==I4 and all(F.H==F and F*F==F for F in setting))
    witnesses = []; hostiles = {}
    for k in contract['witnesses']['mixed_coefficients']:
        HL,HR = PL+k*PL*PR,PR+k*PL*PR
        require('annotation-commutation', HL*HR==HR*HL)
        require('annotation-interchange', swap*HL*swap==HR)
        for (a,b),P in joints.items():
            require('nonnegative-source-eigenvalues', HL*P==(a+k*a*b)*P and HR*P==(b+k*a*b)*P and min(a+k*a*b,b+k*a*b)>=0)
        for a,b in product((0,1),repeat=2):
            require('source-corner', E(k,(-1)**a,(-1)**b)==L**a*R**b)
        require('polynomial-composition-law', zero(E(k,z,w)*E(k,u,v)-E(k,z*u,w*v)))
        require('Laurent-unitarity-law', zero(E(k,z,w).T*E(k,1/z,1/w)-I4))
        require('reflected-square-law', zero(E(k,-1/z,-1/w)-L*R*E(k,1/z,1/w)))
        for generator in (HL,HR):
            real_generator = J*realify(generator)
            require('same-fixed-geometry', zero(-omega*real_generator-2*realify(generator)) and zero(real_generator.T*metric+metric*real_generator))
        for schedule in ('left','right'):
            U = reduce(E(k,phase,1) if schedule=='left' else E(k,1,phase))
            RU = realify(U)
            require('finite-flow-isometry', zero(reduce(RU.T*metric*RU-metric)))
            require('finite-flow-symplectic', zero(reduce(RU.T*omega*RU-omega)))
            for seed_index in range(4):
                seed = I4[:,seed_index]
                psi = reduce(U*seed)
                rho = reduce(psi*psi.H)
                require('normalized-positive-state', reduce(psi.H*psi)==s.ones(1,1) and zero(reduce(rho*rho-rho)))
                records = {}
                for name,setting in effects.items():
                    row = [s.simplify(s.trace(rho*F)) for F in setting]
                    require('all-records-kept/'+name, sum(row)==1 and all(p>=0 for p in row))
                    records[name] = row
                    for F,p in zip(setting,row):
                        require('same-observer-two-routes', s.simplify((seed.H*U.H*F*U*seed)[0]-p)==0)
                reconstructed = reduce(sum((s.trace(rho*P)*P for P in basis),s.zeros(4))/4)
                require('full-state-tomography', reconstructed==rho)
                require('phase-gauge-invariance', reduce((s.I*psi)*(s.I*psi).H)==rho)
                amplitudes = s.Matrix(2,2,list(psi))
                determinant_squared = s.simplify(abs(amplitudes.det())**2)
                require('existing-image-obstruction-retained', determinant_squared==(0 if k==0 else s.Rational(3,16)))
                witnesses.append({'k':k,'schedule':schedule,'seed':seed_index,'HL':HL,'HR':HR,
                                  'state':psi,'density_matrix':rho,'records':records,'determinant_squared':determinant_squared})
        if k==2:
            real_generator = J*realify(HL)
            wrong_omega = omega.copy(); wrong_omega[0,4]=4; wrong_omega[4,0]=-4
            wrong_Q = s.kronecker_product(s.eye(2),Z)
            Ereal = realify(wrong_Q)
            hostiles['wrong_Hamiltonian_sign'] = norm2(-omega*(-real_generator)-2*realify(HL))
            hostiles['mismatched_geometry'] = norm2(-wrong_omega*real_generator-2*realify(HL))
            hostiles['wrong_observer_sign'] = norm2(real_generator.T*Ereal+Ereal*real_generator+realify(s.I*(HL*wrong_Q-wrong_Q*HL)))
            hostiles['extra_tensor_locality'] = norm2(HL*wrong_Q-wrong_Q*HL)
    # All-parameter baseline image identity, independent of the finite probes.
    for j in range(4):
        psi = E(0,z,w)[:,j]
        require('all-parameter-product-image', s.expand(psi[0]*psi[3]-psi[1]*psi[2])==0)
    left = [r for r in witnesses if r['schedule']=='left' and r['seed']==0]
    require('fixed-record-distinction', left[0]['records']['ZZ']==[s.Rational(3,4),0,s.Rational(1,4),0]
            and left[1]['records']['ZZ']==[s.Rational(3,16),s.Rational(3,16),s.Rational(7,16),s.Rational(3,16)])
    N = s.zeros(4); N[0,1]=1
    badA = realify(-s.I*N)
    hostiles['non_Hermitian_generator'] = norm2(badA.T*metric+metric*badA)
    hostiles['odd_source_corner'] = norm2(E(1,-1,1)-L)
    require('hostiles-have-nonzero-residuals', all(x>0 for x in hostiles.values()))
    for path,raw in before.items():
        require('source-input-preserved/'+path.name, path.read_bytes()==raw)
    result = {'schema':'marici.nima.joint-compatibility-free-completion-result.v1','status':'pass',
              'classification':'prediction-preserving-section-falsifies-strict-added-selection-in-declared-completion',
              'checks_passed':len(CHECKS),'generic_Hermitian_parameter_count':16,
              'witnesses':witnesses,'hostile_squared_norms':hostiles,'metric':metric,'symplectic_form':omega,
              'section':'H -> (fixed g, fixed Omega, h_H, -i H psi, exp(-i parameter H), fixed effects); forgetting returns H',
              'prediction_sets':'P(joint completion)=P(original annotation class)',
              'scope':contract['scope'],
              'source_sha256':{p.relative_to(REPO).as_posix():hashlib.sha256(raw).hexdigest() for p,raw in before.items()}}
    OUT.write_text(json.dumps(clean(result),indent=2)+'\n')
    print(json.dumps(clean({k:result[k] for k in ('status','classification','checks_passed','generic_Hermitian_parameter_count','hostile_squared_norms','prediction_sets')}),indent=2))


if __name__=='__main__':
    main()
