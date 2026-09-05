"""Probe the determinant-ratio numerator behind the fifth-pivot derivative."""
import itertools,json
from pathlib import Path

import central_rank_five_pivot_taylor_interval as P

I=P.I; zero=P.zero
def parity(permutation):
    return -1 if sum(permutation[i]>permutation[j] for i in range(len(permutation)) for j in range(i+1,len(permutation)))%2 else 1
def determinant(matrix):
    total=I.box(0); n=len(matrix)
    for permutation in itertools.permutations(range(n)):
        term=I.box(parity(permutation))
        for i in range(n): term=I.mul(term,matrix[i][permutation[i]])
        total=I.add(total,term)
    return total
def determinant_derivative(matrix,derivative):
    total=I.box(0); n=len(matrix)
    for permutation in itertools.permutations(range(n)):
        for differentiated_row in range(n):
            term=I.box(parity(permutation))
            for i in range(n):
                factor=derivative[i][permutation[i]] if i==differentiated_row else matrix[i][permutation[i]]
                term=I.mul(term,factor)
            total=I.add(total,term)
    return total
def coefficient(jet,key): return jet.get(key,I.box(0))
M=[[coefficient(P.matrix[i][j],zero) for j in range(5)] for i in range(5)]
A=[row[:4] for row in M[:4]]
detM=determinant(M); detA=determinant(A)
rows=[]
for variable in range(5):
    key=tuple(1 if i==variable else 0 for i in range(5))
    derivativeM=[[coefficient(P.matrix[i][j],key) for j in range(5)] for i in range(5)]
    derivativeA=[row[:4] for row in derivativeM[:4]]
    ddetM=determinant_derivative(M,derivativeM)
    ddetA=determinant_derivative(A,derivativeA)
    numerator=I.sub(I.mul(ddetM,detA),I.mul(detM,ddetA))
    direct=coefficient(P.fifth,key)
    ratio=I.div(numerator,I.mul(detA,detA))
    assert ratio[0]<=direct[0] and direct[1]<=ratio[1]
    rows.append({
        'coordinate':variable,
        'determinant_ratio_numerator':[str(x) for x in numerator],
        'ratio_derivative_enclosure':[str(x) for x in ratio],
        'direct_ldl_derivative':[str(x) for x in direct],
        'numerator_sign_certified':'negative' if numerator[1]<0 else ('positive' if numerator[0]>0 else 'unresolved'),
    })
result={
    'identity':'d5_prime=(detA*detM_prime-detM*detA_prime)/detA_squared',
    'determinant_M':[str(x) for x in detM],
    'determinant_A':[str(x) for x in detA],
    'coordinates':rows,
    'all_numerator_signs_negative':all(row['numerator_sign_certified']=='negative' for row in rows),
    'diagnostic_only':True,
    'rh_proved':False,
}
if __name__=='__main__':
    output=Path(__file__).parents[1]/'results'/'central-rank-five-determinant-ratio-derivative.json'
    output.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))
