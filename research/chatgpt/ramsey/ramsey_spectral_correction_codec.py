"""Predict columns of the interleaved indexed matrix. Encode all errors as one subset.
Both sides know n and the interleaved order. No eigenvector parameters in payload.
"""
from math import comb
import numpy as np
from ramsey_blind_start_formulas import seed


def predict(rows, spectral):
    n=len(rows)
    if not spectral or n==0:return 0
    a=np.array([[r>>j&1 for j in range(n)] for r in rows]);v,U=np.linalg.eigh(a)
    # Project the first usable coordinate vector into the lowest eigenspace.
    E=U[:,v<v[0]+1e-8];P=E@E.T;j=next(j for j in range(n) if P[j,j]>1e-8)
    return sum(1<<i for i,x in enumerate(P[:,j]) if x>1e-8)


def update(rows,c):return [r|((c>>i&1)<<len(rows)) for i,r in enumerate(rows)]+[c]

def trial(g,spectral):
    n=len(g);N=comb(n,2);rows=[];err=[]
    for i in range(n):
        c=g[i]&((1<<i)-1);p=predict(rows,spectral)
        err.extend(comb(i,2)+j for j in range(i) if (c^p)>>j&1);rows=update(rows,c)
    t=len(err);rank=sum(comb(j,k) for k,j in enumerate(err,1));bits=lambda x,w:format(x,f'0{w}b') if w else ''
    w=N.bit_length();stream=bits(t,w)+bits(rank,(comb(N,t)-1).bit_length())
    t=int(stream[:w],2);rank=int(stream[w:] or '0',2);idx=N-1;es=set()
    for k in range(t,0,-1):
        while comb(idx,k)>rank:idx-=1
        es.add(idx);rank-=comb(idx,k);idx-=1
    rows=[]
    for i in range(n):rows=update(rows,predict(rows,spectral)^sum(1<<j for j in range(i) if comb(i,2)+j in es))
    assert rows==g
    return len(es),len(stream)

if __name__=='__main__':
    orig=seed(7,'double')[0];order=[z for i in range(10) for z in (i,i+10)]
    for m in range(8):
        g=orig.copy()
        for k,(i,j) in enumerate(((0,5),(1,6),(2,7))):
            for x,y in ((i,j),(j,i)):g[x]=(g[x]&~(1<<y))|((m>>k&1)<<y)
        r=[sum((g[i]>>j&1)<<p for p,j in enumerate(order)) for i in order];print(m,trial(r,True),trial(r,False))
