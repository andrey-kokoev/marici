"""Record 4: precommit the original-label selector and baseline choice; compare separately."""
import gzip,json,sys
from collections import Counter
from unittest.mock import patch
import ramsey38_record3_polygon_trial as prev
from ramsey38_ring_budget_screen import screen
from ramsey38_alternating_boundary_paths import find

with gzip.open(prev.catalogue,'rt') as f:words=[next(f).strip() for _ in range(4)]
def graph(word):
    n=ord(word[0])-63;assert n==27
    g={v:set() for v in range(1,n+1)};bits=''.join(f'{ord(c)-63:06b}' for c in word[1:]);
    for bit,(i,j) in zip(bits,((i,j) for j in g for i in range(1,j))):
        if bit=='1':g[i].add(j);g[j].add(i)
    return g
g=graph(words[-1]);roots=[r for r,P in g.items() if len(P)==7 and max(len(n&P) for v,n in g.items() if v not in P|{r})<=4];pf=prev.out/'ramsey38_record4_combined_predictions.json';cf=prev.out/'ramsey38_record4_combined_comparison.json'
def rows(r):return {v:frozenset(g[r]&n) for v,n in g.items() if v not in g[r]|{r}}
files=list(prev.meta['rule_pins'])+['ramsey38_record3_polygon_trial.py','ramsey38_ring_budget_screen.py','ramsey38_alternating_boundary_paths.py','ramsey38_record4_combined_trial.py']
meta=dict(record=4,word_sha=prev.sha(words[-1].encode()),pins={n:prev.sha((prev.here/n).read_bytes()) for n in files},scope='Seven original labels only. All eligible roots, no release plus permission to release any single short row. Lexicographically first compatible polygon shell (baseline), then first also passing ring and alternating-path screens. Unsupported polygon input is an abstention. No filling search during freeze.')
def choose(r,d,rr):
    req={s for v,s in rr.items() if v!=d and len(s)<4};ss=set(rr.values());P=frozenset(g[r]);p=prev.poly
    if prev.rule.classify(r,d)!='pass':return {'class':'order-reject'}
    if not prev.supported(P,req):return {'class':'abstain'}
    c,opts=p.predict(g,r,d);ans={'class':'no-original-proposal'}
    for bd in sorted(opts[None],key=prev.fmt):
        if not p.compatible(bd,ss):continue
        ans.setdefault('baseline',prev.fmt(bd))
        if screen(P,ss,bd)=='pass' and not find(ss|bd,bd):return dict(ans,**{'class':'original','shell':prev.fmt(bd)})
    return ans
if __name__=='__main__' and sys.argv[1]=='freeze':
    data={}
    with patch.object(prev.rule,'N',g):
        for r in roots:
            rr=rows(r);data[r]={d:choose(r,d,rr) for d in [0]+[v for v,s in rr.items() if len(s)<4]};print(r,Counter(a['class'] for a in data[r].values()),flush=True)
    prev.save(pf,dict(meta=meta,predictions=data));print('frozen:',prev.sha(pf.read_bytes()))
elif __name__=='__main__' and sys.argv[1]=='compare':
    import ramsey38_release_census as census
    saved=json.loads(pf.read_text());assert saved['meta']==meta;stats=Counter();results={};miss=[]
    with patch.object(census,'N',g):
        for r in roots:
            labels,rr,buckets=census.predict(r);ss=set(rr.values());known={};cache={}
            def fill(bd):
                if bd not in cache:
                    order=census.first_ball(bd,ss);cache[bd]=[sorted(labels[i] for i in t) for t in order] if order else None
                return cache[bd]
            for hidden,bs in buckets.items():
                for bd in sorted(bs,key=sorted):
                    o=fill(bd)
                    if o:known[hidden]=o;break
            cert={}
            for dd,a in saved['predictions'][str(r)].items():
                d=int(dd);kind='release' if d else 'control';ok=d in known or 0 in known;stats[kind,a['class'],str(ok)]+=1
                for key in ('baseline','shell'):
                    if key in a:
                        order=fill(frozenset(sum(1<<labels.index(v) for v in t) for t in a[key]));stats[kind,key,str(bool(order))]+=1
                        if key=='shell' and order:cert[d]=order
                        if not order:miss.append((r,d,key))
            results[r]={'actual_hidden':known,'exact_selected':cert}
    counts={'/'.join(k):v for k,v in sorted(stats.items())};prev.save(cf,dict(prediction_sha=prev.sha(pf.read_bytes()),counts=counts,failed_specific_shells=miss,roots=results));print(counts,miss)
