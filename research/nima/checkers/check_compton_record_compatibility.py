"""Exact readout pullback for the existing single-Compton proposal.
uv run --with sympy python research/nima/checkers/check_compton_record_compatibility.py
This tests a physical-theory interface, not measured detector data.
"""
import ast
import hashlib
from itertools import product
import json
from pathlib import Path
import sympy as s

OWNER = Path(__file__).resolve().parents[1]
REPO = OWNER.parent.parent
CONTRACT = OWNER/'contracts/compton-record-compatibility.v1.json'
LEGACY = OWNER/'check_qed_bell_experimental_gate.py'
OUT = OWNER/'results/compton-record-compatibility.json'
I2 = s.eye(2)
X = s.Matrix([[0,1],[1,0]])
Y = s.Matrix([[0,-s.I],[s.I,0]])
SIGNS = ((1,1),(-1,1))  # Existing Sinha-Zahed/CGLMP convention.
CHECKS = []


def require(name,value):
    if not bool(value):
        raise AssertionError(name)
    CHECKS.append(name)


def clean(M):
    return M.applyfunc(lambda v:s.simplify(s.expand_trig(v)))


def zero(value):
    value = s.simplify(s.expand_trig(value))
    # Nested radicals from pi/16 sectors need an algebraic-number field,
    # not syntactic equality or a numerical tolerance.
    return value == 0 or s.cancel(value,extension=True) == 0


def equal(A,B):
    return all(zero(v) for v in A-B)


def axis(alpha):
    return s.cos(2*alpha)*X+s.sin(2*alpha)*Y


def density(phi,mu):
    return (I2-mu*axis(phi))/(2*s.pi)


def interval(lo,hi,mu):
    """Integral of the physical POVM density; bounds are radians."""
    return ((hi-lo)*I2/(2*s.pi)-mu*((s.sin(2*hi)-s.sin(2*lo))*X
            +(s.cos(2*lo)-s.cos(2*hi))*Y)/(4*s.pi))


def response(point,alpha,half_width):
    """Exact angles in pi units. Endpoints have zero angular measure."""
    for sign,shift in ((1,s.Rational(1,2)),(-1,s.S.Zero)):
        for turn in (0,1):
            distance = (point-alpha-shift-turn+1) % 2-1
            if abs(distance) < half_width:
                return sign
    return 0


def parent(axes,half_width,mu):
    boundaries = {s.S.Zero,s.Integer(2)}
    for alpha,shift,side in product(axes,(0,s.Rational(1,2),1,s.Rational(3,2)),(-1,1)):
        boundaries.add((alpha+shift+side*half_width) % 2)
    boundaries = sorted(boundaries)
    result = {}
    for lo,hi in zip(boundaries,boundaries[1:]):
        labels = tuple(response((lo+hi)/2,alpha,half_width) for alpha in axes)
        result[labels] = result.get(labels,s.zeros(2))+interval(s.pi*lo,s.pi*hi,mu)
    return {labels:clean(G) for labels,G in result.items()}


def moment(parent_packet,setting):
    return clean(sum(((labels[setting] or 1)*G for labels,G in parent_packet.items()),s.zeros(2)))


def bell_operator(A,B):
    return clean(sum((SIGNS[x][y]*s.kronecker_product(A[x],B[y])
                      for x,y in product(range(2),repeat=2)),s.zeros(4)))


def encoded(M):
    return [[str(v) for v in row] for row in M.tolist()]


def main():
    OUT.unlink(missing_ok=True)
    CHECKS.clear()
    contract = json.loads(CONTRACT.read_text(encoding='utf-8'))
    require('contract',contract['schema'] == 'marici.nima.compton-record-compatibility.v1')
    # Reuse precisely the existing cross-section function without importing its
    # numerical Bell scan or executing its legacy artifact writer.
    tree = ast.parse(LEGACY.read_text(encoding='utf-8'))
    functions = [n for n in tree.body if isinstance(n,ast.FunctionDef) and n.name == 'compton_visibility']
    require('one-existing-Klein-Nishina-function',len(functions) == 1)
    namespace = {'mp':s}  # The same cos/sin formula, evaluated symbolically.
    exec(compile(ast.Module(body=functions,type_ignores=[]),str(LEGACY),'exec'),namespace)
    require('independent-cross-section-control',namespace['compton_visibility'](s.Rational(1,3),s.pi/2) == s.Rational(12,13))
    phi,mu = s.symbols('phi mu',real=True)
    lo,hi = s.symbols('lo hi',real=True)
    require('continuous-parent-normalization',equal(interval(0,2*s.pi,mu),I2))
    require('analytic-integral-not-inserted-effects',equal(s.diff(interval(lo,hi,mu),hi),density(hi,mu)))
    require('continuous-parent-Hermitian',equal(density(phi,mu).H,density(phi,mu)))
    require('continuous-parent-positive-spectrum',equal(axis(phi)**2,I2)
            and s.simplify(s.trace(axis(phi))) == 0)
    # Thus its eigenvalues are (1 +/- mu)/(2*pi), positive for 0<=mu<=1.
    Aaxes = [s.Rational(v) for v in contract['exact_fixtures']['A_axes_in_pi_units']]
    Baxes = [s.Rational(v) for v in contract['exact_fixtures']['B_axes_in_pi_units']]
    widths = [s.Rational(v) for v in contract['exact_fixtures']['half_widths_in_pi_units']]
    pi_low,pi_high = [s.Rational(v) for v in contract['exact_fixtures']['pi_bounds_for_certificates']]
    muA,muB = s.symbols('muA muB',real=True)
    ket = s.Matrix([1,0,0,1])/s.sqrt(2)
    rho = ket*ket.H
    ideal = bell_operator([axis(a*s.pi) for a in Aaxes],[axis(b*s.pi) for b in Baxes])
    require('ideal-projector-control-preserved',s.simplify(s.trace(rho*ideal)) == 2*s.sqrt(2))
    packets = {}
    for d in widths:
        eta = 4*d
        nuA,nuB = [m*s.sin(2*s.pi*d)/(2*s.pi*d) for m in (muA,muB)]
        GA,GB = parent(Aaxes,d,muA),parent(Baxes,d,muB)
        for wing,axes,Gs,m,nu in (('A',Aaxes,GA,muA,nuA),('B',Baxes,GB,muB,nuB)):
            require('parent-complete:'+wing+str(d),equal(sum(Gs.values(),s.zeros(2)),I2))
            for labels,G in Gs.items():
                require('parent-Hermitian:'+wing+str((d,labels)),equal(G,G.H))
                w = s.simplify(s.trace(G)/2)
                V = clean((G-w*I2)/m)
                require('parent-equatorial:'+wing+str((d,labels)),V[0,0] == V[1,1] == 0 and w >= 0)
                r2 = s.simplify(s.pi**2*V[0,1]*V[1,0])
                # G has eigenvalues w +/- mu*sqrt(r2)/pi. Use the classical
                # Archimedes bound 223/71 < pi, not floating eigensolvers.
                require('exact-PSD-certificate:'+wing+str((d,labels)),s.simplify(w*w*pi_low*pi_low-r2) >= 0)
            for x,alpha in enumerate(axes):
                for record in (-1,0,1):
                    actual = sum((G for labels,G in Gs.items() if labels[x] == record),s.zeros(2))
                    expected = (1-eta)*I2 if record == 0 else eta*(I2+record*nu*axis(alpha*s.pi))/2
                    require('record-pullback:'+wing+str((d,x,record)),equal(actual,expected))
        complete = bell_operator([moment(GA,x) for x in range(2)],[moment(GB,y) for y in range(2)])
        decomposed = s.zeros(4)
        classical_values = set()
        for a,b in product(GA,GB):
            c = sum(SIGNS[x][y]*(a[x] or 1)*(b[y] or 1) for x,y in product(range(2),repeat=2))
            classical_values.add(c)
            require('complete-local-response-bound',abs(c) <= 2)
            decomposed += c*s.kronecker_product(GA[a],GB[b])
        require('full-operator-common-parent-comparison:'+str(d),equal(complete,decomposed))
        # Positive normalized GA tensor GB and coefficients in [-2,2] prove
        # -2 I4 <= complete <= 2 I4 for ALL input states, not only rho.
        expected_complete = 2*s.sqrt(2)*eta**2*nuA*nuB+2*(1-eta)**2
        observed = s.simplify(s.trace(rho*complete))
        require('Phi-plus-complete-control:'+str(d),zero(observed-expected_complete))
        require('scalar-acceptance-retained:'+str(d),equal(
            sum((G for labels,G in GA.items() if labels[0] != 0),s.zeros(2)),eta*I2))
        packets[str(d)] = {'eta':str(eta),'nuA':str(nuA),'nuB':str(nuB),
                          'parent_A':{str(k):encoded(v) for k,v in GA.items()},
                          'parent_B':{str(k):encoded(v) for k,v in GB.items()},
                          'complete_CHSH_operator':encoded(complete),
                          'Phi_plus_complete_CHSH':str(observed),
                          'local_response_values':sorted(classical_values)}
    # For any exhaustive stochastic binary classifier |g(phi)|<=1,
    # the Bloch component is bounded by mu/(2*pi) integral |cos(2phi)|.
    absolute_cosine_integral = 4*s.integrate(s.cos(2*phi),(phi,-s.pi/4,s.pi/4))
    require('optimal-exhaustive-binary-sharpness',absolute_cosine_integral == 4)
    nu_full = mu*absolute_cosine_integral/(2*s.pi)
    actual_plus = (I2+nu_full*X)/2
    inserted_plus = (I2+mu*X)/2
    calibration_state = (I2+X)/2
    actual_cal = s.simplify(s.trace(calibration_state*actual_plus))
    inserted_cal = s.simplify(s.trace(calibration_state*inserted_plus))
    residual = s.simplify(actual_cal-inserted_cal)
    require('one-arm-discriminator',s.simplify(residual-mu*(1/s.pi-s.Rational(1,2))) == 0)
    require('old-binary-pullback-fails',residual.subs(mu,1) != 0)
    require('unpolarized-input-control-agrees',s.simplify(s.trace((I2/2)*(actual_plus-inserted_plus))) == 0)
    require('zero-visibility-detector-control-agrees',residual.subs(mu,0) == 0)
    require('full-coverage-cannot-reach-CHSH-two',8*s.sqrt(2)/pi_low**2 < 2)
    d = s.Rational(1,16)
    eta = 4*d
    postselected = s.simplify(2*s.sqrt(2)*(s.sin(2*s.pi*d)/(2*s.pi*d))**2)
    # Positive numerator divided by pi^2. An upper bound on pi proves >2.
    require('selected-table-can-violate',s.simplify(postselected*s.pi**2/pi_high**2-2) > 0)
    inclusive = s.simplify(eta**2*postselected+2*(1-eta)**2)
    require('same-parent-inclusive-table-does-not',s.simplify(eta**2*postselected*s.pi**2/pi_low**2+2*(1-eta)**2) < 2)
    caught = False
    try:
        require('hostile-point-visibility-is-binary-visibility',equal(actual_plus.subs(mu,1),inserted_plus.subs(mu,1)))
    except AssertionError:
        caught = True
    require('wrong-interface-predicate-rejected',caught)
    sources = [Path(__file__).resolve(),CONTRACT,LEGACY]
    result = {'schema':'marici.nima.compton-record-compatibility-result.v1','status':'pass',
              'classification':'declared-Compton-rebinning-interface-rejected; common-parent obstruction constructed',
              'coherence_obligation':contract['obligation'],
              'universal_strength':'all density operators on the supplied two-photon polarization space; all local postprocessings of the fixed angular parent obey Bell locality',
              'continuous_parent_eigenvalues':['(1-mu)/(2*pi)','(1+mu)/(2*pi)'],
              'exact_parent_packets':packets,
              'single_arm_calibration':{'actual_plus':str(actual_cal),'inserted_plus':str(inserted_cal),'residual':str(residual)},
              'postselection_control':{'half_width':'pi/16','muA':'1','muB':'1','eta':'1/4',
                                       'conditional_CHSH':str(postselected),'complete_CHSH':str(inclusive)},
              'checks':CHECKS,'scope':contract['boundary'],
              'physical_status':'no apparatus acquired or tested',
              'source_sha256':{p.relative_to(REPO).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in sources}}
    OUT.parent.mkdir(parents=True,exist_ok=True)
    OUT.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:result[k] for k in ('status','classification','single_arm_calibration','postselection_control','physical_status')},indent=2))


if __name__ == '__main__':
    main()
