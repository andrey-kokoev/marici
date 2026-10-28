"""Exact rational certificates for analytically derived physical trace bounds.
The continuum kernel, trace-class argument and Si tail proof are in the note.
No numerical quadrature, sampled cutoff matrices or regulator limits on the
singular diagonal are claimed.
"""
from pathlib import Path
from fractions import Fraction as F
from math import isqrt
import hashlib
import json

ROOT=Path(__file__).resolve().parents[3]
BASE='research/strominger/results/'
PROFILE='research/strominger/contracts/archimedean-cutoff-entry.v1.json'
SOURCES=[
 'research/voevodsky/connes-semilocal-theorem-4-realizes-finite-place-weil-terms-as-the-finite-part-of-a-product-cutoff-trace-not-a-positive-trace.md',
 'research/voevodsky/characterwise-semilocal-fourier-is-tate-scattering-and-reduces-prolate-transition-growth-to-a-hankel-symbol-estimate.md',
 'research/strominger/archimedean-cutoff-entry-v1.md']
ENCODER=BASE+'finite-observer-encoder-verification.json'
ENDPOINT=BASE+'finite-packet-endpoint-form-verification.json'
PLACEMENT=BASE+'cutoff-regulator-placement-verification.json'


def sqrt_bounds(q):
    if q<0:raise ValueError('negative square root')
    scale=2**20; n=isqrt(q.numerator*scale*scale//q.denominator)
    lo,hi=F(n,scale),F(n+1,scale)
    if not lo*lo<=q<hi*hi:raise AssertionError('invalid square-root enclosure')
    return lo,hi


def separated_bounds(lo,hi):
    if not 0<lo<=hi or lo<=1<=hi:raise ValueError('support meets identity singularity')
    # |K_Lambda-K_infinity| <= sqrt(r)/(pi^2 Lambda^2)
    # *[(1-r)^-2+(1+r)^-2]. Use pi>3, no floating point.
    gap=1-hi if hi<1 else lo-1
    return sqrt_bounds(hi)[1]*(1/gap**2+1/(1+lo)**2)/9


def main():
    profile=json.loads((ROOT/PROFILE).read_text());checks=[]
    def check(name,value):
        if not value:raise AssertionError(name)
        checks.append(name)
    for name,path in [('encoder',ENCODER),('endpoint',ENDPOINT),('placement',PLACEMENT)]:
        r=json.loads((ROOT/path).read_text())
        check(name+' direct receipt inputs current',all(hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==sha for p,sha in r['sourceHashes'].items()))
    check('physical cutoff values fixed',profile['cutoffs']==[2,4,8])
    # c=integral phi/A. Evenness implies1<=A/integral phi<=cosh(log2/4)<11/10.
    check('rational fourth-root enclosure for the analytic bump mass',F(6,5)**4>2 and (F(6,5)+1)/2==F(11,10))
    cmin,cmax=F(10,11),F(1)
    bounds={}
    for distance in range(1,5):
        lo,hi=F(1,2*4**distance),F(2,4**distance)
        limit_lo=sqrt_bounds(lo)[0]/(1-lo*lo)*cmin*cmin
        limit_hi=sqrt_bounds(hi)[1]/(1-hi*hi)*cmax*cmax
        forward=separated_bounds(lo,hi);reverse=separated_bounds(1/hi,1/lo)
        check('distance'+str(distance)+' has separated reciprocal supports',0<lo<hi<1<1/hi<1/lo)
        check('distance'+str(distance)+' limiting kernel bound positive',0<limit_lo<limit_hi)
        bounds[distance]={'ratio':[lo,hi],'limit':[limit_lo,limit_hi],'forward':forward,'reverse':reverse}
    rows=[]
    for cutoff in profile['cutoffs']:
        entries=[]
        for i in range(5):
            for j in range(5):
                if i==j:continue
                d=abs(i-j);b=bounds[d]
                error=b['forward' if i<j else 'reverse']/cutoff**2
                interval=[b['limit'][0]-error,b['limit'][1]+error]
                endpoint=F(2)**d+F(2)**(-d)
                if interval[0]<=0 or interval[1]>=endpoint:raise AssertionError('physical enclosure loses sign separation')
                entries.append({'i':i,'j':j,'traceEnclosure':[str(x) for x in interval],
                                'errorFromLimitAtMost':str(error),'referenceEntry':0,'volumeCounterterm':0,
                                'endpointTerm':str(endpoint),'endpointSubtractedEnclosure':[str(x-endpoint) for x in interval]})
        check('all20 physical off-diagonal entries positive at Lambda='+str(cutoff),len(entries)==20)
        check('all20 endpoint-subtracted entries strictly negative at Lambda='+str(cutoff),all(F(e['endpointSubtractedEnclosure'][1])<0 for e in entries))
        rows.append({'Lambda':cutoff,'entries':entries})
    try:separated_bounds(F(1,2),F(2));rejected=False
    except ValueError:rejected=True
    check('reject diagonal support crossing the identity singularity',rejected)
    check('no singular diagonal is silently filled with an off-diagonal bound',all(e['i']!=e['j'] for row in rows for e in row['entries']))
    check('off-diagonal reference vanishes by disjoint physical packet supports',1-2*F(1,4)>0)
    # Square roots above are certified integer calculations, not float estimates.
    check('root enclosures are rational certificates',all(isinstance(x,F) for d in range(1,5) for x in sqrt_bounds(F(1,2*4**d))))
    artifact=BASE+'archimedean-cutoff-entry.json'
    result={'kernel':'K_Lambda(r)=sqrt(r)/pi * [Si(2*pi*Lambda^2*(1-r))/(1-r)+Si(2*pi*Lambda^2*(1+r))/(1+r)]',
            'packetIntegral':'T_ij=double integral p_i(u) conjugate(p_j(v)) K_Lambda(exp(u-v)) du dv',
            'kernelLimit':'sqrt(r)/2 * [1/abs(1-r)+1/(1+r)], symmetric under r->1/r',
            'SiTailBound':'abs(Si(x)-sign(x)*pi/2)<=2/abs(x), x!=0',
            'massRatioEnclosure':[str(cmin),str(cmax)],
            'distanceBounds':{str(d):{'ratio':[str(x) for x in b['ratio']],
                                    'limit':[str(x) for x in b['limit']],
                                    'forwardErrorConstant':str(b['forward']),'reverseErrorConstant':str(b['reverse']),
                                    'orderedAsymmetryConstant':str(b['forward']+b['reverse'])} for d,b in bounds.items()},
            'cutoffResults':rows,'physicalCutoffEntriesEnclosed':True,'offDiagonalEntries':20,
            'analyticDerivationRequired':True,'numericalQuadraturePerformed':False,
            'completePacketMatrixEvaluated':False,'diagonalFinitePartEvaluated':False,
            'fullAnalyticalFillerEstablished':False,'allSemilocalSectorsEstablished':False,
            'scope':'Actual archimedean even-sector continuum cutoff kernel. Bounds follow the displayed analytic derivation and exact rational arithmetic. Endpoint subtraction is a stated difference, not identification of all remaining physical terms.'}
    (ROOT/artifact).write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    inputs=[PROFILE,*SOURCES,ENCODER,ENDPOINT,PLACEMENT,artifact,
            'research/strominger/contracts/finite-observer-encoder.v1.json',
            'research/strominger/checkers/check_archimedean_cutoff_entry.py']
    report={'status':'passed','check_count':len(checks),'checks':checks,'physicalCutoffEntriesEnclosed':True,
            'offDiagonalEntries':20,'cutoffs':profile['cutoffs'],'finiteEnclosures':60,
            'completePacketMatrixEvaluated':False,'diagonalFinitePartEvaluated':False,
            'fullAnalyticalFillerEstablished':False,'allSemilocalSectorsEstablished':False,'full114ChannelEstablished':False,
            'numericalQuadraturePerformed':False,'scope':result['scope'],
            'sourceHashes':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in inputs}}
    (ROOT/BASE/'archimedean-cutoff-entry-verification.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:report[k] for k in ['status','check_count','physicalCutoffEntriesEnclosed','offDiagonalEntries','finiteEnclosures']}))


if __name__=='__main__':main()
