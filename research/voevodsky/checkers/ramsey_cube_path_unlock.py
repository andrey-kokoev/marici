"""Predict second reverse cuts from a failed one-cut cover; never supply a predecessor. Use the cheapest relaxed-cover cases. Include triangles among the eventual repairs in the verdict."""
from ramsey_cube_retention_floor import G,induced,D,combinations,json,Counter
from ramsey_retention_slice import check

def instance(a,removed,S):
    b=a[:];
    for u,v in removed:b[u]^=1<<v;b[v]^=1<<u
    I=[0]
    for j,v in enumerate(b):I.extend([s|1<<j for s in I if not v&s])
    qs=[s for s in I if s.bit_count()==8 or s.bit_count()==7 and not s&S];E=[(i,j) for i,j in combinations(range(26),2) if not (b[i]>>j&1 or b[i]&b[j] or S>>i&S>>j&1) and (i,j) not in removed];dem=[tuple(e for e in E if all(q>>v&1 for v in e)) for q in qs];ds=[]
    for d in sorted(set(dem),key=lambda d:(len(d),d)):
        if not any(g<=set(d) for g in ds):ds.append(frozenset(d))
    return b,qs,dem,ds

def solve(b,ds,S):
    def rec(g,cs,edges):
        if not cs:
            h=g[:]+[S]
            for i in range(26):h[i]|=(S>>i&1)<<26
            assert check(h,(1<<27)-1,3,8);return edges
        opts=min(([e for e in c if not g[e[0]]&g[e[1]]] for c in cs),key=len)
        for i,j in sorted(opts,key=lambda e:(-sum(e in c for c in cs),e)):
            h=g[:];h[i]|=1<<j;h[j]|=1<<i;p=rec(h,[c for c in cs if (i,j) not in c],edges+[(i,j)])
            if p is not None:return p
    return rec(b,ds,[])

def audit():
    x=json.loads((D.parent/'ramsey_cube_repair_minmax.json').read_text());a=induced(G,x['core_labels']);src=[r for r in x['cases'] if r['cover']==7];runs=[];win=None
    for r in src:
        first=tuple(r['remove']);S=sum(1<<v for v in r['row']);b,qs,dem,ds=instance(a,[first],S);assert solve(b,ds,S) is None;forced={next(iter(d)) for d in ds if len(d)==1};g=b[:]
        for i,j in forced:g[i]|=1<<j;g[j]|=1<<i
        triangles=[(i,j,k) for i,j,k in combinations(range(26),3) if g[i]>>j & g[i]>>k & g[j]>>k &1];rank=Counter()
        required=[]
        for tri in triangles:
            escapes=set()
            for e in combinations(tri,2):
                i,j=e
                if e not in forced:rank[e]+=1;escapes.add(e);continue
                # A new pair inside a singly repairable demand can replace the forced edge
                # only if every common-neighbor path blocking the pair is opened.
                alternatives=[]
                for q,d in zip(qs,dem):
                    if d!=(e,):continue
                    opened=set()
                    for u,v in combinations([v for v in range(26) if q>>v&1],2):
                        m=b[u]&b[v];
                        if m.bit_count()==1 and not(S>>u&S>>v&1):
                            j=m.bit_length()-1;opened.update((tuple(sorted((u,j))),tuple(sorted((v,j)))))
                    rank.update(opened);alternatives.append(opened)
                escapes.update(set.intersection(*alternatives))
            required.append(escapes)
        necessary=set.intersection(*required)
        assert triangles;hist=Counter();passed=[]
        for cut,score in sorted(rank.items(),key=lambda kv:(-kv[1],kv[0])):
            if cut not in necessary:continue
            assert b[cut[0]]>>cut[1]&1;h,_,_,cs=instance(a,[first,cut],S)
            if not cs or cs[0]:hist['individually_breakable']+=1
            add=solve(h,cs,S)
            if add is not None:
                passed.append((cut,score,len(add)));w=dict(row=r['row'],remove=[first,cut],add=add)
                if win is None or len(add)<len(win['add']):win=w
        runs.append(dict(first=first,row=r['row'],forced=sorted(forced),triangles=triangles,candidates=len(rank),necessary=sorted(necessary),scores=sorted(rank.items(),key=lambda kv:(-kv[1],kv[0])),counts=hist,success=passed))
    print([(v['candidates'],len(v['necessary']),v['triangles'],v['counts'],v['success']) for v in runs],win);(D.parent/'ramsey_cube_path_unlock.json').write_text(json.dumps(dict(core_labels=x['core_labels'],runs=runs,witness=win),indent=2)+'\n')
if __name__=='__main__':audit()
