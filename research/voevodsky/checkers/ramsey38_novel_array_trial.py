"""First 20 new support multisets after catalogue records 1--4. No fill-informed selection."""
import gzip,json,sys
from collections import Counter
from functools import lru_cache
from itertools import permutations
from unittest.mock import patch
import ramsey38_record4_combined_trial as t
prev=t.prev;pf=prev.out/'ramsey38_novel20_predictions.json';cf=prev.out/'ramsey38_novel20_comparison.json'
@lru_cache(None)
def perm_table():
    tables=[]
    for p in permutations(range(7)):
        a=[0]*256
        for i in range(1,128):b=i&-i;a[i]=a[i-b]|1<<p[b.bit_length()-1]
        tables.append(bytes(a))
    return tables
@lru_cache(None)
def canon(ms):return min(bytes(sorted(ms.translate(tab))) for tab in perm_table())
def selection():
    seen=set();picks=[];old_count=0
    with gzip.open(prev.catalogue,'rt') as f:
        for i,line in enumerate(f,1):
            word=line.strip();g=t.graph(word)
            for r,n in sorted(g.items()):
                if len(n)!=7:continue
                labs=sorted(n);rr={v:frozenset(s&n) for v,s in g.items() if v not in n|{r}};ms=bytes(sorted(sum(1<<labs.index(w) for w in s) for s in rr.values()));assert len(ms)==19
                if any(x.bit_count()>4 for x in ms):continue
                key=canon(ms)
                if key in seen:continue
                seen.add(key)
                if i<=4:old_count+=1;continue
                picks.append((i,r,word,key,rr))
                if len(picks)==20:return old_count,picks
    raise ValueError('not enough new arrays')
meta=dict(rule=t.meta,selection='Seed seen set with all eligible arrays in records 1..4. Scan by ascending record then root. Select first 20 new canonical multisets. Key = minimum sorted list of 19 masks over all 5040 permutations. Keep repeats and empty masks. Test control and every single permission on original labels.',selector_pin=prev.sha(__import__('pathlib').Path(__file__).read_bytes()))
if __name__=='__main__' and sys.argv[1]=='freeze':
    old,picks=selection();entries=[]
    for i,r,w,key,rr in picks:
        g=t.graph(w)
        with patch.object(t,'g',g),patch.object(prev.rule,'N',g):ds={v:t.choose(r,v,rr) for v in [0]+[v for v,s in rr.items() if len(s)<4]}
        entries.append(dict(record=i,root=r,word=w,key=key.hex(),cases=ds));print(i,r,Counter(a['class'] for a in ds.values()),flush=True)
    prev.save(pf,dict(meta=meta,old_keys=old,entries=entries));print('frozen',prev.sha(pf.read_bytes()),old)
elif __name__=='__main__' and sys.argv[1]=='compare':
    import ramsey38_release_census as c
    saved=json.loads(pf.read_text());assert saved['meta']==meta;counts=Counter();examples=[];mismatches=[]
    for entry in saved['entries']:
        g=t.graph(entry['word']);i,r=entry['record'],entry['root']
        with patch.object(c,'N',g):labels,rr,buckets=c.predict(r)
        known={};cache={};ss=set(rr.values());selected={}
        def fill(bd):
            if bd not in cache:
                o=c.first_ball(bd,ss);cache[bd]=[sorted(labels[j] for j in cell) for cell in o] if o else None
            return cache[bd]
        for v,bs in buckets.items():
            for bd in sorted(bs,key=sorted):
                o=fill(bd)
                if o:known[v]=o;break
        for vv,a in entry['cases'].items():
            v=int(vv);kind='control' if not v else 'release';ok=v in known or 0 in known;counts[kind,a['class'],str(ok)]+=1
            if a['class']!='abstain' and (a['class']=='original')!=ok:mismatches.append((i,r,v,'existence',a['class'],ok))
            for k in ('baseline','shell'):
                if k not in a:continue
                bd=frozenset(sum(1<<labels.index(j) for j in cell) for cell in a[k]);o=fill(bd);counts[kind,k,str(bool(o))]+=1
                if not o:mismatches.append((i,r,v,k,False))
                elif k=='shell':selected[v]=o
        examples.append(dict(record=i,root=r,actual_hidden=known,selected=selected))
    data=dict(prediction_sha=prev.sha(pf.read_bytes()),counts={'/'.join(k):v for k,v in sorted(counts.items())},mismatches=mismatches,certificates=examples);prev.save(cf,data);print(data['counts'],mismatches)
