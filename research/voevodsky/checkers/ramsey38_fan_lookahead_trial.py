"""Freeze new marked transitions before comparing online veto vs branch lookahead."""
from ramsey38_early_sign_trial import P,prev,prior,last,inputs,key,trial,graph,candidates,cycle,combinations,json,gzip,sys
from ramsey38_partial_fan_prune import search
from collections import Counter
F=prev.out/'ramsey38_fan_lookahead_sample.json';R=prev.out/'ramsey38_fan_lookahead_replay.json'
protocol='First three new canonical marked triangle promotions after record 163; every fixed shell/tip passing the previous early-sign screen. Identical cell order and face/support propagation. Online cycle veto alone versus also testing every unset cell at propagation fixpoint. Compare exact surviving face assignments and visited recursive nodes, not wall time or balls.'
def freeze(after=163,excluded=(),dest=F,description=protocol,metadata=None):
    seen={key(e) for f in [P,last,prior,*excluded] for e in json.loads(f.read_text())['cases'] if len(e['A'])==6};cases=[]
    with gzip.open(prev.catalogue,'rt') as fp:
        for i,line in enumerate(fp,1):
            if i<=after:continue
            w=line.strip();g=graph(w)
            for u,v in combinations(sorted(g),2):
                if v not in g[u]:continue
                abc=candidates(g,u,v)
                if not abc:continue
                a,b,c=abc;cy=cycle(g,a,c)
                if len(a)!=6 or cycle(g,a,b) or len(cy)!=6 or any(len(s)!=2 for s in cy.values()):continue
                e=dict(record=i,word=w,u=u,v=v,A=a,B=b,C=c);_,_,x,rs,_=inputs(e)
                if rs[x].bit_count()!=3 or max(map(int.bit_count,rs.values()))>4 or key(e) in seen:continue
                seen.add(key(e));e['sample']=[dict(row=d['row'],bd=d['bd'],tip=int(w)) for d in trial(e) for w,s in d['tips'].items() if s=='pass'];cases.append(e)
                if len(cases)==3:break
            if len(cases)==3:break
    assert len(cases)==3;prev.save(dest,dict(protocol=description,cases=cases,**(metadata or {})));print([(e['record'],len(e['sample'])) for e in cases])
def replay():
    out=[];c=Counter();data=json.loads(F.read_text());assert data['protocol']==protocol
    for e in data['cases']:
        b,_,x,rs,v=inputs(e);S=rs[x];rs[x]|=v;labs=sorted(b[e['u']]);dec=lambda m:frozenset(w for i,w in enumerate(labs) if m>>i&1)
        for d in e['sample']:
            bd=set(map(dec,d['bd']));req=set(map(dec,rs.values()))|{dec(S)|{d['tip']}};a,b=[search(labs,bd,req,None,True,k) for k in [False,True]];assert sorted(a['leaves'])==sorted(b['leaves']);m,n=a['nodes'],b['nodes'];c['online']+=m;c['forward']+=n;c['less' if n<m else 'more' if n>m else 'equal']+=1;c['leaves']+=len(b['leaves']);out.append(dict(record=e['record'],root=e['u'],**d,online=m,forward=n,preblocked=b['preblocked'],leaves=len(b['leaves'])))
    print(c);prev.save(R,dict(sample_sha=prev.sha(F.read_bytes()),counts=dict(c),results=out))
if __name__=='__main__':{'freeze':freeze,'replay':replay}[sys.argv[1]]()
