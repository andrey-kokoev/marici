"""Exact violation signatures for four unordered, possibly repeated, legal rows.
Each signature is a hitting-set constraint. A zero signature denotes a valid join.
Run with uv run --with scipy -- python ... for the optional minimum-size MILP.
"""
from itertools import combinations_with_replacement
from math import comb
import json,sys
from pathlib import Path

def run(flip):
    blue=[0]
    for i in range(12):
        adj=sum(1<<j for j in range(i) if i-j in (1,5,8) and not(flip and (j,i)==(3,8)))
        blue += [s|1<<i for s in blue if not s&adj]
    tests=sorted(b for b in blue if b.bit_count()>=2);assert max(b.bit_count() for b in tests)==4
    masks=[sum(1<<i for i,b in enumerate(tests) if b.bit_count()==k) for k in range(5)]
    misses=[sum(1<<i for i,b in enumerate(tests) if not b&r) for r in blue]
    # Sweep last row using bit-parallel threshold masks; discard supersets of known private tests.
    units=0;clauses=set();valid=0
    for a,b,c in combinations_with_replacement(range(len(blue)),3):
        x,y,z=misses[a],misses[b],misses[c];p=x|y|z;q=(x&y)|(x&z)|(y&z);r=x&y&z
        already=(q&masks[4])|(r&masks[3]);extra=(p&masks[4])|(q&masks[3])|(r&masks[2]);
        if already&units:continue
        for w in misses[c:]:
            v=already|(w&extra)
            if not v:valid+=1
            elif v&units:continue
            elif not v&(v-1):units|=v
            else:clauses.add(v)
    cs=sorted((v for v in clauses if not v&units),key=lambda v:(v.bit_count(),v));small=[]
    for v in cs:
        if not any((c&v)==c for c in small):small.append(v)
    print('flip',flip,'rows/tests',len(blue),len(tests),'valid',valid,'units',units.bit_count(),'residual clauses',len(small),flush=True)
    bits=lambda m:[i for i in range(len(tests)) if m>>i&1];chosen=units
    if small:
        from scipy.optimize import milp,Bounds,LinearConstraint
        import numpy as np
        A=np.array([[int(v>>i&1) for i in range(len(tests))] for v in small]);sol=milp(np.ones(len(tests)),integrality=np.ones(len(tests)),bounds=Bounds(0,1),constraints=LinearConstraint(A,1,np.inf),options={'time_limit':60,'mip_rel_gap':0.0});print(sol.message,sol.fun,sol.mip_dual_bound,flush=True)
        chosen |=sum(1<<i for i,x in enumerate(sol.x) if x>.5);assert all(chosen&v for v in small)
    print('selected',chosen.bit_count(),'rank bits',(comb(len(tests),chosen.bit_count())-1).bit_length(),flush=True)
    return dict(flip=flip,rows=len(blue),tests=len(tests),valid=valid,forced=[tests[i] for i in bits(units)],selected=[tests[i] for i in bits(chosen)],residual_clauses=[[tests[i] for i in bits(c)] for c in small])

if __name__=='__main__':
    for flip in (False,True):
        d=run(flip);Path(__file__).with_name('four_join_budget_'+('flip' if flip else 'base')+'.json').write_text(json.dumps(d))
