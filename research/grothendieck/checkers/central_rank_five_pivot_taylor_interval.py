"""Directed degree-five Taylor coefficients for the degree-29 source pivot."""
import itertools,json,math,os,sys
from decimal import Decimal as D
from pathlib import Path

import reduced_source_central_interval_chords as I

ROOT=Path(__file__).parents[1]; VARIABLES=int(os.environ.get('MARICI_TAYLOR_VARIABLES','5')); ORDER=5; zero=(0,)*VARIABLES
payload=json.loads((ROOT/'results'/'central-H-degree-eleven-interval.json').read_text())
f=[(D(a),D(b)) for a,b in payload['F_coefficients_through_degree_forty_nine']]
SOURCE_DEGREE=len(f)-1
M=D('6.038308')
_anchor_arg=next((arg.split('=',1)[1] for arg in sys.argv[1:] if arg.startswith('--anchor=')),None)
_anchor_text=_anchor_arg or os.environ.get('MARICI_TAYLOR_ANCHOR',','.join(['.01']*VARIABLES))
ANCHOR=tuple(D(value.strip()) for value in _anchor_text.split(','))
if len(ANCHOR)!=VARIABLES:
    raise ValueError(f'MARICI_TAYLOR_ANCHOR requires {VARIABLES} comma-separated values')
if any(value<0 or value>D('.01') for value in ANCHOR):
    raise ValueError('Taylor anchors must lie in [0,0.01]')
CENTER=max(ANCHOR)
INJECT_SOURCE_TAIL='--finite-source-only' not in sys.argv
_radius_arg=next((arg.split('=',1)[1] for arg in sys.argv[1:] if arg.startswith('--radius=')),None)
RADIUS=D(_radius_arg or '.0005')
if RADIUS<=0 or CENTER+RADIUS>=1:
    raise ValueError('Taylor radius must be positive and remain inside the unit source disk')
def up_pow(base,exponent): return I.up.power(base,D(exponent))
def add(a,b):
    out=dict(a)
    for key,value in b.items(): out[key]=I.add(out.get(key,I.box(0)),value)
    return out
def add_all(items):
    out=constant(0)
    for item in items: out=add(out,item)
    return out
def neg(a): return {key:I.neg(value) for key,value in a.items()}
def sub(a,b): return add(a,neg(b))
def scale(a,c): return {key:I.mul(value,c) for key,value in a.items()}
def degree_buckets(a):
    out={}
    for key,value in a.items(): out.setdefault(sum(key),[]).append((key,value))
    return out
def mul(a,b):
    out={}
    left_buckets=degree_buckets(a); right_buckets=degree_buckets(b)
    for left_degree,left_items in left_buckets.items():
        for right_degree,right_items in right_buckets.items():
            if left_degree+right_degree>ORDER: continue
            for left,x in left_items:
                for right,y in right_items:
                    key=tuple(left[i]+right[i] for i in range(VARIABLES))
                    out[key]=I.add(out.get(key,I.box(0)),I.mul(x,y))
    return out
def constant(x): return {zero:I.box(x)}
def inv(a):
    inverse_constant=I.inv(a[zero]); remainder={key:value for key,value in a.items() if key!=zero}
    ratio=scale(remainder,inverse_constant); total=constant(1); term=constant(1)
    for _ in range(1,ORDER+1):
        term=neg(mul(term,ratio)); total=add(total,term)
    return scale(total,inverse_constant)
def div(a,b): return mul(a,inv(b))
def power(a,n):
    out=constant(1)
    for _ in range(n): out=mul(out,a)
    return out
multiindices=[key for key in itertools.product(range(ORDER+1),repeat=VARIABLES) if sum(key)<=ORDER]
tail_derivative_cache={}
def tail_derivative(i,j,degree):
    cache_key=(i,j,degree)
    if cache_key in tail_derivative_cache: return tail_derivative_cache[cache_key]
    order=i+j+degree; value=D(0)
    for p in range(SOURCE_DEGREE,201):
        falling=math.factorial(p)//math.factorial(p-order)
        term=I.up.multiply(M,I.up.multiply(D(falling),up_pow(CENTER,p-order)))
        value=I.up.add(value,I.up.divide(term,D(math.factorial(i)*math.factorial(j))))
    first=I.up.divide(I.up.multiply(M,I.up.multiply(D(201**order),up_pow(CENTER,201-order))),
                      D(math.factorial(i)*math.factorial(j)))
    value=I.up.add(value,I.up.divide(first,D('.989')))
    tail_derivative_cache[cache_key]=value
    return value
def inject_source_tail(jet,i,j):
    if not INJECT_SOURCE_TAIL: return jet
    out=dict(jet)
    for key in multiindices:
        denominator=math.prod(math.factorial(component) for component in key)
        error=I.up.divide(tail_derivative(i,j,sum(key)),D(denominator))
        out[key]=I.add(out.get(key,I.box(0)),(error.copy_negate(),error))
    return out

nodes=[]
for variable in range(VARIABLES):
    key=tuple(1 if i==variable else 0 for i in range(VARIABLES))
    nodes.append({zero:I.box(ANCHOR[variable]),key:I.box(1)})
tables=[]; h=[constant(1)]+[constant(0)]*SOURCE_DEGREE
for node in nodes:
    powers=[power(node,q) for q in range(SOURCE_DEGREE+1)]
    h=[add_all(mul(h[d-q],powers[q]) for q in range(d+1)) for d in range(SOURCE_DEGREE+1)]
    tables.append(h)
matrix=[]
for i in range(VARIABLES):
    row=[]
    for j in range(VARIABLES):
        value=constant(0)
        for n in range(1,len(f)):
            for k in range(i,n):
                ell=n-1-k
                if ell>=j: value=add(value,scale(mul(tables[i][k-i],tables[j][ell-j]),f[n]))
        row.append(inject_source_tail(value,i,j))
    matrix.append(row)
lower=[[constant(0) for _ in range(VARIABLES)] for _ in range(VARIABLES)]; diagonal=[]
for k in range(VARIABLES):
    pivot=matrix[k][k]
    for j in range(k): pivot=sub(pivot,mul(mul(lower[k][j],lower[k][j]),diagonal[j]))
    diagonal.append(pivot); lower[k][k]=constant(1)
    for i in range(k+1,VARIABLES):
        value=matrix[i][k]
        for j in range(k): value=sub(value,mul(mul(lower[i][j],lower[k][j]),diagonal[j]))
        lower[i][k]=div(value,pivot)
fifth=diagonal[-1]; radius=RADIUS
budgets={}
for degree in range(1,ORDER+1):
    budget=D(0)
    for key,value in fifth.items():
        if sum(key)==degree:
            term=I.up.multiply(max(abs(value[0]),abs(value[1])),up_pow(radius,degree))
            budget=I.up.add(budget,term)
    budgets[degree]=budget
total_budget=D(0)
for budget in budgets.values(): total_budget=I.up.add(total_budget,budget)
margin=I.down.subtract(fifth[zero][0],total_budget)
derivative_box_uppers=[]
for variable in range(VARIABLES):
    upper=D(0)
    for key,value in fifth.items():
        if not key[variable]: continue
        if sum(key)==1:
            upper=I.up.add(upper,value[1])
        else:
            coefficient=max(abs(value[0]),abs(value[1]))
            term=I.up.multiply(D(key[variable])*coefficient,up_pow(radius,sum(key)-1))
            upper=I.up.add(upper,term)
    derivative_box_uppers.append(upper)
if VARIABLES == 5:
    assert margin > 0
result={
    'anchor':[str(value) for value in ANCHOR],
    'radius':str(radius),
    'fifth_pivot_constant_interval':[str(x) for x in fifth[zero]],
    'fifth_pivot_coordinate_derivative_intervals':[
        [str(x) for x in fifth[tuple(1 if i==variable else 0 for i in range(VARIABLES))]]
        for variable in range(VARIABLES)],
    'degree_box_budget_uppers':{str(degree):str(value) for degree,value in budgets.items()},
    'coordinate_derivative_degree_five_box_uppers':[str(value) for value in derivative_box_uppers],
    'degree_five_polynomial_coordinatewise_decreasing':all(value<0 for value in derivative_box_uppers),
    'degree_five_polynomial_margin_lower':str(margin),
    'source_polynomial_degree':SOURCE_DEGREE,
    'finite_source_polynomial_interval_certified':True,
    'omitted_source_analytic_tail_through_Taylor_degree_five_injected':INJECT_SOURCE_TAIL,
    'omitted_source_tail_beyond_Taylor_degree_five_certified':False,
    'rational_Taylor_remainder_beyond_degree_five_certified':False,
    'directed_decimal_rounding':True,
    'directed_scalar_arithmetic_version':2,
    'rh_proved':False,
}
if __name__=='__main__':
    output=ROOT/'results'/'central-rank-five-pivot-taylor-interval.json'
    output.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    for key,value in result.items(): print(f'{key}={value}')
