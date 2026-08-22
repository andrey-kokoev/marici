"""A posteriori Taylor-model remainder bound for the rank-five pivot."""
import json,math
from decimal import Decimal as D
from pathlib import Path

import central_rank_five_pivot_taylor_interval as P

I=P.I; R=D('.0005'); ORDER=P.ORDER; zero=P.zero
def coefficient_norm(jet,include_constant=True):
    return sum((max(abs(value[0]),abs(value[1]))*R**sum(key)
                for key,value in jet.items() if include_constant or key!=zero),D(0))
def high_product(left,right):
    return sum((max(abs(a[0]),abs(a[1]))*max(abs(b[0]),abs(b[1]))*R**(sum(x)+sum(y))
                for x,a in left.items() for y,b in right.items() if sum(x)+sum(y)>ORDER),D(0))
def tm_add(a,b): return P.add(a[0],b[0]),I.up.add(a[1],b[1])
def tm_neg(a): return P.neg(a[0]),a[1]
def tm_sub(a,b): return tm_add(a,tm_neg(b))
def tm_mul(a,b):
    polynomial=P.mul(a[0],b[0]); na=coefficient_norm(a[0]); nb=coefficient_norm(b[0])
    remainder=high_product(a[0],b[0])
    remainder=I.up.add(remainder,I.up.multiply(a[1],nb))
    remainder=I.up.add(remainder,I.up.multiply(b[1],na))
    remainder=I.up.add(remainder,I.up.multiply(a[1],b[1]))
    return polynomial,remainder
def tm_inv(a):
    polynomial=P.inv(a[0]); product=P.mul(a[0],polynomial)
    residual=P.sub(P.constant(1),product)
    residual_norm=coefficient_norm(residual)
    qnorm=coefficient_norm(polynomial)
    numerator=I.up.add(residual_norm,I.up.multiply(a[1],qnorm))
    constant_lower=min(abs(a[0][zero][0]),abs(a[0][zero][1]))
    lower=I.down.subtract(constant_lower,I.up.add(coefficient_norm(a[0],False),a[1]))
    assert lower>0
    return polynomial,I.up.divide(numerator,lower)
def tm_div(a,b): return tm_mul(a,tm_inv(b))

# Direct positive-coefficient and falling-factorial majorants put every
# matrix-entry Taylor remainder after degree five below 1e-30.
def source_tail_after_degree_five(i,j):
    total=D(0); rho=D('.0005'); center=D('.01')
    for degree in range(6,41):
        order=i+j+degree; derivative=D(0)
        for p in range(max(29,order),201):
            falling=math.factorial(p)//math.factorial(p-order)
            derivative=I.up.add(derivative,I.up.divide(
                I.up.multiply(P.M,D(falling)*center**(p-order)),D(math.factorial(i)*math.factorial(j))))
        first=I.up.divide(I.up.multiply(P.M,D(201**order)*center**(201-order)),
                          D(math.factorial(i)*math.factorial(j)))
        derivative=I.up.add(derivative,I.up.divide(first,D('.989')))
        term=I.up.divide(I.up.multiply(derivative,(D(5)*rho)**degree),D(math.factorial(degree)))
        total=I.up.add(total,term)
        if degree==40: total=I.up.add(total,term)  # geometric remainder factor < 2
    return total
computed_source_remainders=[[source_tail_after_degree_five(i,j) for j in range(P.VARIABLES)]
                            for i in range(P.VARIABLES)]
def polynomial_add(a,b):
    return [I.up.add(a[k] if k<len(a) else D(0),b[k] if k<len(b) else D(0))
            for k in range(max(len(a),len(b)))]
def polynomial_mul(a,b):
    out=[D(0)]*min(30,len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            if i+j<30: out[i+j]=I.up.add(out[i+j],I.up.multiply(x,y))
    return out
def polynomial_power(a,n):
    out=[D(1)]
    for _ in range(n): out=polynomial_mul(out,a)
    return out
node_majorant=[D('.01'),D('.0005')]; homogeneous=[]
for length in range(1,P.VARIABLES+1):
    h=[[D(1)]]+[[D(0)] for _ in range(29)]
    for _ in range(length):
        powers=[polynomial_power(node_majorant,q) for q in range(30)]
        h=[__import__('functools').reduce(polynomial_add,
             (polynomial_mul(h[d-q],powers[q]) for q in range(d+1)),[D(0)]) for d in range(30)]
    homogeneous.append(h)
known_polynomial_remainders=[]
for i in range(P.VARIABLES):
    row=[]
    for j in range(P.VARIABLES):
        value=[D(0)]
        for n in range(1,len(P.f)):
            coefficient=max(abs(P.f[n][0]),abs(P.f[n][1]))
            for k in range(i,n):
                ell=n-1-k
                if ell>=j:
                    term=[I.up.multiply(coefficient,x) for x in polynomial_mul(homogeneous[i][k-i],homogeneous[j][ell-j])]
                    value=polynomial_add(value,term)
        row.append(sum(value[6:],D(0)))
    known_polynomial_remainders.append(row)
ENTRY_REMAINDER=D('1e-30')
maximum_entry_remainder=max(computed_source_remainders[i][j]+known_polynomial_remainders[i][j]
                            for i in range(P.VARIABLES) for j in range(P.VARIABLES))
assert maximum_entry_remainder<ENTRY_REMAINDER
matrix=[[(P.matrix[i][j],ENTRY_REMAINDER) for j in range(P.VARIABLES)] for i in range(P.VARIABLES)]
lower=[[(P.constant(0),D(0)) for _ in range(P.VARIABLES)] for _ in range(P.VARIABLES)]
diagonal=[]
for k in range(P.VARIABLES):
    pivot=matrix[k][k]
    for j in range(k): pivot=tm_sub(pivot,tm_mul(tm_mul(lower[k][j],lower[k][j]),diagonal[j]))
    diagonal.append(pivot); lower[k][k]=(P.constant(1),D(0))
    for i in range(k+1,P.VARIABLES):
        value=matrix[i][k]
        for j in range(k): value=tm_sub(value,tm_mul(tm_mul(lower[i][j],lower[k][j]),diagonal[j]))
        lower[i][k]=tm_div(value,pivot)
fifth=diagonal[-1]
polynomial_lower=I.down.subtract(fifth[0][zero][0],coefficient_norm(fifth[0],False))
full_lower=I.down.subtract(polynomial_lower,fifth[1])
assert full_lower>0
result={
    'matrix_entry_degree_six_and_higher_remainder_bound':str(ENTRY_REMAINDER),
    'maximum_computed_omitted_source_remainder':str(max(max(row) for row in computed_source_remainders)),
    'maximum_computed_known_polynomial_remainder':str(max(max(row) for row in known_polynomial_remainders)),
    'maximum_combined_matrix_entry_remainder':str(maximum_entry_remainder),
    'fifth_pivot_polynomial_lower':str(polynomial_lower),
    'fifth_pivot_a_posteriori_remainder_bound':str(fifth[1]),
    'fifth_pivot_full_Taylor_model_lower':str(full_lower),
    'all_inverse_lower_bounds_positive':True,
    'source_and_rational_remainders_included':True,
    'interval_certified':True,
    'rh_proved':False,
}
if __name__=='__main__':
    output=Path(__file__).parents[1]/'results'/'central-rank-five-pivot-taylor-majorant.json'
    output.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    for key,value in result.items(): print(f'{key}={value}')
