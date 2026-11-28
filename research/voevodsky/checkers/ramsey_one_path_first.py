"""Generate a preliminary cut from a unique surviving two-edge red path, without supplying any seed route or labels. Audit both path legs and all deletion/centered-pair alternatives."""
from ramsey_partial_removal_veto import propagate,vetoes
from ramsey_frozen_contacts_transfer import bits,budgets,check,CAT,D,json,gzip,Path,tempfile,subprocess,Counter
from itertools import combinations,permutations
from collections import defaultdict

def flip(g,e):
    i,j=e;g[i]^=1<<j;g[j]^=1<<i

def trial(exe,a):
    jobs=[];lines=[];by=defaultdict(Counter);proof=defaultdict(list)
    for z,v in enumerate(a):
        if v.bit_count()!=7:continue
        c=[(i,j) for i,j in combinations(bits(v),2) if (a[i]&a[j]).bit_count()<=2];
        for e,f in combinations(c,2):
            if set(e)&set(f):continue
            paths=[(i,m,j) for i,j in (e,f) for m in bits((a[i]&a[j])&~(1<<z))];
            if len(paths)!=1:continue
            i,m,j=paths[0]
            for k in (i,j):
                cut=tuple(sorted((k,m)));b=a[:];flip(b,cut);tag=len(jobs);jobs.append((z,e,f,cut));lines.append(' '.join(map(str,[z,*b,sum(1<<u for u in e),sum(1<<u for u in f),tag])))
    p=subprocess.run([str(exe)],input='\n'.join(lines),text=True,capture_output=True,check=True);wins=[];seen=Counter()
    for l in p.stdout.splitlines():
        tag,e0,f0,H=map(int,l.split());z,e,f,c=jobs[tag];g=[v&~(1<<z) for v in a];g[z]=0;assert {tuple(bits(e0)),tuple(bits(f0))}=={e,f};
        for h in (c,e,f):flip(g,h)
        outer=[i for i in range(27) if i!=z and not H>>i&1];one,_=vetoes(g,outer,H,z);status,trace=propagate(g,outer,H,one);by[tag][status]+=1;seen[status]+=1
        if status=='conflict':
            used=set(edge for layer in trace for edge in layer);need={i:g[i].bit_count()-(4 if (g[i]&H).bit_count()==1 else 6)-sum(i in edge for edge in used) for i in outer};rem={i:sum(1 for j in outer if g[i]>>j&1 and need[j]>0 and tuple(sorted((i,j))) not in used and tuple(sorted((i,j))) not in one) for i in outer};proof[tag].append(dict(forced_layers=len(trace),deficits=[(i,k,rem[i]) for i,k in need.items() if k<0 or k>rem[i]]));continue
        for rm in ([sum(trace,[])] if status=='solved' else budgets(g,outer,H,one)):
            b=g[:];
            for edge in rm:flip(b,edge)
            if not check(b,((1<<27)-1)^(1<<z),3,8):continue
            # Is there even an order preserving both forbiddances on the reduced core throughout?
            legal_orders=[]
            for seq in permutations([c,e,f]):
                v=[m&~(1<<z) for m in a];v[z]=0
                for h in seq:
                    flip(v,h)
                    if not check(v,((1<<27)-1)^(1<<z),3,8):break
                else:legal_orders.append(seq)
            wins.append(dict(z=z,pair=[e,f],cut=c,other_removals=rm,status=status,legal_orders=legal_orders,core=b,opposite=jobs[tag^1][3],other_tag=tag^1))
    for w in wins:
        t=w.pop('other_tag');w['other_leg_counts']=dict(by[t]);w['other_leg_failures']=proof[t]
    return dict(choices=len(jobs),sets=seen,wins=wins)

def audit():
    ids={236270,236271};graphs={i:__import__('ramsey_retention_slice').decode(s.decode().strip()) for i,s in enumerate(gzip.open(CAT/'r38_27.g6.gz','rb')) if i in ids};res={}
    with tempfile.TemporaryDirectory() as td:
        exe=Path(td)/'frozen.exe';subprocess.run(['rustc','-O',str(Path(__file__).with_name('ramsey_frozen_contacts.rs')),'-o',str(exe)],check=True)
        for i,a in graphs.items():res[i]=trial(exe,a)
    from ramsey_cube_retention_floor import induced,G,iso
    target=induced(G,[i for i in range(34) if i!=34 and not G[34]>>i&1]);
    for i,r in res.items():
        for w in r['wins']:w['cube']=iso(induced(w.pop('core'),[j for j in range(27) if j!=w['z']]),target) is not None
        print(i,r)
    (D.parent/'ramsey_one_path_first.json').write_text(json.dumps(res,indent=2)+'\n')
if __name__=='__main__':audit()
