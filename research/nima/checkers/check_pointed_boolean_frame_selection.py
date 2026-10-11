"""Exhaustive Boolean edge/marked-state attachment controls.
No claim of extracting or executing Agda higher witnesses.
"""
from itertools import product
from pathlib import Path
import hashlib
import json
ROOT=Path(__file__).resolve().parents[1]
EDGES=((0,1),(0,2),(0,3),(1,2),(1,3),(2,3))
TRIANGLES=((0,1,2),(0,1,3),(0,2,3),(1,2,3))
BITS=tuple(product((0,1),repeat=4))

def edges(m):return tuple(m[i]^m[j] for i,j in EDGES)
def move(e,g):return tuple(b^g[i]^g[j] for b,(i,j) in zip(e,EDGES))
def flat(e):
    d=dict(zip(EDGES,e))
    return all(d[i,j]^d[j,k]==d[i,k] for i,j,k in TRIANGLES)
def orientation(bit):return (-1)**bit

def main():
    all_edges=tuple(product((0,1),repeat=6))
    flats=tuple(e for e in all_edges if flat(e))
    assert len(flats)==8
    assert set(flats)=={edges(m) for m in BITS}
    zero=(0,)*6
    assert {move(zero,g) for g in BITS}==set(flats)
    # Any equivariant sign f on this transitive orbit is determined by f(0).
    # Its relative character is (-1)^(g1+g2). Both permitted base signs work.
    for base in (-1,1):
        f=lambda e:base*orientation(e[EDGES.index((1,2))])
        for e,g in product(flats,BITS):
            assert f(move(e,g))==orientation(g[1]^g[2])*f(e)
    # A marked Boolean value selects order (mark, other), relative to the
    # declared counting basis (false,true). Compatible edges preserve that order.
    for m in BITS:
        e=edges(m)
        for b,(i,j) in zip(e,EDGES):
            assert m[i]^b==m[j]
            assert orientation(m[i])*orientation(m[j])==orientation(b)
        for g in BITS:
            moved=tuple(a^b for a,b in zip(m,g))
            assert edges(moved)==move(e,g)
        # Ad_J(I)=I, Ad_J(X)=-X; multiplying by relative orientation
        # therefore fixes the source edge, so also fixes V tensor U.
        b=e[EDGES.index((1,2))]
        assert orientation(m[1])*orientation(m[2])*orientation(b)==1
    # The actual TypedFixture has marks false,true,false,true.
    fixture=(0,1,0,1)
    assert edges(fixture)==(1,0,1,1,0,1)
    # Holding marks fixed while flipping one edge violates pointed compatibility.
    invalid=list(edges(fixture));invalid[EDGES.index((1,2))]^=1
    assert fixture[1]^invalid[EDGES.index((1,2))]!=fixture[2]
    result=dict(schema='marici.nima.pointed-boolean-frame-selection.v1',status='pass',
        flat_edge_assignments=8,marked_assignments=16,frame_assignments=16,
        classification='Every equivariant relative sign on the flat Boolean edge orbit is plus or minus det(V). Compatible marked states give the plus convention through their ordered counting bases.',
        typed_fixture_edge_bits=list(edges(fixture)),
        signal='The marked-state attachment fixes V tensor U, hence its hidden readout equals its ordinary readout. The opposite global convention only negates all outputs; it does not distinguish flat histories.',
        source_distinction='LossyDiagonal stores Bool types, not inhabitants. TypedFixture stores inhabitants but its dependent paths require their transport compatibility.',
        limit='Classification concerns Boolean permutation edge readouts and compatible marked states, not equality of full retained syntax or all WG source types.',
        source_sha256={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in ('agda/RetainedTetrahedralPackage.agda','checkers/check_pointed_boolean_frame_selection.py')})
    (ROOT/'results/pointed-boolean-frame-selection.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))

if __name__=='__main__':main()
