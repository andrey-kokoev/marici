"""Evaluate the particular proposed shells, separate from existence on any shell."""
from ramsey38_record3_polygon_trial import pf,cf,g,rows,sha,json,Counter
from ramsey38_release_census import first_ball
from ramsey38_compare_support_fillings import boundary

if __name__=='__main__':
    preds=json.loads(pf.read_text())['predictions'];report=json.loads(cf.read_text());assert report['prediction_sha']==sha(pf.read_bytes());counts=Counter();miss=[]
    for k,ds in preds.items():
        r=int(k);labels=sorted(g[r]);mask=lambda s:sum(1<<labels.index(v) for v in s);supports=rows(r)
        for dd,a in ds.items():
            if a['class']!='original':continue
            bd=frozenset(mask(t) for t in a['shell']);order=first_ball(bd,{mask(s) for s in supports.values()});counts[('control' if dd=='0' else 'release',bool(order))]+=1
            if not order:miss.append((r,int(dd)));continue
            ts=[frozenset(labels[i] for i in t) for t in order];assert boundary(ts)==frozenset(map(frozenset,a['shell'])) and all(any(s<=t for t in ts) for s in supports.values())
    print(counts,miss)
