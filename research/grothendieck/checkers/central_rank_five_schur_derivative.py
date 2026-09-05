"""Directed Schur-complement decomposition of the rank-five pivot derivative."""
import json
from pathlib import Path

import central_rank_five_pivot_taylor_interval as P

I=P.I; N=P.VARIABLES; zero=P.zero
assert N==5
unit=[tuple(1 if i==variable else 0 for i in range(N)) for variable in range(N)]
def constant(jet): return jet[zero]
def derivative(jet,variable): return jet.get(unit[variable],I.box(0))
def add_all(terms): return I.add(*terms) if terms else I.box(0)

# The leading 4-by-4 LDL factorization of the full matrix factors A.
L=[[constant(P.lower[i][j]) for j in range(4)] for i in range(4)]
D=[constant(P.diagonal[i]) for i in range(4)]
b=[constant(P.matrix[i][4]) for i in range(4)]
y=[]
for i in range(4):
    y.append(I.sub(b[i],add_all(I.mul(L[i][j],y[j]) for j in range(i))))
z=[I.div(y[i],D[i]) for i in range(4)]
c=[I.box(0) for _ in range(4)]
for i in reversed(range(4)):
    c[i]=I.sub(z[i],add_all(I.mul(L[j][i],c[j]) for j in range(i+1,4)))

rows=[]
for variable in range(N):
    direct=derivative(P.fifth,variable)
    corner=derivative(P.matrix[4][4],variable)
    cross=I.neg(I.scale(add_all(I.mul(derivative(P.matrix[i][4],variable),c[i])
                                    for i in range(4)),2))
    leading=add_all(I.mul(I.mul(c[i],derivative(P.matrix[i][j],variable)),c[j])
                    for i in range(4) for j in range(4))
    schur=I.add(corner,cross,leading)
    assert schur[0]<=direct[0] and direct[1]<=schur[1]
    rows.append({
        'coordinate':variable,
        'corner_derivative':[str(x) for x in corner],
        'negative_twice_cross_term':[str(x) for x in cross],
        'leading_block_quadratic_term':[str(x) for x in leading],
        'schur_derivative_enclosure':[str(x) for x in schur],
        'direct_ldl_derivative':[str(x) for x in direct],
        'schur_encloses_direct':True,
    })
result={
    'anchor':[str(value) for value in P.ANCHOR],
    'identity':'d5_prime=a55_prime-2*b_prime^T*c+c^T*A_prime*c, c=A_inverse*b',
    'coordinates':rows,
    'all_schur_enclosures_strictly_negative':all(row['schur_derivative_enclosure'][1].startswith('-') for row in rows),
    'source_tail_injected':P.INJECT_SOURCE_TAIL,
    'directed_decimal_rounding':True,
    'rh_proved':False,
}
if __name__=='__main__':
    output=Path(__file__).parents[1]/'results'/'central-rank-five-schur-derivative.json'
    output.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))
