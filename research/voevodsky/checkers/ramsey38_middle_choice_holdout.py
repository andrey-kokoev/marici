"""Blind middle-mesh choice conditional on two reachable sealed meshes, not on a final shell."""
from ramsey38_early_interior_holdout import prev,json,sys,graph,setup,add,key,gzip,prepare,faces
from ramsey38_three_releases import face_assignments,shelling,extend,boundary,legal
from ramsey38_append_holdout import attaches
from functools import lru_cache
from collections import Counter
P=prev.out/'ramsey38_middle_choice_predictions.json';R=prev.out/'ramsey38_middle_choice_comparison.json'
protocol='Records 60001..95000 inclusive, first five fresh marked arrays with a legal triple edit script and at least two distinct middle balls reachable by vertex-burying append-only extensions for same first two targets. First qualifying root per record; retain all qualifying scripts and ordered edge-row targets there. No final-shell feasibility filter. Shared input pool: all such middle balls on seven labels. Baseline first lex mesh meeting sealed requirements; lookahead first such mesh with a goal-reaching path of <=2 safe attachments, else abstain. Freeze choices; verify independently over all eligible final shells and any attachment count.'
def freeze(after=60000,limit=95000,exclude=(),selector=None,dest=P,description=protocol,done=lambda es:len(es)==5,require_burial=True):
    es=[];seen={key(*setup(graph(e['word']),e['u'])) for path in exclude for e in json.loads(path.read_text())['cases']};tested=0
    with gzip.open(prev.catalogue,'rt') as fp:
        for i,line in enumerate(fp,1):
            if i<=after:continue
            if i>limit:break
            g=graph(line.strip())
            for u in sorted(g):
                if len(g[u])!=7:continue
                L,rs,ms=setup(g,u)
                if len(ms)<3 or max(map(int.bit_count,rs.values()))>4 or sum(s.bit_count()==2 for s in rs.values())<3:continue
                scripts=[(a,b,c) for a in ms for b in setup(add(g,a),u)[2] for c in setup(add(add(g,a),b),u)[2]]
                if not scripts:continue
                k=key(L,rs,ms)
                if k in seen:continue
                seen.add(k);tested+=1
                # An interior middle label cannot occur on any exposed short row.
                # Only the two released size-two rows can contain it once promoted rows are removed.
                def maybe_buried(a,b):
                    for bit in range(7):
                        incident=[s for j,s in rs.items() if j not in (a[0],b[0]) and s.bit_count()<4 and s>>bit&1]
                        if len(incident)<=2 and all(s.bit_count()==2 for s in incident):return True
                    return False
                if require_burial:scripts=[(a,b,c) for a,b,c in scripts if maybe_buried(a,b)]
                if not scripts:continue
                L,rows,cells,dec,stage,_=prepare(g,u);out=[]
                @lru_cache(None)
                def balls(req,bd):return [frozenset(ts) for ts in face_assignments(L,req,set(map(dec,bd))) if shelling(ts)]
                for a,b,c in scripts:
                    r1,S=stage((a,));r2,T=stage(tuple(sorted((a,b))));rr=rs.copy();old=[]
                    for x,v in (a,b,c):old.append(dec(rs[x]));rr[x]|=1<<L.index(v)
                    req=set(map(dec,rr.values()));short={j:dec(s) for j,s in rr.items() if s.bit_count()<4}
                    for H,ends in T.items():
                        middles=[(B,set(L)-set.union(set(),*boundary(B))) for bd in ends if not require_burial or len(bd)<10 for B in balls(r2,bd)];
                        if len(middles)<2:continue
                        for j in sorted(H):
                            if frozenset([j]) not in S:continue
                            starts=[A for bd in S[frozenset([j])] for A in balls(r1,bd)];pool=[B for B,V in middles if any((not require_burial or any(v in f for f in boundary(A) for v in V)) and extend(A,B) is not None for A in starts)];pool=sorted(set(pool),key=faces)
                            if len(pool)<2:continue
                            survivors=[n for n,B in enumerate(pool) if all(any(s<=t for t in B) for s in req if s&(set(L)-set.union(set(),*boundary(B))))];second,=H-{j}
                            for l in sorted(set(rows)-H):
                                goal=H|{l};pick=None;path=None
                                if selector is not None:
                                    pred=selector(L,pool,survivors,req,short,goal,l,old);out.append(dict(goal=[j,second,l],moves=[a,b,c],pool=[faces(B) for B in pool],baseline=next(iter(survivors),None),**pred));continue
                                def walk(B,seq):
                                    bd=boundary(B);hidden={j for j,s in short.items() if not any(s<=f for f in bd)}
                                    if hidden-goal:return
                                    if seq and hidden==goal and not set(old)&bd and all(any(s<=t for t in B) for s in req):return seq
                                    if len(seq)<2:
                                        for t in cells:
                                            if t not in B and attaches(B,t):
                                                o=walk(B|{t},seq+[sorted(t)])
                                                if o:return o
                                for n in survivors:
                                    path=walk(pool[n],[])
                                    if path:pick=n;break
                                out.append(dict(goal=[j,second,l],moves=[a,b,c],pool=[faces(B) for B in pool],baseline=next(iter(survivors),None),look=pick,path=path))
                balls.cache_clear()
                if out:es.append(dict(record=i,u=u,word=line.strip(),requests=out));print(i,u,len(out),flush=True);break
            if done(es):break
    print('screened',tested,'retained',len(es));prev.save(dest,dict(protocol=description,screened=tested,cases=es))
def compare(predictions=P,dest=R):
    counts=Counter();out=[]
    for e in json.loads(predictions.read_text())['cases']:
        g=graph(e['word']);L,rows,cells,dec,stage,_=prepare(g,e['u']);
        @lru_cache(None)
        def finals(ms,goal):
            req,S=stage(ms);return [frozenset(ts) for bd in S.get(goal,[]) for ts in face_assignments(L,req,set(map(dec,bd))) if shelling(ts)]
        for d in e['requests']:
            ms=tuple(map(tuple,d['moves']));h=g
            for m in ms:h=add(h,m);assert legal(h)
            ends=finals(tuple(sorted(ms)),frozenset(d['goal']));pool=[frozenset(map(frozenset,ts)) for ts in d['pool']];ok=[i for i,B in enumerate(pool) if any(extend(B,F) is not None for F in ends)];counts['requests']+=1;counts['feasible']+=bool(ok)
            for k in ('baseline','look') if 'look' in d else ('baseline','edgeface','cone'):counts[k+'_choices']+=d[k] is not None;counts[k+'_hit']+=d[k] in ok
            if d.get('look') is not None:
                M=pool[d['look']];
                for t in map(frozenset,d['path']):assert t not in M and attaches(M,t);M=M|{t}
                assert M in ends
            out.append(dict(record=e['record'],goal=d['goal'],moves=ms,ok=ok))
    print(counts);prev.save(dest,dict(prediction_sha=prev.sha(predictions.read_bytes()),counts=dict(counts),results=out))
if __name__=='__main__':{'freeze':freeze,'compare':compare}[sys.argv[1]]()
