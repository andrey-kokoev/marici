"""Broader competing-mesh trial: no requirement for a vertex to leave the rim."""
from ramsey38_cone_partial_veto_trial import A as suffix,prior,old,previous,prev,freeze,compare,sys,json,select,contrast
from collections import Counter
P=prev.out/'ramsey38_open_middle_cone_predictions.json';R=prev.out/'ramsey38_open_middle_cone_comparison.json';S=prev.out/'ramsey38_open_middle_cone_scores.json'
protocol='Same previously unfilled suffix 230001--477142; remove ONLY early-burial requirement on competing reachable middle balls. First eligible root per record. All ordered targets for every qualifying fixed edit script. Exclude earlier eligible samples canonically. Stop at two records with a partial veto or 12 eligible records. Freeze all predictions before checking final continuations, score all including abstentions. Not an early-burial trial.'
def done(es):return len(es)>=12 or sum(any(contrast(d) for d in e['requests']) for e in es)>=2
def check():
    compare(P,R);data=json.loads(P.read_text());ver=json.loads(R.read_text());it=iter(ver['results']);cnt=Counter();part=[]
    for e in data['cases']:
        for d in e['requests']:
            r=next(it);assert (e['record'],d['goal'],d['moves'])==(r['record'],r['goal'],r['moves']);ok=set(r['ok']);
            for k in ('joint','passes'):
                s=set(d[k]);cnt[k+'_extra']+=len(s-ok);cnt[k+'_miss']+=len(ok-s);cnt[k+'_exact']+=s==ok
            if contrast(d):part.append(dict(record=e['record'],goal=d['goal'],moves=d['moves'],joint=d['joint'],passes=d['passes'],ok=r['ok'],old_hit=d['edgeface'] in ok,new_hit=d['cone'] in ok))
    print(cnt,'partial',len(part));print(part[:4]);prev.save(S,dict(comparison_sha=prev.sha(R.read_bytes()),counts=dict(cnt),partial=part))
if __name__=='__main__':
    if sys.argv[1]=='freeze':freeze(230000,477142,(old,previous,prior,suffix),select,P,protocol,done,require_burial=False)
    elif sys.argv[1]=='compare':check()
