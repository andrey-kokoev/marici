"""Read barriers on an off-exit live-success witness. Do not materialize a lap for the live reader. Trace demanded incidences, actual issuance, and access failures separately."""
from ramsey_three_selector_interventions import rho,X,P,D,json,registry,execute,validate,apex

def trial(p,col,M,N,reader,deny):
    forward=dict(M);back={j:d for d,j in N.items()};inc={j:d for d,j in M.items()};reads=[];events=[];tail=p[col-1];head,={'C','D'}-{tail}
    def get(table,key):
        v=table[key];flag=tuple(sorted((key,v)));reads.append(flag)
        if deny in flag:raise PermissionError
        return v
    def supports(d):return {e for e in registry if any(set(e)=={p[i-1] for i in X[h]} for h in P[d])}
    def candidate(E):
        w,=[(a,b) for a in E for b in E if a[0]==tail and a[1]==b[0] and b[1]==head];return w
    try:
        if reader=='apex':w=candidate(registry)
        elif reader=='exit':
            E=supports(get(inc,29))|supports(get(back,29));w=candidate(E);events.extend(validate(execute(w)))
        else:
            x=0;v=None
            for i in range(100):
                y=get(forward if i%2==0 else back,x);d=min(x,y)
                if x<15 and v is None and apex(x)==col:v=tail
                opts=[e for e in supports(d) if e[0]==v];assert len(opts)<=1
                if opts:
                    e,=opts;events.extend(execute((e,)));v=e[1]
                x=y
                if v==head:break
            assert v==head;w=tuple(e[3] for e in validate(tuple(events)));assert w==candidate(registry)
        status='ok'
    except PermissionError:status='blocked';w=None
    return dict(status=status,word=w,reads=reads,ids=[e[2] for e in events])

def run():
    out=[]
    for bind in json.loads((D/'ramsey_selector_reachability_census.json').read_text()):
        c,=[c for c in bind['classes'] if not c['exit_reached'] and c['live']==['hit','hit']];m=dict(enumerate(c['example']));n={rho[d]:rho[j] for d,j in m.items()}
        for col,M,N in [(2,m,n),(3,n,m)]:
            for reader in ['apex','exit','live']:
                cases=[trial(bind['binding'],col,M,N,reader,k) for k in [None,29,0]];assert [q['status']=='ok' for q in cases]==[True,reader!='exit',reader!='live'];assert len(cases[0]['ids'])==(0 if reader=='apex' else 2);out.append(dict(binding=bind['binding'],col=col,reader=reader,cases=cases))
    return out
if __name__=='__main__':
    out=run();print([(q['reader'],[z['status'] for z in q['cases']]) for q in out[:3]]);(D/'ramsey_selector_read_barrier.json').write_text(json.dumps(out)+'\n')
