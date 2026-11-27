"""From promoted rows plus requested sole release: select a boundary and its exact tips."""
from ramsey38_blind_tip_sets import F,H,SAMPLE as earlier,freeze,prev,json,inputs,sys,setup,trial,compatible,Counter
SAMPLE=prev.out/'ramsey38_choose_shell_sample.json';P=prev.out/'ramsey38_choose_shell_predictions.json';R=prev.out/'ramsey38_choose_shell_comparison.json'
protocol='First three novel transitions after 351. Every short row requested, no boundary supplied. Enumerate eligible seven-label spheres; choose shell with most compatible tips, break ties by sorted boundary mask list. Abstain with no-shell prediction only if no candidate passes. Compare naive first eligible shell, selected shell and exact tips, existence, and best available tip count by exhaustive search.'
def predict():
    freeze(351,(F,H,earlier),SAMPLE,protocol);out=[]
    for e in json.loads(SAMPLE.read_text())['cases']:
        labs,req,S,tips=setup(e);_,_,x,rs,v=inputs(e);rs[x]|=v;dec=lambda m:frozenset(w for i,w in enumerate(labs) if m>>i&1);rows={j:[] for j,s in rs.items() if s.bit_count()<4};bounds=trial(e)
        for d in bounds:
            bd=set(map(dec,d['bd']));ps=sorted(w for w,p in d['tips'].items() if p=='pass' and compatible(bd,set(map(dec,req))|{dec(S)|{w}}));rows[d['row']].append(dict(bd=d['bd'],tips=ps))
        for j,ss in sorted(rows.items()):
            best=min(ss,key=lambda s:(-len(s['tips']),s['bd'])) if ss else None;out.append(dict(record=e['record'],root=e['u'],row=j,eligible=sorted([s['bd'] for s in ss]),choice=best if best and best['tips'] else None))
    prev.save(P,dict(protocol=protocol,sample_sha=prev.sha(SAMPLE.read_bytes()),requests=out));print('requests',len(out),'chosen',sum(bool(d['choice']) for d in out))
def compare():
    from ramsey38_release_census import first_ball
    data=json.loads(P.read_text());assert data['sample_sha']==prev.sha(SAMPLE.read_bytes());cnt=Counter();out=[]
    for e in json.loads(SAMPLE.read_text())['cases']:
        labs,req,S,tips=setup(e)
        for d in data['requests']:
            if (e['record'],e['u'])!=(d['record'],d['root']):continue
            results=[];ch=d['choice'];selected=None
            for bd in d['eligible']:
                cert={}
                for w in tips:
                    o=first_ball(frozenset(bd),req|{S|1<<labs.index(w)})
                    if o:cert[w]=[sorted(labs[i] for i in t) for t in o]
                results.append(dict(bd=bd,tips=sorted(cert),certificates=cert));
                if ch and bd==ch['bd']:selected=sorted(cert)
            k=max([len(r['tips']) for r in results] or [0]);cnt['requests']+=1;cnt['eligible']+=bool(results);cnt['shells']+=len(results);cnt['feasible']+=bool(k);cnt['first_works']+=bool(results and results[0]['tips']);cnt['selected']+=bool(ch);cnt['selected_works']+=bool(selected);cnt['selected_exact']+=bool(ch and selected==ch['tips']);cnt['selected_best']+=bool(ch and len(selected)==k);cnt['correct_none']+=not ch and not k;out.append(dict(record=e['record'],root=e['u'],row=d['row'],max_tips=k,shells=results))
    print(cnt);prev.save(R,dict(prediction_sha=prev.sha(P.read_bytes()),counts=dict(cnt),requests=out))
if __name__=='__main__':{'freeze':predict,'compare':compare}[sys.argv[1]]()
