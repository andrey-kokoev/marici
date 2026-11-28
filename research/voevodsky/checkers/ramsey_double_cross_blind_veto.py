"""Does a uniquely forced cut on each path select a site/pair on record 448077? Precompute protected edges before choice; exact target embeddings score, never generate, proposals."""
from itertools import combinations,islice
from collections import Counter
from ramsey_retention_slice import CAT,D,decode,check
import gzip,json

def audit(on_joint_failure=None,idx=448077,score_cube=True,site_degrees=(7,)):
    with gzip.open(CAT/'r38_27.g6.gz','rt') as f:a=decode(next(islice(f,idx,None)).strip())
    V=(1<<27)-1;I=[0]
    for j,v in enumerate(a):I.extend([q|1<<j for q in I if not q&v]);
    six=[q for q in I if q.bit_count()==6];protected={}
    for i,j in combinations(range(27),2):
        if a[i]>>j&1:protected[i,j]=[q|1<<i|1<<j for q in six if not q&(a[i]|a[j]|1<<i|1<<j)]
    counts=Counter();called=[];summary=[]
    for z,s in enumerate(a):
        if s.bit_count() not in site_degrees:continue
        pool=[(i,j) for i in range(27) if s>>i&1 for j in range(27) if j!=z and not s>>j&1 and not a[i]>>j&1 and a[i]&a[j]];cs=Counter()
        for e,f in combinations(pool,2):
            m,n=(sum(1<<v for v in edge) for edge in (e,f))
            if m&n:continue
            paths=[(i,k,j) for i,j in (e,f) for k in range(27) if a[i]&a[j]&(1<<k)];cs['proposals']+=1;chosen=set()
            for i,k,j in paths:
                opts=[edge for edge in (tuple(sorted((i,k))),tuple(sorted((k,j)))) if not any(not q>>z&1 and q&m!=m and q&n!=n for q in protected[edge])]
                if len(opts)!=1:break
                chosen.add(opts[0])
            else:
                cs['locally_forced']+=1;b=a[:];b[z]=0
                for j in range(27):b[j]&=~(1<<z)
                for u,v in [e,f,*chosen]:b[u]^=1<<v;b[v]^=1<<u
                if check(b,V^(1<<z),3,8):
                    cs['jointly_legal']+=1;called.append(dict(z=z,pair=sorted([sorted(e),sorted(f)]),forced=sorted(chosen),path_counts=sorted((a[i]&a[j]).bit_count() for i,j in (e,f))))
                elif on_joint_failure is not None:on_joint_failure(z,(e,f),chosen,b)
        counts.update(cs);summary.append(dict(z=z,counts=cs))
    if not score_cube:return dict(record=idx,counts=counts,candidates=called)
    from ramsey_forward_link_filter import score
    truth=set();eligible={r['z'] for r in summary}
    for z in eligible:
        for k in score(a,z)[0]:
            if all(sum(a[z]>>i&1 for i in e)==1 and a[e[0]]&a[e[1]] for e in k):truth.add((z,k))
    keys={(r['z'],tuple(map(tuple,r['pair']))) for r in called};hits=keys&truth;print(counts,'sites',len(eligible),len(set(z for z,_ in keys)),'truth',truth,'hits',hits,'false',[r for r in called if (r['z'],tuple(map(tuple,r['pair']))) not in hits][:1]);out=dict(record=idx,counts=counts,site_counts=summary,candidates=called,cube_routes=sorted(truth),hits=sorted(hits));(D.parent/'ramsey_double_cross_blind_veto.json').write_text(json.dumps(out,indent=1)+'\n')
if __name__=='__main__':audit()
