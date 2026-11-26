"""Prospective fixed-shell, specified-tip ablation. No ball solver in freeze."""
from ramsey38_named_gain_trial import inputs,key,templates,face,screen,find,prev,prior,P as last,graph,candidates,cycle
from itertools import combinations
from collections import Counter,deque
import gzip,json,sys
P=prev.out/'ramsey38_early_sign_frozen.json';R=prev.out/'ramsey38_early_sign_comparison.json'
protocol='First five new marked triangle-to-tet transitions from record 114 onward (exclude earlier cycle and named trials modulo column/row permutations). Every original-label boundary sphere with old triangle buried and exactly one other short row hidden, all three candidate tips. Compare ring plus crossing baseline to sign propagation on only required tetrahedra plus fixed boundary rim. Evaluate exact fixed-shell fixed-tip shellable fillings.'
def neg(fs):
    orient=lambda f:{(f[i-1],v) for i,v in enumerate(f)}
    ts=sorted(map(lambda t:tuple(sorted(t)),fs));adj={f:[] for f in ts};sg={}
    for a,b in combinations(ts,2):
        if len(set(a)&set(b))==2:
            w=-1 if orient(a)&orient(b) else 1;adj[a].append((b,w));adj[b].append((a,w))
    for t in ts:
        if t in sg:continue
        sg[t]=1;q=deque([t])
        while q:
            a=q.popleft()
            for b,w in adj[a]:
                value=sg[a]*w
                if b in sg:
                    if value!=sg[b]:return True
                else:sg[b]=value;q.append(b)
    return False

def trial(e):
    b,a,x,rs,vbit=inputs(e);labels=sorted(b[e['u']]);S=rs[x];rs[x]|=vbit;short={j:s for j,s in rs.items() if s.bit_count()<4};results=[];p=frozenset(range(7))
    for bd,cl in templates():
        if S in cl:continue
        hidden=[j for j,s in short.items() if s not in cl]
        if len(hidden)!=1:continue
        fs=frozenset(map(face,bd));caps={i:{(f-{i})|{7} for f in fs if i in f} for i in p};tips={}
        for i,w in enumerate(labels):
            if rs[x]>>i&1:continue
            req={face(s) for s in rs.values()}|{face(S|1<<i)}
            if screen(p,req,fs)!='pass' or find(req|fs,fs):tips[w]='baseline-reject';continue
            bad=[labels[k] for k in p if neg(caps[k]|{t-{k} for t in req if len(t)==4 and k in t})];tips[w]=bad or 'pass'
        results.append(dict(row=hidden[0],bd=sorted(bd),tips=tips))
    return sorted(results,key=lambda d:(d['row'],d['bd']))
if __name__=='__main__' and sys.argv[1]=='freeze':
    seen={key(e) for f in [prior,last] for e in json.loads(f.read_text())['cases'] if len(e['A'])==6};es=[]
    with gzip.open(prev.catalogue,'rt') as f:
        for i,line in enumerate(f,1):
            if i<114:continue
            w=line.strip();g=graph(w)
            for u,v in combinations(sorted(g),2):
                if v not in g[u]:continue
                abc=candidates(g,u,v)
                if not abc:continue
                a,b,c=abc;cy=cycle(g,a,c)
                if len(a)!=6 or cycle(g,a,b) or len(cy)!=6 or any(len(s)!=2 for s in cy.values()):continue
                e=dict(record=i,word=w,u=u,v=v,A=a,B=b,C=c);_,_,x,rs,_=inputs(e)
                if rs[x].bit_count()!=3 or max(map(int.bit_count,rs.values()))>4:continue
                k=key(e)
                if k in seen:continue
                seen.add(k);es.append(dict(e,predictions=trial(e),canonical=k.hex()));print(i,u,v,len(es[-1]['predictions']),flush=True)
                if len(es)==5:break
            if len(es)==5:break
    assert len(es)==5;prev.save(P,dict(protocol=protocol,cases=es));print(prev.sha(P.read_bytes()))
elif __name__=='__main__' and sys.argv[1]=='compare':
    from ramsey38_release_census import first_ball
    data=json.loads(P.read_text());assert data['protocol']==protocol;cnt=Counter();out=[]
    for e in data['cases']:
        b,_,x,rs,v=inputs(e);S=rs[x];rs[x]|=v;ls=sorted(b[e['u']]);cert=[]
        for d in e['predictions']:
            for ws,pred in d['tips'].items():
                w=int(ws);req=set(rs.values())|{S|1<<ls.index(w)};o=first_ball(frozenset(d['bd']),req);typ='sign-reject' if isinstance(pred,list) else pred;cnt[typ,bool(o)]+=1;assert not o or typ=='pass'
                if o:cert.append(dict(row=d['row'],tip=w,bd=d['bd'],order=[sorted(ls[i] for i in t) for t in o]))
        out.append(cert)
    prev.save(R,dict(prediction_sha=prev.sha(P.read_bytes()),counts={f'{k}/{v}':n for (k,v),n in sorted(cnt.items())},certificates=out));print(cnt)
