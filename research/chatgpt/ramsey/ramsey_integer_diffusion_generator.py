"""Integer-only uniform generator of fractional 5-set disjointness certificates.

The state lives on independent five-sets F of a 16-vertex residual H.
Every update uses only D, its maximum degree, and the current integer weights.
All coefficients derive from n=|V(H)|: Q=n**5, lambda=1/n, steps=n**3.

Assumes catalogue completeness separately; checking all 39 classes is not a
classification-independent proof of existence of a certificate for every H.
"""
import argparse, json
from pathlib import Path
from ramsey_r37_full_catalogue_audit import data_rows,decode_graph6,indep_sets
import numpy as np


def generate(g):
    n=len(g)
    F=indep_sets(g,5)
    D=np.array([[(I&T)==0 for I in F] for T in F],dtype=np.int64)
    Q=n**5
    steps=n**3
    delta=int(D.sum(axis=0).max())
    L=delta*delta
    y=np.zeros(len(F),dtype=np.int64)
    # All arithmetic in this loop is integer arithmetic, including division.
    for t in range(steps):
        deficit=np.maximum(0,Q-D@y)
        correction=(D@deficit-Q//n)//L
        y=np.maximum(0,y+correction)
    cover=D@y
    denominator=int(cover.min())
    numerator=int(y.sum())
    assert denominator>0
    assert numerator<6*denominator,(numerator,denominator)
    return F,{'denominator':denominator,
              'weights':{str(F[i]):int(x) for i,x in enumerate(y) if x},
              'numerator':numerator,
              'ratio':numerator/denominator}


def verify_pure_python(g,cert):
    F=indep_sets(g,5)
    weights={int(k):v for k,v in cert['weights'].items()}
    assert set(weights).issubset(F)
    den=cert['denominator'];assert den>0
    assert all(isinstance(w,int) and w>=0 for w in weights.values())
    assert sum(weights.values())==cert['numerator']
    assert sum(weights.values())<6*den
    for T in F:
        assert sum(w for I,w in weights.items() if (I&T)==0)>=den


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('file',nargs='?',default='/mnt/data/r36_16.g6.gz')
    ap.add_argument('--out',default='/mnt/data/ramsey_integer_diffusion_certificates.json')
    args=ap.parse_args()
    rows=data_rows(args.file)
    records=[]
    for index,row in enumerate(rows,1):
        g=decode_graph6(row)
        if sum(x.bit_count() for x in g)!=66: continue
        F,cert=generate(g)
        verify_pure_python(g,cert)
        print(f'{index:4d}: |F|={len(F):2d}, mass={cert["ratio"]:.8f}, support={len(cert["weights"])}')
        records.append({'graph6':row.decode('ascii'),'source_index':index,'cert':cert})
    assert len(records)==39
    out={'source_sha256':'5fd4e68d880e1d4ed05337b97cba0ce15387e1f545744aed80b91bb4b2186f25',
         'rule':{'Q':'n^5','steps':'n^3','lambda':'1/n','L':'maximum_disjointness_degree_squared','rounding':'floor integer'},
         'records':records}
    Path(args.out).write_text(json.dumps(out,indent=2)+'\n')
    print('VERIFIED 39/39; max weight',max(r['cert']['ratio'] for r in records))
    print('output:',args.out)

if __name__=='__main__':main()
