"""Freeze graph-3 boundary predictions on disk before running the separate ball search."""
import gzip,json,sys,hashlib
from collections import Counter
from pathlib import Path
from unittest.mock import patch
import ramsey38_polygon_endpoint_rule as poly
import ramsey38_rotation_transfer as rule
from ramsey38_rotation_holdout import catalogue
here=Path(__file__).resolve().parent;out=here.parent/'results';pf=out/'ramsey38_record3_polygon_predictions.json';cf=out/'ramsey38_record3_polygon_comparison.json'
def sha(b):return hashlib.sha256(b).hexdigest()
with gzip.open(catalogue,'rt') as f:words=[next(f).strip() for _ in range(3)]
g={i:set() for i in range(1,28)};word=words[-1];assert ord(word[0])-63==27
for b,(u,v) in zip(''.join(f'{ord(c)-63:06b}' for c in word[1:]),((u,v) for v in g for u in range(1,v))):
    if b=='1':g[u].add(v);g[v].add(u)
roots=[r for r,p in g.items() if len(p)==7 and max(len(p&n) for v,n in g.items() if v not in p|{r})<=4]
def rows(r):return {v:frozenset(g[r]&n) for v,n in g.items() if v not in g[r]|{r}}
def supported(P,req):
    E=set.union(set(),*(poly.ob.sub(s,2) for s in req));
    for v in P:
        seen={min(P-{v})}
        for _ in P:
            for e in E:
                if v not in e and seen&e:seen.update(e)
        if seen!=P-{v}:return False
    return True
def fmt(fs):return sorted(sorted(f) for f in fs)
def save(p,data):
    text=json.dumps(data,indent=2)+'\n'
    if p.exists():assert p.read_text()==text
    else:p.write_text(text)
meta=dict(record=3,word_sha=sha(word.encode()),rule_pins={n:sha((here/n).read_bytes()) for n in ['ramsey38_polygon_endpoint_rule.py','ramsey38_root15_pair_obstructions.py','ramsey38_rotation_transfer.py','ramsey38_root15_link_rotation.py']},scope='all eligible degree-seven roots, no-release and permission to release one short row; classify original first, then one auxiliary boundary point; abstain on unsupported polygon input')
def predict(r,d,rr):
    req={s for v,s in rr.items() if v!=d and len(s)<4};fs=set(rr.values())
    if rule.classify(r,d)!='pass':return {'class':'order-reject'}
    if not supported(g[r],req):return {'class':'abstain'}
    c,opts=poly.predict(g,r,d)
    if not c['orders_pass']:return {'class':'crossing-reject'}
    for x,typ in [(None,'original'),(28,'aux')]:
        for bd in sorted(opts[x],key=fmt):
            if poly.compatible(bd,fs):return {'class':typ,'shell':fmt(bd)}
    return {'class':'no-proposal'}
if __name__=='__main__' and sys.argv[1]=='freeze':
    data={}
    with patch.object(rule,'N',g):
        for r in roots:
            rr=rows(r);data[r]={d:predict(r,d,rr) for d in [0]+[v for v,s in rr.items() if len(s)<4]};print(r,Counter(a['class'] for a in data[r].values()),flush=True)
    save(pf,dict(meta=meta,predictions=data));print('frozen',sha(pf.read_bytes()))
elif __name__=='__main__' and sys.argv[1]=='compare':
    import ramsey38_release_census as census
    saved=json.loads(pf.read_text());assert saved['meta']==meta;results={};counts=Counter();mismatch=[]
    with patch.object(census,'N',g):
        for r in roots:
            labels,rr,buckets=census.predict(r);cert={}
            for hidden,shells in buckets.items():
                for bd in sorted(shells,key=sorted):
                    order=census.first_ball(bd,set(rr.values()))
                    if order:cert[hidden]=[sorted(labels[i] for i in t) for t in order];break
            results[r]=cert
            for dd,p in saved['predictions'][str(r)].items():
                d=int(dd);ok=d in cert or 0 in cert;typ=p['class'];counts['/'.join(('single' if d else 'control',typ,str(ok)))]+=1
                if typ!='abstain' and (typ=='original')!=ok:mismatch.append((r,d,typ,ok))
    save(cf,dict(prediction_sha=sha(pf.read_bytes()),counts=dict(sorted(counts.items())),original_label_mismatches=mismatch,certificates=results));print(counts,'mismatch:',mismatch)
