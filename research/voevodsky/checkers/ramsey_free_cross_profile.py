"""All two-crossing-addition completions of record 448077. Only the proved regularity gate fixes 76 core edges. Score overlap and contact separately after free row search."""
from ramsey_port_descendants import D,CAT,decode,gzip,islice,json,induced,combinations,check,classify,subprocess,tempfile,Path
from concurrent.futures import ThreadPoolExecutor
from collections import Counter

def run():
    idx=448077
    with gzip.open(CAT/'r38_27.g6.gz','rt') as f:a=decode(next(islice(f,idx,None)).strip())
    with tempfile.TemporaryDirectory() as td:
        def execute(name,inputs,chunk):
            exe=Path(td)/(name+'.exe');subprocess.run(['rustc','--edition=2021','-O',str(Path(__file__).with_name(name+'.rs')),'-o',str(exe)],check=True)
            def work(lo):return lo,subprocess.run([str(exe)],input='\n'.join(' '.join(map(str,g)) for g in inputs[lo:lo+chunk]),text=True,capture_output=True,check=True).stdout.splitlines()
            with ThreadPoolExecutor(6) as ex:return list(ex.map(work,range(0,len(inputs),chunk)))
        sites={};jobs=[];meta=[];keys=set();
        for _,lines in execute('ramsey_all_cross_76',[[z,*a] for z in range(27)],1):
            for l in lines:
                if l.startswith('done '):
                    _,z,n,k=l.split();sites[int(z)]=dict(pairs=int(n),cores=int(k),seven_pass=0,outputs=0);continue
                _,z,i,j,u,v,graph=l.split(' ',6);z,i,j,u,v=map(int,(z,i,j,u,v));g=json.loads(graph);vs=[t for t in range(27) if t!=z];old=induced(a,vs);assert sum(map(int.bit_count,g))==152 and check(g,(1<<26)-1,3,8);adds=[(vs[p],vs[q]) for p,q in combinations(range(26),2) if g[p]>>q&1 and not old[p]>>q&1];assert adds==[(vs[i],vs[j]),(vs[u],vs[v])];key=(z,*g);assert key not in keys;keys.add(key);jobs.append(g);meta.append((z,adds))
        assert len(sites)==27 and sum(c['cores'] for c in sites.values())==len(jobs)
        for z,c in sites.items():
            edges=sum(1 for i,j in combinations(range(27),2) if z not in (i,j) and (a[z]>>i^a[z]>>j)&1 and not a[i]>>j&1);assert c['pairs']==edges*(edges-1)//2
        print('all pairs',sum(c['pairs'] for c in sites.values()),'76-edge cores',len(jobs),flush=True);tags=[int(s) for _,ls in execute('ramsey_port_seven_screen',jobs,50) for s in ls];assert len(tags)==len(jobs);passed=[i for i,v in enumerate(tags) if v];print('pass',len(passed),flush=True);output=[];done=[]
        for i in passed:sites[meta[i][0]]['seven_pass']+=1
        for lo,lines in execute('ramsey_free_port_census',[jobs[i] for i in passed],2):
            for l in lines:
                k,v=l.split(' ',1)
                if k=='done':done.append(lo+int(v));continue
                i=passed[lo+int(k)];z,adds=meta[i];sites[z]['outputs']+=1;output.append(dict(z=z,additions=adds,core=jobs[i],profile=classify(jobs[i],json.loads(v))))
        assert done==list(range(len(passed))) and any(w['z']==5 and w['additions']==[(3,8),(6,20)] for w in output);out=dict(record=idx,sites=sites,totals={k:sum(c[k] for c in sites.values()) for k in ('pairs','cores','seven_pass','outputs')},outputs=output);out['core_candidates']=[dict(z=z,additions=adds,core=g,passes_seven=bool(t)) for (z,adds),g,t in zip(meta,jobs,tags)];print(out['totals'],flush=True);(D.parent/'ramsey_free_cross_profile.json').write_text(json.dumps(out,indent=1)+'\n')
if __name__=='__main__':run()
