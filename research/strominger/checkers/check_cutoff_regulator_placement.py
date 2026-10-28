"""Audit finite-regulator trace placement before using a physical cutoff claim.
Exact finite operator controls test a claimed algebraic identity, not a physical
Tate cutoff model. The owning source is not modified by this checker.
"""
from pathlib import Path
from fractions import Fraction as F
import hashlib
import json
from exact_multiradical import Radical as R,mm,adj,identity,serialize,sqrt

ROOT=Path(__file__).resolve().parents[3]
BASE='research/strominger/results/'
SOURCE='research/voevodsky/exact-regulator-transport-aligns-the-physical-product-cutoff-with-the-eight-leg-hardy-readout.md'


def mul(*matrices):
    a=matrices[0]
    for b in matrices[1:]:a=mm(a,b)
    return a

def tr(a):return sum((a[i][i] for i in range(len(a))),R())
def sub(a,b):return [[x-y for x,y in zip(row,col)] for row,col in zip(a,b)]
def scale(c,a):return [[c*x for x in row] for row in a]
def block(a,b,c,d):return [x+y for x,y in zip(a,b)]+[x+y for x,y in zip(c,d)]


def evaluate(P,Qt,Q0,Z,A,B):
    delta=sub(Qt,Q0);Z2=mm(Z,Z)
    ordered=tr(mul(Z,P,delta,A,adj(B),Z))
    claimed=tr(mul(adj(mm(Z,B)),P,delta,mm(A,Z)))
    corrected=tr(mul(adj(B),Z2,P,delta,A))
    defect=tr(mul(sub(mm(adj(B),Z2),mul(Z,adj(B),Z)),P,delta,A))
    # Exact source-style relative projection feature, now with correct legs.
    Psi=Qt+Q0
    J4=[[R((1 if i<2 else -1) if i==j else 0) for j in range(4)] for i in range(4)]
    zero=[[R(0) for _ in range(4)] for _ in range(4)]
    Kherm=block(zero,J4,J4,zero)
    imaginary=sqrt(-1)
    Kskew=block(zero,scale(-imaginary,J4),scale(imaginary,J4),zero)
    def theta(X):return scale(sqrt(F(1,2)),mul(Psi,P,X)+mm(Psi,X))
    left=mm(Z2,B);right=A
    tleft,tright=theta(left),theta(right)
    herm=tr(mul(adj(tleft),Kherm,tright));skew=tr(mul(adj(tleft),Kskew,tright))
    return {'ordered':ordered,'claimed':claimed,'corrected':corrected,'defect':defect,
            'featureReconstruction':herm+imaginary*skew,'hermitianChannel':herm,'skewChannel':skew,
            'projectionFeatureIdentity':mul(adj(Psi),J4,Psi)==delta,
            'readoutHermiticity':Kherm==adj(Kherm) and Kskew==adj(Kskew)}


def main():
    checks=[]
    def check(name,value):
        if not value:raise AssertionError(name)
        checks.append(name)
    half=R(F(1,2));P=[[half,half],[half,half]];Z=P
    V=[[R(1),R(0)],[R(0),R(-1)]];Q0=P;Qt=mul(V,P,adj(V))
    A=[[R(1),R(0)],[R(0),R(2)]];B=[[R(3),R(0)],[R(0),R(4)]]
    result=evaluate(P,Qt,Q0,Z,A,B)
    check('counterexample uses actual orthogonal projections',all(x==adj(x) and mm(x,x)==x for x in [P,Qt,Q0,Z]))
    check('phase conjugation preserves the reference projection rank',mul(adj(V),V)==identity(2) and Qt==mul(V,Q0,adj(V)))
    check('observer multipliers commute and are normal',mm(A,B)==mm(B,A) and mm(A,adj(A))==mm(adj(A),A) and mm(B,adj(B))==mm(adj(B),B))
    check('regulator does not commute with observer multiplier',mm(Z,B)!=mm(B,Z))
    check('source claimed factorization fails by an exact quarter',result['ordered']==R(F(-11,2)) and result['claimed']==R(F(-21,4)) and result['ordered']-result['claimed']==R(F(-1,4)))
    check('correct cyclic placement reproduces the ordered trace',result['corrected']==result['ordered'])
    check('commutator defect accounts for the full error',result['defect']==result['ordered']-result['claimed'])
    check('corrected unequal-leg feature reproduces the ordered trace',result['featureReconstruction']==result['ordered'])
    check('relative projection feature and both Hermitian readout matrices are exact',result['projectionFeatureIdentity'] and result['readoutHermiticity'])
    variants=[]
    for phase in [R(-1),sqrt(-1)]:
        V=[[R(1),R(0)],[R(0),phase]];qt=mul(V,P,adj(V))
        for z in [identity(2),P,[[R(1),R(0)],[R(0),R(F(1,2))]]]:
            for aa,bb in [(A,B),(B,A),(A,A),(B,B)]:
                trial=evaluate(P,qt,Q0,z,aa,bb)
                if trial['corrected']!=trial['ordered'] or trial['featureReconstruction']!=trial['ordered'] or trial['defect']!=trial['ordered']-trial['claimed']:
                    raise AssertionError('corrected placement fails')
                variants.append(trial)
    check('24 exact projection and non-idempotent regulator controls pass the corrected identities',len(variants)==24)
    check('a commuting regulator removes the source factorization defect',evaluate(P,Qt,Q0,identity(2),A,B)['ordered']==evaluate(P,Qt,Q0,identity(2),A,B)['claimed'])
    check('skew channel is not silently erased in complex-phase controls',any(t['skewChannel']!=R(0) for t in variants))
    # The general symbolic derivation uses only the cyclic trace law:
    # tr(Z P D A B* Z) = tr(B* Z^2 P D A).
    # Claimed: tr(B* Z P D A Z) = tr(Z B* Z P D A).
    # Difference: tr((B*Z^2-ZB*Z) P D A).
    artifact=BASE+'cutoff-regulator-placement.json'
    payload={'controlOrigin':'exact finite algebraic counterexample, not sampled physical cutoff data',
             'matrices':{name:serialize(x) for name,x in [('P',P),('Qt',Qt),('Q0',Q0),('Z',Z),('A',A),('B',B)]},
             'values':{k:v.record() for k,v in result.items() if isinstance(v,R)},
             'claimedFormula':'tr((Z B)* P DeltaQ (A Z))',
             'orderedFormula':'tr(Z P DeltaQ A B* Z)',
             'correctFormula':'tr(B* Z^2 P DeltaQ A), for self-adjoint Z',
             'defectFormula':'tr((B* Z^2-Z B* Z) P DeltaQ A)',
             'correctFeatureLegs':{'left':'Z^2 B','right':'A'},
             'featureFormula':'tr(Theta(left)* (Kherm+i Kskew) Theta(right))',
             'conditionalSimplification':'Z^2=Z only when the actual regulator is a projection',
             'fullPhysicalCutoffEvaluated':False,'packetCutoffResidualEvaluated':False,
             'sourceUnitaryTransportRefuted':False,'globalConjectureRefuted':False}
    (ROOT/artifact).write_text(json.dumps(payload,indent=2)+'\n',encoding='utf-8')
    inputs=[SOURCE,artifact,'research/strominger/checkers/exact_multiradical.py',
            'research/strominger/checkers/check_cutoff_regulator_placement.py']
    report={'status':'passed','check_count':len(checks),'checks':checks,
            'claimedFactorizationValidWithoutExtraCommutation':False,'correctedFiniteTraceIdentityVerified':True,
            'counterexampleOrderedTrace':'-11/2','counterexampleClaimedTrace':'-21/4','counterexampleDefect':'-1/4',
            'correctedControlCases':24,'fullPhysicalCutoffEvaluated':False,'packetCutoffResidualEvaluated':False,
            'sourceUnitaryTransportRefuted':False,'globalConjectureRefuted':False,
            'sourceHashes':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in inputs},
            'scope':'A finite-regulator observer-leg rewrite in the cited source is not a consequence of cyclicity without extra commutation. The corrected trace/feature identity is proved algebraically and tested exactly. No physical cutoff operator or intended packet residual is replaced by these controls.'}
    (ROOT/BASE/'cutoff-regulator-placement-verification.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:report[k] for k in ['status','check_count','counterexampleOrderedTrace','counterexampleClaimedTrace','counterexampleDefect','correctedControlCases']}))


if __name__=='__main__':main()
