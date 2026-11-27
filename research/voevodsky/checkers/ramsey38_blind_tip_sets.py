"""Prospective exact tip sets, per fixed boundary, including empty predictions."""
from ramsey38_cached_holdout import F,H,freeze,prev,inputs,json,sys
from ramsey38_early_sign_trial import trial
from ramsey38_polygon_endpoint_rule import compatible
from collections import Counter
SAMPLE=prev.out/'ramsey38_tipset_sample.json';P=prev.out/'ramsey38_tipset_predictions.json';R=prev.out/'ramsey38_tipset_comparison.json'
protocol='First three novel marked transitions after record 331 excluding prior samples. All eligible sole-release shells, not restricted to early-sign positives. Three tip candidates. Baseline=early sign survivors; final=those also admitting compatible capped link rotations. Freeze both sets before querying seven-original-label shellable ball search.'
def setup(e):
    b,_,x,rs,v=inputs(e);S=rs[x];rs[x]|=v;labs=sorted(b[e['u']]);return labs,set(rs.values()),S,[w for i,w in enumerate(labs) if not rs[x]&(1<<i)]
def predict():
    freeze(331,(F,H),SAMPLE,protocol);es=[]
    for e in json.loads(SAMPLE.read_text())['cases']:
        labs,req,S,tips=setup(e);dec=lambda m:frozenset(w for i,w in enumerate(labs) if m>>i&1);shells=[]
        for d in trial(e):
            base=sorted(w for w,s in d['tips'].items() if s=='pass');bd=set(map(dec,d['bd']));pred=[w for w in base if compatible(bd,set(map(dec,req))|{dec(S)|{w}})];shells.append(dict(row=d['row'],bd=d['bd'],baseline=base,pred=pred))
        es.append(dict(record=e['record'],root=e['u'],shells=shells));print(e['record'],len(shells),flush=True)
    prev.save(P,dict(protocol=protocol,sample_sha=prev.sha(SAMPLE.read_bytes()),entries=es));print(prev.sha(P.read_bytes()))
def compare():
    from ramsey38_release_census import first_ball
    data=json.loads(P.read_text());assert data['sample_sha']==prev.sha(SAMPLE.read_bytes());out=[];cnt=Counter()
    for e,entry in zip(json.loads(SAMPLE.read_text())['cases'],data['entries'],strict=True):
        labs,req,S,tips=setup(e);assert len(tips)==3
        for d in entry['shells']:
            cert={};bd=frozenset(d['bd'])
            for w in tips:
                o=first_ball(bd,req|{S|1<<labs.index(w)})
                if o:cert[w]=[sorted(labs[i] for i in t) for t in o]
            truth=sorted(cert);cnt['shells']+=1;cnt['true_nonempty']+=bool(truth);cnt['actual_tips']+=len(truth)
            for k in ['baseline','pred']:
                p=d[k];cnt[k+'_exact']+=p==truth;cnt[k+'_exact_nonempty']+=bool(truth) and p==truth;cnt[k+'_extra']+=len(set(p)-set(truth));cnt[k+'_missed']+=len(set(truth)-set(p))
            out.append(dict(record=e['record'],root=e['u'],**d,actual=truth,certificates=cert))
    print(cnt);prev.save(R,dict(prediction_sha=prev.sha(P.read_bytes()),counts=dict(cnt),cases=out))
if __name__=='__main__':{'freeze':predict,'compare':compare}[sys.argv[1]]()
