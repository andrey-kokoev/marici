"""Frozen second-goal lookahead vs committing to the first predicted one-step move."""
from ramsey38_two_move_trial import finals,add,source,options,triples,disks,propagate,setup,graph,prev,json,Counter,sys
from ramsey38_disk_filter_trial import key,old,gzip
P=prev.out/'ramsey38_two_goal_holdout_predictions.json';R=prev.out/'ramsey38_two_goal_holdout_comparison.json'
protocol='First five new canonical multi-promotion arrays after record 451, first eligible root/record with at least two distinct edge targets and a legal two-edit sequence. Exclude previous promotion/disk trials. Every ordered target pair. Rank first triples by previous disk-filter rule. Greedy fixes top first triple; lookahead takes first ranked triple with a predicted second edit and shell satisfying both goals. Both use same second-stage order. Freeze exact proposals (including first tip) before verifying. Remeshing allowed, both triangles buried and exactly both rows released at end.'
def ranked(L,rs,moves,j):
    dec=lambda m:frozenset(w for i,w in enumerate(L) if m>>i&1);out=[]
    for z in options(L,rs,moves,j):
        bd=set(map(dec,z['bd']));x,v=z['edge'];s=dec(rs[x]);fixed={dec(r) for y,r in rs.items() if y!=x}|{s|{v}};ps=[]
        for w in z['tips']:
            if set.union(set(),*bd)!=set(L) or all(propagate({a:disks(L,a,bd,fixed|{s|{w}}) for a in L})[0][-1].values()):ps.append(w)
        if ps:out.append(dict(z,tips=ps))
    return triples(sorted(out,key=lambda d:(-len(d['tips']),d['edge'],d['bd'])))
def choices(f,j,l):
    out={}
    for (a,b),zs in f.items():
        for z in zs:
            if z['hidden']==sorted((j,l)):out.setdefault(a,[]).append((b,z['bd']))
    return out
def freeze():
    seen={key(*setup(graph(e['word']),e['u'])) for p in [source,old] for e in json.loads(p.read_text())['cases']};es=[]
    with gzip.open(prev.catalogue,'rt') as fp:
        for i,line in enumerate(fp,1):
            if i<=451:continue
            word=line.strip();g=graph(word)
            for u in sorted(g):
                if len(g[u])!=7:continue
                L,rs,moves=setup(g,u);rows=sorted(j for j,s in rs.items() if s.bit_count()==2)
                if len(moves)<2 or len(rows)<2 or max(map(int.bit_count,rs.values()))>4 or not any(setup(add(g,m),u)[2] for m in moves):continue
                k=key(L,rs,moves)
                if k in seen:continue
                seen.add(k);e=dict(record=i,u=u,word=word);f=finals(e,False);pred=[]
                for j in rows:
                    first=ranked(L,rs,moves,j)
                    for l in rows:
                        if l==j:continue
                        c=choices(f,j,l);routes=[(t,min(c[t[0]])) for t in first if t[0] in c];best=next(iter(routes),None);pred.append(dict(j=j,l=l,first=first[:1],greedy=best if best and best[0]==first[0] else None,look=best))
                es.append(dict(e,requests=pred));print(i,u,len(pred),flush=True);break
            if len(es)==5:break
    assert len(es)==5;prev.save(P,dict(protocol=protocol,cases=es))
def compare():
    cnt=Counter();out=[]
    for e in json.loads(P.read_text())['cases']:
        L,rs,moves=setup(graph(e['word']),e['u']);f=finals(e,True);ok={j:options(L,rs,moves,j,True) for j in {r['j'] for r in e['requests']}};local=Counter()
        for r in e['requests']:
            j,l=r['j'],r['l'];valid=set(triples(ok[j]));cs=choices(f,j,l);feasible=any(t[0] in cs for t in valid);local['requests']+=1;local['feasible']+=feasible
            for k in ['greedy','look']:
                p=r[k];hit=False
                if p:
                    (a,bd,w),(b,end)=p;a=tuple(a);hit=(a,tuple(bd),w) in valid and (tuple(b),end) in cs.get(a,[])
                local[k+'_proposed']+=bool(p);local[k+'_hit']+=hit
        cnt.update(local);out.append(dict(record=e['record'],counts=dict(local),first_certs=ok,final_certs=[dict(a=a,b=b,shells=zs) for (a,b),zs in f.items()]));print(e['record'],local)
    prev.save(R,dict(prediction_sha=prev.sha(P.read_bytes()),counts=dict(cnt),cases=out));print(cnt)
if __name__=='__main__':{'freeze':freeze,'compare':compare}[sys.argv[1]]()
