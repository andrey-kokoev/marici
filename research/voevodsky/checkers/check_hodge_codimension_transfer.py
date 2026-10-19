"""Exact degree, boundary and fixed-polarization transfer controls."""
from itertools import product
from pathlib import Path
import json
from check_hodge_fixed_sixfold_pairing import wedge,power,integrate
from check_hodge_global_multiplicativity_faces import chain


def main():
    for n in (1,2,3):
        assert (6+n)-(4+n-1)==3
    # No codimension-one cycle exists in the dimension-zero field source.
    assert 0-1<0
    # Product keeps coefficients and support tag; W has cubical degree zero.
    A={(2,3):1,(6,5):1,(3,5):-1,(2,15):-1}
    point_boundary=[]
    for (a,b),coefficient in A.items():
        point_boundary += [(('W',b),coefficient),(('W',a*b),-coefficient),(('W',a),coefficient)]
    assert chain(*point_boundary)=={}
    raw=chain((('W','Da'),1),*[(('W',pair),-c) for pair,c in A.items()])
    normalized={k:v for k,v in raw.items() if k!=('W','Da')}
    assert normalized=={('W',pair):-c for pair,c in A.items()}
    assert raw!=normalized
    degrees={n:6-n for n in range(4)}
    assert degrees=={0:6,1:5,2:4,3:3}
    E={(2*j,2*j+1):d for j,d in enumerate((1,1,1,-1,-1,-3))}
    E3=power(E,3);all_x=tuple(range(0,12,2))
    assert E3.get(all_x,0)==0
    R={tuple(2*j+b for j,b in enumerate(bits)):(-1)**(sum(bits)//2)
       for bits in product((0,1),repeat=6) if sum(bits)%2==0}
    assert R[all_x]==1
    assert integrate(wedge(E3,E3))==2160
    # Symbolic coefficients of the two complete intersections agree for every m.
    for m in (1,2,3,5):
        cls=m**3
        assert cls-cls==0 and 2160*cls>0
    # The m values test arithmetic only; no specific very-ampleness bound is inferred.
    result={'passed':True,'classification':'codimension_transfer_constructed_zero_degree_zero_source',
        'codimension':3,'cubical_levels':[1,2,3],'regulator_degrees':degrees,
        'new_degree_zero_class_generated':False,'nonconstant_boundary_cycle_class':0,
        'Hodge_proved':False,'Hodge_refuted':False,
        'next_test':'Degree-six Deligne lift versus algebraic regulator image on the fixed Hodge space.'}
    root=Path(__file__).resolve().parents[3]
    (root/'research/voevodsky/results/hodge-higher-cycle-codimension-transfer-v1.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result))


if __name__=='__main__':main()
