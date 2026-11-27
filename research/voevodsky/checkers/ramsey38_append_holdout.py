"""Prospective mesh proposals: infer a collar from the symmetric difference of two boundaries."""
from ramsey38_two_goal_holdout import P as prior,source,old,key,gzip,ranked,finals,add,graph,setup,prev,json,sys
from ramsey38_shared_twist10 import face_assignments,faces,combinations
from ramsey38_support_ball_completion import shelling
from ramsey38_compare_support_fillings import boundary
from collections import defaultdict,Counter
P=prev.out/'ramsey38_append_holdout_predictions.json';R=prev.out/'ramsey38_append_holdout_comparison.json'
protocol='First five novel arrays after 492 under prior two-goal eligibility. Every ordered distinct size-two row pair. Before shelling: try predicted shell pairs with boundary XOR equal to boundary of one or two added tetrahedra, shortest collar first then lexical order. Select lexical first face-count-compatible old mesh disjoint from collar, meeting final supports after adding it and permitting disk attachments. No shelling test on initial mesh before freeze. Verify shelling, retained cells, both boundaries, supports, releases and graph legality independently. A no-proposal is not an impossibility claim.'
def attaches(acc,t):
    hs=[s&t for s in acc];fs=[h for h in hs if len(h)==3];return 1<=len(fs)<=3 and len(set(fs))==len(fs) and all(any(h<=f for f in fs) for h in hs)
def proposals(e,selector=None):
    L,rs,moves=setup(graph(e['word']),e['u']);dec=lambda m:frozenset(w for i,w in enumerate(L) if m>>i&1);bits=lambda s:sum(1<<L.index(v) for v in s);cells=sorted(map(frozenset,combinations(L,4)),key=sorted);collars=defaultdict(list);f=finals(e,False);cache={};out=[]
    for k in (1,2):
        for seq in combinations(cells,k):collars[frozenset(map(bits,boundary(seq)))].append(seq)
    rows=sorted(j for j,s in rs.items() if s.bit_count()==2)
    for j in rows:
        first=ranked(L,rs,moves,j)
        for l in rows:
            if l==j:continue
            cands=[]
            for a,bd,w in first:
                for (m,n),zs in f.items():
                    if m!=a:continue
                    for z in zs:
                        if z['hidden']!=sorted((j,l)):continue
                        for seq in collars[frozenset(bd)^frozenset(z['bd'])]:cands.append((len(seq),a,bd,w,n,z['bd'],faces(seq)))
            if selector is not None:
                out.append(dict(j=j,l=l,**selector(e,L,rs,sorted(cands))));continue
            pick=None
            for _,a,bd,w,n,end,collar in sorted(cands):
                x,v=a;y,t=n;r1={**rs,x:rs[x]|1<<L.index(v)};req=set(map(dec,r1.values()))|{dec(rs[x])|{w}};r2={**r1,y:rs[y]|1<<L.index(t)};needs=set(map(dec,r2.values()));k=(a,bd,w)
                if k not in cache:cache[k]=sorted((faces(ts) for ts in face_assignments(L,req,set(map(dec,bd)))),key=lambda z:z)
                for mesh in cache[k]:
                    acc=set(map(frozenset,mesh));extra=list(map(frozenset,collar));final=acc|set(extra)
                    if acc&set(extra) or not all(any(s<=c for c in final) for s in needs):continue
                    for order in (extra,extra[::-1]):
                        if all(attaches(acc|set(order[:i]),c) for i,c in enumerate(order)):
                            pick=dict(first=a,second=n,tip=w,bd=bd,end=end,mesh=mesh,append=[sorted(c) for c in order]);break
                    if pick:break
                if pick:break
            out.append(dict(j=j,l=l,pick=pick,collar_candidates=len(cands)))
    return out

def freeze(after=492,extras=(),selector=None,dest=P,description=protocol,done=lambda es:len(es)==5):
    seen={key(*setup(graph(e['word']),e['u'])) for p in [source,old,prior,*extras] for e in json.loads(p.read_text())['cases']};es=[]
    with gzip.open(prev.catalogue,'rt') as fp:
        for i,line in enumerate(fp,1):
            if i<=after:continue
            word=line.strip();g=graph(word)
            for u in sorted(g):
                if len(g[u])!=7:continue
                L,rs,moves=setup(g,u)
                if len(moves)<2 or sum(s.bit_count()==2 for s in rs.values())<2 or max(map(int.bit_count,rs.values()))>4 or not any(setup(add(g,m),u)[2] for m in moves):continue
                k=key(L,rs,moves)
                if k in seen:continue
                seen.add(k);e=dict(record=i,u=u,word=word);e['requests']=proposals(e,selector);es.append(e);print(i,u,sum(bool(d['pick']) for d in e['requests']),flush=True);break
            if done(es):break
    assert done(es);prev.save(dest,dict(protocol=description,cases=es))
def compare():
    from ramsey38_choose_promotion_trial import legal
    data=json.loads(P.read_text());cnt=Counter();out=[]
    for e in data['cases']:
        g=graph(e['word']);u=e['u'];L,rs,_=setup(g,u);dec=lambda m:frozenset(w for i,w in enumerate(L) if m>>i&1)
        for d in e['requests']:
            cnt['requests']+=1;p=d['pick'];
            if not p:continue
            cnt['proposed']+=1;a=p['first'];n=p['second'];h=add(g,a);hh=add(h,n);assert legal(h) and legal(hh);mesh=set(map(frozenset,p['mesh']));o=shelling(mesh);extras=list(map(frozenset,p['append']));end=mesh|set(extras)
            for gg,cells,bd,hidden,buried in [(h,mesh,p['bd'],[d['j']],[a]),(hh,end,p['end'],[d['j'],d['l']],[a,n])]:
                _,rr,_=setup(gg,u);fs=boundary(cells);assert fs==set(map(dec,bd)) and all(any(dec(s)<=t for t in cells) for s in rr.values());assert sorted(j for j,s in rr.items() if s.bit_count()<4 and not any(dec(s)<=f for f in fs))==sorted(hidden);assert all(dec(rs[x]) not in fs for x,v in buried)
            assert dec(rs[a[0]])|{p['tip']} in mesh;fin=shelling(end);retained=mesh<=end and all(attaches(mesh|set(extras[:i]),t) for i,t in enumerate(extras));cnt['initial_fills']+=bool(o);cnt['final_fills']+=bool(fin);cnt['append_verified']+=bool(o and fin and retained);out.append(dict(record=e['record'],j=d['j'],l=d['l'],initial_order=[sorted(t) for t in o],final_order=[sorted(t) for t in fin],retained=retained))
    print(cnt);prev.save(R,dict(prediction_sha=prev.sha(P.read_bytes()),counts=dict(cnt),results=out))
if __name__=='__main__':{'freeze':freeze,'compare':compare}[sys.argv[1]]()
