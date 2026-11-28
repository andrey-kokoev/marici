"""Both additions cross the deleted row. Compare single-leg, joint blue-eight and target-replay choices; never assume paths are unique or disjoint."""
from ramsey_centered_family_envelope import enumerate_all,G,induced,D,CAT,decode,iso,wl,deg,json,combinations,Counter,defaultdict,gzip
from ramsey_retention_slice import has
from itertools import product

def audit():
    V=json.loads((D.parent/'ramsey_cube_unlock_free_row.json').read_text())['core_labels'];a=induced(G,V);rows=json.loads((D.parent/'ramsey_cube_cut_location.json').read_text())['cases'];F=(1<<26)-1;stats=Counter();pathct=Counter();legct=Counter();samples={};bykey=defaultdict(list);cases=[]
    def typ(g):
        key=wl(g)
        for t in bykey[key]:
            if iso(g,samples[t]) is not None:return t
        t=len(samples);samples[t]=g;bykey[key].append(t);return t
    for r in rows:
        if r['locations']!=[1,1]:continue
        stats['signatures']+=1;s=set(r['row']);cuts=list(map(tuple,r['cuts']));es,models=enumerate_all(a,r)
        for m,g in models.items():
            removed={e for k,e in enumerate(es) if m>>k&1};post=[v&F for v in g[:26]];paths=[];mult=[]
            for e in cuts:
                i,=set(e)&s;u,=set(e)-s;ms=[j for j in range(26) if g[i]&g[u]&(1<<j)];mult.append(len(ms));paths.extend([(i,j,u) for j in ms]);post[i]|=1<<u;post[u]|=1<<i
            def veto(edges):
                h=post[:]
                for i,j in edges:h[i]&=~(1<<j);h[j]&=~(1<<i)
                return has([~v for v in h],F,8)
            opts=[tuple(tuple(sorted((j,y))) for y in (i,u)) for i,j,u in paths];single={e:veto([e]) for ds in opts for e in ds};actual=[tuple('IO'[k] for k,e in enumerate(ds) if e in removed) for ds in opts];legct.update(actual);pathct[tuple(sorted(mult))]+=1;short={frozenset(combo) for combo in product(*opts)};# A shared leg may break more than one path; only compare inclusion-minimal choices.
            short={v for v in short if not any(w<v for w in short)};alone={v for v in short if not any(single[e] for e in v)};joint={v for v in alone if not veto(v)};truth={v for v in short if v<=removed};assert truth and truth<=joint;stats.update(dict(models=1,solved_singly=(alone==truth),solved_jointly=(joint==truth),new_joint_veto=bool(alone-joint),unresolved=bool(joint-truth),multiple_working_prefixes=len(truth)>1));cases.append(dict(type=typ(g),row=sorted(s),pair=cuts,paths=paths,removed=sorted(removed),single_veto=[e for e in single if single[e]],counts=[len(short),len(alone),len(joint),len(truth)],wrong_after_joint=[sorted(v) for v in sorted(joint-truth,key=sorted)],correct=[sorted(v) for v in sorted(truth,key=sorted)]))
    pending=set(samples);ids={};degs={deg(g) for g in samples.values()};edges={sum(map(int.bit_count,g))//2 for g in samples.values()};w=bytes([(j-63).bit_count() if 63<=j<=126 else 0 for j in range(256)])
    for idx,l in enumerate(gzip.open(CAT/'r38_27.g6.gz','rb')):
        st=l.strip();
        if sum(st[1:].translate(w)) not in edges:continue
        g=decode(st.decode());
        if deg(g) not in degs:continue
        for t in bykey.get(wl(g),[]):
            if t in pending and iso(samples[t],g) is not None:ids[t]=idx;pending.remove(t)
        if not pending:break
    assert not pending
    for c in cases:c['record']=ids[c.pop('type')]
    print(stats,'multiplicities',pathct,'removed leg kinds',legct,'types',len(ids),'choice counts',Counter(tuple(c['counts']) for c in cases));(D.parent/'ramsey_double_cross_paths.json').write_text(json.dumps(dict(stats=stats,leg_counts={str(k):v for k,v in legct.items()},cases=cases),indent=1)+'\n')
if __name__=='__main__':audit()
