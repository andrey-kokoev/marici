"""Three legal edits at one root, exactly one additional edge-row inside at each stage."""
from ramsey38_two_move_trial import add,setup,templates,legal,prev,json,sys,combinations
from ramsey38_disk_filter_trial import key,graph,gzip
from ramsey38_append_holdout import attaches,faces,face_assignments,boundary,shelling
from ramsey38_append_531_routes import extend
from itertools import permutations
from functools import lru_cache
from collections import defaultdict,Counter
P=prev.out/'ramsey38_three_release_predictions.json';R=prev.out/'ramsey38_three_release_comparison.json'
protocol='After catalogue 1652 through 5000, first three canonically distinct roots (one per record) with a legal triple promotion and a chain of eligible boundaries for three distinct original edge rows. Select by boundaries only, before filling. Every ordered triple of such target labels requested. At each stage bury all promoted triangles and hide exactly the accumulated targets. Constructor tries first face-count mesh per initial shell and <=2 attachments per step; no shelling test before freeze. Independent all-shell, all-mesh, unrestricted-length append-only census.'
def prepare(g,u):
    L,rs,moves=setup(g,u);rows=sorted(j for j,s in rs.items() if s.bit_count()==2);goals=set(rows);ts=tuple(sorted(map(frozenset,combinations(L,4)),key=sorted));dec=lambda m:frozenset(v for i,v in enumerate(L) if m>>i&1)
    @lru_cache(None)
    def stage(ms):
        rr=rs.copy();old=set()
        for x,v in ms:old.add(rs[x]);rr[x]|=1<<L.index(v)
        short=[(j,s) for j,s in rr.items() if s.bit_count()<4];out=defaultdict(list)
        for bd,cl in templates():
            if old&cl:continue
            h=frozenset(j for j,s in short if s not in cl)
            if len(h)==len(ms) and h<=goals:out[h].append(tuple(sorted(bd)))
        return frozenset(map(dec,rr.values())),out
    chains=[]
    for m in moves:
        h=add(g,m)
        for n in setup(h,u)[2]:
            h2=add(h,n)
            for o in setup(h2,u)[2]:
                A,B,C=[stage(tuple(sorted(s)))[1] for s in [(m,),(m,n),(m,n,o)]]
                for a in A:
                    for b in B:
                        if not a<b:continue
                        for c in C:
                            if b<c:chains.append(((next(iter(a)),next(iter(b-a)),next(iter(c-b))),(m,n,o),(A[a],B[b],C[c])))
    return L,rows,ts,dec,stage,chains

def solve(g,u,verify,require_burial=False,boundary_filter=None):
    L,rows,ts,dec,stage,chains=prepare(g,u);out={};counts=Counter();
    @lru_cache(None)
    def candidates(req,b):
        bd=set(map(dec,b));aa=sorted([frozenset(z) for z in face_assignments(L,req,bd)],key=faces);return [a for a in aa if shelling(a)] if verify else aa[:1]
    for goal,ms,shells in chains:
        req=[stage(tuple(sorted(ms[:i])))[0] for i in (1,2,3)];counts['chains']+=1
        if verify:
            h=g
            for m in ms:h=add(h,m);assert legal(h)
        if goal in out:continue
        def walk(i,old,plan):
            for b in sorted(shells[i]):
                if boundary_filter and not boundary_filter(tuple(z['bd'] for z in plan)+(b,)):continue
                bd=set(map(dec,b))
                if i==0 or verify:opts=candidates(req[i],b)
                else:
                    opts=(old|set(extra) for n in (1,2) for extra in combinations([t for t in ts if t not in old],n))
                for a in opts:
                    if i:
                        if not old<a or not all(any(s<=t for t in a) for s in req[i]):continue
                        if not verify and boundary(a)!=bd:continue
                        o=extend(old,a)
                        if o is None:continue
                    else:o=sorted(a,key=sorted)
                    step=dict(bd=b,cells=faces(a),append=[sorted(t) for t in o] if i else [])
                    if i==2:
                        route=plan+[step]
                        if require_burial:
                            rims=[set.union(set(),*(dec(f) for f in z['bd'])) for z in route]
                            if not any(a-b for a,b in zip(rims,rims[1:])):continue
                        return route
                    res=walk(i+1,a,plan+[step]);
                    if res:return res
        p=walk(0,frozenset(),[])
        if p:out[goal]=dict(goal=goal,moves=ms,stages=p)
    return list(out.values()),len(list(permutations(rows,3))),len(chains)

def freeze():
    es=[];seen=set();scanned=0
    with gzip.open(prev.catalogue,'rt') as fp:
        for i,line in enumerate(fp,1):
            if i<=1652:continue
            if i>5000:break
            w=line.strip();g=graph(w)
            for u in sorted(g):
                if len(g[u])!=7:continue
                L,rs,m=setup(g,u)
                if len(m)<3 or max(map(int.bit_count,rs.values()))>4 or sum(s.bit_count()==2 for s in rs.values())<3:continue
                k=key(L,rs,m)
                if k in seen:continue
                if not any(setup(add(add(g,a),b),u)[2] for a in m for b in setup(add(g,a),u)[2]):continue
                seen.add(k);scanned+=1
                if not prepare(g,u)[-1]:continue
                p,N,c=solve(g,u,False);es.append(dict(record=i,word=w,u=u,requests=N,chains=c,plans=p));print(i,u,N,c,len(p),flush=True);break
            if len(es)==3:break
    print('structurally screened',scanned);prev.save(P,dict(protocol=protocol,screened=scanned,cases=es))
def compare(predictions=P,destination=R,boundary_filter=None):
    data=json.loads(predictions.read_text());out=[];cnt=Counter()
    for e in data['cases']:
        g=graph(e['word']);u=e['u'];gold,N,c=solve(g,u,True,boundary_filter=boundary_filter);valid={tuple(z['goal']) for z in gold};cnt['requests']+=N;cnt['feasible']+=len(gold);hits=[]
        for p in e['plans']:
            assert not boundary_filter or boundary_filter(tuple(s['bd'] for s in p['stages']))
            h=g;old=None;ok=True;promoted=[]
            for i,(m,z) in enumerate(zip(p['moves'],p['stages'])):
                L,rs,moves=setup(h,u);assert tuple(m) in moves;promoted.append(rs[m[0]]);h=add(h,m);assert legal(h);L,rs,_=setup(h,u);dec=lambda m:frozenset(w for k,w in enumerate(L) if m>>k&1);a=set(map(frozenset,z['cells']));bd=boundary(a);assert bd==set(map(dec,z['bd'])) and all(any(dec(s)<=t for t in a) for s in rs.values());assert all(dec(s) not in bd for s in promoted) and sorted(j for j,s in rs.items() if s.bit_count()<4 and not any(dec(s)<=f for f in bd))==sorted(p['goal'][:i+1]);ok &= bool(shelling(a))
                if old is not None:
                    seq=list(map(frozenset,z['append']));assert old<a and set(seq)==a-old and all(attaches(old|set(seq[:k]),t) for k,t in enumerate(seq))
                old=a
            if ok:assert tuple(p['goal']) in valid;hits.append(p['goal'])
        cnt['proposed']+=len(e['plans']);cnt['verified']+=len(hits);out.append(dict(record=e['record'],feasible=gold,verified=hits));print(e['record'],len(gold),len(hits),flush=True)
    print(cnt);prev.save(destination,dict(prediction_sha=prev.sha(predictions.read_bytes()),counts=dict(cnt),cases=out))
if __name__=='__main__':{'freeze':freeze,'compare':compare}[sys.argv[1]]()
