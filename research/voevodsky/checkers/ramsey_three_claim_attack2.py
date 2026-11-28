"""Second falsification pass: degree-six sites, exact port completion, and a bounded reverse three-cut search."""
from ramsey_three_claim_attack import *
from itertools import combinations
from ramsey_retention_slice import check

def complete(a,allowed=None):
    I=[0]
    for i,v in enumerate(a):I.extend([q|1<<i for q in I if not v&q])
    sets=[[]]+[[q for q in I if q.bit_count()==k] for k in range(1,8)];rows=[s for s in sets[6]+sets[7] if allowed is None or s in allowed];miss={s:[0]+[sum(1<<j for j,q in enumerate(sets[k]) if not q&s) for k in range(1,8)] for s in rows};nodes=Counter();N=len(a);V=(1<<N)-1
    # load(q) <=8 means at most 8-|q| rows can miss q. Use bit-sliced counts of sets missed by >=t selected rows.
    def visit(p,opts,levels):
        nodes[len(p)]+=1
        if len(p)==8:
            b=a[:]+[s|(1<<34) for s in p]+[((1<<8)-1)<<26];
            for j,s in enumerate(p,26):
                for i in range(N):b[i]|=(s>>i&1)<<j
            assert check(b,(1<<35)-1,3,9);return p
        for j,s in enumerate(opts):
            ms=miss[s];nxt=[[]]+[[old|(ms[k]&last) for old,last in zip(levels[k],[-1]+levels[k])] for k in range(1,8)];rem=[r for r in opts[j:] if all(not miss[r][k]&nxt[k][-1] for k in range(1,8))];
            if len(p)==7 or rem:
                out=visit(p+[s],rem,nxt)
                if out:return out
    sol=visit([],rows,[[]]+[[0]*(8-k) for k in range(1,8)]);return dict(rows=len(rows),search_nodes=nodes,solution=sol)

def cheap(a,cuts):
    h=a[:];
    for i,j in cuts:h[i]^=1<<j;h[j]^=1<<i
    I=[0]
    for i,v in enumerate(h):I.extend([q|1<<i for q in I if not q&v]);
    es=[(i,j) for i,j in combinations(range(26),2) if (i,j) not in cuts and not h[i]&((1<<j)|h[j]) and max(h[i].bit_count(),h[j].bit_count())<7];qs=[(q if q.bit_count()==7 else 0,sum(1<<k for k,(i,j) in enumerate(es) if q>>i&q>>j&1)) for q in I if q.bit_count() in (7,8)];must=[q for q,m in qs if not m];sat=sum(1<<j for j,v in enumerate(h) if v.bit_count()>=7)
    for s in I:
        if not 4<=s.bit_count()<=7 or s&sat or any(not q&s for q in must):continue
        g=h[:]+[s];
        for i in range(26):g[i]|=(s>>i&1)<<26
        ds={m for q,m in qs if not q&s}
        def dfs(b,ds,path):
            if not ds:
                assert check(b,(1<<27)-1,3,8);return path
            if len(path)==7:return
            ok=sum(1<<k for k,(i,j) in enumerate(es) if not b[i]&b[j] and max(b[i].bit_count(),b[j].bit_count())<7);opts=min((m&ok for m in ds),key=int.bit_count)
            while opts:
                bit=opts&-opts;opts-=bit;i,j=es[bit.bit_length()-1];c=b[:];c[i]|=1<<j;c[j]|=1<<i;v=dfs(c,{m for m in ds if not m&bit},path+[(i,j)])
                if v is not None:return v
        ans=dfs(g,ds,[])
        if ans is not None:return dict(cuts=cuts,row=s,other=ans)

def run():
    T=D.parent;prev=json.loads((T/'ramsey_three_claim_attack.json').read_text());base=json.loads((T/'ramsey_double_cross_blind_veto.json').read_text());idx=base['record'];
    with gzip.open(CAT/'r38_27.g6.gz','rt') as f:b=decode(next(islice(f,idx,None)).strip())
    port={}
    for n in prev['passed_port_indices']:
        r=base['candidates'][n];h=b[:]
        for i,j in r['pair']+r['forced']:h[i]^=1<<j;h[j]^=1<<i
        port[n]=complete(induced(h,[i for i in range(27) if i!=r['z']]))
    print('ports',port,flush=True);labels=json.loads((T/'ramsey_cube_unlock_free_row.json').read_text())['core_labels'];a=induced(G,labels);known={sum((G[u]>>v&1)<<i for i,v in enumerate(labels)) for u in range(35) if u not in labels};assert complete(a,known)['solution'];seed=list(map(tuple,json.loads((T/'ramsey_cube_cut_location.json').read_text())['cases'][0]['cuts']));tried=0;success=None
    for e in combinations(range(26),2):
        if e in seed or not a[e[0]]>>e[1]&1:continue
        tried+=1;success=cheap(a,seed+[e]);
        if success:break
    print('cost',seed,tried,success,flush=True);idx=99148;src=generate(idx=idx,score_cube=False,site_degrees=(6,7));res=finish(src);out=dict(port=port,cost=dict(seed=seed,tried=tried,success=success),amended_transfer=dict(record=idx,starts=res['start_count'],cases=res['case_counts'],survivors=res['survivors']));(T/'ramsey_three_claim_attack2.json').write_text(json.dumps(out,indent=1)+'\n')
if __name__=='__main__':run()
