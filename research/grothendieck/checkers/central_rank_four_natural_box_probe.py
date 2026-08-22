"""Conditioning probe for the first normalized rank-four continuum box."""
import itertools,json,math
from decimal import Decimal as D
from pathlib import Path

import central_rank_three_loewner_continuum as C

I=C.I
def parity(p):
    return -1 if sum(p[i]>p[j] for i in range(4) for j in range(i+1,4))%2 else 1
def det4(matrix):
    out=I.box(0)
    for permutation in itertools.permutations(range(4)):
        term=I.box(1)
        for i,j in enumerate(permutation): term=I.mul(term,matrix[i][j])
        out=I.add(out,term if parity(permutation)>0 else I.neg(term))
    return out

matrix=[[C.entry(i,j)[0] for j in range(4)] for i in range(4)]
box=det4(matrix)
center=D('.005')
def center_entry(i,j):
    return sum(((a+b)/2)*D(math.comb(k,i)*math.comb(n-1-k,j))*center**(n-1-i-j)
               for n,(a,b) in enumerate(C.f) for k in range(n)
               if k>=i and n-1-k>=j)
center_matrix=[[I.box(center_entry(i,j)) for j in range(4)] for i in range(4)]
center_det=det4(center_matrix)[0]
result={
    'domain':['0','0.01'],
    'natural_normalized_rank_four_determinant_interval':[str(x) for x in box],
    'midpoint_normalized_rank_four_determinant':str(center_det),
    'natural_box_certifies_sign':box[0]>0 or box[1]<0,
    'diagnosis':'independent mixed-derivative boxes lose correlations; use correlated LDL or simplex subdivision',
    'interval_certified_negative_minor':False,
    'rh_proved':False,
}
if __name__=='__main__':
    output=Path(__file__).parents[1]/'results'/'central-rank-four-natural-box-probe.json'
    output.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    for key,value in result.items(): print(f'{key}={value}')
