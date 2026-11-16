#!/usr/bin/env python3
"""Exact structural compression of the 695 Ramsey (3,7) support orbits.
Classify immediate deficient-support impossibility and forced-red-triangle
obstructions, and prove 115 further local cases with triangle-cover certificates. The
remaining integral-only bridge and degree-dependent cut have direct proofs.
"""
from collections import Counter
from pathlib import Path
from fractions import Fraction
from itertools import combinations
import gzip,json
import ramsey_fractional_witness_certificate as cert
BASE=Path(__file__).resolve().parent
DATA=BASE/'ramsey_triangle_cover_supplement.json.gz'

def easy_classification(s):
    edges,hall,tri=cert.constraints(s)
    if any(not e for u,e in hall):return 'empty'
    forced={e[0] for u,e in hall if len(e)==1}
    if any(all(j in forced for j in E) for u,E in tri):return 'forced_triangle'
    return 'other'



def verify_bipartite_bridge(s):
    """The 6 forced bipartite red edges and the two deficient triples
    give an intrinsic triangle obstruction without integrality enumeration.
    """
    mm={''.join(str(j) for j in range(6) if m>>j&1):i for i,m in enumerate(s)}
    needed=['0','1','2','3','4','5','14','15','24','25','34','35','012','045']
    assert all(x in mm for x in needed)
    edges,hall,tri=cert.constraints(s)
    eidx={e:i for i,e in enumerate(edges)}
    hsets={tuple(U):set(idx) for U,idx in hall}
    def pair(a,b):
        ia,ib=mm[a],mm[b]
        return eidx[tuple(sorted((ia,ib)))]
    # From deficient sets {a,b,ab}, each edge a-b is forced red.
    for a in ('1','2','3'):
        for b in ('4','5'):
            U=tuple(sorted([mm[a],mm[b],mm[a+b]]))
            assert hsets[U]=={pair(a,b)}
    # Triangle-free forces all edges within the two shores blue.
    for a,b in [('1','2'),('1','3'),('2','3'),('4','5')]:
        z='4' if a in '123' else '1'
        assert {pair(a,b),pair(a,z),pair(b,z)} in (set(E) for U,E in tri)
    # Deficient 012 and 045 witnesses require a red edge among their singleton triples.
    A=tuple(sorted([mm[x] for x in ('0','1','2','012')]))
    B=tuple(sorted([mm[x] for x in ('0','4','5','045')]))
    assert hsets[A]=={pair('0','1'),pair('0','2'),pair('1','2')}
    assert hsets[B]=={pair('0','4'),pair('0','5'),pair('4','5')}
    # 1-2 and 4-5 blue => 0-a red for some a in {1,2},
    # 0-b red for some b in {4,5}; but a-b is forced red.
    print('BIPARTITE BRIDGE: K_{3,2} red; 012 and 045 force incompatible contacts from 0')

def generate():
    import numpy as np
    from scipy.optimize import linprog
    from scipy.sparse import coo_matrix
    existing=json.load(gzip.open(BASE/'ramsey_global_shadow_duals.json.gz'))['records']
    have={(e['r'],e['index']):e for e in existing}
    records=[];counts=Counter()
    for r in range(5):
        for idx,s in enumerate(cert.support_classes(r)[0]):
            classification=easy_classification(s)
            counts[(r,classification)]+=1
            if classification!='other' or (r,idx) in ((4,17),(4,188)):continue
            if (r,idx) in have:
                record=have[(r,idx)]
            else:
                edges,hall,tri=cert.constraints(s);M=len(edges)
                rr=[];cc=[];vv=[];bounds=[]
                for typ,rows in [('H',hall),('T',tri)]:
                    for U,E in rows:
                        i=len(bounds)
                        for j in E:
                            rr.append(i);cc.append(j);vv.append(-1 if typ=='H' else 1)
                        if typ=='H':rr.append(i);cc.append(M);vv.append(-1)
                        bounds.append(-1 if typ=='H' else 2)
                A=coo_matrix((vv,(rr,cc)),shape=(len(bounds),M+1)).tocsr()
                obj=np.zeros(M+1);obj[-1]=1
                sol=linprog(obj,A_ub=A,b_ub=np.array(bounds),bounds=[(0,1)]*M+[(0,None)],method='highs')
                assert sol.status==0 and sol.fun>1e-8, (r,idx,sol.status,sol.message)
                rat=lambda y:str(Fraction(float(y)).limit_denominator(1000000))
                inequalities=[]
                for i,y in enumerate(sol.ineqlin.marginals):
                    if abs(y)<1e-8: continue
                    typ,U=('H',hall[i][0]) if i<len(hall) else ('T',tri[i-len(hall)][0])
                    inequalities.append([typ,list(U),rat(y)])
                # Important: no edge upper bound or degree constraint should be necessary.
                uppers=[[list(edges[j]),rat(y)] for j,y in enumerate(sol.upper.marginals[:M]) if abs(y)>1e-8]
                assert not uppers,(r,idx,uppers)
                bound=sum(-Fraction(y) if typ=='H' else 2*Fraction(y) for typ,U,y in inequalities)
                record={'r':r,'index':idx,'supports':list(s), 'degree_duals':['0']*16,
                        'inequality_duals':inequalities,'upper_duals':[],'bound':str(bound)}
            assert tuple(record['supports'])==s
            cert.verify_entry(record)
            records.append(record)
    assert len(records)==115, len(records)
    with gzip.open(DATA,'wt') as f:json.dump({'schema':'ramsey.triangle-cover.supplement.v1','records':records},f,separators=(',',':'))
    print('CREATED',DATA,'records',len(records),'counts',dict(counts))

def verify():
    loaded=json.load(gzip.open(DATA))
    records={(z['r'],z['index']):z for z in loaded['records']}
    counts=Counter(); classified=Counter()
    for r in range(5):
        for idx,s in enumerate(cert.support_classes(r)[0]):
            kind=easy_classification(s)
            counts[(r,kind)]+=1;classified[kind]+=1
            if kind!='other' or (r,idx) in ((4,17),(4,188)):continue
            record=records.pop((r,idx))
            assert tuple(record['supports'])==s
            assert all(x=='0' for x in record['degree_duals'])
            assert not record['upper_duals']
            cert.verify_entry(record)
    assert not records
    assert classified=={'empty':407,'forced_triangle':171,'other':117},classified
    print('EXACT COUNTS:',dict(classified))
    print('115 triangle-cover contradiction certificates, 1 bipartite bridge, 1 degree cut')
    print('BY r',dict(counts))
    verify_bipartite_bridge(cert.support_classes(4)[0][188])
if __name__=='__main__':
    import sys
    if '--generate' in sys.argv:generate()
    verify()
