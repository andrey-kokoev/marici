"""Actual vacuum normal forms and exact factorial summability obstructions."""
from collections import defaultdict
from itertools import combinations,permutations
from fractions import Fraction as Q
from math import comb,factorial
from pathlib import Path
import json


def jets(column,n):
    out=[defaultdict(int) for _ in range(n+1)]
    for word,coefficient in column.items():
        state=0;edges=[]
        for j in word:
            target=state|(1<<j)
            edges.append(('e',state,target,0));state=target
        for k in range(n+1):
            for chosen in combinations(edges,k):
                # All buffers are vacuum. Their endpoint types are determined
                # by the retained ordered edges and the two outer endpoints.
                key=(0,state,chosen,((),)*(k+1))
                out[k][key]+=coefficient
    return [{key:c for key,c in jet.items() if c} for jet in out]


def mass(column):return sum(abs(c) for c in column.values())


def total(n,t):return sum(t**k*factorial(k)*comb(n,k) for k in range(n+1))


def main():
    path_checks=relation_checks=general_checks=0
    for n in range(2,13):
        word=tuple(range(n));other=(1,0)+tuple(range(2,n))
        single=jets({word:1},n);relation=jets({word:1,other:-1},n)
        assert not relation[0] and mass(relation[n])==2
        for k in range(n+1):
            assert mass(single[k])==comb(n,k)
            expected=2*(comb(n,k)-(comb(n-2,k) if k<=n-2 else 0))
            assert mass(relation[k])==expected
            path_checks+=1;relation_checks+=1
        for t in (Q(2),Q(5,2),Q(3)):
            observed=sum(t**k*factorial(k)*mass(relation[k]) for k in range(n+1))
            assert observed==2*(total(n,t)-total(n-2,t))
            assert observed>=2*factorial(n)*t**n
    for n in range(2,6):
        words=list(permutations(range(n)))[:8]
        column={word:(i%5)-2 for i,word in enumerate(words)}
        column[words[0]]-=sum(column.values())
        column={word:c for word,c in column.items() if c}
        assert column and sum(column.values())==0
        family=jets(column,n)
        assert mass(family[n])==mass(column)
        for t in (Q(2),Q(5,2),Q(4)):
            observed=sum(t**k*factorial(k)*mass(family[k]) for k in range(n+1))
            lower=factorial(n)*t**n*mass(column)
            assert lower<=observed<=2*lower
            general_checks+=1
    ratio_checks=0
    for p,C in ((p,C) for p in range(5) for C in (1,2,3)):
        m=2*C*C*3**p
        ratio=Q(C*C,m+1)*Q(2*m+3,2*m+1)**p
        assert ratio<=Q(1,2)  # source-series eventual ratio bound.
        ratio_checks+=1
    for m in range(1,13):
        for t in (Q(2),Q(3)):
            top=2*factorial(2*m)*t**(2*m)/factorial(m)
            assert top>=2*factorial(m)*t**(2*m)
            following=2*factorial(2*m+2)*t**(2*m+2)/factorial(m+1)
            assert following/top==2*(2*m+1)*t*t
    result={'passed':True,'single_path_cut_counts':path_checks,
            'diamond_suffix_cut_counts':relation_checks,
            'signed_vacuum_factorial_norm_comparisons':general_checks,
            'source_series_ratio_checks':ratio_checks,
            'scope':'Exact vacuum-record counts. Infinite source convergence, nonsummability and the all-radius domain characterization are proved in the companion note.'}
    path=Path(__file__).resolve().parents[1]/'results/factorial-jet-necessity.json'
    path.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))


if __name__=='__main__':main()
