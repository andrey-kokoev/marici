"""Predecessor constraints for centered forward additions: no degree-seven final vertex can lose a link. Use the degree-seven subgraph and its boundary counts, not a full target embedding."""
from ramsey_forward_link_filter import CAT,D,decode,G,induced,combinations,json,islice,gzip,Counter

from ramsey_retention_slice import check

def budgets(g,out,mask,banned=None):
    needs={i:g[i].bit_count()-(4 if (g[i]&mask).bit_count()==1 else 6) for i in out};res=[]
    def go(ds,chosen):
        if not ds:res.append(chosen);return
        options=[];already=frozenset(chosen)
        def allowed(i,j):
            if not banned:return True
            e=(min(i,j),max(i,j));return all(not ban<=(already|{e}) for ban in banned.get(e,()))
        for i,k in ds.items():
            nb=[j for j,v in ds.items() if v and g[i]>>j&1 and allowed(i,j)];
            if len(nb)<k:return
            options.append((len(list(combinations(nb,k))),i,nb))
        _,i,nb=min(options);k=ds[i];rest=ds.copy();del rest[i]
        for js in combinations(nb,k):
            if banned and k>1:
                new=[(min(i,j),max(i,j)) for j in js];installed=frozenset(chosen+new)
                if any(ban<=installed for e in new for ban in banned.get(e,())):continue
            nxt=rest.copy()
            for j in js:nxt[j]-=1
            go(nxt,chosen+[(i,j) for j in js])
    go(needs,[]);return res

def audit():
    record=262402
    with gzip.open(CAT/'r38_27.g6.gz','rt') as f:a=decode(next(islice(f,record,None)).strip())
    target=induced(G,json.loads((D.parent/'ramsey_cube_unlock_free_row.json').read_text())['core_labels']);seven=lambda g:[i for i,v in enumerate(g) if v.bit_count()==7];H=sum(1<<i for i in seven(target));inside=sorted((target[i]&H).bit_count() for i in seven(target));profile=sorted((v&H).bit_count() for i,v in enumerate(target) if not H>>i&1);role=sorted(((v&H).bit_count(),v.bit_count()) for i,v in enumerate(target) if not H>>i&1);results=[]
    for z,v in enumerate(a):
        if v.bit_count()!=7:continue
        vs=[j for j in range(27) if j!=z];marks=[(i,j) for i,j in combinations(vs,2) if a[i]&a[j]==1<<z and not a[i]>>j&1];st=Counter();wits=[]
        for e,f in combinations(marks,2):
            if set(e)&set(f):continue
            g=[v&~(1<<z) for v in a];g[z]=0
            for i,j in (e,f):g[i]|=1<<j;g[j]|=1<<i
            assert max(map(int.bit_count,g))==7;st['pairs']+=1;pc=Counter()
            for h in combinations(seven(g),8):
                mask=sum(1<<i for i in h);st['sets']+=1
                if sorted((g[i]&mask).bit_count() for i in h)!=inside:continue
                pc['inside']+=1;out=[j for j in vs if not mask>>j&1];degrees=[(g[j]&mask).bit_count() for j in out]
                if sorted(degrees)!=profile:continue
                pc['boundary']+=1
                # Within each fixed contact-count class, final total degrees can only decrease.
                avail=sorted(zip(degrees,[g[j].bit_count() for j in out]));assert [d for d,_ in avail]==[d for d,_ in role]
                if any(x<y for (_,x),(_,y) in zip(avail,role)):continue
                pc['degrees']+=1;edits=budgets(g,out,mask);pc['budget']+=bool(edits);legal=[]
                for rm in edits:
                    assert len(rm)==9;gg=g[:]
                    for i,j in rm:gg[i]^=1<<j;gg[j]^=1<<i
                    if check(gg,((1<<27)-1)^(1<<z),3,8):legal.append(rm)
                pc['legal']+=bool(legal);wits.append(dict(pair=(e,f),seven=h,removal_lists=len(edits),legal_removals=legal))
            for k,n in pc.items():st[k+'_sets']+=n;st[k+'_pairs']+=bool(n)
        results.append(dict(z=z,counts=st,survivors=wits));print(z,dict(st))
    res=dict(record=record,inside=inside,outside=role,results=results);(D.parent/'ramsey_forward_rigid_seven.json').write_text(json.dumps(res,indent=2)+'\n')
if __name__=='__main__':audit()
