"""Two links read through one fixed sheet occurrence. Width 9 only."""
from collections import Counter,defaultdict
from itertools import product,permutations,combinations
import json,runpy
from ramsey_excel_corner_collisions import D,local,cube,analyze


def audit():
    C=[''.join(x) for x in product('01*',repeat=3) if x!=('*',)*3];by=defaultdict(list)
    for p in analyze(9)['pieces']:
        a=tuple(p['start'])
        for r in cube(a):
            b=local(a,r)
            for s in C:
                if all(x=='*' or int(x)==y for x,y in zip(s,b)):
                    for i in range(3):
                        if s[i]=='*':by[tuple(r),i].append((s,a,1-2*b[i]))
    marks=[]
    for (r,i),oc in by.items():
        for s,a,ds in oc:
            ends=[(t,h,d) for t,h,d in oc if any(x!='*' and y!='*' and x!=y for x,y in zip(s,t))]
            for (t,h,dt),(u,k,du) in combinations(ends,2):
                if t!=u:marks.append((s,t,u,dt==du,dict(row=r,axis=i+1,starts=[a,h,k],steps=[ds,dt,du])))
    g=runpy.run_path(str(D/'ramsey_cube_construct35.py'));assert C==g['cells'];E=[(s,t) for i,s in enumerate(C) for j,t in enumerate(C) if i<j and g['G'][i]>>j&1];maps=[];graphs={}
    for p in permutations(range(3)):
        for b in product(range(2),repeat=3):
            f={s:''.join('*' if s[i]=='*' else str(int(s[i])^v) for i,v in zip(p,b)) for s in C};maps.append(f);graphs.setdefault(frozenset(frozenset((f[s],f[t])) for s,t in E),(p,b))
    assert len(graphs)==8
    def colors(s,t,u):return [(frozenset((s,t)) in G,frozenset((s,u)) in G) for G in graphs]
    hist=Counter();wh=defaultdict(set);examples={};orbit_keys=set();relation={}
    for s,t,u,pred,obs in marks:
        cs=colors(s,t,u)
        if any(len(set(bits))<2 for bits in zip(*cs)):continue
        n=sum(a==b for a,b in cs);hits=n if pred else 8-n;hist[hits]+=1;wh[s,*sorted((t,u))].add(pred)
        geom={(f[s],*sorted((f[t],f[u]))) for f in maps};orbit_keys.add(min(geom));relation[s,*sorted((t,u))]=n;assert all(sum(a==b for a,b in colors(*q))==n for q in geom)
        examples.setdefault(str(hits),dict(cells=[s,t,u],**obs,predict_equal=pred,graph_colors=[dict(transform=tr,colors=co) for tr,co in zip(graphs.values(),cs)]))
    out=dict(all_marks=len(marks),eligible_marks=sum(hist.values()),distinct_wedges=len(wh),geometry_classes=len(orbit_keys),wedges_by_equal_color_frequency=Counter(relation.values()),conflicting_sheet_predictions=sum(len(p)>1 for p in wh.values()),by_predictions_correct_out_of_eight=hist,examples=examples);print({k:v for k,v in out.items() if k!='examples'});print([(k,v['cells'],v['row'],v['steps']) for k,v in examples.items()]);(D.parent/'results/ramsey_swap_wedge.json').write_text(json.dumps(out,indent=2)+'\n')
if __name__=='__main__':audit()
