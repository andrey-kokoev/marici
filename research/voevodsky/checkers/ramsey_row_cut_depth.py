"""Complete obstruction-depth census at the two false sites that survive the distinct-row and pair-cut tests. Depth 9 means no failing subset. Control: test the actual winning eight, not an exhaustive positive-site census."""
from ramsey_row_cut_tests import sets,D,CAT,gzip,islice,decode,json,induced,combinations,check,subprocess,tempfile,Path

import os

def static_cover(rows,packs,six,vs):
    masks={};U=(1<<len(packs))-1
    for q in six:
        bits=sum(1<<i for i,p in enumerate(packs) if sum(not rows[j]&q for j in p)>=3)
        if bits:masks[bits]=q
    missing=U;cert=[]
    while missing:
        best=max(masks,key=lambda m:(m&missing).bit_count(),default=0)
        if not best&missing:break
        cert.append(best);missing&=~best
    return dict(static_packings=len(packs),survive_all_old_sixes=missing.bit_count(),greedy_cover=[dict(old_blue_six=[v for j,v in enumerate(vs) if masks[m]>>j&1],packings_hit=m.bit_count()) for m in cert])

def run():
    T=D.parent;prior=json.loads((T/'ramsey_row_cut_tests.json').read_text());pos=json.loads((T/'ramsey_free_cross_profile.json').read_text())['outputs'][0]['profile']['rows'];out=[]
    with gzip.open(CAT/'r38_27.g6.gz','rt') as f:b=decode(next(islice(f,448077,None)).strip())
    with tempfile.TemporaryDirectory() as td:
        exe=Path(td)/'census.exe';subprocess.run(['rustc','--edition=2021','-O',str(Path(__file__).with_suffix('.rs')),'-o',str(exe)],check=True)
        for c in prior:
            z=c['start']['z']
            if z not in (5,12,22):continue
            vs=[i for i in range(27) if i!=z];h=b[:];adds=c['start']['pair'];
            for u,v in adds+c['start']['forced']+[c['extra']]:h[u]^=1<<v;h[v]^=1<<u
            g=induced(h,vs);fixed=g[:];six=sets(g,6)
            for i,j in combinations(range(26),2):
                if g[i]>>j&1 and [vs[i],vs[j]] not in adds and not any(not s&(g[i]|g[j]) for s in six):fixed[i]^=1<<j;fixed[j]^=1<<i
            rows=sets(fixed,7);assert len(rows)==c['result']['candidate_rows'];
            if z==5:assert set(pos)<=set(rows);rows=pos
            ls=subprocess.run([str(exe)],input='\n'.join(' '.join(map(str,v)) for v in [g,rows]),text=True,capture_output=True,check=True).stdout.splitlines();depth,flags,best,examples=map(json.loads,ls);assert sum(depth)==sum(flags)>0 and sum(flags[1:])==depth[2] and (depth[8]==1 if z==5 else depth[8]==0);print(z,depth,flags,flush=True)
            labels=lambda ids:[[v for j,v in enumerate(vs) if rows[i]>>j&1] for i in ids];out.append(dict(z=z,domain='winning eight only' if z==5 else 'all optimistic seven-site rows',rows=len(rows),pairwise_packings=sum(depth),minimum_failure_size={i+1:k for i,k in enumerate(depth) if k},triple_types={'bits':'1=core blue eight, 2=three ports miss blue six, 4=two ports miss new blue seven','counts':flags},best_packing=labels(best),flag_examples=[labels(x) for x in examples]))
            raw=subprocess.run([str(exe)],input='\n'.join(' '.join(map(str,v)) for v in [g,rows]),env={**os.environ,'ROW_LIST_STATIC':'1'},text=True,capture_output=True,check=True).stdout.splitlines();packs=[json.loads(l[5:]) for l in raw if l.startswith('rows ')];assert len(packs)>=sum(depth);out[-1]['before_pair_cut_test']=static_cover(rows,packs,six,vs);print(z,out[-1]['before_pair_cut_test'],flush=True)
    (T/'ramsey_row_cut_depth.json').write_text(json.dumps(out,indent=1)+'\n')
if __name__=='__main__':run()
