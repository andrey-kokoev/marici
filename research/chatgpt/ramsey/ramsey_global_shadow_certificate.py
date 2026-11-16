#!/usr/bin/env python3
"""Exact reduced local-to-global obstruction audit for the R(3,7)<=23 support system.

Assuming the standard 6-regularity reduction, all 695 support-orbit classes
partition into:
 593 impossible by triangle-free graph on the singleton support vertices,
     combined with Hall witness clauses all of whose possible red edges lie
     inside those singleton vertices;
 101 impossible via rational LP duals involving only Hall deficits up to size5,
     triangle inequalities and 0<=x<=1 -- NO degree equations on T;
   1 exceptional r4 support needing a 10-versus-9 cut contradiction from
     residual degree equations (fully combinatorial verifier separately).

Verification uses only the Python standard library. Generation of the 101
rational certificates uses SciPy as a discovery stage, never for verification.
"""
from itertools import combinations
from collections import Counter
from fractions import Fraction
from pathlib import Path
import gzip,json,sys
import ramsey_fractional_witness_certificate as cert
HERE=Path(__file__).resolve().parent
DATA=HERE/'ramsey_global_shadow_duals.json.gz'
TRIPLES=lambda sites:tuple(combinations(sites,3))

def singleton_shadow_count(s):
    singles={m.bit_length()-1:i for i,m in enumerate(s) if m.bit_count()==1}
    sites=tuple(sorted(singles)); E=tuple(combinations(sites,2))
    eid={p:j for j,p in enumerate(E)}
    red_edges,hall,_=cert.constraints(s)
    edge_index={e:j for j,e in enumerate(red_edges)}
    smap={edge_index[tuple(sorted((singles[a],singles[b])))]:eid[(a,b)]
          for a,b in E if tuple(sorted((singles[a],singles[b]))) in edge_index}
    assert len(smap)==len(E)
    clauses={tuple(sorted(smap[e] for e in indices)) for U,indices in hall
             if all(e in smap for e in indices)}
    tri=[tuple(eid[e] for e in combinations(U,2)) for U in TRIPLES(sites)]
    count=0
    for mask in range(1<<len(E)):
        if any(not any(mask>>i&1 for i in cl) for cl in clauses):continue
        if any(all(mask>>i&1 for i in cl) for cl in tri):continue
        count+=1
    return count

def shadow_census():
    all_s=[];stats=[]; survivors=[]
    for r in range(5):
        ss=cert.support_classes(r)[0]
        n=0
        for idx,s in enumerate(ss):
            if singleton_shadow_count(s):
                survivors.append((r,idx,s));n+=1
        stats.append((r,len(ss),len(ss)-n,n))
        all_s+=ss
    assert [q[1] for q in stats]==[6,40,170,279,200]
    assert [q[3] for q in stats]==[1,5,32,48,16]
    return stats,survivors

def generate():
    import numpy as np
    from scipy.optimize import linprog
    from scipy.sparse import coo_matrix
    stats,survivors=shadow_census()
    records=[]
    for r,idx,masks in survivors:
        if r==4 and idx==17:continue
        edges,hall,tri=cert.constraints(masks);M=len(edges)
        row=[];col=[];val=[];b=[]
        for typ,cs in [('H',hall),('T',tri)]:
            for U,inds in cs:
                i=len(b)
                for j in inds:row.append(i);col.append(j);val.append(-1 if typ=='H' else 1)
                if typ=='H':row.append(i);col.append(M);val.append(-1)
                b.append(-1 if typ=='H' else 2)
        A=coo_matrix((val,(row,col)),shape=(len(b),M+1)).tocsr()
        c=np.zeros(M+1);c[-1]=1
        sol=linprog(c,A_ub=A,b_ub=b,bounds=[(0,1)]*M+[(0,None)],method='highs')
        assert sol.status==0 and sol.fun>1e-9,(r,idx,sol.status,sol.message)
        rat=lambda v: str(Fraction(float(v)).limit_denominator(1000000))
        inequalities=[]
        for j,v in enumerate(sol.ineqlin.marginals):
            if abs(v)<1e-9:continue
            if j<len(hall):inequalities.append(['H',list(hall[j][0]),rat(v)])
            else:inequalities.append(['T',list(tri[j-len(hall)][0]),rat(v)])
        ups=[[list(edges[j]),rat(v)] for j,v in enumerate(sol.upper.marginals[:M]) if abs(v)>1e-9]
        bound=sum((-Fraction(v) if typ=='H' else 2*Fraction(v)) for typ,U,v in inequalities)+sum(Fraction(v) for e,v in ups)
        record={'r':r,'index':idx,'supports':list(masks),'degree_duals':['0']*16,
            'inequality_duals':inequalities,'upper_duals':ups,'bound':str(bound)}
        cert.verify_entry(record)
        records.append(record)
        if len(records)%15==0:print('EXACT RECORDS',len(records), 'last',r,idx, 'bound',bound,flush=True)
    assert len(records)==101
    obj={'schema':'ramsey.global-shadow.dual.v1','records':records}
    with gzip.open(DATA,'wt') as f:json.dump(obj,f,separators=(',',':'))
    print('SAVED',DATA,DATA.stat().st_size,flush=True)

def verify():
    stats,survivors=shadow_census()
    with gzip.open(DATA,'rt') as f:obj=json.load(f)
    assert obj['schema']=='ramsey.global-shadow.dual.v1'
    records={(rec['r'],rec['index']):rec for rec in obj['records']}
    expected={(r,i) for r,i,m in survivors if (r,i)!=(4,17)}
    assert set(records)==expected and len(records)==101
    bounds=[];t_counts=Counter()
    for r,idx,m in survivors:
        if (r,idx)==(4,17):continue
        rec=records[(r,idx)]
        assert tuple(rec['supports'])==m
        assert all(x=='0' for x in rec['degree_duals'])
        bounds.append(cert.verify_entry(rec))
        t_counts[r]+=1
    print('CENSUS r, classes, shadow-excluded, no-shadow-exclusion:',stats)
    print('EXACT rational proof for 101 further classes, by r:',dict(t_counts))
    print('Range of positive rational bounds:',min(bounds),max(bounds))
    print('Only unresolved class in this two-stage audit is (r,index)=(4,17); proven by 10-versus-9 structural cut.')

if __name__=='__main__':
    if '--generate' in sys.argv:generate()
    verify()
