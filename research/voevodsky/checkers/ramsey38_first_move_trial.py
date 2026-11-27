"""Select one complete first move from the promoted array, without a row request."""
from ramsey38_choose_shell_trial import F,H,earlier,SAMPLE as previous,freeze,prev,json,sys,setup,trial,compatible
S=prev.out/'ramsey38_first_move_sample.json';P=prev.out/'ramsey38_first_move_predictions.json';R=prev.out/'ramsey38_first_move_comparison.json'
protocol='First three new canonical promotions after record 373. No requested row, shell or tip. Maximize predicted tip count on one shell across all sole releases. Break ties by smallest row then boundary masks, take smallest passing tip. Baseline first eligible row/boundary and smallest of three tips. Freeze before any filling; enumerate all eligible triples for misses, optimality and no-move checks.'
def predict():
    freeze(373,(F,H,earlier,previous),S,protocol);out=[]
    for e in json.loads(S.read_text())['cases']:
        labs,req,s,tips=setup(e);dec=lambda m:frozenset(w for i,w in enumerate(labs) if m>>i&1);opts=[]
        for d in trial(e):
            bd=set(map(dec,d['bd']));ps=sorted(w for w,k in d['tips'].items() if k=='pass' and compatible(bd,set(map(dec,req))|{dec(s)|{w}}));opts.append(dict(row=d['row'],bd=d['bd'],tips=ps))
        opts.sort(key=lambda d:(d['row'],d['bd']));best=min(opts,key=lambda d:-len(d['tips']),default=None);pick=lambda d,w:dict(row=d['row'],bd=d['bd'],tip=w);ch=pick(best,best['tips'][0]) if best and best['tips'] else None;baseline=pick(opts[0],min(tips)) if opts else None;out.append(dict(record=e['record'],root=e['u'],options=opts,choice=ch,baseline=baseline));print(e['record'],e['u'],ch,flush=True)
    prev.save(P,dict(protocol=protocol,sample_sha=prev.sha(S.read_bytes()),cases=out))
def compare():
    from ramsey38_release_census import first_ball
    p=json.loads(P.read_text());assert p['sample_sha']==prev.sha(S.read_bytes());out=[]
    for e,z in zip(json.loads(S.read_text())['cases'],p['cases'],strict=True):
        labs,req,s,tips=setup(e);valid=[];width={};predrows=set();actualrows=set()
        for d in z['options']:
            if d['tips']:predrows.add(d['row'])
            key=(d['row'],tuple(d['bd']));width[key]=0
            for w in tips:
                o=first_ball(frozenset(d['bd']),req|{s|1<<labs.index(w)})
                if o:width[key]+=1;valid.append(dict(row=d['row'],bd=d['bd'],tip=w,order=[sorted(labs[i] for i in t) for t in o]));actualrows.add(d['row'])
        def hit(q):return bool(q) and any(all(c[k]==v for k,v in q.items()) for c in valid)
        q=z['choice'];res=dict(record=e['record'],selected_fills=hit(q),baseline_fills=hit(z['baseline']),selected_width=width[q['row'],tuple(q['bd'])] if q else 0,max_width=max(width.values(),default=0),eligible_shells=len(width),valid_triples=len(valid),predicted_rows=sorted(predrows),feasible_rows=sorted(actualrows));print(res);out.append(dict(**res,certificates=valid))
    prev.save(R,dict(prediction_sha=prev.sha(P.read_bytes()),cases=out))
if __name__=='__main__':{'freeze':predict,'compare':compare}[sys.argv[1]]()
