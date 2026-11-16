#!/usr/bin/env python3
"""Exact proof-DAG extraction for the 693 unit-propagation contradictions.
Reasons refer to matroid circuits and allowed triangles, never to LP results.
"""
from collections import Counter
from itertools import combinations
import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parent))
from ramsey_fractional_witness_certificate import support_classes,constraints
from ramsey_support_matroid_circuit_audit import circuits_of

def explain(s):
    edges,hall,tri=constraints(s)
    cmap=dict(hall)
    h=[(C,tuple(cmap[C])) for C in circuits_of(s)]
    t=[(U,E) for U,E in tri]
    # assign variable index to polarity with supporting premise rule and other variables
    vals={}; causes={}
    for iteration in range(20):
        progress=False
        for kind,clauses,pol in [('H',h,1),('T',t,0)]:
            for U,cl in clauses:
                opp=1-pol
                known_opp=[e for e in cl if vals.get(e)==opp]
                if len(known_opp)==len(cl):
                    terminal=(kind,U,tuple(known_opp))
                    # traverse the derivations of each false literal
                    seen=set(); visited=set()
                    def walk(e):
                        if e in visited:return
                        visited.add(e)
                        K,V,deps=causes[e]
                        seen.add((K,V))
                        for d in deps:walk(d)
                    for e in known_opp:walk(e)
                    seen.add((kind,U))
                    return False, {'iterations':iteration+1,'derived':len(causes),'used_clauses':len(seen),'involved_vertices':len(set(v for K,U in seen for v in U)),'terminal_kind':kind,'terminal_U':U,'used':seen}
                unknown=[e for e in cl if e not in vals]
                if len(unknown)==1 and len(known_opp)==len(cl)-1:
                    e=unknown[0];vals[e]=pol;causes[e]=(kind,U,tuple(known_opp));progress=True
        if not progress: return True, {'iterations':iteration+1,'derived':len(causes)}
    raise RuntimeError('no convergence')

def main():
    bound=Counter();steps=Counter();terminations=Counter();maxcore=(0,None);surv=[]
    sums=Counter();sizecores=Counter()
    for r in range(5):
        for i,s in enumerate(support_classes(r)[0]):
            ok,info=explain(s)
            if ok:surv.append((r,i,info));continue
            k=info['used_clauses'];bound[k]+=1
            steps[info['iterations']]+=1
            terminations[info['terminal_kind']]+=1
            sizecores[info['involved_vertices']]+=1
            sums[(r,info['terminal_kind'])]+=1
            if k>maxcore[0]:maxcore=(k,(r,i,info))
    print('survivors:',surv)
    print('termination:',dict(terminations),'core clause sizes:',dict(sorted(bound.items())))
    print('iterations:',dict(sorted(steps.items())))
    print('involved vertices:',dict(sorted(sizecores.items())))
    print('maximal core:',maxcore[0], maxcore[1][0:2], {k:v for k,v in maxcore[1][2].items() if k!='used'})
    assert [(r,i) for r,i,_ in surv]==[(4,17),(4,188)]

if __name__=='__main__':main()
