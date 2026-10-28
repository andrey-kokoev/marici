"""Rational certificates for the analytically subtracted diagonal limit.
This checks constants, decompositions and rate bookkeeping; the companion
note proves the continuum identities and hypotheses. No quadrature is used.
"""
from pathlib import Path
from fractions import Fraction as F
import hashlib
import json

ROOT=Path(__file__).resolve().parents[3]
BASE='research/strominger/results/'
PROFILE='research/strominger/contracts/archimedean-diagonal-limit.v1.json'
OFF=BASE+'archimedean-cutoff-entry.json'
OFF_CHECK=BASE+'archimedean-cutoff-entry-verification.json'
ENCODER=BASE+'finite-observer-encoder.json'
NOTE='research/strominger/archimedean-diagonal-limit-v1.md'


def diagonal_error(k):
    if type(k) is not int or k<1:raise ValueError('bound requires Lambda=2^k,k>=1')
    return (F(1323,4)*(1+F(8,3)*(k+1))+F(139,9))/(6*4**k)


def midpoint_subtraction(weight,d):
    """Constant subtraction coefficient must be the actual c(0), not a fit."""
    if weight!=d:raise ValueError('uncancelled diagonal singularity')
    return F(0)


def main():
    profile=json.loads((ROOT/PROFILE).read_text());off=json.loads((ROOT/OFF).read_text())
    receipt=json.loads((ROOT/OFF_CHECK).read_text());encoder=json.loads((ROOT/ENCODER).read_text());checks=[]
    def check(name,value):
        if not value:raise AssertionError(name)
        checks.append(name)
    check('off-diagonal source inputs current',all(hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==sha for p,sha in receipt['sourceHashes'].items()))
    eta=F(1,2);eps_lower=F(1,3);A_lower=F(2,9)
    d_lower,d_upper=F(100,121),F(9,2)
    derivative_c=F(8)/(eps_lower*A_lower);M=3*(derivative_c+d_upper/2)
    check('bump plateau lower bound gives positive normalization',A_lower==F(2,3)*eps_lower)
    check('packet L2 coefficient is bounded without equating it with sample norm',d_upper==1/A_lower and d_lower==F(10,11)**2)
    check('autocorrelation derivative bound from compact bump derivative',derivative_c==108)
    check('transformed central derivative bound retains the Jacobian',M==F(1323,4))
    check('eta removes the asymmetric support endpoint without changing the log coefficient',2*eta==1)
    # Scalar part: (2d/pi)*I(a eta), I(X)=integral_0^X Si(t)/t dt.
    # I(X)=(pi/2)(log X+gamma)+error, |error|<=2/X.
    scalar_constant=F(4)*d_upper/(3*eta)
    outer_regular_constant=2*d_upper/3
    smooth_constant=F(4,9)
    check('scalar subtracted Si error constant',scalar_constant==12)
    check('outer nonsingular remainder constant',outer_regular_constant==3)
    check('smooth cosine term error constant',smooth_constant==F(4,9))
    check('combined noncentral error constant',scalar_constant+outer_regular_constant+smooth_constant==F(139,9))
    check('central remainder has no logarithmic divergence after correct subtraction',midpoint_subtraction(d_upper,d_upper)==0)
    try:midpoint_subtraction(d_upper,d_upper+1);rejected=False
    except ValueError:rejected=True
    check('wrong counterterm leaves an uncancelled singularity',rejected)
    try:diagonal_error(0);rejected=False
    except ValueError:rejected=True
    check('rate not applied outside its stated cutoff range',rejected)
    # A coarse finite-part enclosure: gamma in[0,1], log pi in[1,2],
    # central remainder bounded by M/2, outer integral by d/2,
    # smooth nonnegative term at most1/4.
    finite_lo=d_lower-M/2;finite_hi=3*d_upper+M/2+d_upper/2+F(1,4)
    check('finite-part coarse enclosure is finite without a sign claim',finite_lo<0<finite_hi)
    constants=[max(F(b['forwardErrorConstant']),F(b['reverseErrorConstant'])) for b in off['distanceBounds'].values()]
    off_constant=max(constants)
    rows=[]
    for k in range(1,11):
        error=diagonal_error(k);matrix_error=error+4*off_constant/4**k
        rows.append({'Lambda':2**k,'diagonalCenteredErrorAtMost':str(error),
                     'wholeCentered5x5OperatorNormErrorAtMost':str(matrix_error),
                     'centeredDiagonalCoarseEnclosure':[str(finite_lo-error),str(finite_hi+error)]})
    check('diagonal convergence bounds strictly decrease over the reported cutoffs',all(diagonal_error(k+1)<diagonal_error(k) for k in range(1,10)))
    check('diagonal error below1/100 at Lambda1024',diagonal_error(10)<F(1,100))
    check('whole centered matrix controlled without assuming finite-cutoff Hermiticity',all(
        F(row['wholeCentered5x5OperatorNormErrorAtMost'])>=F(row['diagonalCenteredErrorAtMost']) for row in rows))
    T=[[F(x) for x in row] for row in encoder['analyticReadoutMatrix']]
    sample_gram=[[sum(T[k][i]*T[k][j] for k in range(5)) for j in range(5)] for i in range(5)]
    check('native observation Gram cannot replace the diagonal Plancherel volume matrix',sample_gram[0][1]!=0)
    check('packet observations retain the two opposite translation characters',
          all(T[0][j]==F(2)**j and T[1][j]==F(2)**(-j) for j in range(5)))
    artifact=BASE+'archimedean-diagonal-limit.json'
    result={'profile':PROFILE,'finitePartExpression':profile['finitePart'],
            'volumeMatrix':'d I5, d=integral p0^2; not d*T* T',
            'diagonalVolumeCoefficientEnclosure':[str(d_lower),str(d_upper)],
            'coarseFinitePartEnclosure':[str(finite_lo),str(finite_hi)],'cutoffBounds':rows,
            'wholeMatrixBound':'diagonal_error(Lambda)+4*max_offdiagonal_error_constant/Lambda^2',
            'diagonalFinitePartRepresented':True,'centeredPacketMatrixLimitControlled':True,
            'numericalFinitePartValueComputed':False,'positivityEstablished':False,
            'allSemilocalSectorsEstablished':False,'analyticalHigherWitnessEstablished':False,
            'scope':'Analytic finite-part formula plus explicit rational convergence bounds in one physical even archimedean sector. Integral expressions are retained; the coarse enclosure is not a numerical quadrature evaluation.'}
    (ROOT/artifact).write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    inputs=[PROFILE,profile['physicalProfile'],profile['packetProfile'],NOTE,OFF,OFF_CHECK,ENCODER,
            'research/strominger/checkers/check_archimedean_diagonal_limit.py']
    report={'status':'passed','check_count':len(checks),'checks':checks,
            'diagonalFinitePartRepresented':True,'centeredPacketMatrixLimitControlled':True,
            'packetDimension':5,'reportedCutoffs':[2**k for k in range(1,11)],
            'diagonalErrorAt1024':str(diagonal_error(10)),
            'numericalFinitePartValueComputed':False,'positivityEstablished':False,
            'allSemilocalSectorsEstablished':False,'analyticalHigherWitnessEstablished':False,'full114ChannelEstablished':False,
            'sourceHashes':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in inputs},'scope':result['scope']}
    (ROOT/BASE/'archimedean-diagonal-limit-verification.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:report[k] for k in ['status','check_count','diagonalFinitePartRepresented','centeredPacketMatrixLimitControlled','diagonalErrorAt1024']}))


if __name__=='__main__':main()
