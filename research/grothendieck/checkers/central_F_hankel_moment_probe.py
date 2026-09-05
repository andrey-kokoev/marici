"""Probe whether the directed central F coefficients form finite Hankel moment data."""
import itertools,json
from decimal import Decimal as D
from pathlib import Path

import reduced_source_central_interval_chords as I

ROOT=Path(__file__).parents[1]
payload=json.loads((ROOT/'results'/'central-H-degree-eleven-interval.json').read_text())
f=[(D(a),D(b)) for a,b in payload['F_coefficients_through_degree_forty_nine']]
def parity(p):
    return -1 if sum(p[i]>p[j] for i in range(len(p)) for j in range(i+1,len(p)))%2 else 1
def determinant(matrix):
    total=I.box(0); n=len(matrix)
    for p in itertools.permutations(range(n)):
        term=I.box(parity(p))
        for i in range(n): term=I.mul(term,matrix[i][p[i]])
        total=I.add(total,term)
    return total
def ldl_determinant(matrix):
    n=len(matrix); lower=[[I.box(0) for _ in range(n)] for _ in range(n)]; pivots=[]
    for k in range(n):
        pivot=matrix[k][k]
        for j in range(k): pivot=I.sub(pivot,I.mul(I.mul(lower[k][j],lower[k][j]),pivots[j]))
        pivots.append(pivot); lower[k][k]=I.box(1)
        if pivot[0]<=0: return None,pivots
        for i in range(k+1,n):
            value=matrix[i][k]
            for j in range(k): value=I.sub(value,I.mul(I.mul(lower[i][j],lower[k][j]),pivots[j]))
            lower[i][k]=I.div(value,pivot)
    value=I.box(1)
    for pivot in pivots: value=I.mul(value,pivot)
    return value,pivots
rows=[]
for shift in range(10):
    for rank in range(1,6):
        matrix=[[f[shift+i+j+1] for j in range(rank)] for i in range(rank)]
        value=determinant(matrix)
        rows.append({'shift':shift,'rank':rank,'interval':[str(x) for x in value],
                     'sign':'positive' if value[0]>0 else ('negative' if value[1]<0 else 'unresolved')})
twisted=[I.scale(value,-1 if (index-1)%2 else 1) for index,value in enumerate(f)]
twisted_rows=[]
for shift in range(10):
    for rank in range(1,6):
        matrix=[[twisted[shift+i+j+1] for j in range(rank)] for i in range(rank)]
        value,pivots=ldl_determinant(matrix)
        sign='positive' if value is not None and value[0]>0 else 'unresolved'
        twisted_rows.append({'shift':shift,'rank':rank,
                             'interval':[str(x) for x in value] if value is not None else None,
                             'pivot_intervals':[[str(x) for x in pivot] for pivot in pivots],
                             'sign':sign})
extended_twisted_rows=[]
for rank in range(1,11):
    for shift in range(0,51-2*rank):
        matrix=[[twisted[shift+i+j+1] for j in range(rank)] for i in range(rank)]
        value,pivots=ldl_determinant(matrix)
        extended_twisted_rows.append({
            'shift':shift,'rank':rank,
            'final_pivot_interval':[str(x) for x in pivots[-1]],
            'sign':'positive' if value is not None and value[0]>0 else 'unresolved'})
sign_counts={sign:sum(row['sign']==sign for row in rows) for sign in ('positive','negative','unresolved')}
first_negative=next((row for row in rows if row['sign']=='negative'),None)
result={
    'tested_coefficient_family':'F_coefficients_through_degree_forty_nine',
    'tested_shifts':list(range(10)),
    'tested_ranks':list(range(1,6)),
    'minors':rows,
    'sign_counts':sign_counts,
    'alternating_sign_twisted_minors':twisted_rows,
    'alternating_sign_twisted_sign_counts':{sign:sum(row['sign']==sign for row in twisted_rows) for sign in ('positive','negative','unresolved')},
    'alternating_sign_twisted_first_negative':next((row for row in twisted_rows if row['sign']=='negative'),None),
    'alternating_sign_twisted_unresolved':[
        {'shift':row['shift'],'rank':row['rank'],'interval':row['interval'],'pivot_intervals':row['pivot_intervals']}
        for row in twisted_rows if row['sign']=='unresolved'],
    'all_tested_alternating_sign_twisted_Hankel_minors_positive':all(row['sign']=='positive' for row in twisted_rows),
    'extended_alternating_Hankel_test':{
        'maximum_rank':10,
        'admissible_shifts_use_coefficients_only_through_degree_forty_nine':True,
        'case_count':len(extended_twisted_rows),
        'positive_count':sum(row['sign']=='positive' for row in extended_twisted_rows),
        'unresolved_count':sum(row['sign']=='unresolved' for row in extended_twisted_rows),
        'first_unresolved':next((row for row in extended_twisted_rows if row['sign']=='unresolved'),None),
        'cases':extended_twisted_rows,
    },
    'first_negative':first_negative,
    'all_tested_Hankel_minors_positive':all(row['sign']=='positive' for row in rows),
    'finite_probe_only':True,
    'Stieltjes_measure_constructed':False,
    'rh_proved':False,
}
if __name__=='__main__':
    output=ROOT/'results'/'central-F-hankel-moment-probe.json'
    output.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))
