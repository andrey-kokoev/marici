"""Remove all mark filters, retain the pole pair and disjoint simple half-routes. Inspect component shapes and leaf collisions of the residual; separate equal-profile-count control from unrestricted data."""
from ramsey_strip_unmirrored_holdout import groups,N,s,t,full,fill,Counter,combinations
for L in (9,11):
    paths=[(frozenset(p),c) for (l,c),ps in groups.items() if l==L for p in ps];h=Counter();hidden=Counter();good=Counter();example=None;peeling=Counter();arms=Counter()
    for (p,c),(q,d) in combinations(paths,2):
        if not p.isdisjoint(q):continue
        rem=frozenset(full-{s,t}-p-q);ok=fill(rem);isol=any(not N[v]&rem for v in rem);h[ok,isol]+=1
        if isol:continue
        todo=set(rem);parts=[]
        while todo:
            x=todo.pop();part={x};st=[x]
            while st:
                n=todo&N[st.pop()];part.update(n);st.extend(n);todo-=n
            parts.append((sum(v<15 for v in part),sum(v>=15 for v in part),tuple(sorted(len(N[v]&part) for v in part))))
        shape=tuple(sorted(parts)); rest=set(rem);stages=[]
        while rest:
            leaves={v for v in rest if len(N[v]&rest)==1};pairs={tuple(sorted((v,next(iter(N[v]&rest))))) for v in leaves};active={v for pair in pairs for v in pair};stages.append(len(pairs))
            if len(active)!=2*len(pairs) or not active:break
            rest-=active
        peeling[ok,tuple(stages),len(rest)]+=1
        branches=[v for v in rem if len(N[v]&rem)==3]
        if L==11 and len(branches)==1:
            root,=branches;lens=[]
            for v in N[root]&rem:
                prev=root;k=1
                while (options:=(N[v]&rem)-{prev}):prev,v=v,next(iter(options));k+=1
                lens.append(k)
            arms[tuple(sorted(lens))]+=1
        if ok:good[shape]+=1
        else:
            hidden[c==d,shape]+=1
            if example is None:example=(sorted(rem),shape)
    print('peeling',L,peeling,'arms',arms);print(L,h,'hidden',hidden,'good shapes',good,'example',example)
