"""Actual lower-layer obstruction and corrected frame cocycles."""
from pathlib import Path
from itertools import product
import importlib.util
import json
import sympy as s

HERE=Path(__file__).resolve().parent

def load(name,file):
    spec=importlib.util.spec_from_file_location(name,HERE/file)
    module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
    return module

g=load('growth','check_translated_cubic_observer_growth.py')
t=load('tower','check_all_depth_observer_tower.py')
f=g.f


def main():
    keys=[((('e',*ea,1),('e',*eb,1),('e',15,31,0)),((),(),(),()))
          for ea in ((0,1),(1,3)) for eb in ((3,7),(7,15))]
    keys.append(((('e',0,1,1),('e',5,7,1),('e',15,31,0)),((),(),(),())))
    a=f['relation']((0,1),1)
    middle={((2,3),(0,1)):1}
    c=f['relation']((4,5),0)
    hostile=f['chain_product']([a,middle,c])
    assert len(hostile)==8
    assert all(len(word)==6 and sum(marks)==2 for word,marks in hostile)
    assert not t.ordered(0,hostile,1)
    assert t.ordered(0,hostile,2)
    image=t.ordered(0,hostile,3)
    row=s.Matrix([image.get(key,0) for key in keys])
    assert row==s.Matrix([0,1,0,1,0])
    ma,ga,mc,gb=s.symbols('ma ga mc gb',positive=True)
    mb=ma+ga;md=mc+gb
    old=s.Matrix([[ma*mc,-ma*md,-mb*mc,mb*md,0]])
    private=s.Matrix([[ga*gb,0,0,0,-ma*md]])
    delta=private-old
    assert s.simplify((old*row)[0]-ga*md)==0
    assert private*row==s.zeros(1,1)
    v0=s.Matrix([1,1,1,1,0]);vx=s.Matrix([0,1,0,0,1])
    hidden=row-md/gb*v0
    assert s.simplify((old*hidden)[0])==0
    assert s.simplify((private*hidden)[0]+ga*md)==0
    assert s.simplify(s.det(s.Matrix.hstack(old.T,private.T).T[:,[0,1]]))!=0
    columns=0
    for pairs in g.pairings(tuple(range(6))):
        for kinds in ((1,1,0),(1,0,1),(0,1,1)):
            start=0;ds=[]
            for pair,kind in zip(pairs,kinds):
                ds.append(g.one(f['derivative'](start,f['relation'](pair,kind))))
                start|=sum(1<<j for j in pair)
            im=g.join(g.join(ds[0],ds[1]),ds[2])
            values=s.Matrix([im.get(key,0) for key in keys])
            assert s.simplify((delta*values)[0])==0
            columns+=1
    # Common lower-layer correction channels give triangular frame changes.
    offsets=((0,0),(1,0),(0,1))
    def transition(gidx,fidx):
        dg=offsets[gidx];df=offsets[fidx]
        return s.Matrix([[1,dg[0]-df[0],dg[1]-df[1]],[0,1,0],[0,0,1]])
    routes=0
    for i,j,k in product(range(3),repeat=3):
        assert transition(k,j)*transition(j,i)==transition(k,i)
        assert transition(i,j)*transition(j,i)==s.eye(3)
        # Preceding tower coordinates are unchanged under this stage change.
        full=s.diag(s.ones(1,1),transition(j,i))
        drop=s.Matrix([[1,0,0,0]])
        assert drop*full==drop
        routes+=1
    assert 1+30**2==901
    result={'passed':True,'actual_I2_hostile_terms':len(hostile),
        'hostile_selected_coefficients':list(row),
        'minimal_I3_columns_annihilated_by_correction':columns,
        'corrected_frame_composition_routes':routes,
        'scope':'Actual I2 obstruction and I3 agreement. General minimal refinement and saturated tower coherence use the finite-support module proof; no extension-class preservation follows merely from the cocycle.'}
    # Convert Sympy integers before JSON serialization.
    result['hostile_selected_coefficients']=[int(v) for v in row]
    out=HERE.parent/'results/saturated-frame-corrections.json'
    out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))


if __name__=='__main__':main()
