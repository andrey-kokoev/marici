import json
import hashlib
from sage.misc.sage_eval import sage_eval

R.<u,v> = PolynomialRing(QQ)
F=R.fraction_field()
D=-4+12*u-6*u*v+4*v-9*u^2+4*u^2*v-v^2
H=-2-3*u+2*u*v+v-u^2*v+u^3
L=u+v-2

a9_path='research/benincasa/bivariate_soft_gram_connection.json'
a3_path='research/benincasa/marked-wall-quotient-connection.json'
a9_bytes=open(a9_path,'rb').read(); a3_bytes=open(a3_path,'rb').read()
a9=json.loads(a9_bytes); a3=json.loads(a3_bytes)

def parse(x):
    if isinstance(x,(int,Integer)): return F(x)
    return F(sage_eval(str(x).replace('^','**'),locals={'u':u,'v':v,'D':D,'H':H}))

def A3(axis):
    z=F(0); d=a3[axis]
    return matrix(F,[[parse(d['alpha']),z,z],
                     [parse(d['beta1']),parse(d['gamma1']),z],
                     [parse(d['beta2']),z,parse(d['gamma2'])]])

A9v=matrix(F,[[parse(x) for x in row] for row in a9['connection_v']])
A3v=A3('v')

Ru.<uu> = PolynomialRing(QQ)
Ku=Ru.fraction_field()

def restrict(z):
    return Ku(z.numerator()(u=uu,v=2-uu))/Ku(z.denominator()(u=uu,v=2-uu))

def residue(A):
    return matrix(Ku,A.nrows(),A.ncols(),[restrict(F(L)*z) for z in A.list()])

R9=residue(A9v); R3=residue(A3v)
Hom=identity_matrix(Ku,3).tensor_product(R9)-R3.transpose().tensor_product(identity_matrix(Ku,9))
cp9=R9.charpoly(); x9=cp9.parent().gen()
cp3=R3.charpoly(); x3=cp3.parent().gen()
cph=Hom.charpoly(); xh=cph.parent().gen()

assert cp9 == x9^7*(x9+1)*(x9+2)
assert cp3 == x3^2*(x3+Ku(1)/2)
assert cph == xh^14*(xh+1)^2*(xh+2)^2*(xh-Ku(1)/2)^7*(xh+Ku(1)/2)*(xh+Ku(3)/2)

result={
    'schema':'marici.linear-quartic-intersection-indicial-excess.v1',
    'carrier':'u+v-2=0',
    'generic_spectra':{
        'R9':'x^7*(x+1)*(x+2)',
        'R3':'x^2*(x+1/2)',
        'Hom':'x^14*(x+1)^2*(x+2)^2*(x-1/2)^7*(x+1/2)*(x+3/2)',
    },
    'intersection_spectrum':'Entry 864 gives the identical spectrum at (u,v)=(8/5,2/5)',
    'spectral_excess':False,
    'source_hashes':{
        a9_path:hashlib.sha256(a9_bytes).hexdigest(),
        a3_path:hashlib.sha256(a3_bytes).hexdigest(),
    },
    'status':'no_indicial_excess',
}

with open('research/nima/linear-quartic-intersection-indicial-excess.json','w') as handle:
    json.dump(result,handle,indent=2,sort_keys=True); handle.write('\n')
print(json.dumps(result,indent=2,sort_keys=True))
