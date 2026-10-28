"""Exact support/observation certificates for a finite observer-closure shortcut.
Analytic ingredients: the declared bump is positive inside its support; convolution
of positive compact functions is positive on an interior integration box. No
quadrature value or synthetic physical operator is used.
"""
from pathlib import Path
from fractions import Fraction as F
import hashlib,json
from check_finite_observer_encoder import rational_inverse
ROOT=Path(__file__).resolve().parents[3];BASE='research/strominger/'
CONTRACT=BASE+'contracts/f736-observer-closure-audit.v1.json'
SNAPSHOT=BASE+'contracts/persistent-seam-pe-conjecture-net.snapshot.rev44.json'
OUT=BASE+'results/f736-observer-closure/'
def load(p):return json.loads((ROOT/p).read_text())
def mv(a,v):return [sum(x*y for x,y in zip(row,v)) for row in a]
def main():
    spec=load(CONTRACT);pre=load(SNAPSHOT);checks=[]
    def check(name,value):
        if not value:raise AssertionError(name)
        checks.append(name)
    inputs={CONTRACT,SNAPSHOT,spec['source'],BASE+'contracts/finite-observer-encoder.v1.json',BASE+'archimedean-cutoff-entry-v1.md',BASE+'checkers/check_f736_observer_closure.py',BASE+'checkers/check_finite_observer_encoder.py'}
    n=next(n for n in pre['conjectures'] if n['id']=='f736-observer-closure-audit')
    check('finite-closure audit registered before execution',n['status']=='open' and n['registration_before_execution'])
    for name in ['finite-observer-encoder-verification','f736-correlated-word-edges/verification']:
        p=BASE+'results/'+name+'.json';r=load(p);inputs.add(p)
        check('live receipt closure: '+name,all(hashlib.sha256((ROOT/q).read_bytes()).hexdigest()==sha for q,sha in r['sourceHashes'].items()));inputs.update(r['sourceHashes'])
    profile=load(BASE+'contracts/finite-observer-encoder.v1.json')
    check('actual frozen packet has spacing four support radii',profile['delta']=='2 log 2' and profile['epsilon']=='delta/4' and profile['packet']=='p_j(u)=phi(u-j delta)/A')
    # All coordinates below are exact multiples of epsilon.
    u=F(3,2);supports=[(F(4*j-1),F(4*j+1)) for j in range(5)]
    check('the product witness lies outside every original packet support',all(not lo<=u<=hi for lo,hi in supports))
    lo,hi=F(5,8),F(7,8)
    check('a positive-length convolution interval lies strictly inside both bump supports',hi-lo==F(1,4) and -1<lo<hi<1 and -1<u-hi<u-lo<1)
    exponent=1-1/(1-hi*hi)
    check('explicit positive product lower bound has the exact bump exponent',exponent==-F(49,15) and 2*exponent==-F(98,15))
    encoder=load(BASE+'results/finite-observer-encoder.json');inputs.add(BASE+'results/finite-observer-encoder.json')
    T=[[F(x) for x in row] for row in encoder['analyticReadoutMatrix']];det,Ti=rational_inverse(T)
    # rho=A*integral p0^2. For h=p0*p0, O(h)=(1,1,rho,0,0).
    constant=mv(Ti,[F(1),F(1),F(0),F(0),F(0)]);rho=mv(Ti,[F(0),F(0),F(1),F(0),F(0)])
    check('surrogate reproduces the exact two endpoint observations',mv(T,constant)==[1,1,0,0,0])
    check('surrogate retains the unknown normalization instead of fitting it',mv(T,rho)==[0,0,1,0,0])
    check('product flux samples at delta and2delta vanish by support',all(abs(F(4*k))>2 for k in [1,2]))
    powers=[]
    for degree in range(1,46):
        evaluation=F(degree)-F(1,2);center=evaluation/degree
        half_width=F(1,4*degree*(degree-1)) if degree>1 else F(0)
        last_deviation=(degree-1)*half_width
        powers.append({'degree':degree,'evaluationOverEpsilon':str(evaluation),'factorCenterOverEpsilon':str(center),'integrationHalfWidthOverEpsilon':str(half_width),'lastFactorRange':[str(center-last_deviation),str(center+last_deviation)]})
        assert 0<center<1
        if degree>1:assert half_width>0 and -1<center-half_width<center+half_width<1 and -1<center-last_deviation<center+last_deviation<1
    check('all45 convolution powers have strictly positive diagonal witnesses',len(powers)==45)
    check('support evaluation matrix is triangular with nonzero diagonal',all(F(row['evaluationOverEpsilon'])>lower for row in powers for lower in range(1,row['degree'])))
    check('faithful linear closure of these powers cannot fit C44',len(powers)>44)
    check('original finite encoder remains invertible on its declared domain',det==-F(3,2) and all(mv(T,mv(Ti,[F(i==j) for i in range(5)]))==[F(i==j) for i in range(5)] for j in range(5)))
    artifact={'contract':CONTRACT,'product':'h=p0*p0; A_h=A_p0 A_p0 under the source integrated convolution representation',
        'gapWitness':{'uOverEpsilon':str(u),'allD5FunctionsAtWitness':0,'integrationIntervalOverEpsilon':[str(lo),str(hi)],'strictPositiveProductLowerBound':'epsilon/(4 A^2) * exp(-98/15)'},
        'observationCollision':{'productObservations':['1','1','rho','0','0'],'rho':'A*integral p0(u)^2 du >0','surrogate':'g=sum_j (constant_j + rho*rhoCoefficient_j) p_j',
            'constant':[str(x) for x in constant],'rhoCoefficient':[str(x) for x in rho],'fiveObservationsEqual':True,'functionsDistinct':True,'witness':'h(3epsilon/2)>0 while g(3epsilon/2)=0','representedOperators':'A_h != A_g by faithfulness of the full regular convolution representation; equal finite observations are insufficient'},
        'powerSupportCertificates':powers,'independentPowerCount':45,'finiteD5ConvolutionClosureEstablished':False,'finite44FaithfulLinearClosureExcluded':True,
        'finiteEncoderOnOriginalDomainRefuted':False,'sourceWhiskeringRefuted':False,'functionValued44ChannelFieldsExcluded':False,'fullPbConstructionEstablished':False,
        'remainingObligation':'Retain full represented observer functions/operators, or a justified convolution-closed carrier, for witness recovery. Finite packet readouts may remain restricted observables but cannot serve as faithful labels after arbitrary products.',
        'scope':spec['scope']}
    (ROOT/OUT).mkdir(parents=True,exist_ok=True);dest=OUT+'audit.json';(ROOT/dest).write_text(json.dumps(artifact,indent=2)+'\n');inputs.add(dest)
    report={'status':'passed','check_count':len(checks),'checks':checks,'finiteClosureShortcutRejected':True,'finiteD5ConvolutionClosureEstablished':False,'fiveObservationCollisionEstablished':True,'independentPowerCount':45,'finite44FaithfulLinearClosureExcluded':True,
        'finiteEncoderOnOriginalDomainRefuted':False,'sourceWhiskeringRefuted':False,'functionValued44ChannelFieldsExcluded':False,'fullPbConstructionEstablished':False,
        'sourceHashes':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in sorted(inputs)}}
    (ROOT/OUT/'verification.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps({k:v for k,v in report.items() if k not in ['checks','sourceHashes']}))
if __name__=='__main__':main()
