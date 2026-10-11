"""Both-branch preparation and independent-calibration record comparison.
uv run --with sympy python research/nima/checkers/check_bell_preparation_herald_record.py
No apparatus execution or Born/physical-record derivation. Foreign receipts stay unchanged.
"""
from contextlib import redirect_stdout
from fractions import Fraction
import hashlib
import io
from itertools import product
import json
from pathlib import Path
import runpy
import sympy as s

ROOT = Path(__file__).resolve().parents[1]
REPO = ROOT.parent.parent
OUT = ROOT/'results/bell-preparation-herald-record.json'
CONTRACT = ROOT/'contracts/bell-preparation-herald-record.v1.json'
CHECKS = []
SIGNS = (-1,1)
RECORDS = (-1,0,1)  # 0 is a no-click record, not a binary effect label.


def require(name,condition):
    if not bool(condition):
        raise AssertionError(name)
    CHECKS.append(name)


def eq(a,b):
    return (a-b).applyfunc(s.simplify) == s.zeros(*a.shape)


def observed(ideal,K,etaA,etaB):
    """Classical record channels AFTER the complete quantum instrument."""
    def loss(record,sign,eta):
        return 1-eta if record == 0 else eta if record == sign else s.S.Zero
    return {(r,x,y,u,v):s.expand(sum(K[r,h]*loss(u,a,etaA)*loss(v,b,etaB)*ideal[h,x,y,a,b]
             for h,a,b in product(range(2),SIGNS,SIGNS)))
            for r,x,y,u,v in product(range(2),range(2),range(2),RECORDS,RECORDS)}


def decode_records(table):
    decoded = {}
    for (r,x,y,u,v),value in table.items():
        key = (r,x,y,(-1)**(r*x)*u if u else 0,v)
        decoded[key] = value  # A permutation of records, not filtering or renormalization.
    return decoded


def chsh(table):
    return s.simplify(sum((1 if (x,y) != (1,1) else -1)*(u if u else 1)*(v if v else 1)*p
                         for (r,x,y,u,v),p in table.items()))


def calibrate(table):
    # Separate identity-filler trials at existing settings x=1, y=0.
    C = {(r,u):s.simplify(sum(table[r,1,0,u,v] for v in RECORDS))
         for r,u in product(range(2),RECORDS)}
    etaA = s.simplify(sum(C[r,u] for r,u in product(range(2),SIGNS)))
    etaB = s.simplify(sum(table[r,1,0,u,v] for r,u,v in product(range(2),RECORDS,SIGNS)))
    if etaA == 0:
        raise ValueError('No detected Alice calibration records; K is not identifiable')
    K = s.Matrix(2,2,lambda r,h:s.cancel(2*C[r,(-1)**h]/etaA))
    return K,etaA,etaB,C


def main():
    OUT.unlink(missing_ok=True)
    CHECKS.clear()
    contract = json.loads(CONTRACT.read_text(encoding='utf-8'))
    require('frozen-contract',contract['schema'] == 'marici.nima.bell-preparation-herald-record.v1')
    gp = REPO/contract['source']['filler_module']
    bp = REPO/contract['source']['analyzer_module']
    ap = REPO/contract['source']['instrument_module']
    cp = ROOT/'checkers/check_gram_bell_readout_comparison.py'
    receipts = [ROOT/'results'/name for name in ('gram-selection-principle-repaired.json',
                'entanglement-repaired.json','gram-bell-readout-comparison.json')]
    receipts += [REPO/'research/aspect/results/combined_bell_instrument.json']
    before = {str(p):p.read_bytes() if p.exists() else None for p in receipts}
    gram,bell,comparison = [runpy.run_path(str(p)) for p in (gp,bp,cp)]
    # Entire existing predecessor main/assertions run through its existing write-only adapter.
    with redirect_stdout(io.StringIO()):
        instrument,old_result = comparison['retained'](ap)
    require('complete-predecessor-survives',old_result['status'] == 'pass'
            and old_result['instrument_records_forgotten_to_static_table'] == 16
            and old_result['zxz_repeat_probability']['rational'] == '1/2')
    Q = instrument['Q']
    def encode(M):
        def scalar(value):
            value = s.expand(value)
            b = value.coeff(s.sqrt(2)); a = s.simplify(value-b*s.sqrt(2))
            require('exact-Qsqrt2-coefficient',a.is_Rational and b.is_Rational)
            return Q(Fraction(int(a.p),int(a.q)),Fraction(int(b.p),int(b.q)))
        return [[scalar(value) for value in row] for row in M.tolist()]
    def decode(M):
        return s.Matrix([[s.Rational(v.rational.numerator,v.rational.denominator)
                         +s.sqrt(2)*s.Rational(v.root2.numerator,v.root2.denominator) for v in row] for row in M])
    def action(f):
        matrix = s.zeros(4)
        for j,point in enumerate(gram['CODES']):
            matrix[gram['code'](f(point)),j] = 1
        return matrix
    fillers = gram['FILLERS']
    matrices = {name:action(f) for name,f in fillers.items()}
    require('entire-five-filler-source',list(fillers) == ['id','swap','twist','flip_fst','flip_both'])
    for name,P in matrices.items():
        require('unitary:'+name,P.H*P == s.eye(4))
    for f,g in product(fillers,repeat=2):
        require('source-composition:'+f+'/'+g,matrices[f]*matrices[g]
                == action(lambda point:fillers[f](fillers[g](point))))
    rho0 = bell['states']()['product00']
    prepared = {h:decode(instrument['instrument'](encode(rho0),
                         encode((s.eye(2)+(-1)**h*bell['X'])/2),True)) for h in range(2)}
    routes = {name:{h:P*prepared[h]*P.H for h in range(2)} for name,P in matrices.items()}
    for name,branches in routes.items():
        require('whole-preparation:'+name,all(s.trace(branches[h]) == s.Rational(1,2) for h in range(2)))
    for h in range(2):
        psi = s.Matrix([1,0,0,(-1)**h])/s.sqrt(2)
        require('actual-twist-branch:'+str(h),routes['twist'][h] == psi*psi.H/2)
    cq = s.diag(routes['twist'][0],routes['twist'][1])
    forgotten = routes['twist'][0]+routes['twist'][1]
    require('complete-classical-quantum-preparation',cq.shape == (8,8) and cq == cq.H and s.trace(cq) == 1)
    require('forget-herald-is-not-Bell',forgotten == bell['states']()['classical_mixture']
            and bell['chsh'](forgotten) == s.sqrt(2))
    ideal,continuations = {},{}
    for route in ('id','twist'):
        ideal[route],continuations[route] = {},{}
        for h,x,y,a,b in product(range(2),range(2),range(2),SIGNS,SIGNS):
            pa,pb = (s.eye(2)+a*bell['ALICE'][x])/2,(s.eye(2)+b*bell['BOB'][y])/2
            result = decode(instrument['joint_instrument'](encode(routes[route][h]),encode(pa),encode(pb)))
            direct = s.kronecker_product(pa,pb)*routes[route][h]*s.kronecker_product(pa,pb)
            require('full-continuation:'+route+str((h,x,y,a,b)),eq(result,direct))
            probability = s.simplify(s.trace(result))
            require('positive-pairing:'+route+str((h,x,y,a,b)),probability >= 0)
            continuations[route][h,x,y,a,b] = result
            ideal[route][h,x,y,a,b] = probability
    for x,y,a,b in product(range(2),range(2),SIGNS,SIGNS):
        U = s.kronecker_product(bell['Z'],s.eye(2))
        require('full-minus-frame-comparison:'+str((x,y,a,b)),
                eq(U*continuations['twist'][1,x,y,a,b]*U.H,
                   continuations['twist'][0,x,y,(-1)**x*a,b]))
    e0,e1,etaA,etaB = s.symbols('e0 e1 etaA etaB',real=True)
    K = s.Matrix([[1-e0,e1],[e0,1-e1]])
    require('stochastic-herald-columns',s.ones(1,2)*K == s.ones(1,2))
    raw = observed(ideal['twist'],K,etaA,etaB)
    corrected = decode_records(raw)
    require('all-records-retained',len(raw) == len(corrected) == 72)
    for table in (raw,corrected):
        for x,y in product(range(2),repeat=2):
            require('context-normalization',s.simplify(sum(table[r,x,y,u,v]
                    for r,u,v in product(range(2),RECORDS,RECORDS))-1) == 0)
        for r,x,u in product(range(2),range(2),RECORDS):
            require('Alice-no-signalling',s.simplify(sum(table[r,x,0,u,v]-table[r,x,1,u,v] for v in RECORDS)) == 0)
        for r,y,v in product(range(2),range(2),RECORDS):
            require('Bob-no-signalling',s.simplify(sum(table[r,0,y,u,v]-table[r,1,y,u,v] for u in RECORDS)) == 0)
    S = chsh(corrected)
    expected = s.sqrt(2)*(2-e0-e1)*etaA*etaB+2*(1-etaA)*(1-etaB)
    require('inclusive-record-prediction',s.simplify(S-expected) == 0)
    require('raw-forgetting-value',s.simplify(chsh(raw)-(s.sqrt(2)*etaA*etaB+2*(1-etaA)*(1-etaB))) == 0)
    calibration = observed(ideal['id'],K,etaA,etaB)
    reconstructed,a_rec,b_rec,C = calibrate(calibration)
    require('independent-calibration-identifies-channel',eq(reconstructed,K) and a_rec == etaA and b_rec == etaB)
    predicted = decode_records(observed(ideal['twist'],reconstructed,a_rec,b_rec))
    require('whole-record-law-predicted-without-Bell-fit',all(s.simplify(predicted[k]-corrected[k]) == 0 for k in corrected))
    # Anisotropy matters: calibrated record error does not scale every correlation equally.
    correlations = {(x,y):s.simplify(sum(u*v*corrected[r,x,y,u,v]
                    for r,u,v in product(range(2),SIGNS,SIGNS))).subs({etaA:1,etaB:1})
                    for x,y in product(range(2),repeat=2)}
    require('not-one-global-visibility',correlations[0,0] == s.sqrt(2)/2
            and s.simplify(correlations[1,0]-(1-e0-e1)/s.sqrt(2)) == 0)
    good = decode_records(observed(ideal['twist'],s.eye(2),s.S.One,s.S.One))
    bad = decode_records(observed(ideal['twist'],s.Matrix([[0,1],[1,0]]),s.S.One,s.S.One))
    require('both-source-branches-succeed-with-frame',chsh(good) == 2*s.sqrt(2))
    require('wrong-record-frame-changes-readout',chsh(bad) == 0 and good != bad)
    for table in (good,bad):
        for r,x,y in product(range(2),repeat=3):
            require('balanced-herald-marginal-not-a-certificate',s.simplify(sum(table[r,x,y,u,v]
                    for u,v in product(RECORDS,repeat=2))) == s.Rational(1,2))
    cal_good = observed(ideal['id'],s.eye(2),s.S.One,s.S.One)
    inferred,a,b,_ = calibrate(cal_good)
    wrong_transfer = decode_records(observed(ideal['twist'],inferred,a,b))
    residual = s.simplify(chsh(wrong_transfer)-chsh(bad))
    require('mode-dependent-channel-hostile',wrong_transfer != bad and residual == 2*s.sqrt(2))
    caught = False
    try:
        calibrate(observed(ideal['id'],s.eye(2),s.S.Zero,s.S.One))
    except ValueError:
        caught = True
    require('zero-retention-calibration-refused',caught)
    caught = False
    try:
        require('deliberately-false-record-descent',good == bad)
    except AssertionError:
        caught = True
    require('failed-required-predicate-raises',caught)
    require('predecessor-receipts-unchanged',before == {str(p):p.read_bytes() if p.exists() else None for p in receipts})
    encode_matrix = lambda M:[[str(v) for v in row] for row in M.tolist()]
    sources = [Path(__file__).resolve(),CONTRACT,gp,bp,ap,cp]
    result = {'schema':'marici.nima.bell-preparation-herald-record.v1','status':'pass',
              'classification':'conditional calibration-to-record comparison; no physical interface or new probability law derived',
              'coherence_obligation':contract['obligation'],
              'source_actions':{name:encode_matrix(M) for name,M in matrices.items()},
              'all_preparation_branches':{name:{str(h):encode_matrix(M) for h,M in branches.items()} for name,branches in routes.items()},
              'classical_quantum_preparation':encode_matrix(cq),
              'full_twist_continuations':{str(k):encode_matrix(M) for k,M in continuations['twist'].items()},
              'raw_complete_record_law':{str(k):str(v) for k,v in raw.items()},
              'decoded_complete_record_law':{str(k):str(v) for k,v in corrected.items()},
              'independent_calibration':{str(k):str(v) for k,v in C.items()},
              'reconstructed_K':encode_matrix(reconstructed),
              'inclusive_CHSH':str(s.factor(S)),
              'unit_retention_record_modes':{'correct':'2*sqrt(2)','forgotten':'sqrt(2)','inverted':'0'},
              'mode_transfer_hostile_CHSH_residual':str(residual),
              'given_not_derived':contract['source']['given']+contract['classical_record_channels']['transfer_assumptions'],
              'physical_disposition':'deferred: independently calibrated preparation/record bundle and physical trial authority absent from inspected material',
              'scope':contract['physical_boundary'],'checks':CHECKS,
              'source_sha256':{p.relative_to(REPO).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in sources}}
    OUT.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:result[k] for k in ('status','classification','inclusive_CHSH','unit_retention_record_modes',
                       'mode_transfer_hostile_CHSH_residual','physical_disposition')},indent=2))


if __name__ == '__main__':
    main()
