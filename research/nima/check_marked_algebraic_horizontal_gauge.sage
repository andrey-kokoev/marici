import json
import hashlib

R.<u,v> = PolynomialRing(QQ)
F = R.fraction_field()

y = (u+v)/2-1
Ptop = u*(u-2)*(v-2)
P6 = 1-u-v+v^2/4+u*v/2-7*u^2/4+u^2*v+u^3-u^3*v+u^4
D1 = (v-u)*(y-u^2)*(y+u^2)
Q = -u^4+4*u^3*v-4*u^3-4*u^2*v+4*u^2-8*u*v-4*v^2+16*u+16*v-16
h = u*(u+v)*(u+v-4)*P6/4
alpha = (1-y^2)*(y^2-u^4)
v_beta = 2*(u^2+y^2)
v_gamma = -2*y^2*(u^2+1)
split_line = matrix(F, 1, 4, [h, alpha, v_beta, v_gamma])

connection_path = 'research/benincasa/bivariate_soft_gram_connection.json'
wall_path = 'research/benincasa/marked-wall-quotient-connection.json'
connection_bytes = open(connection_path,'rb').read()
wall_bytes = open(wall_path,'rb').read()
connection = json.loads(connection_bytes)
wall = json.loads(wall_bytes)

Dwall = F(sage_eval(wall['D'],locals={'u':u,'v':v}))
Hwall = F(sage_eval(wall['H'],locals={'u':u,'v':v}))

def parse(s):
    return F(sage_eval(s,locals={'u':u,'v':v,'D':Dwall,'H':Hwall}))

def wall_matrix(axis):
    d=wall[axis]
    return matrix(F,[[parse(d['alpha']),0,0],
                     [parse(d['beta1']),parse(d['gamma1']),0],
                     [parse(d['beta2']),0,parse(d['gamma2'])]])

def final_matrix(key):
    A=matrix(F,[[parse(z) for z in row] for row in connection[key]])
    return A.matrix_from_rows_and_columns([5,6,7,8],[5,6,7,8])

Wu = wall_matrix('u').transpose()
Wv = wall_matrix('v').transpose()
A4u = final_matrix('connection_u').transpose()
A4v = final_matrix('connection_v').transpose()

# The first marked coefficient coordinate is the top quotient.  Entry 867's
# second algebraic line is v_alg+h*e6, and its character differs from the
# top character by dlog(Ptop*D1).  This gives the surviving triangular gauge.
top_to_split = 1/(Ptop*D1)
X = matrix(F, 3, 4, [top_to_split*z for z in split_line[0]] + [0]*8)

checks = {}
for name,t,W,A4 in [('u',u,Wu,A4u),('v',v,Wv,A4v)]:
    residual = X.derivative(t)-W*X+X*A4
    assert residual == 0
    checks[name] = {'horizontal_residual_zero':True}

denominator_lcm = lcm([R(z.denominator()) for z in X.list() if z != 0])
assert gcd(denominator_lcm,Q) == 1
assert X.rank() == 1

result = {
    'schema':'marici.marked-algebraic-horizontal-gauge.v1',
    'field':'QQ(u,v)',
    'coefficient_convention':'transpose packet matrices; nabla=d-A',
    'connection_sha256':hashlib.sha256(connection_bytes).hexdigest(),
    'wall_connection_sha256':hashlib.sha256(wall_bytes).hexdigest(),
    'generator':'(Ptop*D1)^(-1) q_top^vee tensor (v_alg+h e6)',
    'rank':int(X.rank()),
    'checks':checks,
    'denominator_lcm_factorization':str(factor(denominator_lcm)),
    'Q_coprime_denominator':True,
    'candidate_independent':True,
    'status':'exact_horizontal_gauge_pass',
}

with open('research/nima/marked-algebraic-horizontal-gauge.json','w') as handle:
    json.dump(result,handle,indent=2,sort_keys=True)
    handle.write('\n')

print(json.dumps(result,indent=2,sort_keys=True))
