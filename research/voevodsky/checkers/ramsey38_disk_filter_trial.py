"""New-array prospective comparison of the frozen disk-agreement filter."""
from ramsey38_choose_promotion_trial import P as old,prev,json,graph,gzip,setup,options,legal,sys
from ramsey38_tip_disk_domains import disks,propagate
from ramsey38_novel_array_trial import perm_table
from collections import Counter
P=prev.out/'ramsey38_disk_filter_predictions.json';R=prev.out/'ramsey38_disk_filter_comparison.json'
protocol='First five canonically new multi-promotion arrays after record 428, excluding previous edit trial; first eligible root per record. All edge targets. Baseline order test versus also requiring nonempty local vertex-disk domains after neighbor propagation. Leave baseline unchanged if not all labels on boundary. Same ranking. Score first triple and every surviving triple before any filling calls.'
def key(L,rs,moves):
    sig=[(s,sum(1<<L.index(v) for y,v in moves if y==x)) for x,s in rs.items()];return min(tuple(sorted((t[s],t[m]) for s,m in sig)) for t in perm_table())
def freeze():
    seen={key(*setup(graph(e['word']),e['u'])) for e in json.loads(old.read_text())['cases']};out=[]
    with gzip.open(prev.catalogue,'rt') as f:
        for i,line in enumerate(f,1):
            if i<=428:continue
            word=line.strip();g=graph(word)
            for u in sorted(g):
                if len(g[u])!=7:continue
                L,rs,moves=setup(g,u);targets=sorted(j for j,s in rs.items() if s.bit_count()==2)
                if len(moves)<2 or not targets or max(map(int.bit_count,rs.values()))>4:continue
                k=key(L,rs,moves)
                if k in seen:continue
                seen.add(k);dec=lambda m:frozenset(w for l,w in enumerate(L) if m>>l&1);rows=[]
                for j in targets:
                    opts=options(L,rs,moves,j);new=[]
                    for z in opts:
                        bd=set(map(dec,z['bd']));x,v=z['edge'];s=dec(rs[x]);fixed={dec(r) for y,r in rs.items() if y!=x}|{s|{v}};passed=[]
                        for w in z['tips']:
                            if set.union(set(),*bd)!=set(L) or all(propagate({a:disks(L,a,bd,fixed|{s|{w}}) for a in L})[0][-1].values()):passed.append(w)
                        if passed:new.append(dict(z,tips=passed))
                    new.sort(key=lambda z:(-len(z['tips']),z['edge'],z['bd']));rows.append(dict(row=j,old=opts,new=new))
                out.append(dict(record=i,word=word,u=u,requests=rows));print(i,u,flush=True);break
            if len(out)==5:break
    assert len(out)==5;prev.save(P,dict(protocol=protocol,cases=out))
def triples(opts):return [(tuple(z['edge']),tuple(z['bd']),w) for z in opts for w in z['tips']]
def compare():
    data=json.loads(P.read_text());cnt=Counter();res=[]
    for e in data['cases']:
        g=graph(e['word']);L,rs,moves=setup(g,e['u']);
        for x,v in moves:
            h={w:set(s) for w,s in g.items()};h[x].add(v);h[v].add(x);assert legal(h)
        for d in e['requests']:
            opts=options(L,rs,moves,d['row'],True);truth=set(triples(opts));cnt['requests']+=1;cnt['feasible']+=bool(truth);cnt['true_triples']+=len(truth)
            for k in ['old','new']:
                p=triples(d[k]);cnt[k+'_hit']+=bool(p and p[0] in truth);cnt[k+'_proposed']+=bool(p);cnt[k+'_extra']+=len(set(p)-truth);cnt[k+'_missed']+=len(truth-set(p))
            res.append(dict(record=e['record'],root=e['u'],row=d['row'],options=opts))
    print(cnt);prev.save(R,dict(prediction_sha=prev.sha(P.read_bytes()),counts=dict(cnt),requests=res))
if __name__=='__main__':{'freeze':freeze,'compare':compare}[sys.argv[1]]()
