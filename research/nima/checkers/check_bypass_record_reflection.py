"""Source-bound bypass reflection and parity-herald hostile. Not measured data.
uv run --with sympy python research/nima/checkers/check_bypass_record_reflection.py
"""
from fractions import Fraction
from itertools import product, permutations
from pathlib import Path
import hashlib
import json
import runpy
import sympy as s

OWNER = Path(__file__).resolve().parents[1]
REPO = OWNER.parent.parent
CONTRACT = OWNER/'contracts/bypass-record-reflection.v1.json'
OUT = OWNER/'results/bypass-record-reflection.json'
CHECKS = []
SIGNS = (-1, 1)
OBS = (-1, 0, 1)
Y = tuple(product(OBS, repeat=2))


def require(name, condition):
    if not bool(condition):
        raise AssertionError(name)
    CHECKS.append(name)


def encode(M):
    return [[str(x) for x in row] for row in M.tolist()]


def l1(M):
    return sum(abs(x) for x in M)


def margins(P):
    return P*s.ones(P.cols, 1), P.T*s.ones(P.rows, 1)


def reflect(P):
    mu, nu = margins(P)
    return 2*mu*nu.T-P


def centered(P):
    mu, nu = margins(P)
    return P-mu*nu.T


def parity(p):
    return sum(p[j] > p[k] for j in range(4) for k in range(j+1, 4)) % 2


def monomial(p, phases=(0,0,0,0)):
    M = s.zeros(4)
    for j in range(4):
        M[p[j], j] = s.I**phases[j]
    return M


def main():
    OUT.unlink(missing_ok=True)
    CHECKS.clear()
    c = json.loads(CONTRACT.read_text())
    paths = {name: REPO/path for name, path in c['source'].items()}
    inputs = [Path(__file__).resolve(), CONTRACT, *paths.values()]
    before = {p: p.read_bytes() for p in inputs}
    old = json.loads(paths['projective_receipt'].read_text())
    require('predecessor-current', old['status'] == 'pass' and all(
        hashlib.sha256((REPO/p).read_bytes()).hexdigest() == h for p,h in old['source_sha256'].items()))
    protected = [OWNER/'results/bell-preparation-herald-record.json', OWNER/'results/filler-phase-spectator.json',
                 REPO/'research/aspect/results/combined_bell_instrument.json']
    prior = {p: p.read_bytes() if p.exists() else None for p in protected}
    gram, quantum, instrument = [runpy.run_path(str(paths[name])) for name in ('fillers','states','instrument')]
    source = {name: tuple(gram['code'](f(point)) for point in gram['CODES']) for name,f in gram['FILLERS'].items()}
    require('all-five-live-fillers', {name:list(p) for name,p in source.items()} == old['source_functions'] and len(source) == 5)
    lifts = {tuple(row['permutation']):monomial(row['permutation'],row['phase_exponents']) for row in old['representatives']}
    require('all-source-actions', sorted(lifts) == list(permutations(range(4))))
    T, S = lifts[source['twist']], lifts[source['swap']]
    P_T, P_S = monomial(source['twist']), monomial(source['swap'])
    I, X, Z, Q = quantum['I2'], quantum['X'], quantum['Z'], instrument['Q']
    def to_Q(M):
        M = M.applyfunc(s.simplify)
        require('native-real-coefficients', all(v.is_Rational for v in M))
        return [[Q(Fraction(int(v.p),int(v.q))) for v in row] for row in M.tolist()]
    def from_Q(M):
        return s.Matrix([[s.Rational(v.rational.numerator,v.rational.denominator)
                          +s.sqrt(2)*s.Rational(v.root2.numerator,v.root2.denominator) for v in row] for row in M])
    preparations = {side:{h:from_Q(instrument['instrument'](to_Q(quantum['states']()['product00']),
                         to_Q((I+(-1)**h*X)/2),side=='A')) for h in range(2)} for side in ('A','B')}
    for h in range(2):
        A, B = preparations['A'][h], preparations['B'][h]
        require('balanced-nonzero-preparations', s.trace(A) == s.trace(B) == s.Rational(1,2))
        require('ports-not-identical', A != B)
        require('strict-fixed-sector', P_T*B*P_T.H == B)
        require('projective-exchanges-branches', T*B*T.H == preparations['B'][1-h])
        require('canonical-port-transport', P_S*B*P_S.H == A)
        require('projective-port-transport', S*B*S.H == A)

    def ideal(M, prep, axes=(Z,X)):
        result = {}
        for h,a,b in product(range(2), SIGNS, SIGNS):
            rho = M*prep[h]*M.H
            pa, pb = (I+a*axes[0])/2, (I+b*axes[1])/2
            # Factor the joint projector. A-Z removes inter-A imaginary entries;
            # keep every a branch. No click/branch postselection is performed.
            left = s.kronecker_product(pa,I)
            actual = from_Q(instrument['joint_instrument'](to_Q(left*rho*left.H),to_Q(pa),to_Q(pb)))
            E = s.kronecker_product(pa,pb)
            require('native-joint-continuation', actual == E*rho*E.H)
            result[h,a,b] = actual
        require('ideal-total-trace', sum(s.trace(M) for M in result.values()) == 1)
        return result

    K, RA, RB = [s.Matrix([[s.Rational(v) for v in row] for row in c['exact_noise_fixture'][name]])
                  for name in ('herald','alice','bob')]
    J = s.Matrix([[0,1],[1,0]])
    for R in (K,RA,RB):
        require('complete-stochastic-record-map', all(x >= 0 for x in R) and s.ones(1,R.rows)*R == s.ones(1,2))
    def observed(rows, herald=K):
        states = {}
        for r,y in product(range(3),range(9)):
            a_record,b_record = Y[y]
            states[r,y] = sum((herald[r,h]*RA[OBS.index(a_record),SIGNS.index(a)]
                              *RB[OBS.index(b_record),SIGNS.index(b)]*M
                              for (h,a,b),M in rows.items()),s.zeros(4))
        P = s.Matrix(3,9,lambda r,y:s.trace(states[r,y]))
        require('all-reported-cells', len(states) == 27 and all(x >= 0 for x in P) and sum(P) == 1)
        return P,states
    def store(rows, herald=K):
        P,states = observed(rows,herald)
        return {'records':encode(P),'continuations':{f'{r},{y}':encode(M) for (r,y),M in states.items()}}

    # Entrywise formal identity; stochastic normalization supplies the marginals.
    u,v,x,y = s.symbols('u v x y')
    require('generic-record-and-matrix-entry-reflection', s.expand(
        2*((u+v)/2)*((x+y)/2)-(u*x+v*y)/2-(u*y+v*x)/2) == 0)
    base = ideal(s.eye(4),preparations['B'])
    strict = ideal(P_T,preparations['B'])
    projective = ideal(T,preparations['B'])
    P0,C0 = observed(base)
    PT,CT = observed(projective)
    require('strict-table-is-bypass', observed(strict) == (P0,C0))
    require('projective-full-record-reflection', PT == reflect(P0))
    mu,nu = margins(P0)
    for r,y in product(range(3),range(9)):
        expected = 2*mu[r]*sum((C0[q,y] for q in range(3)),s.zeros(4))-C0[r,y]
        require('reported-matrix-reflection', CT[r,y] == expected)
    require('centered-reflection', centered(PT) == -centered(P0))
    require('record-noncollapse', l1(centered(P0)) > 0 and l1(PT-P0) == 2*l1(centered(P0)))
    rscore = s.Matrix([1,-1,0]); bscore = s.Matrix([b for a,b in Y])
    raw0,rawT = (rscore.T*P0*bscore)[0],(rscore.T*PT*bscore)[0]
    covariance0,covarianceT = (rscore.T*centered(P0)*bscore)[0],(rscore.T*centered(PT)*bscore)[0]
    require('uncentered-flip-rival-rejected', raw0+rawT != 0)
    require('centered-score-flips', covarianceT == -covariance0 and covariance0 != 0)

    # Coxeter braid in C2 forces equal adjacent-generator values.
    characters = [bits for bits in product((0,1),repeat=3)
                  if all((2*bits[i]+bits[i+1]) % 2 == (bits[i]+2*bits[i+1]) % 2 for i in (0,1))]
    require('complete-binary-character-class', characters == [(0,0,0),(1,1,1)])
    for p,q in product(lifts,repeat=2):
        pq = tuple(p[q[j]] for j in range(4))
        require('source-parity-composes', pq in lifts and parity(pq) == (parity(p)+parity(q)) % 2)
    orbit = []; same_A = 0
    for p,U in lifts.items():
        canonical = ideal(monomial(p),preparations['B'])
        lifted = ideal(U,preparations['B'])
        sign = parity(p)
        same_A += p[0]//2 == p[1]//2
        for h,a,b in canonical:
            require('full-ideal-parity-alias', lifted[h,a,b] == canonical[h ^ sign,a,b])
        pp,cp = observed(lifted)
        pf,cf = observed(canonical,K*J**sign)
        require('all-reported-continuations-alias', cp == cf and pp == pf)
        orbit.append({'permutation':list(p),'parity':sign,'records':encode(pp),
                      'ideal_canonical':{str(key):encode(M) for key,M in canonical.items()},
                      'ideal_projective':{str(key):encode(M) for key,M in lifted.items()},
                      'reported_projective':{str(key):encode(M) for key,M in cp.items()},
                      'parity_herald_rival':'exactly_equal_to_reported_projective'})
    require('source-partition-count', same_A == 8 and len(orbit)-same_A == 16)

    reference_A = ideal(s.eye(4),preparations['A'],(X,Z))
    swap_strict = ideal(P_S,preparations['B'],(X,Z))
    swap_projective = ideal(S,preparations['B'],(X,Z))
    PA,CA = observed(reference_A)
    require('new-reader-source-transport', observed(swap_strict) == observed(swap_projective) == (PA,CA))
    PF,CF = observed(swap_strict,K*J)
    require('new-reader-parity-rival-reflects', PF == reflect(PA))
    require('new-reader-separates', l1(PF-PA) > 0 and CF != CA)

    blind_K = s.Matrix([[s.Rational(1,2)]*2,[s.Rational(1,3)]*2,[s.Rational(1,6)]*2])
    PB,CB = observed(base,blind_K)
    require('lost-herald-exact-degeneracy', observed(projective,blind_K) == (PB,CB) and centered(PB) == s.zeros(3,9))
    unbalanced = {0:s.Rational(4,3)*preparations['B'][0],1:s.Rational(2,3)*preparations['B'][1]}
    PU,_ = observed(ideal(s.eye(4),unbalanced)); PUT,_ = observed(ideal(T,unbalanced))
    unbalanced_residual = l1(PUT-reflect(PU))
    require('balance-is-a-real-premise', unbalanced_residual > 0)
    columns = [j for j,(a,b) in enumerate(Y) if b != 0]
    clicked0,clickedT = P0[:,columns],PT[:,columns]
    clicked0,clickedT = clicked0/sum(clicked0),clickedT/sum(clickedT)
    click_residual = l1(clickedT-reflect(clicked0))
    require('click-conditioning-is-not-innocent', click_residual > 0)
    incompatible = s.eye(3)/3
    require('negative-reflection-not-clipped', min(reflect(incompatible)) == -s.Rational(1,9))

    estimated0 = s.Rational(99,100)*P0; estimated0[0,0] += s.Rational(1,100)
    estimatedT = s.Rational(199,200)*PT; estimatedT[2,8] += s.Rational(1,200)
    e0,eT = l1(estimated0-P0),l1(estimatedT-PT)
    require('reflection-error-bound-example', l1(reflect(estimated0)-reflect(P0)) <= 5*e0)
    require('test-error-bound-example', l1(estimatedT-reflect(estimated0)) <= eT+5*e0)
    require('example-prediction-balls-disjoint', l1(reflect(estimated0)-estimated0) > 2*eT+6*e0)
    require('inputs-preserved', all(p.read_bytes() == data for p,data in before.items()))
    require('foreign-and-predecessor-receipts-preserved', all((p.read_bytes() if p.exists() else None) == data for p,data in prior.items()))
    result = {'schema':'marici.nima.bypass-record-reflection-result.v1','status':'pass',
              'classification':'bypass-reflection-survives-parity-herald-alias-broken-by-cross-port-reader',
              'physical_admission_required':False,'measured_records':False,'checks_passed':len(CHECKS),
              'record_order':c['record_order'],'readout_columns':[list(pair) for pair in Y],
              'herald_map':encode(K),'alice_record_map':encode(RA),'bob_record_map':encode(RB),
              'preparations':{side:{str(h):encode(M) for h,M in rows.items()} for side,rows in preparations.items()},
              'cases':{'B_bypass':store(base),'B_strict_twist':store(strict),'B_projective_twist':store(projective),
                       'A_bypass':store(reference_A),'swap_strict':store(swap_strict),
                       'swap_projective':store(swap_projective),'swap_parity_herald_rival':store(swap_strict,K*J)},
              'old_reader_source_orbit':orbit,'old_reader_alias_count':len(orbit),
              'same_A_image_pairs':same_A,'cross_A_image_pairs':len(orbit)-same_A,
              'binary_herald_characters':[list(bits) for bits in characters],
              'uncentered_scores':{'bypass':str(raw0),'projective_twist':str(rawT)},
              'centered_scores':{'bypass':str(covariance0),'projective_twist':str(covarianceT)},
              'twist_record_separation_l1':str(l1(PT-P0)), 'swap_rival_separation_l1':str(l1(PF-PA)),
              'hostiles':{'blind_herald_separation':'0','unbalanced_preparation_residual_l1':str(unbalanced_residual),
                          'click_conditioning_residual_l1':str(click_residual),'incompatible_reflection_minimum':'-1/9'},
              'error_example':{'epsilon_0':str(e0),'epsilon_T':str(eT),'prediction_balls_disjoint':True},
              'scope':c['scope'],'source_sha256':{p.relative_to(REPO).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in inputs}}
    # store() above checks complete records again; report the final check count.
    result['checks_passed'] = len(CHECKS)
    OUT.parent.mkdir(parents=True,exist_ok=True)
    OUT.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:result[k] for k in ('status','classification','checks_passed','old_reader_alias_count',
                    'uncentered_scores','centered_scores','twist_record_separation_l1','swap_rival_separation_l1','hostiles')},indent=2))


if __name__ == '__main__':
    main()
