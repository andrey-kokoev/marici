"""High-precision quadratic Taylor model of the weakest rank-five pivot."""
import json
from decimal import Decimal as D,localcontext
from pathlib import Path

ROOT=Path(__file__).parents[1]; VARIABLES=5; ORDER=5
payload=json.loads((ROOT/'results'/'central-H-degree-eleven-interval.json').read_text())
f=[(D(a)+D(b))/2 for a,b in payload['F_coefficients_through_degree_twenty_nine']]
zero=(0,)*VARIABLES
def add(a,b):
    out=dict(a)
    for key,value in b.items(): out[key]=out.get(key,D(0))+value
    return {key:value for key,value in out.items() if value}
def add_all(items):
    out=constant(0)
    for item in items: out=add(out,item)
    return out
def neg(a): return {key:-value for key,value in a.items()}
def sub(a,b): return add(a,neg(b))
def scale(a,c): return {key:value*c for key,value in a.items()}
def mul(a,b):
    out={}
    for left,x in a.items():
        for right,y in b.items():
            key=tuple(left[i]+right[i] for i in range(VARIABLES))
            if sum(key)<=ORDER: out[key]=out.get(key,D(0))+x*y
    return {key:value for key,value in out.items() if value}
def constant(x): return {zero:D(x)}
def inv(a):
    a0=a[zero]; remainder=sub(a,constant(a0)); ratio=scale(remainder,D(1)/a0)
    total=constant(1); term=constant(1)
    for _ in range(1,ORDER+1):
        term=neg(mul(term,ratio)); total=add(total,term)
    return scale(total,D(1)/a0)
def div(a,b): return mul(a,inv(b))
def power(a,n):
    out=constant(1)
    for _ in range(n): out=mul(out,a)
    return out

with localcontext() as context:
    context.prec=100
    nodes=[]
    for variable in range(VARIABLES):
        key=tuple(1 if i==variable else 0 for i in range(VARIABLES))
        nodes.append({zero:D('.01'),key:D(1)})
    tables=[]
    for length in range(1,VARIABLES+1):
        h=[constant(1)]+[constant(0)]*29
        for node in nodes[:length]:
            powers=[power(node,q) for q in range(30)]
            h=[add_all(mul(h[d-q],powers[q]) for q in range(d+1)) for d in range(30)]
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
            row.append(value)
        matrix.append(row)
    lower=[[constant(0) for _ in range(VARIABLES)] for _ in range(VARIABLES)]
    diagonal=[]
    for k in range(VARIABLES):
        pivot=matrix[k][k]
        for j in range(k): pivot=sub(pivot,mul(mul(lower[k][j],lower[k][j]),diagonal[j]))
        diagonal.append(pivot); lower[k][k]=constant(1)
        for i in range(k+1,VARIABLES):
            value=matrix[i][k]
            for j in range(k): value=sub(value,mul(mul(lower[i][j],lower[k][j]),diagonal[j]))
            lower[i][k]=div(value,pivot)
    fifth=diagonal[-1]; radius=D('.0005')
    linear=sum(abs(value)*radius for key,value in fifth.items() if sum(key)==1)
    budgets={degree:sum(abs(value)*radius**degree for key,value in fifth.items() if sum(key)==degree)
             for degree in range(1,ORDER+1)}
    result={
        'anchor':['0.01']*5,
        'radius':str(radius),
        'fifth_pivot_constant':str(fifth[zero]),
        'linear_coefficients':{str(key):str(value) for key,value in fifth.items() if sum(key)==1},
        'quadratic_coefficient_count':sum(sum(key)==2 for key in fifth),
        'degree_box_budgets':{str(degree):str(value) for degree,value in budgets.items()},
        'margin_after_degree_five_box':str(fifth[zero]-sum(budgets.values(),D(0))),
        'directed_interval_certified':False,
        'reconnaissance_only':True,
        'rh_proved':False,
    }
if __name__=='__main__':
    output=ROOT/'results'/'central-rank-five-pivot-quadratic-taylor.json'
    output.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    for key,value in result.items(): print(f'{key}={value}')
