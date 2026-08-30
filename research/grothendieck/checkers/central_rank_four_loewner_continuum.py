"""Directed continuum rank-four Loewner positivity on [0,0.01]."""
import itertools,json,math
from decimal import Decimal as D
from pathlib import Path

import central_rank_four_loewner_grid as G

I=G.I; C=G.C; X=(D(0),D('.01')); STEP=D('.001'); HALF=STEP/D(2)

# All nearest-grid anchors, including confluent configurations.
points=[D(i)/D(1000) for i in range(11)]
anchors=[(G.determinant(G.matrix(nodes)),nodes)
         for nodes in itertools.combinations_with_replacement(points,4)]
weakest=min(anchors,key=lambda row:row[0][0])
assert all(value[0]>0 for value,_ in anchors)

def homogeneous(count,max_degree=23):
    h=[I.box(1)]+[I.box(0)]*max_degree
    for _ in range(count):
        h=[I.add(*(I.mul(h[d-q],I.powi(X,q)) for q in range(d+1)))
           for d in range(max_degree+1)]
    return h
def derivative_h(h,max_degree=23):
    return [I.box(0)]+[
        I.add(*(I.scale(I.mul(I.powi(X,q-1),h[d-q]),q) for q in range(1,d+1)))
        for d in range(1,max_degree+1)]

H=[homogeneous(i+1) for i in range(4)]; DH=[derivative_h(H[i]) for i in range(4)]
def matrix_entry(i,j,variable=None):
    value=I.box(0)
    for n in range(1,len(C.f)):
        for k in range(i,n):
            ell=n-1-k
            if ell<j: continue
            if variable is None:
                factor=I.mul(H[i][k-i],H[j][ell-j])
            else:
                factor=I.box(0)
                if variable<=i: factor=I.add(factor,I.mul(DH[i][k-i],H[j][ell-j]))
                if variable<=j: factor=I.add(factor,I.mul(H[i][k-i],DH[j][ell-j]))
            value=I.add(value,I.mul(C.f[n],factor))
    if variable is None:
        tail=C.derivative_tail(i,j)
    else:
        multiplicity=int(variable<=i)+int(variable<=j); m=i+j+1; tail=D(0); r=D('.01')
        for p in range(23,201):
            falling=math.factorial(p)//math.factorial(p-m)
            term=I.up.multiply(D(multiplicity)*C.M,D(falling)*r**(p-m))
            tail=I.up.add(tail,I.up.divide(term,D(math.factorial(i)*math.factorial(j))))
        first=I.up.divide(I.up.multiply(D(multiplicity)*C.M,D(201**m)*r**(201-m)),
                          D(math.factorial(i)*math.factorial(j)))
        tail=I.up.add(tail,I.up.divide(first,D('.989')))
    return I.add(value,(tail.copy_negate(),tail))

A=[[matrix_entry(i,j) for j in range(4)] for i in range(4)]
def det3(rows,columns):
    value=I.box(0)
    for permutation in itertools.permutations(columns):
        inversions=sum(permutation[a]>permutation[b] for a in range(3) for b in range(a+1,3))
        term=I.box(1)
        for a,j in enumerate(permutation): term=I.mul(term,A[rows[a]][j])
        value=I.add(value,I.neg(term) if inversions%2 else term)
    return value
cofactor=[]
for i in range(4):
    row=[]
    for j in range(4):
        value=det3([r for r in range(4) if r!=i],[q for q in range(4) if q!=j])
        row.append(I.neg(value) if (i+j)%2 else value)
    cofactor.append(row)

derivative_bounds=[]
for variable in range(4):
    derivative=I.box(0)
    for i in range(4):
        for j in range(4): derivative=I.add(derivative,I.mul(cofactor[i][j],matrix_entry(i,j,variable)))
    derivative_bounds.append(max(abs(derivative[0]),abs(derivative[1])))
transport_cost=I.up.multiply(HALF,sum(derivative_bounds,D(0)))
continuum_lower=I.down.subtract(weakest[0][0],transport_cost)
assert continuum_lower>0

result={
    'domain':['0','0.01'],
    'nondecreasing_anchor_count':len(anchors),
    'weakest_anchor':[str(x) for x in weakest[1]],
    'weakest_anchor_normalized_determinant_interval':[str(x) for x in weakest[0]],
    'global_coordinate_derivative_absolute_bounds':[str(x) for x in derivative_bounds],
    'nearest_grid_transport_cost_upper':str(transport_cost),
    'continuum_normalized_rank_four_lower_bound':str(continuum_lower),
    'all_distinct_rank_four_Loewner_minors_strictly_positive':True,
    'confluent_limits_nonnegative':True,
    'directed_decimal_rounding':True,
    'analytic_tail_bounds_included':True,
    'interval_certified':True,
    'zero_locations_used':False,
    'rh_proved':False,
}
if __name__=='__main__':
    output=Path(__file__).parents[1]/'results'/'central-rank-four-loewner-continuum.json'
    output.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    for key,value in result.items(): print(f'{key}={value}')
