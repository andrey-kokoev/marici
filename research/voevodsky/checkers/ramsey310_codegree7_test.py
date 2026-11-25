"""Necessary four exclusive supports at codegree seven in the 9-regular branch."""
import gzip
from pathlib import Path
P=Path(__file__).resolve().parents[2]/'chatgpt/ramsey/pauli-realization-catalogues/r38_27.g6.gz'
F=(1<<27)-1

def sets(A,m,k,s=0):
    if not k:
        yield s;return
    while m.bit_count()>=k:
        b=m&-m;m^=b
        yield from sets(A,m&~A[b.bit_length()-1],k-1,s|b)

def test(A):
    six=list(sets(A,F,6)); seven=list(sets(A,F,7));miss=[sum(1<<j for j,t in enumerate(seven) if not s&t) for s in six]
    unions={s|six[j] for i,s in enumerate(six) for j in range(i+1) if not miss[i]&miss[j]}
    # For each pair-union, test if its complement contains another pair-union.
    us=list(unions); possible=any(not s&t for i,s in enumerate(us) for t in us[:i]);return len(six),len(seven),len(us),possible

if __name__=='__main__':
    n=m=0
    with gzip.open(P,'rb') as f:
        for line in f:
            n+=1;b=[v-63 for v in line.strip()]; assert b[0]==27
            e=sum(v.bit_count() for v in b[1:]);assert e>=85
            if e!=85:continue
            A=[0]*27;k=0
            for j in range(27):
                for i in range(j):
                    if b[1+k//6]>>(5-k%6)&1:A[i]|=1<<j;A[j]|=1<<i
                    k+=1
            m+=1;print(n,test(A),flush=True)
    print('records',n,'at minimum',m)
