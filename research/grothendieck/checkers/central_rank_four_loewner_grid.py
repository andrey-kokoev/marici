"""Directed Vandermonde-normalized rank-four Loewner grid."""
import itertools,json
from decimal import Decimal as D
from pathlib import Path

import central_rank_three_loewner_continuum as C

I=C.I
def homogeneous(nodes,max_degree=23):
    h=[I.box(1)]+[I.box(0)]*max_degree
    for node in nodes:
        powers=[I.powi(I.box(node),q) for q in range(max_degree+1)]
        h=[I.add(*(I.mul(h[d-q],powers[q]) for q in range(d+1))) for d in range(max_degree+1)]
    return h
def matrix(nodes):
    tables=[homogeneous(nodes[:i+1]) for i in range(4)]
    out=[]
    for i in range(4):
        row=[]
        for j in range(4):
            value=I.box(0)
            for n in range(1,len(C.f)):
                for k in range(i,n):
                    ell=n-1-k
                    if ell>=j:
                        value=I.add(value,I.mul(C.f[n],I.mul(tables[i][k-i],tables[j][ell-j])))
            tail=C.derivative_tail(i,j)
            row.append(I.add(value,(tail.copy_negate(),tail)))
        out.append(row)
    return out
def parity(permutation):
    return -1 if sum(permutation[i]>permutation[j] for i in range(4) for j in range(i+1,4))%2 else 1
def determinant(a):
    value=I.box(0)
    for permutation in itertools.permutations(range(4)):
        term=I.box(1)
        for i,j in enumerate(permutation): term=I.mul(term,a[i][j])
        value=I.add(value,term if parity(permutation)>0 else I.neg(term))
    return value

points=[D(i)/D(1000) for i in range(11)]
rows=[(determinant(matrix(nodes)),nodes) for nodes in itertools.combinations(points,4)]
weakest=min(rows,key=lambda row:row[0][0])
assert all(determinant[0]>0 for determinant,_ in rows)
result={
    'grid_points':[str(x) for x in points],
    'quadruple_count':len(rows),
    'all_Vandermonde_normalized_rank_four_minors_strictly_positive':True,
    'weakest_quadruple':[str(x) for x in weakest[1]],
    'weakest_normalized_determinant_interval':[str(x) for x in weakest[0]],
    'Newton_complete_homogeneous_evaluation':True,
    'directed_decimal_rounding':True,
    'interval_certified':True,
    'zero_locations_used':False,
    'rh_proved':False,
}
if __name__=='__main__':
    output=Path(__file__).parents[1]/'results'/'central-rank-four-loewner-grid.json'
    output.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    for key,value in result.items(): print(f'{key}={value}')
