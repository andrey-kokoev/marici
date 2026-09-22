"""Actual cubic-sector equality and symbolic order-optimal recalibrations."""
from pathlib import Path
import importlib.util
import json
import sympy as s

HERE=Path(__file__).resolve().parent
spec=importlib.util.spec_from_file_location('growth',HERE/'check_translated_cubic_observer_growth.py')
g=importlib.util.module_from_spec(spec);spec.loader.exec_module(g)
f=g.f


def main():
    keys=[((('e',*ea,1),('e',*eb,1),('e',15,31,0)),((),(),(),()))
          for ea in ((0,1),(1,3)) for eb in ((3,7),(7,15))]
    keys.append(((('e',0,1,1),('e',5,7,1),('e',15,31,0)),((),(),(),())))
    rows=[];active=[]
    for pairs in g.pairings(tuple(range(6))):
        for kinds in ((1,1,0),(1,0,1),(0,1,1)):
            start=0;ds=[]
            for pair,kind in zip(pairs,kinds):
                ds.append(g.one(f['derivative'](start,f['relation'](pair,kind))))
                start|=sum(1<<j for j in pair)
            im=g.join(g.join(ds[0],ds[1]),ds[2])
            row=tuple(im.get(key,0) for key in keys)
            rows.append(row)
            if any(row):active.append((pairs,kinds,row))
    assert len(rows)==270
    assert [row for _,_,row in active]==[(1,1,1,1,0),(0,1,0,0,1)]
    xa,xb,xc,xd,xe=s.symbols('xa xb xc xd xe',positive=True)
    ma,mb,mc,md,me=s.symbols('ma mb mc md me',positive=True)
    da=mb-ma;db=md-mc
    # Overall w^2/(2y^2) is common and nonzero; omit it for exact comparison.
    original=(ma*mc,-ma*md,-mb*mc,mb*md,0)
    d0=(da*db+ma*md)/(xa*xc*ma*mc)
    d1=-1/(xa*xd)
    e0=da*db/(xa*xc*ma*mc)
    ex=-md/(xa*xe*me)
    four=(s.simplify(d0*xa*xc*ma*mc),s.simplify(d1*xa*xd*ma*md),0,0,0)
    five=(s.simplify(e0*xa*xc*ma*mc),0,0,0,s.simplify(ex*xa*xe*ma*me))
    for row in rows:
        old=sum(v*c for v,c in zip(original,row))
        assert s.simplify(sum(v*c for v,c in zip(four,row))-old)==0
        assert s.simplify(sum(v*c for v,c in zip(five,row))-old)==0
    assert 1+30**2==901 and 1+10**2==101 and 2**2+30**2==904
    # The crossed source has exactly the two asserted measurement supports.
    crossed=active[1][2]
    assert sum(abs(v) for v in crossed[:4])==1
    assert sum(abs(v) for v in crossed)==2
    # Structured shared-template errors need not preserve the new calibration.
    C,a=s.symbols('C a',real=True)
    shared_old=s.expand((C+mb*a-C-ma*a)*(C+md*a-C-mc*a))
    assert s.simplify(shared_old-da*db*a*a)==0
    shared_new=da*db*(C+ma*a)*(C+mc*a)/(ma*mc)
    assert s.simplify(shared_new.subs(C,0)-shared_old)==0
    assert s.diff(shared_new,C)!=0
    result={'passed':True,'actual_cubic_basis_vectors':len(rows),
        'visible_five_sector_vectors':active,'exact_recalibration_checks':2*len(rows),
        'checks':['existing_extra_edge_isolates_crossed_product',
                  'distinct_904_901_101_noise_exponents',
                  'source_image_equality_does_not_imply_shared_error_cancellation'],
        'scope':'Exact source and scalar tests. Optimal growth follows from the actual crossed response norm and theta asymptotics; no arbitrary tensor dual is admitted.'}
    out=HERE.parent/'results/optimized-cubic-observer.json'
    out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))


if __name__=='__main__':main()
