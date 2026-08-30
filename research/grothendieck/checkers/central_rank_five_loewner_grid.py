"""Directed Newton-LDL rank-five Loewner grid certificate."""
import itertools,json,math
from decimal import Decimal as D
from pathlib import Path

import reduced_source_central_interval_chords as I

ROOT=Path(__file__).parents[1]; N=5; M=D('6.038308'); R=D('.01')
payload=json.loads((ROOT/'results'/'central-H-degree-eleven-interval.json').read_text())
f=[(D(a),D(b)) for a,b in payload['F_coefficients_through_degree_twenty_nine']]
def tail(i,j):
    m=i+j; value=D(0)
    for p in range(29,201):
        falling=math.factorial(p)//math.factorial(p-m)
        term=I.up.multiply(M,D(falling)*R**(p-m))
        value=I.up.add(value,I.up.divide(term,D(math.factorial(i)*math.factorial(j))))
    first=I.up.divide(I.up.multiply(M,D(201**m)*R**(201-m)),D(math.factorial(i)*math.factorial(j)))
    return I.up.add(value,I.up.divide(first,D('.989')))
def homogeneous(nodes):
    h=[I.box(1)]+[I.box(0)]*29
    for node in nodes:
        powers=[I.powi(I.box(node),q) for q in range(30)]
        h=[I.add(*(I.mul(h[d-q],powers[q]) for q in range(d+1))) for d in range(30)]
    return h
def matrix(nodes):
    tables=[homogeneous(nodes[:i+1]) for i in range(N)]; out=[]
    for i in range(N):
        row=[]
        for j in range(N):
            value=I.box(0)
            for n in range(1,len(f)):
                for k in range(i,n):
                    ell=n-1-k
                    if ell>=j: value=I.add(value,I.mul(f[n],I.mul(tables[i][k-i],tables[j][ell-j])))
            error=tail(i,j); row.append(I.add(value,(error.copy_negate(),error)))
        out.append(row)
    return out
def pivots(a):
    lower=[[I.box(0) for _ in range(N)] for _ in range(N)]; diagonal=[]
    for k in range(N):
        pivot=a[k][k]
        for j in range(k): pivot=I.sub(pivot,I.mul(I.mul(lower[k][j],lower[k][j]),diagonal[j]))
        diagonal.append(pivot); lower[k][k]=I.box(1)
        if pivot[0]<=0: return diagonal
        for i in range(k+1,N):
            value=a[i][k]
            for j in range(k): value=I.sub(value,I.mul(I.mul(lower[i][j],lower[k][j]),diagonal[j]))
            lower[i][k]=I.div(value,pivot)
    return diagonal

def grid_result():
    points=[D(i)/D(1000) for i in range(11)]
    rows=[]
    for nodes in itertools.combinations(points,N):
        diagonal=pivots(matrix(nodes)); rows.append((diagonal,nodes))
    assert all(len(diagonal)==N and all(pivot[0]>0 for pivot in diagonal) for diagonal,_ in rows)
    weakest=min(rows,key=lambda row:row[0][-1][0])
    return {
        'grid_points':[str(x) for x in points],
        'quintuple_count':len(rows),
        'all_rank_five_Newton_LDL_pivots_strictly_positive':True,
        'weakest_quintuple':[str(x) for x in weakest[1]],
        'weakest_final_pivot_interval':[str(x) for x in weakest[0][-1]],
        'all_pivots_at_weakest_quintuple':[[str(a),str(b)] for a,b in weakest[0]],
        'degree_twenty_nine_tail_included':True,
        'directed_decimal_rounding':True,
        'interval_certified':True,
        'zero_locations_used':False,
        'rh_proved':False,
    }
if __name__=='__main__':
    result=grid_result()
    output=ROOT/'results'/'central-rank-five-loewner-grid.json'
    output.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    for key,value in result.items(): print(f'{key}={value}')
