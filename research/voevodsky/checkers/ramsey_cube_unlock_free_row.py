"""Keep the path-predicted two reverse cuts. Choose the restored row from scratch and add any number of other core links. All tests are necessary or exhaustive."""
from ramsey_cube_retention_floor import G,induced,D,combinations,Counter,json
from ramsey_retention_slice import check

def search(a,cuts,on_residual=None):
    b=a[:]
    for i,j in cuts:b[i]^=1<<j;b[j]^=1<<i
    I=[0]
    for i,v in enumerate(b):I.extend([s|1<<i for s in I if not s&v])
    Q=[s for s in I if s.bit_count()==7];O=[s for s in I if s.bit_count()==8];es=[(i,j) for i,j in combinations(range(26),2) if not b[i]&(1<<j|b[j]) and (i,j) not in cuts and max(b[i].bit_count(),b[j].bit_count())<7];masks=[1<<i|1<<j for i,j in es];d={q:sum(1<<k for k,e in enumerate(masks) if q&e==e) for q in Q+O};perm=[q for q in Q if not d[q]];st=Counter();w=None
    for s in sorted(I,key=int.bit_count,reverse=True):
        if not 4<=s.bit_count()<=7 or any(b[i].bit_count()==7 and s>>i&1 for i in range(26)):continue
        st['degree_allowed_rows']+=1
        if any(not q&s for q in perm):continue
        st['hit_permanent']+=1;g=b[:]+[s]
        for i in range(26):g[i]|=(s>>i&1)<<26
        allow=sum(1<<k for k,(i,j) in enumerate(es) if max(g[i].bit_count(),g[j].bit_count())<7 and not g[i]&g[j]);ds={allow&d[q] for q in O};ds.update(allow&d[q] for q in Q if not q&s)
        if 0 in ds:continue
        st['each_breakable']+=1;small=[]
        for m in sorted(ds,key=int.bit_count):
            if not any(x&m==x for x in small):small.append(m)
        forced=[es[m.bit_length()-1] for m in small if m.bit_count()==1];fc=g[:]
        for i,j in forced:fc[i]|=1<<j;fc[j]|=1<<i
        over=any(v.bit_count()>7 for v in fc);tri=any(fc[i]&fc[j] for i,j in forced)
        if over or tri:
            st['forced_degree_and_triangle' if over and tri else 'forced_degree' if over else 'forced_triangle']+=1;continue
        st['pass_forced']+=1
        if on_residual is not None:on_residual(cuts,s,g,es,small)
        def rec(g,ds,added):
            if not ds:
                assert check(g,(1<<27)-1,3,8);return added
            m=min(ds,key=int.bit_count)
            while m:
                h=m&-m;m-=h;k=h.bit_length()-1;i,j=es[k];v=g[:];v[i]|=1<<j;v[j]|=1<<i;ok=sum(1<<n for n,(u,t) in enumerate(es) if max(v[u].bit_count(),v[t].bit_count())<7 and not v[u]&(v[t]|1<<t));left={x&ok for x in ds if not x&h}
                if 0 in left:continue
                found=rec(v,left,added+[es[k]])
                if found is not None:return found
        added=rec(g,small,[])
        if added is not None:
            w=dict(removed=cuts,row=[i for i in range(26) if s>>i&1],added=added);break
    return st,w

def audit():
    prior=json.loads((D.parent/'ramsey_cube_path_unlock.json').read_text());V=prior['core_labels'];a=induced(G,V);keys={tuple(sorted([tuple(r['first']),tuple(z)])) for r in prior['runs'] for z in r['necessary']};stats=Counter();out=[];wins=[]
    for k in sorted(keys):
        c,w=search(a,k);stats.update(c);out.append(dict(cuts=k,counts=c,witness=w))
        if w:wins.append(w)
    print(len(keys),stats,len(wins),wins[:1]);(D.parent/'ramsey_cube_unlock_free_row.json').write_text(json.dumps(dict(core_labels=V,counts=stats,runs=out,winners=wins),indent=2)+'\n')
if __name__=='__main__':audit()
