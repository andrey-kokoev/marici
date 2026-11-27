"""Compose two boundary differences and match the same initial star through all three stages."""
from ramsey38_three_releases import P,R,prev,json,prepare,graph,boundary,attaches,shelling,faces,combinations,permutations,lru_cache,defaultdict,Counter
from ramsey38_mesh_single_pin import reduce_domains,disks

def predict(g,u,allow_interior=False,boundary_filter=None):
    L,rows,ts,dec,stage,chains=prepare(g,u);delta=defaultdict(list);cnt=Counter();plans={};bits=lambda f:sum(1<<L.index(v) for v in f)
    for k in (1,2):
        for seq in combinations(ts,k):delta[frozenset(map(bits,boundary(seq)))].append(frozenset(seq))
    @lru_cache(None)
    def dom(a,b,r):return set(disks(L,a,set(map(dec,b)),r,allow_interior=allow_interior))
    for goal,ms,ss in sorted(chains,key=lambda z:(z[0],z[1])):
        if goal in plans:continue
        req=[stage(tuple(sorted(ms[:i])))[0] for i in (1,2,3)]
        for b in sorted(ss[1]):
            left=[(a,E) for a in sorted(ss[0]) for E in delta.get(frozenset(a)^frozenset(b),())];right=[(c,H) for c in sorted(ss[2]) for H in delta.get(frozenset(b)^frozenset(c),())]
            for a,E in left:
                for c,H in right:
                    if goal in plans or E&H:continue
                    if boundary_filter and not boundary_filter((a,b,c)):continue
                    if not allow_interior and any(set.union(set(),*map(dec,h))!=set(L) for h in (a,b,c)):continue
                    cnt['collar_chains']+=1;Q={};mid={}
                    for v in L:
                        e=frozenset(t for t in E if v in t);h=frozenset(t for t in H if v in t);J=dom(v,b,req[1]|E);K=dom(v,c,req[2]|E|H);mid[v]=[s for s in dom(v,a,req[0]) if not s&E and s|e in J];Q[v]=[s for s in mid[v] if not s&H and s|e|h in K]
                    if not all(Q.values()):continue
                    Q,_=reduce_domains(Q)
                    if not all(Q.values()):continue
                    sizes={v:len(q) for v,q in Q.items()};pin=None
                    if max(sizes.values())>1:
                        pin=min(L,key=lambda v:(-sizes[v],v));Q,_=reduce_domains({**Q,pin:[min(Q[pin],key=faces)]})
                    if not all(len(q)==1 for q in Q.values()):continue
                    A=frozenset.union(*(q[0] for q in Q.values()));order=lambda old,extra:next((s for s in permutations(sorted(extra,key=sorted)) if all(attaches(old|set(s[:i]),t) for i,t in enumerate(s))),None);o=order(A,E);p=order(A|E,H)
                    if not o or not p:continue
                    assert not A&(E|H);first_only,_=reduce_domains(mid);plans[goal]=dict(goal=goal,moves=ms,shells=[a,b,c],mesh=faces(A),additions=[[sorted(t) for t in s] for s in (o,p)],first_only_sizes={v:len(s) for v,s in first_only.items()},sizes=sizes,pin=pin)
    return list(plans.values()),dict(cnt)

def run():
    out=[];gold=json.loads(R.read_text());assert gold['prediction_sha']==prev.sha(P.read_bytes());
    for e,z in zip(json.loads(P.read_text())['cases'],gold['cases'],strict=True):
        g=graph(e['word']);ps,counts=predict(g,e['u']);L=sorted(g[e['u']]);dec=lambda m:frozenset(v for i,v in enumerate(L) if m>>i&1);goals={tuple(q['goal']) for q in z['feasible']};print(e['record'],counts,len(ps),flush=True)
        for q in ps:
            from ramsey38_three_releases import legal,setup,add
            a=set(map(frozenset,q['mesh']));h=g;buried=[];orders=[]
            for i,(m,b) in enumerate(zip(q['moves'],q['shells'])):
                _,rs,moves=setup(h,e['u']);assert m in moves;buried.append(dec(rs[m[0]]));h=add(h,m);assert legal(h);_,rs,_=setup(h,e['u']);
                if i:
                    for t in map(frozenset,q['additions'][i-1]):assert t not in a and attaches(a,t);a.add(t)
                f=boundary(a);assert f==set(map(dec,b)) and not set(buried)&f and all(any(dec(s)<=t for t in a) for s in rs.values());assert {j for j,s in rs.items() if s.bit_count()<4 and not any(dec(s)<=t for t in f)}==set(q['goal'][:i+1]);orders.append([sorted(t) for t in shelling(a)])
            q['orders']=orders;q['verified']=all(orders);assert not q['verified'] or tuple(q['goal']) in goals;print(q['goal'],q['first_only_sizes'],q['sizes'],q['pin'],q['verified'])
        out.append(dict(record=e['record'],counts=counts,plans=ps))
    prev.save(prev.out/'ramsey38_three_matched_stars.json',dict(scope='Retrospective replay using original graph inputs only for proposal generation',cases=out))
if __name__=='__main__':run()
