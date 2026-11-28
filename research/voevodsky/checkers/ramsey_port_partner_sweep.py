"""Fix deletion 5; keep at least one of the two known additions, but free its crossing partner and every old cut. All triangles after both additions are considered, including those using both new links."""
from ramsey_port_descendants import descendants,D,CAT,decode,gzip,islice,json,induced,combinations,check,classify,subprocess,tempfile,Path
from concurrent.futures import ThreadPoolExecutor
from collections import Counter

def covers(triangles):
    ps={frozenset()}
    for t in triangles:
        ns={p|{e} for p in ps for e in t};ps={p for p in ns if not any(q<p for q in ns)}
    return ps

def run():
    idx=448077;z=5
    with gzip.open(CAT/'r38_27.g6.gz','rt') as f:a=decode(next(islice(f,idx,None)).strip())
    vs=[i for i in range(27) if i!=z];h=induced(a,vs);active=(1<<26)-1;cross=[(i,j) for i,j in combinations(range(26),2) if not h[i]>>j&1 and (a[z]>>vs[i]^a[z]>>vs[j])&1];anchors={(vs.index(i),vs.index(j)) for i,j in ((3,8),(6,20))};cases=[];jobs=[];owner=[]
    def orig(es):return [(vs[u],vs[v]) for u,v in sorted(es)]
    for e,f in combinations(cross,2):
        adds={e,f}
        if not adds&anchors:continue
        b=h[:];
        for i,j in adds:b[i]|=1<<j;b[j]|=1<<i
        tri=[{(i,j),(j,k),(i,k)}-adds for i,j,k in combinations(range(26),3) if (b[i]>>j)&(b[i]>>k)&(b[j]>>k)&1];unique={};roots=0
        for p in covers(tri):
            c=b[:]
            for i,j in p:c[i]^=1<<j;c[j]^=1<<i
            if not check(c,active,3,8):continue
            roots+=1
            for g,rm in descendants(c,adds):unique[tuple(g)]=orig(p|set(rm))
        tag=len(cases);cases.append(dict(additions=orig(adds),legal_prefixes=roots,cores=len(unique),screen=0,families=0));
        for g,rm in unique.items():jobs.append(g);owner.append((tag,rm))
    print('pairs',len(cases),'cores',len(jobs),flush=True)
    with tempfile.TemporaryDirectory() as td:
        def execute(stem,graphs,chunk):
            exe=Path(td)/(stem+'.exe');subprocess.run(['rustc','--edition=2021','-O',str(Path(__file__).with_name(stem+'.rs')),'-o',str(exe)],check=True)
            def work(lo):return lo,subprocess.run([str(exe)],input='\n'.join(' '.join(map(str,g)) for g in graphs[lo:lo+chunk]),text=True,capture_output=True,check=True).stdout.splitlines()
            with ThreadPoolExecutor(6) as ex:return list(ex.map(work,range(0,len(graphs),chunk)))
        tags=[int(s) for lo,lines in execute('ramsey_port_seven_screen',jobs,80) for s in lines];assert len(tags)==len(jobs);passed=[i for i,t in enumerate(tags) if t];print('passed',len(passed),flush=True);done=[];witnesses=[]
        for i in passed:cases[owner[i][0]]['screen']+=1
        for lo,lines in execute('ramsey_free_port_census',[jobs[i] for i in passed],2):
            for l in lines:
                k,v=l.split(' ',1)
                if k=='done':done.append(lo+int(v));continue
                i=passed[lo+int(k)];tag,rm=owner[i];c=cases[tag];c['families']+=1;witnesses.append(dict(additions=c['additions'],cuts=rm,output=classify(list(jobs[i]),json.loads(v))))
        assert done==list(range(len(passed))) and any(set(map(tuple,w['additions']))==set(orig(anchors)) for w in witnesses)
    counts={k:sum(c[k] for c in cases) for k in ('cores','screen','families','legal_prefixes')};print(counts,'positive pairs',sum(bool(c['families']) for c in cases),'pairs with legal starts',sum(bool(c['cores']) for c in cases));(D.parent/'ramsey_port_partner_sweep.json').write_text(json.dumps(dict(record=idx,deleted=z,core_labels=vs,counts=counts,cases=cases,witnesses=witnesses),indent=1)+'\n')
if __name__=='__main__':run()
