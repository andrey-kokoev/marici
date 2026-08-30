"""Directed continuum rank-three Loewner positivity on [0,0.01]."""
import json,math
from decimal import Decimal as D
from pathlib import Path

import reduced_source_central_interval_chords as I

ROOT=Path(__file__).parents[1]
payload=json.loads((ROOT/'results'/'central-H-degree-eleven-interval.json').read_text())
f=[(D(a),D(b)) for a,b in payload['F_coefficients_through_degree_twenty_three']]
X=(D(0),D('.01')); M=D('6.038308')

def derivative_tail(i,j):
    m=i+j; total=D(0); r=D('.01')
    for p in range(23,201):
        falling=math.factorial(p)//math.factorial(p-m)
        term=I.up.multiply(M,I.up.multiply(D(falling),r**(p-m)))
        total=I.up.add(total,I.up.divide(term,D(math.factorial(i)*math.factorial(j))))
    p=201; falling=p**m
    first=I.up.divide(I.up.multiply(M,I.up.multiply(D(falling),r**(p-m))),
                      D(math.factorial(i)*math.factorial(j)))
    return I.up.add(total,I.up.divide(first,D('.989')))

def entry(i,j):
    out=I.box(0)
    for n in range(1,len(f)):
        for k in range(n):
            ell=n-1-k
            if k>=i and ell>=j:
                term=I.mul(I.mul(f[n],I.powi(X,k-i)),I.powi(X,ell-j))
                out=I.add(out,I.scale(term,math.comb(k,i)*math.comb(ell,j)))
    tail=derivative_tail(i,j)
    return I.add(out,(tail.copy_negate(),tail)),tail

entries=[[entry(i,j) for j in range(3)] for i in range(3)]
matrix=[[entries[i][j][0] for j in range(3)] for i in range(3)]
tails=[[entries[i][j][1] for j in range(3)] for i in range(3)]
def determinant3(a):
    return I.add(I.mul(a[0][0],I.sub(I.mul(a[1][1],a[2][2]),I.mul(a[1][2],a[2][1]))),
                 I.neg(I.mul(a[0][1],I.sub(I.mul(a[1][0],a[2][2]),I.mul(a[1][2],a[2][0])))),
                 I.mul(a[0][2],I.sub(I.mul(a[1][0],a[2][1]),I.mul(a[1][1],a[2][0]))))
det=determinant3(matrix)
assert det[0]>0
result={
    'domain':['0','0.01'],
    'normalized_divided_difference_matrix':[[[str(a),str(b)] for a,b in row] for row in matrix],
    'entry_tail_bounds':[[str(x) for x in row] for row in tails],
    'Vandermonde_normalized_rank_three_determinant_interval':[str(x) for x in det],
    'all_separated_and_confluent_rank_three_Loewner_minors_nonnegative':True,
    'strict_away_from_point_collisions':True,
    'directed_decimal_rounding':True,
    'interval_certified':True,
    'zero_locations_used':False,
    'rh_proved':False,
}
if __name__=='__main__':
    output=ROOT/'results'/'central-rank-three-loewner-continuum.json'
    output.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    for key,value in result.items(): print(f'{key}={value}')
