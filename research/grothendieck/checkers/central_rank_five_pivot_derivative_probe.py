"""Differentiate Newton-LDL pivots at the weakest confluent rank-five anchor."""
import json,math
from decimal import Decimal as D
from pathlib import Path

import central_rank_five_loewner_grid as G

I=G.I; N=5; nodes=[D('.01')]*5
H=[G.homogeneous(nodes[:i+1]) for i in range(N)]
def derivative_h(h,x):
    return [I.box(0)]+[
        I.add(*(I.scale(I.mul(I.powi(I.box(x),q-1),h[d-q]),q) for q in range(1,d+1)))
        for d in range(1,30)]
DH=[derivative_h(H[i],nodes[0]) for i in range(N)]
def derivative_tail(i,j,variable):
    multiplicity=int(variable<=i)+int(variable<=j); m=i+j+1; value=D(0)
    for p in range(29,201):
        falling=math.factorial(p)//math.factorial(p-m)
        term=I.up.multiply(D(multiplicity)*G.M,D(falling)*G.R**(p-m))
        value=I.up.add(value,I.up.divide(term,D(math.factorial(i)*math.factorial(j))))
    first=I.up.divide(I.up.multiply(D(multiplicity)*G.M,D(201**m)*G.R**(201-m)),
                      D(math.factorial(i)*math.factorial(j)))
    return I.up.add(value,I.up.divide(first,D('.989')))
def derivative_entry(i,j,variable):
    value=I.box(0)
    for n in range(1,len(G.f)):
        for k in range(i,n):
            ell=n-1-k
            if ell<j: continue
            factor=I.box(0)
            if variable<=i: factor=I.add(factor,I.mul(DH[i][k-i],H[j][ell-j]))
            if variable<=j: factor=I.add(factor,I.mul(H[i][k-i],DH[j][ell-j]))
            value=I.add(value,I.mul(G.f[n],factor))
    error=derivative_tail(i,j,variable)
    return I.add(value,(error.copy_negate(),error))
def dual_pivots(a,da):
    lower=[[I.box(0) for _ in range(N)] for _ in range(N)]
    dlower=[[I.box(0) for _ in range(N)] for _ in range(N)]
    diagonal=[]; ddiagonal=[]
    for k in range(N):
        pivot=a[k][k]; dpivot=da[k][k]
        for j in range(k):
            pivot=I.sub(pivot,I.mul(I.mul(lower[k][j],lower[k][j]),diagonal[j]))
            dpivot=I.sub(dpivot,I.add(
                I.mul(I.mul(I.scale(lower[k][j],2),dlower[k][j]),diagonal[j]),
                I.mul(I.mul(lower[k][j],lower[k][j]),ddiagonal[j])))
        diagonal.append(pivot); ddiagonal.append(dpivot); lower[k][k]=I.box(1)
        for i in range(k+1,N):
            numerator=a[i][k]; dnumerator=da[i][k]
            for j in range(k):
                numerator=I.sub(numerator,I.mul(I.mul(lower[i][j],lower[k][j]),diagonal[j]))
                dnumerator=I.sub(dnumerator,I.add(
                    I.mul(I.mul(dlower[i][j],lower[k][j]),diagonal[j]),
                    I.mul(I.mul(lower[i][j],dlower[k][j]),diagonal[j]),
                    I.mul(I.mul(lower[i][j],lower[k][j]),ddiagonal[j])))
            lower[i][k]=I.div(numerator,pivot)
            dlower[i][k]=I.div(I.sub(dnumerator,I.mul(lower[i][k],dpivot)),pivot)
    return diagonal,ddiagonal

A=G.matrix(nodes); rows=[]
for variable in range(N):
    dA=[[derivative_entry(i,j,variable) for j in range(N)] for i in range(N)]
    diagonal,ddiagonal=dual_pivots(A,dA)
    rows.append((diagonal,ddiagonal))
fifth_bounds=[max(abs(row[1][-1][0]),abs(row[1][-1][1])) for row in rows]
local_half_step_cost=I.up.multiply(D('.0005'),sum(fifth_bounds,D(0)))
fifth_lower=rows[0][0][-1][0]
result={
    'anchor':[str(x) for x in nodes],
    'fifth_pivot_interval':[str(x) for x in rows[0][0][-1]],
    'fifth_pivot_coordinate_derivative_intervals':[[str(a),str(b)] for _,derivatives in rows for a,b in [derivatives[-1]]],
    'fifth_pivot_coordinate_derivative_absolute_bounds':[str(x) for x in fifth_bounds],
    'linearized_half_grid_transport_cost':str(local_half_step_cost),
    'fifth_pivot_margin_after_linearized_cost':str(I.down.subtract(fifth_lower,local_half_step_cost)),
    'local_derivative_probe_only':True,
    'global_cell_derivative_enclosure_still_required':True,
    'directed_decimal_rounding':True,
    'rh_proved':False,
}
if __name__=='__main__':
    output=Path(__file__).parents[1]/'results'/'central-rank-five-pivot-derivative-probe.json'
    output.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    for key,value in result.items(): print(f'{key}={value}')
