import json
import hashlib
from sage.misc.sage_eval import sage_eval

R.<u,v> = PolynomialRing(QQ)
F=R.fraction_field()
D=-4+12*u-6*u*v+4*v-9*u^2+4*u^2*v-v^2
H=-2-3*u+2*u*v+v-u^2*v+u^3

a9_path='research/benincasa/bivariate_soft_gram_connection.json'
a3_path='research/benincasa/marked-wall-quotient-connection.json'
a9_bytes=open(a9_path,'rb').read()
a3_bytes=open(a3_path,'rb').read()
a9=json.loads(a9_bytes)
a3=json.loads(a3_bytes)

def parse(x):
    if isinstance(x,(int,Integer)):
        return F(x)
    return F(sage_eval(str(x).replace('^','**'),locals={'u':u,'v':v,'D':D,'H':H}))

def A3(axis):
    z=F(0); d=a3[axis]
    return matrix(F,[[parse(d['alpha']),z,z],
                     [parse(d['beta1']),parse(d['gamma1']),z],
                     [parse(d['beta2']),z,parse(d['gamma2'])]])

A9u=matrix(F,[[parse(x) for x in row] for row in a9['connection_u']])
A9v=matrix(F,[[parse(x) for x in row] for row in a9['connection_v']])
A3u=A3('u'); A3v=A3('v')

P.<z> = PolynomialRing(QQ)
K.<s> = NumberField(z^2-2)
L=LaurentSeriesRing(K,'r',default_prec=4)
r=L.gen()

def at_exceptional(t0):
    uu=L(2)+r
    vv=L(2)+L(t0)*r
    def residue(Au,Av):
        return matrix(K,Au.nrows(),Au.ncols(),[
            (parse(a)(uu,vv)+L(t0)*parse(b)(uu,vv))[-1]
            for a,b in zip(Au.list(),Av.list())])
    R9=residue(A9u,A9v)
    R3=residue(A3u,A3v)
    Hom=identity_matrix(K,3).tensor_product(R9)-R3.transpose().tensor_product(identity_matrix(K,9))
    cp9=R9.charpoly(); cp3=R3.charpoly(); cph=Hom.charpoly()
    integer_roots=[n for n in range(-12,13) if cph(K(n))==0]
    return R9,R3,Hom,cp9,cp3,cph,integer_roots

records=[]
computed=[]
for label,t0 in [('+',K(3)+2*s),('-',K(3)-2*s)]:
    R9,R3,Hom,cp9,cp3,cph,roots=at_exceptional(t0)
    records.append({
        'point':label,
        't':str(t0),
        'R9_charpoly':str(factor(cp9)),
        'R3_charpoly':str(factor(cp3)),
        'Hom_charpoly':str(factor(cph)),
        'Hom_integer_roots':roots,
        'R9_rank':int(R9.rank()),
        'R3_rank':int(R3.rank()),
    })
    computed.append((cp9,cp3,cph))

assert computed[0] == computed[1]

# Tangential exceptional connection.  Since dv=t dr+r dt, its dt block is
# lim_{r->0} r*A_v.  Compute it over QQ(t) before selecting the quartic
# points and test whether their quadratic is a pole divisor.
Rt.<tau> = PolynomialRing(QQ)
Kt=Rt.fraction_field()
Lt=LaurentSeriesRing(Kt,'rho',default_prec=3)
rho=Lt.gen(); uug=Lt(2)+rho; vvg=Lt(2)+Lt(tau)*rho

def tangential(A):
    return matrix(Kt,A.nrows(),A.ncols(),[
        (rho*parse(a)(uug,vvg))[0] for a in A.list()])

T9=tangential(A9v)
T3=tangential(A3v)
den9=lcm([Rt(z.denominator()) for z in T9.list() if z != 0])
den3=lcm([Rt(z.denominator()) for z in T3.list() if z != 0])
qexc=Rt(tau^2-6*tau+1)
assert gcd(den9,qexc) == 1
assert gcd(den3,qexc) == 1

result={
    'schema':'marici.deep-quartic-exceptional-residue.v1',
    'blowup_chart':'u=2+r, v=2+r*t',
    'quartic_exceptional_equation':'t^2-6*t+1',
    'records':records,
    'conjugate_spectra_equal':True,
    'exceptional_tangential_connection':{
        'nine_master_denominator':str(factor(den9)),
        'marked_wall_denominator':str(factor(den3)),
        'gcd_with_quartic_exceptional_equation':'1',
        'regular_at_both_quartic_directions':True,
    },
    'source_hashes':{
        a9_path:hashlib.sha256(a9_bytes).hexdigest(),
        a3_path:hashlib.sha256(a3_bytes).hexdigest(),
    },
    'status':'quartic_directions_are_regular_points_of_resonant_exceptional_connection',
    'scope':'exact radial spectrum and tangential pole support; physical activation not inferred',
}

with open('research/nima/deep-quartic-exceptional-residue.json','w') as handle:
    json.dump(result,handle,indent=2,sort_keys=True)
    handle.write('\n')

print(json.dumps(result,indent=2,sort_keys=True))
