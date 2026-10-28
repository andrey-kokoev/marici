"""Exact ring subdivision and role-selection test for the small FCC octahedron."""
from itertools import combinations
from fractions import Fraction
from pathlib import Path
import json


def sub(a,b): return tuple(x-y for x,y in zip(a,b))
def det(a,b,c):
    return a[0]*(b[1]*c[2]-b[2]*c[1])-a[1]*(b[0]*c[2]-b[2]*c[0])+a[2]*(b[0]*c[1]-b[1]*c[0])
def volume(t): return Fraction(abs(det(*(sub(p,t[0]) for p in t[1:]))),6)


def main():
    entry=(0,0,0);exit=(2,0,0)
    ring=((1,1,0),(1,0,1),(1,-1,0),(1,0,-1))
    tetrahedra=[(entry,exit,ring[i],ring[(i+1)%4]) for i in range(4)]
    assert all(volume(t)==Fraction(1,3) for t in tetrahedra)
    assert sum(map(volume,tetrahedra))==Fraction(4,3)
    face_counts={}
    for t in tetrahedra:
        for f in combinations(t,3):
            key=tuple(sorted(f));face_counts[key]=face_counts.get(key,0)+1
    assert list(face_counts.values()).count(1)==8
    assert list(face_counts.values()).count(2)==4
    lengths=sorted(sum(x*x for x in sub(a,b)) for a,b in combinations(tetrahedra[0],2))
    assert lengths==[2,2,2,2,2,4]
    # The inserted polar diagonal is not a nearest-neighbour FCC edge.
    assert sum(x*x for x in sub(entry,exit))==4
    # Rotation fixing each pole acts transitively on both equatorial vertices
    # and tetrahedral wedges; it therefore cannot preserve a nontrivial P/N split.
    def rotate(p): return (p[0],-p[2],p[1])
    assert rotate(entry)==entry and rotate(exit)==exit
    assert tuple(rotate(p) for p in ring)==ring[1:]+ring[:1]
    assignments=[]
    for pair in combinations(range(4),2):
        protons=set(pair)
        alternating=all((i in protons)!=((i+1)%4 in protons) for i in range(4))
        invariant={(i+1)%4 for i in protons}==protons
        assert not invariant
        assignments.append({'P':list(pair),'N':sorted(set(range(4))-protons),
                            'alternating':alternating,'quarter_turn_invariant':invariant})
    assert sum(a['alternating'] for a in assignments)==2
    # Invariant subsets under the pole-preserving quarter turn are only empty/full.
    invariant=[]
    for size in range(5):
        for subset in combinations(range(4),size):
            if {(i+1)%4 for i in subset}==set(subset):invariant.append(subset)
    assert invariant==[(),(0,1,2,3)]
    out={'status':'pass','entry':entry,'exit':exit,'equatorial_cycle':ring,
         'tetrahedral_wedges':tetrahedra,'wedge_volumes':[str(volume(t)) for t in tetrahedra],
         'boundary_faces':8,'internal_faces':4,'wedge_edge_lengths_squared':lengths,
         'two_plus_two_assignments':assignments,
         'result':'Four shared-edge tetrahedral wedges reproduce the abstract nuclear ring pattern. Alternation yields 2+2 with two colour choices; directed endpoints alone select neither. Wedges require a subdivision and are not regular primitive honeycomb tetrahedra.'}
    path=Path(__file__).with_name('results')/'helium-role-test-v1.json'
    path.write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(out))


if __name__=='__main__':main()
