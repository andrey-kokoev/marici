import json
import hashlib
from sage.misc.sage_eval import sage_eval

R.<u,v> = PolynomialRing(QQ)
F=R.fraction_field()
Q=-u^4+4*u^3*v-4*u^3-4*u^2*v+4*u^2-8*u*v-4*v^2+16*u+16*v-16
D=-4+12*u-6*u*v+4*v-9*u^2+4*u^2*v-v^2
H=-2-3*u+2*u*v+v-u^2*v+u^3

paths=['research/benincasa/bivariate_soft_gram_connection.json',
       'research/benincasa/marked-wall-quotient-connection.json']
packet_bytes=[open(path,'rb').read() for path in paths]
packets=[json.loads(data) for data in packet_bytes]

def parse(x):
    return F(sage_eval(str(x).replace('^','**'),locals={'u':u,'v':v,'D':D,'H':H}))

den=R(1)
for key in ['connection_u','connection_v']:
    for row in packets[0][key]:
        for x in row:
            den=lcm(den,R(parse(x).denominator()))
for axis in ['u','v']:
    for key in ['alpha','beta1','gamma1','beta2','gamma2']:
        den=lcm(den,R(parse(packets[1][axis][key]).denominator()))

factors=[R(f) for f,e in factor(den)]

S.<x,y> = PolynomialRing(QQ)
def initial(poly,u0,v0):
    shifted=S(poly(u=u0+x,v=v0+y))
    degrees=[sum(mon) for mon,c in shifted.dict().items() if c != 0]
    order=min(degrees)
    form=sum(c*x^mon[0]*y^mon[1] for mon,c in shifted.dict().items() if sum(mon)==order)
    return order,S(form)

records=[]
for point in [(2,2),(0,2)]:
    van=[f for f in factors if f(u=point[0],v=point[1])==0]
    q_order,q_initial=initial(Q,*point)
    records.append({
        'point':[int(q) for q in point],
        'vanishing_connection_factors':[str(factor(f)) for f in van],
        'Q_order':int(q_order),
        'Q_initial':str(q_initial),
        'carrier_initials':[{
            'factor':str(factor(f)),
            'order':int(initial(f,*point)[0]),
            'initial':str(initial(f,*point)[1]),
        } for f in van],
    })

assert records[0]['Q_initial'] == '-4*x^2 + 24*x*y - 4*y^2'
assert records[1]['Q_initial'] == '-4*x^2 - 8*x*y - 4*y^2'

# In the blowup chart x=r, y=r*t, the first tangent cone cuts the
# exceptional divisor at t^2-6t+1=0.  Its roots are distinct from the
# existing connection directions t=0,1,infinity.  At (0,2), the tangent
# cone is -4(x+y)^2 and hence the doubled existing direction t=-1.
T.<t> = PolynomialRing(QQ)
q22_exceptional=t^2-6*t+1
assert q22_exceptional.discriminant() == 32
assert q22_exceptional(0) != 0 and q22_exceptional(1) != 0
q02_exceptional=(t+1)^2

result={
    'schema':'marici.deep-quartic-local-carriers.v1',
    'records':records,
    'blowup':{
        '(2,2)':{
            'Q_exceptional_equation':str(q22_exceptional),
            'Q_exceptional_points':'t=3+-2*sqrt(2)',
            'existing_directions':['t=0 (v-2)','t=1 (u-v)','t=infinity (u-2)'],
            'new_exceptional_direction':True,
        },
        '(0,2)':{
            'Q_exceptional_equation':str(q02_exceptional),
            'Q_exceptional_point':'t=-1 with multiplicity two',
            'existing_direction':'u+v-2 has initial x+y and the same t=-1 point',
            'new_exceptional_direction':False,
        },
    },
    'connection_factor_count':int(len(factors)),
    'source_hashes':{path:hashlib.sha256(data).hexdigest()
                     for path,data in zip(paths,packet_bytes)},
    'status':'deep_quartic_tangent_directions_classified',
    'scope':'carrier and tangent-cone classification only; no coefficient or physical activation claimed',
}

with open('research/nima/deep-quartic-local-carriers.json','w') as handle:
    json.dump(result,handle,indent=2,sort_keys=True)
    handle.write('\n')

print(json.dumps(result,indent=2,sort_keys=True))
