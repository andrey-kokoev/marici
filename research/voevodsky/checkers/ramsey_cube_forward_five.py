"""Independent forward test of the degree-six branch. Compare with all cube roots via verified isomorphisms."""
from ramsey_cube_retention_floor import G,induced,iso,D,CAT,decode,json,Counter
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from math import comb
import subprocess,tempfile,gzip

def audit():
    W=[i for i in range(34) if not G[34]>>i&1];target=induced(G,W);assert Counter(x.bit_count() for x in target)=={4:6,6:12,7:8};assert all(iso(target,induced(G,[i for i in range(35) if i!=r and not G[r]>>i&1])) is not None for r in range(35));jobs=[];w=bytes([(j-63).bit_count() if 63<=j<=126 else 0 for j in range(256)])
    for idx,l in enumerate(gzip.open(CAT/'r38_27.g6.gz','rb')):
        s=l.strip();e=sum(s[1:].translate(w));assert e>=85
        if e!=85:continue
        a=decode(s.decode());
        for z,n in enumerate(a):
            if n.bit_count()==6:
                V=[j for j in range(27) if j!=z];jobs.append((idx,z,V,induced(a,V)))
    assert len({j[0] for j in jobs})==4;recs=[];wins=[]
    with tempfile.TemporaryDirectory() as td:
        exe=Path(td)/'five.exe';subprocess.run(['rustc','--edition=2021','-O',str(Path(__file__).with_suffix('.rs')),'-o',str(exe)],check=True)
        def run(job):
            idx,z,V,a=job;p=subprocess.run([str(exe)],input=' '.join(map(str,a+target)),capture_output=True,text=True,check=True);ct,gs=map(json.loads,p.stdout.split('|'));assert ct[0]==comb(79,4) and ct[-1]==len(gs);success=[]
            for g in gs:
                f=iso(g,target)
                if f is not None:success.append(dict(record=idx,deleted=z,old_vertices=V,root=34,target_vertices=[W[i] for i in f],remove=[(V[i],V[j]) for i in range(26) for j in range(i) if (a[i]&~g[i])>>j&1],add=[(V[i],V[j]) for i in range(26) for j in range(i) if (g[i]&~a[i])>>j&1]))
            return dict(record=idx,deleted=z,counts=ct),success
        with ThreadPoolExecutor(8) as pool:
            for rec,ws in pool.map(run,jobs):recs.append(rec);wins.extend(ws)
    sums=list(map(sum,zip(*(r['counts'] for r in recs))));out=dict(stages=['four_removals','histogram_extendible','exact_degree_after_old_blue_addition','triangle_free','neighbor_degree_match'],totals=sums,deletions=recs,matches=wins);print('deletions',len(jobs),'totals',sums,'matches',len(wins));(D.parent/'ramsey_cube_forward_five.json').write_text(json.dumps(out,indent=2)+'\n')
if __name__=='__main__':audit()
