"""Local prospective discovery: generate every legal single recoloring directly from each predecessor, hide its known route, apply the frozen contact/veto rule anew. Only afterwards compare output cores with the original route and identify catalogue records."""
from ramsey_partial_removal_veto import propagate,vetoes
from ramsey_frozen_contacts_transfer import bits,budgets,check,CAT,D,json,tempfile,subprocess,Path,Counter,decode,gzip
from itertools import combinations
from collections import defaultdict

def build(exe,a):
    zs=[z for z,n in enumerate(a) if n.bit_count()==7];p=subprocess.run([str(exe)],input='\n'.join(' '.join(map(str,[z]+a)) for z in zs),text=True,capture_output=True,check=True);st=Counter();out=[]
    for line in p.stdout.splitlines():
        z,e,f,H=map(int,line.split());g=[n&~(1<<z) for n in a];g[z]=0;pair=sorted([bits(e),bits(f)])
        for i,j in pair:g[i]|=1<<j;g[j]|=1<<i
        outer=[i for i in range(27) if i!=z and not H>>i&1];one,_=vetoes(g,outer,H,z);status,steps=propagate(g,outer,H,one);st[status]+=1
        if status=='conflict':continue
        for rm in ([sum(steps,[])] if status=='solved' else budgets(g,outer,H,one)):
            b=g[:]
            for i,j in rm:b[i]^=1<<j;b[j]^=1<<i
            if check(b,((1<<27)-1)^(1<<z),3,8):out.append(dict(z=z,add=pair,rm=rm,core=b,status=status))
    return st,out

def audit():
    ids={236272,262402};seeds={i:decode(l.strip().decode()) for i,l in enumerate(gzip.open(CAT/'r38_27.g6.gz','rb')) if i in ids};jobs=[]
    for idx,a in seeds.items():
        for i,j in combinations(range(27),2):
            b=a[:];b[i]^=1<<j;b[j]^=1<<i
            if check(b,(1<<27)-1,3,8):jobs.append((idx,i,j,b))
    with tempfile.TemporaryDirectory() as td:
        exe=Path(td)/'frozen.exe';subprocess.run(['rustc','-O',str(Path(__file__).with_name('ramsey_frozen_contacts.rs')),'-o',str(exe)],check=True);base={i:build(exe,a)[1] for i,a in seeds.items()};found=[build(exe,b) for _,_,_,b in jobs]
    # Blind predictions complete. Use full target, labels and catalogue only for scoring and identification.
    from ramsey_cube_retention_floor import G,induced,iso,wl,deg
    target=induced(G,[i for i in range(34) if not G[34]>>i&1]);lookup=defaultdict(list);stats=Counter();rs=[]
    for (idx,i,j,b),(st,ans) in zip(jobs,found):
        stats['trials']+=1;stats['legal_outputs']+=len(ans);stats['positive_trials']+=bool(ans);seedkeys={(r['z'],tuple(r['core'])) for r in base[idx]}
        for r in ans:
            c=r.pop('core');r['inherited_labeled_core']=(r['z'],tuple(c)) in seedkeys;r['cube']=iso(induced(c,[u for u in range(27) if u!=r['z']]),target) is not None;stats['cube']+=r['cube'];stats['not_inherited']+=not r['inherited_labeled_core']
        rec=dict(seed=idx,changed=[i,j],added_red=not bool(seeds[idx][i]>>j&1),counts=st,outputs=ans);ref=base[idx][0];z=ref['z'];c=ref['core'];before=induced(b,[v for v in range(27) if v!=z]);rm=[];ad=[]
        for u,v in combinations([v for v in range(27) if v!=z],2):
            if (b[u]^c[u])>>v&1:(rm if b[u]>>v&1 else ad).append((u,v))
        bb=b[:]
        for u,v in rm+ad:bb[u]^=1<<v;bb[v]^=1<<u
        assert induced(bb,[v for v in range(27) if v!=z])==induced(c,[v for v in range(27) if v!=z]);rec['transported_route']=dict(z=z,add=ad,remove=rm,initial_middles=[bits(b[u]&b[v]) for u,v in ad]);rs.append(rec);lookup[wl(b)].append((b,rec))
    w=bytes([(j-63).bit_count() if 63<=j<=126 else 0 for j in range(256)]);es={sum(map(int.bit_count,b))//2 for _,_,_,b in jobs};degs={deg(b) for _,_,_,b in jobs}
    for idx,line in enumerate(gzip.open(CAT/'r38_27.g6.gz','rb')):
        s=line.rstrip()
        if sum(s[1:].translate(w)) not in es:continue
        a=decode(s.decode());
        if deg(a) not in degs:continue
        for b,r in lookup.get(wl(a),[]):
            if 'record' not in r and iso(b,a) is not None:r['record']=idx
        if all('record' in r for r in rs):break
    assert all('record' in r for r in rs);print(stats,[(r['seed'],r['record'],r['added_red'],len(r['outputs'])) for r in rs]);(D.parent/'ramsey_contact_blind_neighbors.json').write_text(json.dumps(dict(counts=stats,trials=rs),indent=2)+'\n')
if __name__=='__main__':audit()
