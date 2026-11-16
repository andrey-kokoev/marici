#!/usr/bin/env python3
"""Finite circuit-shape and exceptional-shadow audit for Ramsey R(3,7).
Classifies local matroid circuit templates in the 115 non-immediate
unit-propagation proofs and the two surviving singleton red graphs.
"""
import sys,gzip,json
from pathlib import Path
from itertools import permutations
from collections import Counter
root=Path(__file__).resolve().parent
sys.path.insert(0,str(root))
from ramsey_fractional_witness_certificate import support_classes
from ramsey_support_matroid_circuit_audit import find_circuit
from ramsey_circuit_unit_propagation import propagate
from ramsey_propagation_proof_cores import explain


def circuit_shape(masks):
    labels=tuple(i for i in range(6) if any((m>>i)&1 for m in masks))
    d=len(labels)
    words=tuple(sum(1<<j for j,z in enumerate(labels) if (m>>z)&1) for m in masks)
    return min(tuple(sorted(sum(1<<p[j] for j in range(d) if (x>>j)&1)
                            for x in words)) for p in permutations(range(d)))

def graph_type(edge_set):
    verts=set(range(6))
    deg=tuple(sorted((sum(x in e for e in edge_set) for x in verts),reverse=True))
    adj={u:{v for e in edge_set for v in e if u in e and v!=u} for u in verts}
    comps=[];todo=set(verts)
    while todo:
        start=todo.pop();component={start};front=[start]
        while front:
            u=front.pop()
            for v in adj[u]:
                if v not in component:component.add(v);todo.discard(v);front.append(v)
        comps.append(component)
    sizes=sorted(map(len,comps),reverse=True)
    if deg==(3,2,2,2,2,1) and sizes==[6]:
        # A 5-cycle and pendant leaf; unique graph on those six degrees?
        leaf=next(i for i in verts if len(adj[i])==1)
        cycleverts=verts-{leaf}
        assert len(edge_set)==6
        assert sum(len(adj[v]&cycleverts) for v in cycleverts)==10
        return 'five-cycle-plus-leaf'
    if deg==(3,3,2,2,2,0) and sizes==[5,1]:
        A={v for v in verts if len(adj[v])==2}
        B={v for v in verts if len(adj[v])==3}
        if all(tuple(sorted((a,b))) in edge_set for a in A for b in B):
            return 'K3,2-plus-isolate'
    return ('unclassified',deg,sizes)

def audit():
    C=Counter();size_counter=Counter();S=Counter()
    records=json.load(gzip.open(root/'ramsey_triangle_cover_supplement.json.gz'))['records']
    for r in records:
        m=r['supports']
        for typ,U,y in r['inequality_duals']:
            if typ!='H':continue
            sub=tuple(m[j] for j in U)
            c=find_circuit(tuple(U),m)
            assert c==tuple(U)
            shape=circuit_shape(sub)
            C[shape]+=1;size_counter[len(U)]+=1
    assert len(C)==27 and size_counter=={3:349,4:347,5:59}
    print('115 earlier rational certificates: 755 minimal circuit clauses, 27 types')
    print('by size:',dict(size_counter),'distinct types:',{k:sum(len(x)==k for x in C) for k in (3,4,5)})
    U=Counter(); prop_proofs=0
    for r in range(5):
        for idx,m in enumerate(support_classes(r)[0]):
            ok,info=explain(m)
            if ok or info['used_clauses']<=4:continue
            prop_proofs+=1
            for typ,verts in info['used']:
                if typ=='H':U[circuit_shape(tuple(m[i] for i in verts))]+=1
    assert prop_proofs==115
    assert len(U)==23 and sum(U.values())==725
    print('115 nontrivial unit-propagation cores: 725 circuit clauses, 23 local circuit types')
    print('propagation types by size:',{k:sum(len(x)==k for x in U) for k in (3,4,5)})
    for idx in (17,188):
        m=support_classes(4)[0][idx]
        pairs={tuple(i for i in range(6) if (s>>i)&1) for s in m if s.bit_count()==2}
        typ=graph_type(pairs)
        S[typ]+=1
        assert propagate(m)[0]
        print('critical support class',idx,'singleton shadow',typ,'pair supports',sorted(pairs))
    assert S=={'five-cycle-plus-leaf':1,'K3,2-plus-isolate':1}
    print('EXACT CHECK PASSED')

if __name__=='__main__':audit()
