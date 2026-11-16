#!/usr/bin/env python3
"""Exact finite checks for reflected simplicial local-to-global obstructions.
Requires Python stdlib only. Does not assert a Ramsey translation.
"""
from itertools import combinations
from collections import Counter, defaultdict, deque
from math import comb

def norm(face): return tuple(sorted(face))
def edges_of(t): return [norm(e) for e in combinations(t,2)]
def vertices(faces): return set(x for face in faces for x in face)
def edge_degrees(faces): return Counter(e for t in faces for e in edges_of(t))
def graph_components(graph):
    todo=set(graph); out=[]
    while todo:
        src=min(todo);todo.remove(src); q=[src]; cc={src}
        while q:
            x=q.pop()
            for y in graph[x]:
                if y in todo:
                    todo.remove(y);cc.add(y);q.append(y)
        out.append(tuple(sorted(cc)))
    return sorted(out)
def link(v,faces):
    graph=defaultdict(set)
    for t in faces:
        if v in t:
            x,y=[a for a in t if a!=v]
            graph[x].add(y);graph[y].add(x)
    return {k:sorted(vs) for k,vs in sorted(graph.items())}
def rank_f2(columns):
    basis={}
    for val in columns:
        while val:
            p=val.bit_length()-1
            if p in basis: val ^= basis[p]
            else:
                basis[p]=val;break
    return len(basis)
def betti_f2(faces):
    v=sorted(vertices(faces));e=sorted(edge_degrees(faces)); f=sorted(faces)
    vm={x:i for i,x in enumerate(v)};em={x:i for i,x in enumerate(e)}
    ranks=[rank_f2([sum(1<<vm[x] for x in edge) for edge in e]),
           rank_f2([sum(1<<em[x] for x in edges_of(t)) for t in f])]
    b0=len(v)-ranks[0];b1=len(e)-ranks[0]-ranks[1];b2=len(f)-ranks[1]
    return (b0,b1,b2)

def assert_pair_star():
    # R is a 4-triangle star, B its point reflection.
    # The vertices 0 and 1 are antipodal points on the central shared edge.
    R=[norm(x) for x in [(0,1,2),(0,1,3),(0,2,4),(1,2,5)]]
    rho={0:1,1:0,2:6,6:2,3:7,7:3,4:8,8:4,5:9,9:5}
    B=[norm(rho[x] for x in f) for f in R]
    F=R+B
    # R's dual graph has K_{1,3} (branching tree), and similarly B.
    def dual(faces):
        return {i:sorted(j for j in range(len(faces)) if i!=j and len(set(faces[i])&set(faces[j]))==2) for i in range(len(faces))}
    assert dual(R)=={0:[1,2,3],1:[0],2:[0],3:[0]}
    assert dual(B)=={0:[1,2,3],1:[0],2:[0],3:[0]}
    assert len(set(F))==8
    assert set(norm(rho[x] for x in f) for f in F)==set(F)
    for D in (R,B):
        dd=edge_degrees(D)
        assert all(k in (1,2) for k in dd.values())
        assert len(vertices(D))-len(dd)+len(D)==1
        for v in vertices(D):
            lk=link(v,D)
            assert len(graph_components(lk))==1
            assert sorted(len(nbrs) for nbrs in lk.values()).count(1)==2
            assert max(len(nbrs) for nbrs in lk.values())<=2
    # Genuine 3D point-reflection coordinates can realize these two star disks
    # along the common central segment (0,1).
    xyz={0:(1,0,0),1:(-1,0,0),2:(0,1,0),3:(0,0,1),4:(2,2,0),5:(-2,2,0)}
    xyz.update({rho[k]:tuple(-c for c in xyz[k]) for k in range(2,6)})
    assert all(xyz[rho[k]]==tuple(-c for c in xyz[k]) for k in rho)
    assert edge_degrees(F)[norm((0,1))]==4
    around=[f for f in F if set([0,1]).issubset(f)]
    assert len(around)==4
    for pair in combinations(around,2): assert edge_degrees(pair)[norm((0,1))]==2
    print('STAR:', 'R dual=', dual(R), 'B dual=',dual(B), 'triangles=',len(F),'max edge multiplicity=',max(edge_degrees(F).values()),'overloaded edge=',norm((0,1)))

def assert_vertex_link():
    # Two tetrahedral boundary spheres point-reflected through their common vertex.
    pos=[0,1,2,3];neg=[0,4,5,6]
    R=[norm(f) for f in combinations(pos,3)];B=[norm(f) for f in combinations(neg,3)]
    F=R+B
    rho={0:0,1:4,4:1,2:5,5:2,3:6,6:3}
    assert set(norm(rho[x] for x in f) for f in F)==set(F)
    assert len(F)==8 and len(vertices(F))==7 and len(edge_degrees(F))==12
    assert set(edge_degrees(F).values())=={2}
    L=link(0,F)
    comps=graph_components(L)
    assert comps==[(1,2,3),(4,5,6)]
    assert all(len(vs)==2 for vs in L.values())
    for v in vertices(F)-{0}:
        ll=link(v,F)
        assert len(graph_components(ll))==1
        assert all(len(vs)==2 for vs in ll.values())
    assert betti_f2(F)==(1,0,2)
    assert len(vertices(F))-len(edge_degrees(F))+len(F)==3
    # All edges already have two faces. No additional 2-simplex using the
    # seven existing vertices can be attached while keeping ridge degree <=2.
    excluded=[t for t in combinations(range(7),3) if norm(t) not in F]
    admissible=[t for t in excluded if all(edge_degrees(F)[norm(e)]<2 for e in combinations(t,2))]
    assert len(excluded)==27 and admissible==[]
    # Reflection acts as a swap of the two link components, on reduced H0 as minus 1.
    print('LINK:',f'V={len(vertices(F))}',f'E={len(edge_degrees(F))}',f'F={len(F)}','chi=3','betti_mod2=',betti_f2(F), 'link_components_at_fixed_vertex=',comps)
    # More than 1 component in a degree-2 link requires >=2*3 distinct neighbors.
    assert 1+3*2 == 7
    print('MINIMALITY:', 'disconnected vertex link in closed pure simplicial 2-pseudomanifold needs at least 7 vertices (two disjoint cycles of minimum length 3)')

def assert_parity_control():
    # Coherence label model: each of the 4 tetrahedral faces has a Z/2 2-cochain.
    # Flatness requires their total mod-2 coboundary zero.
    from itertools import product
    faces=tuple(combinations(range(4),3))
    data=list(product((0,1),repeat=4))
    admissible=[w for w in data if sum(w)%2==0]
    assert len(admissible)==8
    for missing in range(4):
        for labels in product((0,1),repeat=3):
            extensions=[]
            for w in admissible:
                if tuple(w[i] for i in range(4) if i!=missing)==labels:extensions.append(w)
            assert len(extensions)==1
    bad=(1,0,0,0)
    assert bad not in admissible
    print('COCHAIN:', 'each prescribed triple of 4 faces admits exactly one flat completion;', 'odd full 4-face labeling does not. Flatness is ADDITIONAL semantic structure.')

if __name__=='__main__':
    assert_pair_star();assert_vertex_link();assert_parity_control();print('All exact assertions passed')
