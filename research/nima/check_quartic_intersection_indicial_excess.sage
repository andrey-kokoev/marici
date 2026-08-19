import json
import hashlib
from sage.misc.sage_eval import sage_eval

R.<u,v> = PolynomialRing(QQ)
F = R.fraction_field()
D = -4+12*u-6*u*v+4*v-9*u^2+4*u^2*v-v^2
H = -2-3*u+2*u*v+v-u^2*v+u^3

a9_path = 'research/benincasa/bivariate_soft_gram_connection.json'
a3_path = 'research/benincasa/marked-wall-quotient-connection.json'
a9_bytes = open(a9_path,'rb').read()
a3_bytes = open(a3_path,'rb').read()
a9 = json.loads(a9_bytes)
a3 = json.loads(a3_bytes)

def parse(x):
    if isinstance(x,(int,Integer)):
        return F(x)
    return F(sage_eval(str(x).replace('^','**'),locals={'u':u,'v':v,'D':D,'H':H}))

def A3(axis):
    z=F(0); d=a3[axis]
    return matrix(F,[[parse(d['alpha']),z,z],
                     [parse(d['beta1']),parse(d['gamma1']),z],
                     [parse(d['beta2']),z,parse(d['gamma2'])]])

A9v = matrix(F,[[parse(x) for x in row] for row in a9['connection_v']])
A3v = A3('v')

# Work over QQ(u), adjoining a generic root of each carrier equation in v.
Ru.<uu> = PolynomialRing(QQ)
Ku = Ru.fraction_field()
Pv.<vv> = PolynomialRing(Ku)

def map_fraction(z,K,root):
    return K(z.numerator()(u=uu,v=root))/K(z.denominator()(u=uu,v=root))

def generic_residue(carrier,label):
    carrier_p = Pv(carrier(u=uu,v=vv))
    K.<root> = Pv.quotient(carrier_p)
    dv = F(carrier.derivative(v))
    def residue_matrix(A):
        entries=[]
        for z in A.list():
            normal = F(carrier)*z/dv
            entries.append(map_fraction(normal,K,root))
        return matrix(K,A.nrows(),A.ncols(),entries)
    R9=residue_matrix(A9v)
    R3=residue_matrix(A3v)
    Hom=identity_matrix(K,3).tensor_product(R9)-R3.transpose().tensor_product(identity_matrix(K,9))
    cp9=R9.charpoly(); x9=cp9.parent().gen()
    cp3=R3.charpoly(); x3=cp3.parent().gen()
    cph=Hom.charpoly(); xh=cph.parent().gen()
    assert cp9 == x9^9
    assert cp3 == x3^2*(x3+K(1)/2)
    assert cph == xh^18*(xh-K(1)/2)^9
    return {
        'carrier':label,
        'R9_charpoly':'x^9',
        'R3_charpoly':'x^2*(x+1/2)',
        'Hom_charpoly':'x^18*(x-1/2)^9',
    }

records=[generic_residue(D,'D'),generic_residue(H,'H')]
result={
    'schema':'marici.quartic-intersection-indicial-excess.v1',
    'field':'generic carrier function fields over QQ(u)',
    'records':records,
    'intersection_spectra':'Entry 864: same R9, R3, and Hom characteristic polynomials at Q intersect D and Q intersect H',
    'spectral_excess_at_tested_Q_intersections':False,
    'scope':'generic D/H spectra compared with the exact representative Q intersections; no claim about deeper soft intersections',
    'source_hashes':{
        a9_path:hashlib.sha256(a9_bytes).hexdigest(),
        a3_path:hashlib.sha256(a3_bytes).hexdigest(),
    },
    'status':'no_indicial_spectral_jump',
}

with open('research/nima/quartic-intersection-indicial-excess.json','w') as handle:
    json.dump(result,handle,indent=2,sort_keys=True)
    handle.write('\n')

print(json.dumps(result,indent=2,sort_keys=True))
