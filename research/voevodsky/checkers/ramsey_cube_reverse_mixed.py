"""Exact four-recolor test in reverse: remove one cube red link, add three, and restore the degree-seven vertex. Generate additions by hitting surviving blue-clique demands, not by fitting a target graph."""
from ramsey_cube_retention_floor import G,induced,iso,D,combinations,Counter,json
from ramsey_retention_slice import check

def audit():
    root=34;V=[i for i in range(35) if i!=root and not G[root]>>i&1];a=induced(G,V);F=(1<<26)-1
    maps=[]
    for r in range(35):
        W=[i for i in range(35) if i!=r and not G[r]>>i&1];b=induced(G,W);f=iso(a,b);assert f is not None and all((a[i]>>j&1)==(b[f[i]]>>f[j]&1) for i,j in combinations(range(26),2));maps.append([W[j] for j in f])
    counts=Counter();examples=[];per=[]
    for u,v in combinations(range(26),2):
        if not a[u]>>v&1:continue
        b=a[:];b[u]^=1<<v;b[v]^=1<<u;I=[0]
        for i,n in enumerate(b):I.extend([s|1<<i for s in I if not n&s])
        Q=[s for s in I if s.bit_count()==7];octs=[s for s in I if s.bit_count()==8];E=[(j,k) for j,k in combinations(range(26),2) if not b[j]&(b[k]|1<<k) and (j,k)!=(u,v)];ends=[(1<<j)|(1<<k) for j,k in E];dem={q:sum(1<<j for j,e in enumerate(ends) if q&e==e) for q in Q+octs};perm=[q for q in Q if not dem[q]];st=Counter();win=None
        for s in Q:
            if any(not s&q for q in perm):continue
            st['pass_permanent']+=1;allowed=sum(1<<j for j,e in enumerate(ends) if s&e!=e);ds={dem[q]&allowed for q in octs+[q for q in Q if not q&s]};
            if 0 in ds:continue
            st['each_breakable']+=1
            used=0;pcs=[]
            for d in sorted(ds,key=lambda m:(m.bit_count(),m)):
                if not d&used:used|=d;pcs.append(d)
            if len(pcs)>=4:st['four_disjoint_demands']+=1
            def finish(chosen,rem):
                if not rem:
                    pads=[j for j in range(len(E)) if allowed>>j&1 and j not in chosen]
                    for pad in combinations(pads,3-len(chosen)):
                        edits=chosen+list(pad);g=b[:]+[s]
                        for j in range(26):g[j]|=((s>>j)&1)<<26
                        for h in edits:
                            i,j=E[h];g[i]|=1<<j;g[j]|=1<<i
                        if check(g,(1<<27)-1,3,8):return edits
                    return None
                if len(chosen)==3:return None
                m=min(rem,key=int.bit_count)
                while m:
                    bit=m&-m;m-=bit;res=finish(chosen+[bit.bit_length()-1],[d for d in rem if not d&bit]);
                    if res is not None:return res
            edits=finish([],sorted(ds))
            if edits is not None:
                win=dict(remove=[u,v],add=[E[j] for j in edits],restored_row=[j for j in range(26) if s>>j&1]);examples.append(win);break
        counts['cuts']+=1;counts['cuts_passing_permanent']+=bool(st['pass_permanent']);counts['cuts_each_breakable']+=bool(st['each_breakable']);counts.update(st);per.append(dict(removed=[u,v],counts=st,example=win))
    assert len(per)==76
    out=dict(core_labels=V,root_maps=maps,counts=counts,examples=examples,per_cut=per);print(counts,'successes',len(examples),examples[:1]);(D.parent/'ramsey_cube_reverse_mixed.json').write_text(json.dumps(out,indent=2)+'\n')
if __name__=='__main__':audit()
