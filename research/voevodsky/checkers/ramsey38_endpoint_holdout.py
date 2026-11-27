"""Paired prospective test of independent endpoint domains after exposure-cone filtering."""
from ramsey38_open_middle_cone_trial import P as past,old,previous,prior,suffix,freeze,compare,prev,json,sys,select,Counter
from ramsey38_endpoint_conjectures import domain,combinations
from functools import lru_cache
P=prev.out/'ramsey38_endpoint_holdout_predictions.json';R=prev.out/'ramsey38_endpoint_holdout_comparison.json';S=prev.out/'ramsey38_endpoint_holdout_scores.json'
protocol='After 241737, previously unseen canonical competing reachable middle pools (no burial required). All scripts/goals of first eligible root per record. Stop after two records with a cone survivor rejected by a disjoint nonempty edge projection or 16 records or catalogue end. Keep separate singleton-domain and edge-pair failures. Freeze sets and first choices before unrestricted final search; no global star solve or shell supplied.'
@lru_cache(maxsize=20000)
def opts(L,v,M,req,prot,hidden):return domain(L,v,M,req,prot,hidden)
def predict(L,pool,survivors,req,short,goal,l,old):
    z=select(L,pool,survivors,req,short,goal,l,old);prot=frozenset(s for j,s in short.items() if j not in goal);hidden=frozenset(old)|{short[j] for j in goal};passed=[];reject=[]
    for i in z['passes']:
        D={v:opts(tuple(L),v,pool[i],frozenset(req),prot,hidden) for v in L};empty=[v for v,s in D.items() if not s];pair=None
        if not empty:
            for a,b in combinations(L,2):
                A={frozenset(t for t in s if b in t) for s in D[a]};B={frozenset(t for t in s if a in t) for s in D[b]}
                if not A&B:pair=[a,b];break
        if empty or pair:reject.append(dict(mesh=i,empty=empty,pair=pair))
        else:passed.append(i)
    return dict(**z,endpoint=next(iter(passed),None),endpoint_set=passed,rejections=reject)
def done(es):return len(es)>=16 or sum(any(r['pair'] for d in e['requests'] for r in d['rejections']) for e in es)>=2
def check():
    compare(P,R);data=json.loads(P.read_text());ver=json.loads(R.read_text());it=iter(ver['results']);cnt=Counter();diff=[]
    for e in data['cases']:
        for d in e['requests']:
            r=next(it);assert (r['record'],r['goal'],r['moves'])==(e['record'],d['goal'],d['moves']);ok=set(r['ok']);cnt['actual_meshes']+=len(ok)
            for name in ['passes','endpoint_set']:
                ps=set(d[name]);cnt[name+'_extra']+=len(ps-ok);cnt[name+'_miss']+=len(ok-ps);cnt[name+'_exact']+=ps==ok;cnt[name+'_choice']+=bool(ps);cnt[name+'_hit']+=bool(ps and min(ps) in ok)
            for z in d['rejections']:cnt['empty' if z['empty'] else 'pair']+=1
            if d['rejections'] or set(d['endpoint_set'])!=ok:diff.append(dict(record=e['record'],goal=d['goal'],moves=d['moves'],cone=d['passes'],endpoint=d['endpoint_set'],rejections=d['rejections'],actual=r['ok']))
    print(cnt,'differing requests',len(diff));prev.save(S,dict(comparison_sha=prev.sha(R.read_bytes()),counts=dict(cnt),differences=diff))
if __name__=='__main__':
    if sys.argv[1]=='freeze':freeze(241737,477142,(old,previous,prior,suffix,past),predict,P,protocol,done,require_burial=False)
    elif sys.argv[1]=='compare':check()
