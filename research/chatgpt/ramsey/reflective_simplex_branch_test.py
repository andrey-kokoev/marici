"""Exhaustive antipodal triangulations of a six-panel prism.

R is four triangles: central (0,2,4), ears (0,1,2), (2,3,4), (4,5,0).
B is its point reflection. B_i=-T_i; the bottom vertex directly below
T_i is B_(i+3 mod 6). Opposite side panels must use opposite diagonals.

A second red four-triangle disk with path dual graph is tested as control.
Requires networkx for graph-isomorphism checks.
"""
from itertools import combinations, product
from collections import Counter
import networkx as nx

T = [('T', i) for i in range(6)]
B = [('B', i) for i in range(6)]
R_STAR = [(0,2,4), (0,1,2), (2,3,4), (4,5,0)]
R_CHAIN = [(0,1,2), (0,2,3), (0,3,4), (0,4,5)]

def complex_for(red_faces, bits):
    # Inversion exchanges the two diagonals of opposite side panels.
    choices = list(bits) + [1 - b for b in bits]
    red = [tuple(T[i] for i in face) for face in red_faces]
    blue = [tuple(B[i] for i in face) for face in red_faces]
    green = []
    for i, x in enumerate(choices):
        a, b = T[i], T[(i + 1) % 6]
        c, d = B[(i + 3) % 6], B[(i + 4) % 6]
        green += [(a,b,d),(a,d,c)] if x == 0 else [(a,b,c),(b,c,d)]
    faces = red + blue + green
    edges = Counter(tuple(sorted(edge)) for f in faces for edge in combinations(f, 2))
    graph = nx.Graph(); graph.add_nodes_from(T+B); graph.add_edges_from(edges)
    opposite = lambda node: ('B' if node[0]=='T' else 'T', node[1])
    face_set = {frozenset(f) for f in faces}
    assert {frozenset(opposite(v) for v in f) for f in faces} == face_set
    assert len(faces) == 20 and len(edges) == 30 and len(graph) == 12
    assert set(edges.values()) == {2}   # each edge exactly two triangles
    assert 12-30+20 == 2
    for v in graph:
        link=nx.Graph()
        for face in faces:
            if v in face:
                w=[u for u in face if u!=v]
                link.add_edge(*w)
        assert nx.is_connected(link)
        assert set(dict(link.degree()).values()) == {2}  # link a circle
    return graph, red, blue, green

def main():
    for label, red in [('branched',R_STAR),('linear',R_CHAIN)]:
        balanced=[]
        print(label)
        for bits in product((0,1), repeat=3):
            graph, rf, bf, gf = complex_for(red, bits)
            degrees = sorted(dict(graph.degree()).values())
            uniform = len(set(degrees)) == 1
            if uniform:
                balanced.append(bits)
                assert degrees==[5]*12
                assert nx.is_isomorphic(graph, nx.icosahedral_graph())
            print('  '+''.join(map(str,bits))+' => '+str(dict(sorted(Counter(degrees).items())))+(' ICOSAHEDRON' if uniform else ''))
        print('  uniform-degree completions:',balanced)
        if label=='branched': assert balanced==[(1,0,1)]
        else: assert not balanced

    graph, red, blue, green=complex_for(R_STAR,(1,0,1))
    bridge=nx.Graph()
    bridge.add_nodes_from(T+B)
    for f in red+blue+green:
        bridge.add_edges_from(e for e in combinations(f,2) if e[0][0]!=e[1][0])
    assert nx.is_connected(bridge)
    assert bridge.number_of_edges()==12 and len(nx.cycle_basis(bridge))==1
    assert len(nx.cycle_basis(bridge)[0])==6
    print('green mixed-edge bridge: unique 6-cycle plus 6 pendant edges')

if __name__ == '__main__': main()
