"""Compose frozen first choices. Final certificate is ONE ball hiding exactly both targets."""
from ramsey38_disk_filter_trial import P as source,prev,json,setup,graph,legal,disks,propagate,options,triples,Counter,sys
from ramsey38_choose_promotion_trial import templates,face,screen,find,combinations,compatible
P=prev.out/'ramsey38_two_move_predictions.json';R=prev.out/'ramsey38_two_move_comparison.json'
protocol='Reuse five prior graphs and their immutable one-step choices (not new first-step data). All ordered pairs of distinct original size-two targets. First promotion must realize first sole release; second must promote a different triangle legally at same root. One final seven-label shellable ball must hide exactly both short rows and bury BOTH promoted triangles. May remesh. Score greedy first choice and deterministic first predicted final shell on its branch against all legal sequences. No need to preserve old tip or particular cells.'
def add(g,m):
    x,v=m;h={w:set(s) for w,s in g.items()};h[x].add(v);h[v].add(x);return h

def finals(e,verify):
    g=graph(e['word']);u=e['u'];L,rs,moves=setup(g,u);dec=lambda m:frozenset(w for i,w in enumerate(L) if m>>i&1);targets={j for j,s in rs.items() if s.bit_count()==2};out={};cache={}
    for m in moves:
        h=add(g,m);_,r1,seconds=setup(h,u)
        if verify:assert legal(h)
        for n in seconds:
            if verify:assert legal(add(h,n))
            k=tuple(sorted((m,n)))
            if k not in cache:
                x,v=m;y,w=n;r={**r1,y:r1[y]|1<<L.index(w)};req=set(r.values());short=[(j,s) for j,s in r.items() if s.bit_count()<4];ls=[]
                for bd,cl in templates():
                    if rs[x] in cl or rs[y] in cl:continue
                    hidden=sorted(j for j,s in short if s not in cl)
                    if len(hidden)!=2 or not set(hidden)<=targets:continue
                    if verify:
                        from ramsey38_release_census import first_ball
                        o=first_ball(bd,req)
                        if not o:continue
                        order=[sorted(L[i] for i in t) for t in o]
                    else:
                        rf=set(map(face,req));fs=set(map(face,bd));ff=set(map(dec,bd));rr=set(map(dec,req))
                        if screen(frozenset(range(7)),rf,fs)!='pass' or find(rf|fs,fs) or not compatible(ff,rr):continue
                        if set.union(set(),*ff)==set(L) and not all(propagate({a:disks(L,a,ff,rr) for a in L})[0][-1].values()):continue
                        order=[]
                    ls.append(dict(hidden=hidden,bd=sorted(bd),order=order))
                cache[k]=sorted(ls,key=lambda z:z['bd'])
            out[m,n]=cache[k]
    return out

def run(verify):
    data=json.loads(source.read_text());pred=json.loads(P.read_text()) if verify else None;cnt=Counter();out=[]
    for e in data['cases']:
        L,rs,moves=setup(graph(e['word']),e['u']);f=finals(e,verify);rows=[d['row'] for d in e['requests']];cnt['legal_sequences']+=len(f);res=[]
        for d in e['requests']:
            j=d['row'];first=triples(d['new']);ok=triples(options(L,rs,moves,j,True)) if verify else first
            for l in rows:
                if l==j:continue
                choices=[(a,b,z) for (a,b),zs in f.items() if any(t[0]==a for t in ok) for z in zs if z['hidden']==sorted([j,l])];greedy=[(b,z['bd']) for a,b,z in choices if first and first[0] in ok and a==first[0][0]];p=min(greedy,default=None);rec=dict(row=j,second=l,choice=p,any_route=bool(choices));cnt['requests']+=1;cnt['first_available']+=bool(ok);cnt['any_route']+=bool(choices);cnt['greedy_route']+=bool(p)
                if verify:
                    frozen=next(r for c in pred['cases'] if c['record']==e['record'] for r in c['requests'] if r['row']==j and r['second']==l)['choice'];hit=bool(frozen and (tuple(frozen[0]),frozen[1]) in greedy);cnt['proposed']+=bool(frozen);cnt['hit']+=hit;rec.update(hit=hit,certificates=[dict(first=a,second=b,**z) for a,b,z in choices]);
                res.append(rec)
        out.append(dict(record=e['record'],root=e['u'],requests=res));print(e['record'],len(f),sum(r['any_route'] for r in res),flush=True)
    dest=R if verify else P;prev.save(dest,dict(protocol=protocol,input_sha=prev.sha((P if verify else source).read_bytes()),counts=dict(cnt),cases=out));print(cnt)
if __name__=='__main__':run(sys.argv[1]=='compare')
