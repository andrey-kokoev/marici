"""Exact six-step FCC graph intervals and octahedral cell counts."""
from itertools import product, permutations
from collections import Counter
from pathlib import Path
import json


def add(a,b): return tuple(x+y for x,y in zip(a,b))
def sub(a,b): return tuple(x-y for x,y in zip(a,b))
def distance(a,b):
    d=tuple(abs(x-y) for x,y in zip(a,b))
    assert sum(d)%2==0
    return max(max(d),sum(d)//2)


def interval(a,b):
    length=distance(a,b)
    return {p for p in product(*(range(min(x,y)-length,max(x,y)+length+1) for x,y in zip(a,b)))
            if sum(p)%2==0 and distance(a,p)+distance(p,b)==length}


def main():
    # Six nearest-neighbour steps along one straight root direction.
    root_start=(0,0,0);root_end=(6,6,0)
    straight=interval(root_start,root_end)
    assert straight=={(i,i,0) for i in range(7)}

    # Opposite octahedral vertices at graph distance six.
    # The centre has odd coordinate parity; every actual vertex has even parity.
    centre=(1,0,0);start=(-2,0,0);end=(4,0,0)
    points=interval(start,end)
    expected={p for p in product(range(-2,5),range(-3,4),range(-3,4))
              if sum(p)%2==0 and sum(abs(v) for v in sub(p,centre))<=3}
    assert points==expected and distance(start,end)==6
    grades=dict(sorted(Counter(distance(start,p) for p in points).items()))
    assert grades=={0:1,1:4,2:9,3:16,4:9,5:4,6:1}
    directions={v for v in product((-1,0,1),repeat=3) if sum(abs(x) for x in v)==2}
    edges={tuple(sorted((p,add(p,d)))) for p in points for d in directions if add(p,d) in points}
    tetrahedra=[];octahedra=[]
    for corner in product(range(-3,5),range(-4,4),range(-4,4)):
        cube=[add(corner,v) for v in product((0,1),repeat=3)]
        tet=tuple(sorted(v for v in cube if sum(v)%2==0))
        if set(tet)<=points: tetrahedra.append(tet)
        if sum(corner)%2:
            octa=tuple(sorted(add(corner,tuple(sign if i==axis else 0 for i in range(3)))
                              for axis in range(3) for sign in (-1,1)))
            if set(octa)<=points:octahedra.append(octa)
    # Primitive tetrahedron has volume 1/3 in integer FCC coordinates; an
    # octahedron has volume 4/3. Their sum must fill radius-three L1 octahedron.
    assert len(tetrahedra)+4*len(octahedra)==108
    # All proper signed coordinate permutations and translations preserve the
    # counts: exact bijection of this point set and its graph-distance grades.
    symmetry_cases=0
    for perm in permutations(range(3)):
        for signs in product((-1,1),repeat=3):
            def transform(p):return tuple(signs[i]*p[perm[i]] for i in range(3))
            transformed={transform(p) for p in points}
            a,b=transform(start),transform(end)
            assert Counter(distance(a,p) for p in transformed)==Counter(distance(start,p) for p in points)
            symmetry_cases+=1
    paths={start:1}
    for grade in range(1,7):
        for p in points:
            if distance(start,p)==grade:
                paths[p]=sum(paths.get(sub(p,d),0) for d in directions if distance(start,sub(p,d))==grade-1)
    report={'status':'pass','lattice':'FCC / A3, even-sum integer chart',
      'rule':'All vertices on shortest nearest-neighbour paths between the endpoints',
      'straight_root_axis':{'endpoints':[root_start,root_end],'distance':6,'vertices':len(straight),'shape':'line'},
      'octahedral_axis':{'endpoints':[start,end],'centre':centre,'distance':6,'vertices':len(points),
        'grades':grades,'edges':len(edges),'tetrahedra':len(tetrahedra),'octahedra':len(octahedra),
        'volume':36,'shortest_paths':paths[end],'signed_coordinate_symmetries_checked':symmetry_cases},
      'points':sorted(points),'tetrahedron_cells':tetrahedra,'octahedron_cells':octahedra,
      'conclusion':'Six-step octahedral graph interval exists with grades 1,4,9,16,9,4,1. Straight root-axis six steps instead gives a line. No proton/neutron role readout has been supplied; neither count is a Pb-208 identification.'}
    target=Path(__file__).with_name('results')/'six-step-octahedron-v1.json';target.parent.mkdir(exist_ok=True)
    target.write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in report.items() if k not in ('points','tetrahedron_cells','octahedron_cells')}))


if __name__=='__main__':main()
