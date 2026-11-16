"""Auditable catalogue-based six-port obstruction for R(3,7).

Input: McKay's 2576 graph6 records for triangle-free 16-vertex graphs
with independence number <6, supplied as a .gz file.

Modes:
  --generate: solve a rationally-verified LP certificate for each 33-edge graph
      (requires scipy, numpy), and write a JSON certificate record.
  --verify: independently parse the entire graph6 catalogue, check all graph
      Ramsey constraints, independently verify every certificate with Python
      integer arithmetic, and check whether a six-clique exists in the
      rank-five compatibility graph. Requires only Python standard library.

The verification relies on the catalogue being exhaustive as a classification
of (3,6;16) graphs; it checks SHA-256 against the supplied expected reference.
"""
import argparse
from collections import Counter
from itertools import combinations
import gzip
import hashlib
import json
from pathlib import Path

EXPECTED_SHA = '5fd4e68d880e1d4ed05337b97cba0ce15387e1f545744aed80b91bb4b2186f25'
EXPECTED_RECORDS = 2576
EXPECTED_RELEVANT = 39


def decode_graph6(line):
    line = line.strip()
    if line.startswith(b'>>graph6<<'):
        line = line[10:]
    if not line:
        return None
    n = line[0]-63
    assert n==16
    mask = [0]*n
    vals = [b-63 for b in line[1:]]
    assert all(0 <= v <64 for v in vals)
    idx=0
    for j in range(1,n):
        for i in range(j):
            if vals[idx//6] & (1 << (5-idx%6)):
                mask[i] |= 1<<j
                mask[j] |= 1<<i
            idx+=1
    return mask


def triangle_free(A):
    return all((A[i]&A[j])==0 for i in range(len(A)) for j in range(i+1,len(A)) if A[i]&(1<<j))


def indep_sets(A, r):
    return [sum(1<<j for j in S) for S in combinations(range(len(A)),r)
            if all((A[i]&(1<<j))==0 for i,j in combinations(S,2))]


def clique_exists(A, size):
    def rec(av, needed):
        if needed==0:return True
        while av.bit_count()>=needed:
            bit=av & -av
            v=bit.bit_length()-1
            av-=bit
            if rec(av & A[v],needed-1):return True
        return False
    return rec((1<<len(A))-1,size)


def check_integer_certificate(A, C):
    F = indep_sets(A,5)
    assert len(F)>0
    weights={int(i):int(v) for i,v in C['weights'].items()}
    assert set(weights) <= set(F)
    den=C['denominator']
    assert isinstance(den,int) and den>0 and all(w>0 for w in weights.values())
    assert sum(weights.values())<6*den,('weight >=6',sum(weights.values()),den)
    for T in F:
        cover=sum(w for I,w in weights.items() if I&T==0)
        assert cover>=den,('coverage fail',T,cover,den)
    return {'independent_fives':len(F), 'total_numerator':sum(weights.values()),
            'denominator':den,'positive_weights':len(weights)}


def generate_cert(A, denominator=1000):
    import numpy as np
    from scipy.optimize import linprog
    F=indep_sets(A,5)
    M=np.array([[(x&y)==0 for y in F] for x in F],dtype=float)
    # Dual of maximum fractional packing: min 1^T y, M y >= 1, y>=0.
    # A_ub=-M ensures we work with min rather than extracting the dual of max.
    res=linprog(np.ones(len(F)),A_ub=-M,b_ub=-np.ones(len(F)),
                bounds=(0,None),method='highs')
    assert res.success,res.message
    # Round each weight upwards; then verify all inequalities *exactly*.
    raw=np.maximum(res.x,0)
    y=np.array([int(np.ceil(v*denominator+1e-7)) if v>1e-9 else 0 for v in raw],dtype=int)
    cert={'denominator':denominator, 'weights':{str(F[i]):int(x) for i,x in enumerate(y) if x},
          'lp_estimate':float(res.fun)}
    check_integer_certificate(A,cert)
    return cert


def six_compatible(A):
    F=indep_sets(A,5)
    D=[sum(1<<j for j,other in enumerate(F) if (mask&other)==0) for mask in F]
    K=[0]*len(F)
    for i in range(len(F)):
        for j in range(i+1,len(F)):
            if (D[i]&D[j])==0:
                K[i]|=1<<j
                K[j]|=1<<i
    return clique_exists(K,6), any(d==0 for d in D),len(F),clique_exists(K,5)


def data_rows(path):
    path=Path(path)
    assert hashlib.sha256(path.read_bytes()).hexdigest()==EXPECTED_SHA,'catalogue checksum mismatch'
    with gzip.open(path,'rb') as z:
        lines=[line.strip() for line in z if line.strip()]
    assert len(lines)==EXPECTED_RECORDS,('unexpected catalogue size',len(lines))
    return lines


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('catalogue')
    group=parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--generate',action='store_true')
    group.add_argument('--verify',action='store_true')
    parser.add_argument('--certificates',default='/mnt/data/ramsey_r37_full_catalogue_certificates.json')
    args=parser.parse_args()
    rows=data_rows(args.catalogue)
    graphs=[decode_graph6(x) for x in rows]
    assert all(len(x)==16 for x in graphs)
    edges=Counter(sum(z.bit_count() for z in A)//2 for A in graphs)
    relevant=[]
    for line,A in zip(rows,graphs):
        e=sum(z.bit_count() for z in A)//2
        if e!=33:continue
        assert all(2<=z.bit_count()<=5 for z in A)
        assert triangle_free(A)
        assert not indep_sets(A,6)
        relevant.append((line.decode('ascii'),A))
    assert len(relevant)==EXPECTED_RELEVANT
    if args.generate:
        records=[]
        for i,(line,A) in enumerate(relevant):
            C=generate_cert(A)
            no6,repeated,nf,yes5=six_compatible(A)
            assert not no6 and not repeated
            records.append({'graph6':line,'cert':C,'n_independent_fives':nf,
                            'compatibility_five_clique_exists':yes5})
            print(f'{i+1:2d}/39 I5={nf:3d} LP={C["lp_estimate"]:.7f} exact={sum(C["weights"].values())}/1000')
        out={'sha256':EXPECTED_SHA,'total_graphs':len(rows),'edge_distribution':dict(sorted(edges.items())),
             'records':records}
        Path(args.certificates).write_text(json.dumps(out,indent=2)+'\n')
        print('Written',args.certificates)
    else:
        certificates=json.loads(Path(args.certificates).read_text())
        assert certificates['sha256']==EXPECTED_SHA
        assert len(certificates['records'])==EXPECTED_RELEVANT
        lookup={r['graph6']:r for r in certificates['records']}
        assert set(lookup)=={row[0] for row in relevant}
        vals=[]
        counts=Counter()
        for line,A in relevant:
            C=lookup[line]['cert']
            vals.append(check_integer_certificate(A,C))
            no6,repeated,nf,yes5=six_compatible(A)
            assert not no6 and not repeated
            counts['with_K5']+=yes5
        assert len(vals)==39
        print('FULL CATALOGUE VERIFIED: 2576 graph6, 39 33-edge residuals, 0 six-cliques, 0 repeatable rows')
        print('edge distribution',dict(sorted(edges.items())))
        print('K5 present',counts['with_K5'],'K5 absent',39-counts['with_K5'])
        print('max exact fractional cover weight',max(v['total_numerator']/v['denominator'] for v in vals))
        print('independent five-set range',min(v['independent_fives'] for v in vals),max(v['independent_fives'] for v in vals))


if __name__=='__main__':main()
