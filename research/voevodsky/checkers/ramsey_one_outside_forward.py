"""One outside endpoint, one common red neighbor per proposed link in the original predecessor. All degree-seven deletion sites. No target matching until outputs fixed."""
from ramsey_one_path_first import flip,propagate,budgets,bits,check,CAT,D,json,gzip,Path,tempfile,subprocess,Counter,combinations
from ramsey_retention_slice import has,decode
from itertools import islice
from collections import defaultdict

def trial(exe,a):
    V=(1<<27)-1;old=[(i,j) for i,j in combinations(range(27),2) if not a[i]>>j&1 and (a[i]&a[j]).bit_count()==1];jobs=[];levels=Counter();winners={};by=defaultdict(Counter)
    for z,row in enumerate(a):
        if row.bit_count()!=7:continue
        center=[e for e in old if all(row>>i&1 for i in e)];cross=[e for e in old if z not in e and sum(row>>i&1 for i in e)==1];V0=V^(1<<z);b=[n&V0 for n in a];b[z]=0
        for e in center:
            for f in cross:
                if set(e)&set(f):continue
                levels['pairs']+=1;u=next(i for i in f if not row>>i&1);m,=bits(a[f[0]]&a[f[1]]);g=b[:];flip(g,e);flip(g,f);comp=g[u].bit_count()>7
                for i in f:
                    cut=tuple(sorted((i,m)));h=g[:];flip(h,cut)
                    more=[None] if h[u].bit_count()<=7 else [tuple(sorted((u,v))) for v in bits(b[u]&h[u])];
                    for extra in more:
                        v=h[:];
                        if extra:flip(v,extra)
                        prefix=(cut,extra) if extra else (cut,);levels['cut_trials']+=1
                        # Remaining graph may only lose links. Each new blue eight needs at least one preliminary removal in it.
                        B=[~n for n in v];bad=False
                        for j,k in prefix:
                            if has(B,V0&~(v[j]|v[k]|1<<j|1<<k),6):bad=True;break
                        if bad:continue
                        levels['precut_veto_pass']+=1;jobs.append((z,e,f,u,comp,m,prefix,v))
    lines='\n'.join(' '.join(map(str,[z,*g,tag])) for tag,(z,e,f,u,comp,m,c,g) in enumerate(jobs));res=subprocess.run([str(exe)],input=lines,text=True,capture_output=True,check=True);bystage=defaultdict(Counter)
    for line in res.stdout.splitlines():
        tag,_,_,H=map(int,line.split());z,e,f,u,comp,m,pre,g=jobs[tag];key=(z,e,f);outer=[j for j in range(27) if j!=z and not H>>j&1];need={j:g[j].bit_count()-(4 if (g[j]&H).bit_count()==1 else 6) for j in outer};B=[~n for n in g];ban={}
        for i,j in combinations(outer,2):
            edge=(i,j)
            if g[i]>>j&1 and (edge in (e,f) or (need[i]*need[j]>0 and has(B,V&~(1<<z|1<<i|1<<j|g[i]|g[j]),6))):ban[edge]=[frozenset([edge])]
        status,trace=propagate(g,outer,H,ban);levels[status]+=1;bystage[key][status]+=1
        if status=='conflict':continue
        for rm in ([sum(trace,[])] if status=='solved' else budgets(g,outer,H,ban)):
            h=g[:];
            for c in rm:flip(h,c)
            if not check(h,V^(1<<z),3,8):continue
            identity=(z,e,f,tuple(sorted(pre+tuple(rm))));w=winners.setdefault(identity,dict(z=z,center=e,cross=f,outside=u,outside_initial_degree=a[u].bit_count(),middle=m,degree_seven_core=bits(H),final_outside_degree=h[u].bit_count(),removed=identity[-1],histories=[],core=h));w['histories'].append(dict(prefix=pre,forced_steps=trace,status=status))
    for w in winners.values():
        key=(w['z'],w['center'],w['cross']);w['pair_status']=bystage[key];w['surviving_prefixes_before_contact']=[c for z,e,f,u,comp,m,c,g in jobs if (z,e,f)==key]
    return dict(counts=levels,outputs=list(winners.values()))

def audit():
    ids=(99152,319751);graphs={i:decode(l.strip()) for i,l in enumerate(gzip.open(CAT/'r38_27.g6.gz','rt')) if i in ids};out={}
    with tempfile.TemporaryDirectory() as td:
        exe=Path(td)/'rigid.exe';subprocess.run(['rustc','-O',str(Path(__file__).with_name('ramsey_frozen_contacts.rs')),'-o',str(exe)],check=True)
        for i,a in graphs.items():out[i]=trial(exe,a)
    from ramsey_cube_retention_floor import iso,induced,G
    target=induced(G,[j for j in range(34) if not G[34]>>j&1]);
    for i,r in out.items():
        for w in r['outputs']:w['cube']=iso(induced(w.pop('core'),[j for j in range(27) if j!=w['z']]),target) is not None
        print(i,r['counts'],[(w['z'],w['center'],w['cross'],w['outside'],w['final_outside_degree'],w['cube'],len(w['histories'])) for w in r['outputs']])
    (D.parent/'ramsey_one_outside_forward.json').write_text(json.dumps(out,indent=2)+'\n')
if __name__=='__main__':audit()
