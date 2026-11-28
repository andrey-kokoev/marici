from ramsey_row_cut_tests import D,CAT,gzip,islice,decode,json,combinations,sets,subprocess,tempfile,Path

def run():
    T=D.parent;src=json.loads((T/'ramsey_six_hit_screen.json').read_text());zwin,core,_=src['run']['outputs'][0]
    with gzip.open(CAT/'r38_27.g6.gz','rt') as f:b=decode(next(islice(f,448077,None)).strip())
    src7=sets(b,7);out=[]
    with tempfile.TemporaryDirectory() as td:
        exe=Path(td)/'joint.exe';subprocess.run(['rustc','-O',str(Path(__file__).with_suffix('.rs')),'-o',str(exe)],check=True)
        for r in src['baseline_prefixes']:
            if r['failed_probe']:continue
            z=r['z'];vs=[j for j in range(27) if j!=z];adds=r['additions'];g=r['core'];six=sets(g,6);seven=sets(g,7);ss=set(six);probes=[q for s in src7 if s>>z&1 and (q:=sum((s>>v&1)<<j for j,v in enumerate(vs))) in ss];fixed=g[:]
            for i,j in combinations(range(26),2):
                if g[i]>>j&1 and [i,j] not in adds and not any(not q&(g[i]|g[j]) for q in six):fixed[i]^=1<<j;fixed[j]^=1<<i
            rows=sets(fixed,7);ls=subprocess.run([str(exe)],input='\n'.join(' '.join(map(str,v)) for v in [rows,seven,probes]),text=True,capture_output=True,check=True).stdout.splitlines();n,early,total,individual,pairs=map(int,ls[-1].split());labels=lambda q:[v for j,v in enumerate(vs) if q>>j&1];res=dict(z=z,additions=[[vs[i],vs[j]] for i,j in adds],cores_probed=total,packs_visited=n,all_pairs_witnessed=bool(early),individually_feasible=individual,joint_failures=pairs);print(res,flush=True)
            if pairs:
                x,y=map(int,ls[0].split());w=[]
                for q,line in zip([x,y],ls[1:3]):
                    rr=[rows[i] for i in json.loads(line)];assert len(set(rr))==8 and sum(not q&s for s in rr)<=2 and all(sum(not d&s for s in rr)<=1 for d in seven);w.append(list(map(labels,rr)))
                res['certificate']=dict(sixes=list(map(labels,[x,y])),individual_families=w);assert not early
            out.append(res)
    (T/'ramsey_joint_six_demands.json').write_text(json.dumps(out,indent=1)+'\n')
if __name__=='__main__':run()
