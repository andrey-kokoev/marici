"""All 477 locally and jointly safe starts. Normalize degree-eight vertices exhaustively, then apply fixed numerical contact counts and single-link veto propagation. Target identity is withheld until scoring."""
from ramsey_one_path_first import flip,propagate,budgets,bits,check,CAT,D,json,gzip,Path,tempfile,subprocess,Counter
from ramsey_retention_slice import has,decode
from itertools import islice,combinations

def audit(src=None):
    standalone=src is None
    if standalone:src=json.loads((D.parent/'ramsey_double_cross_blind_veto.json').read_text())
    starts=src['candidates'];idx=src['record']
    with gzip.open(CAT/'r38_27.g6.gz','rt') as f:a=decode(next(islice(f,idx,None)).strip())
    jobs=[];lines=[];stage=[Counter() for _ in starts];stats=Counter();V=(1<<27)-1
    for n,r in enumerate(starts):
        z=r['z'];active=V^(1<<z);adds=set(map(tuple,r['pair']));g=[v&active for v in a];g[z]=0
        for e in list(adds)+list(map(tuple,r['forced'])):flip(g,e)
        assert check(g,active,3,8);seen=set()
        def normalize(h,rm):
            high=next((i for i,v in enumerate(h) if v.bit_count()>7),None)
            if high is None:
                key=tuple(sorted(rm))
                if key not in seen:
                    seen.add(key);tag=len(jobs);jobs.append((n,key,h));lines.append(' '.join(map(str,[z,*h,tag])));stage[n]['normal']+=1
                return
            B=[~v for v in h]
            for j in bits(h[high]):
                e=tuple(sorted((high,j)))
                if e in adds or has(B,active&~(h[high]|h[j]|1<<high|1<<j),6):continue
                b=h[:];flip(b,e);normalize(b,rm+[e])
        normalize(g,[])
    with tempfile.TemporaryDirectory() as td:
        exe=Path(td)/'contacts.exe';subprocess.run(['rustc','-O',str(Path(__file__).with_name('ramsey_frozen_contacts.rs')),'-o',str(exe)],check=True);p=subprocess.run([str(exe)],input='\n'.join(lines),text=True,capture_output=True,check=True)
    survivors=[]
    for l in p.stdout.splitlines():
        tag,_,_,H=map(int,l.split());n,pre,g=jobs[tag];r=starts[n];z=r['z'];active=V^(1<<z);adds=set(map(tuple,r['pair']));out=[i for i in range(27) if i!=z and not H>>i&1];B=[~v for v in g];ban={}
        for i,j in combinations(out,2):
            e=(i,j)
            if g[i]>>j&1 and (e in adds or has(B,active&~(g[i]|g[j]|1<<i|1<<j),6)):ban[e]=[frozenset([e])]
        status,steps=propagate(g,out,H,ban);stage[n]['interfaces']+=1;stage[n][status]+=1
        if status=='conflict':continue
        legal=[]
        for rm in ([sum(steps,[])] if status=='solved' else budgets(g,out,H,ban)):
            b=g[:];
            for e in rm:flip(b,e)
            if check(b,active,3,8):legal.append(sorted(pre+tuple(rm)+tuple(map(tuple,r['forced']))))
        survivors.append(dict(start=r,pre=pre,seven=bits(H),status=status,forced_rounds=steps,legal=legal))
    def key(r):return r['z'],tuple(map(tuple,r['pair']))
    truth={(z,tuple(map(tuple,pair))) for z,pair in src.get('cube_routes',[])};left={key(r['start']) for r in survivors};recovered={key(r['start']) for r in survivors if r['legal']};assert truth<=recovered
    from ramsey_cube_retention_floor import iso,induced,G
    target=induced(G,[i for i in range(34) if not G[34]>>i&1]);graphs=set();cubes=set()
    for r in survivors:
        start=r['start'];z=start['z'];v=[i for i in range(27) if i!=z];r['cube']=[]
        for rm in r['legal']:
            g=a[:]
            for e in start['pair']+rm:flip(g,e)
            h=induced(g,v);k=(z,tuple(h));graphs.add(k);is_cube=iso(h,target) is not None;r['cube'].append(is_cube)
            if is_cube:cubes.add(k)
    stage_counts={k:sum(bool(st[k]) for st in stage) for k in ('normal','interfaces','solved','stalled','conflict')};tot=sum(stage,Counter());res=dict(record=idx,start_count=len(starts),candidate_counts=stage_counts,case_counts=tot,surviving_candidates=len(left),false_propagation_survivors=sorted(left-truth) if 'cube_routes' in src else None,legal_candidates=len(recovered),distinct_legal_graphs=len(graphs),cube_graphs=len(cubes),survivors=survivors);print({k:v for k,v in res.items() if k!='survivors'});print('successful traces',[(r['pre'],[len(s) for s in r['forced_rounds']]) for r in survivors if any(r['cube'])])
    if standalone:(D.parent/'ramsey_cross_residual_propagation.json').write_text(json.dumps(res,indent=2)+'\n')
    return res
if __name__=='__main__':audit()
