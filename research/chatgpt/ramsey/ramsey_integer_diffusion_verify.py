"""Independent standard-library verifier of the integer-diffusion Ramsey receipts.
Does not solve an LP, use NumPy/SciPy, or run the generator.
"""
from itertools import combinations
from fractions import Fraction
from pathlib import Path
import gzip,hashlib,json,sys

EXPECTED_SHA='5fd4e68d880e1d4ed05337b97cba0ce15387e1f545744aed80b91bb4b2186f25'

def decode(s):
    n=ord(s[0])-63
    assert n==16 and len(s)==21
    vals=[ord(c)-63 for c in s[1:]]
    A=[0]*n;k=0
    for j in range(1,n):
        for i in range(j):
            if vals[k//6] & (1 << (5-k%6)):
                A[i]|=1<<j;A[j]|=1<<i
            k+=1
    return A

def indep(A,k):
    for v in combinations(range(16),k):
        mask=sum(1<<i for i in v)
        if all((A[i]&mask)==0 for i in v):
            yield mask

def main():
    source=Path(sys.argv[1] if len(sys.argv)>1 else '/mnt/data/r36_16.g6.gz')
    cert_file=Path(sys.argv[2] if len(sys.argv)>2 else '/mnt/data/ramsey_integer_diffusion_certificates.json')
    assert hashlib.sha256(source.read_bytes()).hexdigest()==EXPECTED_SHA
    with gzip.open(source,'rt',encoding='ascii') as f: rows=[a.strip() for a in f if a.strip()]
    assert len(rows)==2576
    receipt=json.loads(cert_file.read_text())
    assert receipt['source_sha256']==EXPECTED_SHA
    relevant=[(i,txt) for i,txt in enumerate(rows,1)
              if sum(z.bit_count() for z in decode(txt))//2==33]
    assert len(relevant)==39 and len(receipt['records'])==39
    worst=(Fraction(0),None)
    for (index,txt),r in zip(relevant,receipt['records']):
        assert r['graph6']==txt and r['source_index']==index
        A=decode(txt)
        assert all(not (A[i]&A[j]) for i in range(16) for j in range(i+1,16) if A[i]>>j&1)
        assert not next(indep(A,6),None)
        F=list(indep(A,5)); assert F
        c=r['cert']; y={int(k):int(w) for k,w in c['weights'].items()}
        assert all(w>0 for w in y.values()) and set(y)<=set(F)
        m=int(c['denominator']);total=int(c['numerator'])
        assert m>0 and sum(y.values())==total and total<6*m
        assert all(sum(w for I,w in y.items() if not I&T)>=m for T in F)
        ratio=Fraction(total,m)
        assert abs(float(ratio)-c['ratio'])<1e-11
        if ratio>worst[0]:worst=(ratio,index)
    print('VERIFIED 2576 original graph6 entries and 39/39 integer certificates')
    print('Worst exact ratio numerator/denominator:',worst[0], 'source index:',worst[1])
    print('All 39 satisfy total < 6 * min_cover, independently of optimization software')

if __name__=='__main__':main()
