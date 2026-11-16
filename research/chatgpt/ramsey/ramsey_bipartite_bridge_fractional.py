#!/usr/bin/env python3
"""Exact feasible fractional countermodel to a degree-free triangle-cover
certificate for exceptional support orbit (r,index)=(4,188). Discovery uses
scipy, verification uses integer fractions only.
"""
import json,sys
from fractions import Fraction
from pathlib import Path
from ramsey_fractional_witness_certificate import support_classes,constraints
HERE=Path(__file__).parent
PATH=HERE/'ramsey_bipartite_bridge_fractional.json'

def verify():
    import itertools
    s=support_classes(4)[0][188]
    edges,hall,tri=constraints(s)
    obj=json.loads(PATH.read_text())
    assert obj['supports']==list(s) and obj['edges']==[list(e) for e in edges]
    xs=[Fraction(q) for q in obj['values']]
    assert len(xs)==len(edges) and all(0<=v<=1 for v in xs)
    assert all(sum(xs[j] for j in E)>=1 for U,E in hall)
    assert all(sum(xs[j] for j in E)<=2 for U,E in tri)
    assert any(v not in (0,1) for v in xs)
    print('EXACT fractional countermodel: edges',len(xs),'Hall',len(hall),'triangles',len(tri),'denoms',sorted({x.denominator for x in xs}))

def generate():
    import numpy as np
    from scipy.optimize import linprog
    from scipy.sparse import coo_matrix
    s=support_classes(4)[0][188]
    edges,hall,tri=constraints(s);M=len(edges)
    rr=[];cc=[];vals=[];bounds=[]
    for typ,coll in [('H',hall),('T',tri)]:
        for U,E in coll:
            i=len(bounds)
            for j in E:rr.append(i);cc.append(j);vals.append(-1 if typ=='H' else 1)
            bounds.append(-1 if typ=='H' else 2)
    A=coo_matrix((vals,(rr,cc)),shape=(len(bounds),M)).tocsr()
    sol=linprog(np.zeros(M),A_ub=A,b_ub=bounds,bounds=[(0,1)]*M,method='highs')
    assert sol.status==0
    xs=[str(Fraction(float(x)).limit_denominator(100000)) for x in sol.x]
    PATH.write_text(json.dumps({'supports':list(s),'edges':[list(e) for e in edges],'values':xs},separators=(',',':')))
    print('CREATED',PATH)
if __name__=='__main__':
    if '--generate' in sys.argv:generate()
    verify()
