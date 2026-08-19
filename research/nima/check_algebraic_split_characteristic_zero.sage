import json
import hashlib

R.<u,v> = PolynomialRing(QQ)
F = R.fraction_field()

y = (u+v)/2-1
P6 = 1-u-v+v^2/4+u*v/2-7*u^2/4+u^2*v+u^3-u^3*v+u^4
D1 = (v-u)*(y-u^2)*(y+u^2)
h = u*(u+v)*(u+v-4)*P6/4

alpha = (1-y^2)*(y^2-u^4)
beta = 2*(u^2+y^2)
gamma = -2*y^2*(u^2+1)
K = matrix(F, [[1,0,0,0], [0,alpha,beta,gamma]])

connection_path = 'research/benincasa/bivariate_soft_gram_connection.json'
with open(connection_path,'rb') as handle:
    connection_bytes = handle.read()
packet = json.loads(connection_bytes)

def parse_matrix(key):
    return matrix(F, [[F(sage_eval(q,locals={'u':u,'v':v})) for q in row]
                      for row in packet[key]])

checks = {}
for name,t,A in [('u',u,parse_matrix('connection_u')),
                 ('v',v,parse_matrix('connection_v'))]:
    # The packet records derivatives of basis masters by rows.  Coefficient
    # columns therefore use the transposed final block.
    A4 = A.matrix_from_rows_and_columns([5,6,7,8],[5,6,7,8]).transpose()
    E = K.derivative(t) + K*A4
    g00 = E[0,0]
    g01 = E[0,1]/alpha
    g10 = E[1,0]
    g11 = E[1,1]/alpha
    G = matrix(F, [[g00,g01],[g10,g11]])
    closure = E-G*K
    split_residual = h.derivative(t)+(g00-g11)*h+g10

    assert closure == 0
    assert g01 == 0
    assert g00 == -P6.derivative(t)/(2*P6)
    assert g11 == D1.derivative(t)/D1
    assert split_residual == 0
    checks[name] = {
        'plane_closure':True,
        'g01_zero':True,
        'g00_minus_half_dlog_P6':True,
        'g11_dlog_D1':True,
        'split_residual_zero':True,
    }

result = {
    'schema':'marici.algebraic-split-characteristic-zero.v1',
    'field':'QQ(u,v)',
    'connection_packet':connection_path,
    'connection_sha256':hashlib.sha256(connection_bytes).hexdigest(),
    'matrix_action':'transpose final 4x4 block for coefficient columns',
    'h':str(factor(h)),
    'checks':checks,
    'status':'exact_characteristic_zero_split',
    'Q_denominator_power':int(0),
}

with open('research/nima/algebraic-split-characteristic-zero.json','w') as handle:
    json.dump(result,handle,indent=2,sort_keys=True)
    handle.write('\n')

print(json.dumps(result,indent=2,sort_keys=True))
