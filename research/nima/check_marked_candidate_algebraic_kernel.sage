import json
import hashlib

R.<u,v> = PolynomialRing(QQ)
F = R.fraction_field()

def mons(d):
    return [(i,s-i) for s in range(d+1) for i in range(s+1)]

def polynomial(coefficients,degree):
    return R(sum(QQ(c)*u^i*v^j
                 for c,(i,j) in zip(coefficients,mons(degree))))

candidate_path='research/benincasa/marked-extension-charzero-candidate.json'
with open(candidate_path,'rb') as handle:
    candidate_bytes=handle.read()
candidate=json.loads(candidate_bytes)

B={axis:matrix(F,4,3) for axis in ['u','v']}
for entry in candidate['entries']:
    numerator=polynomial(entry['numerator'],entry['numerator_degree'])
    denominator=polynomial(entry['denominator'],entry['denominator_degree'])
    B[entry['axis']][entry['row'],entry['column']]=F(numerator)/F(denominator)

y=(u+v)/2-1
G=matrix(F,[[0,1,(u^2+y^2)/2,(u^2+1)/2],
            [0,0,-(u^2+1)/2,-(u^2+y^2)/(2*y^2)]])
P6=1-u-v+v^2/4+u*v/2-7*u^2/4+u^2*v+u^3-u^3*v+u^4
h=u*(u+v)*(u+v-4)*P6/4
alpha=(1-y^2)*(y^2-u^4)
Q=-u^4+4*u^3*v-4*u^3-4*u^2*v+4*u^2-8*u*v-4*v^2+16*u+16*v-16

checks={}
for axis in ['u','v']:
    gysin=G*B[axis]
    quotient=matrix(F,1,3,[B[axis][1,c]/alpha for c in range(3)])
    e6_split=matrix(F,1,3,[B[axis][0,c]-h*quotient[0,c]
                            for c in range(3)])
    assert all(z==0 for z in gysin.list())
    assert all(z!=0 for z in quotient.list())
    assert all(z!=0 for z in e6_split.list())
    assert all(gcd(R(z.denominator()),Q)==1 for z in B[axis].list())
    checks[axis]={
        'gysin_zero_entries':int(sum(z==0 for z in gysin.list())),
        'gysin_total_entries':int(len(gysin.list())),
        'quotient_nonzero_components':int(sum(z!=0 for z in quotient.list())),
        'e6_split_nonzero_components':int(sum(z!=0 for z in e6_split.list())),
        'Q_denominator_entries':int(sum(gcd(R(z.denominator()),Q)!=1
                                        for z in B[axis].list())),
    }

result={
    'schema':'marici.marked-candidate-algebraic-kernel.v1',
    'candidate_path':candidate_path,
    'candidate_sha256':hashlib.sha256(candidate_bytes).hexdigest(),
    'candidate_certification_status':candidate['certification_status'],
    'checks':checks,
    'interpretation':'candidate image lies in the full split algebraic plane, with nonzero components on both lines and no Q denominator',
    'source_identity_certified':False,
}

with open('research/nima/marked-candidate-algebraic-kernel.json','w') as handle:
    json.dump(result,handle,indent=2,sort_keys=True)
    handle.write('\n')

print(json.dumps(result,indent=2,sort_keys=True))
