#!/usr/bin/env python3
"""Test triangle-free 40-point graphs fixed by the 24-element Steiner stabilizer.

The Steiner S(3,6,42) is reconstructed from the published permutation
cycles. Choose p=1,q=10: the 24-element stabilizer of p also fixes q.
It acts in three point orbits of sizes 8,8,24 on remaining 40 points,
and in 36 edge orbits. A full invariant graph is a 36-bit selection.

Triangle constraints and optional independent-10-set cuts are exact.
Optimization uses scipy.optimize.milp; independent witnesses use
networkx maximal clique in the complement (exact branch bound).
"""
from itertools import combinations
from collections import Counter
import numpy as np
from scipy.optimize import milp, Bounds, LinearConstraint
from scipy.sparse import csr_matrix, lil_matrix
import networkx as nx
from steiner_ramsey_matrix_test import *


def make_problem():
    group=group_from_generators((perm_from_cycles(ALPHA_CYCLES),perm_from_cycles(BETA_CYCLES)))
    p,q=1,10
    st=[g for g in group if g[p]==p]
    assert len(st)==24 and all(g[q]==q for g in st)
    P=tuple(x for x in range(1,43) if x not in (p,q))
    index={x:i for i,x in enumerate(P)}
    tuples=set(combinations(range(40),2))
    orbits=[]
    while tuples:
        a,b=min(tuples)
        O={tuple(sorted((index[g[P[a]]],index[g[P[b]]]))) for g in st}
        tuples-=O
        orbits.append(O)
    assert len(orbits)==36 and sum(map(len,orbits))==780
    emap={edge:j for j,orb in enumerate(orbits) for edge in orb}
    orbit_degrees=[]
    for orbit in orbits:
        degrees=Counter(v for e in orbit for v in e)
        orbit_degrees.append(np.array([degrees[i] for i in range(40)]))
    # Triples have at most 3 distinct edge-orbit indices; aggregate constraints.
    trip_constraints={}
    forced_zero=set()
    for a,b,c in combinations(range(40),3):
        indices=[emap[a,b],emap[a,c],emap[b,c]]
        d=tuple(sorted(Counter(indices).items()))
        if len(d)==1:forced_zero.add(indices[0])
        trip_constraints[d]=trip_constraints.get(d,0)+1
    print('Steiner 24 stabilizer on 40 points: 36 edge orbits, sizes', Counter(map(len,orbits)))
    print('triangle rows compressed',len(trip_constraints),'forced-zero orbit classes',len(forced_zero))
    print('point orbits sizes',end=' ')
    seen=set();pointOrbits=[]
    for v in range(40):
        if v not in seen:
            O={index[g[P[v]]] for g in st}
            pointOrbits.append(O);seen|=O
    print(sorted(map(len,pointOrbits)))
    return P,orbits,emap,orbit_degrees,trip_constraints,forced_zero


def optimize(max_time=30, cycles=1):
    P,orbits,emap,degree_orbits,trip_counts,forced=make_problem()
    n=len(orbits)
    constraints=[]
    for row,num in trip_counts.items():
        coeff=np.zeros(n)
        for i,c in row:coeff[i]=c
        constraints.append((coeff,-np.inf,2))
    # Red neighborhood of any vertex in a red triangle-free Ramsey(3,10)
    # graph is independent of size its degree, so degree <= 9.
    for v in range(40):
        coeff=np.array([degree_orbits[i][v] for i in range(n)],dtype=float)
        constraints.append((coeff,-np.inf,9))
    max_edges=np.array([len(o) for o in orbits],dtype=float)
    selected_idx=[]
    for iteration in range(cycles):
        A=csr_matrix(np.vstack([r for r,_,_ in constraints]))
        lb=np.array([a for _,a,_ in constraints])
        ub=np.array([b for _,_,b in constraints])
        result=milp(-max_edges,integrality=np.ones(n),bounds=Bounds(np.zeros(n),np.ones(n)),constraints=LinearConstraint(A,lb,ub),options={'time_limit':max_time})
        if result.x is None:
            print('Optimization',iteration,'status',result.message)
            return
        chosen={i for i,x in enumerate(result.x) if x>.5}
        E=[e for i in chosen for e in orbits[i]]
        g=nx.Graph();g.add_nodes_from(range(40));g.add_edges_from(E)
        alpha=len(nx.algorithms.clique.max_weight_clique(nx.complement(g),weight=None)[0]);
        degrees=Counter(dict(g.degree()).values())
        print(f'iteration {iteration}: edges={len(E)}, orbit classes={len(chosen)}, independence={alpha}, degree={dict(degrees)}, milp={result.message}',flush=True)
        if alpha<=9:
            print('RAMSEY(3,10) 40-VERTEX WITNESS FOUND:',[(P[u],P[v]) for u,v in E]);return
        # Any 10-set inside an alpha-witness must contain a red edge.
        max_set=nx.algorithms.clique.max_weight_clique(nx.complement(g),weight=None)[0]
        # Add up to 12 distinct independent-10 cuts from the current witness.
        already = {tuple(np.where(r>0)[0]) for r,lo,hi in constraints if lo==1}
        added=0
        for T in combinations(sorted(max_set),10):
            indices={emap[e] for e in combinations(T,2)}
            signature=tuple(sorted(indices))
            if signature in already:continue
            already.add(signature)
            coeff=np.zeros(n)
            for i in indices:coeff[i]=1
            constraints.append((coeff,1,np.inf))
            added+=1
            if added>=12:break
        print('  independent-10 cuts added',added,flush=True)
        if not added:break

if __name__=='__main__':
    import sys
    optimize(float(sys.argv[1]) if len(sys.argv)>1 else 20,int(sys.argv[2]) if len(sys.argv)>2 else 2)
