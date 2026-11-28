"""Same reduced cores, remove the retention constraint; check both six and seven ports."""
from ramsey_retention_slice import D,CAT,check,decode
from concurrent.futures import ThreadPoolExecutor
from itertools import product
from pathlib import Path
import ast,json,gzip,tempfile,subprocess

def audit():
    prev=json.loads((D.parent/'ramsey_delete_one_grow_two.json').read_text());ids=set(prev['records']);graphs={i:l.strip() for i,l in enumerate(gzip.open(CAT/'r38_27.g6.gz','rt')) if i in ids};assert graphs.keys()==ids
    results={6:{},7:{}}
    with tempfile.TemporaryDirectory() as td:
        exe=Path(td)/'joint.exe';subprocess.run(['rustc','-O',str(Path(__file__).with_name('ramsey_deleted27_six_joint.rs')),'-o',str(exe)],check=True)
        def scan(args):
            i,k=args;a=decode(graphs[i]);res=subprocess.run([str(exe),str(k)],input=f'{i} {graphs[i]}',capture_output=True,text=True,check=True);seen=set();yes={}
            for l in res.stdout.splitlines():
                j,z,x=l.split(' ',2);z=int(z);assert int(j)==i and z not in seen;seen.add(z);rows=ast.literal_eval(x)
                if not rows:continue
                assert len(rows)==k and all(not (s>>z&1) for s in rows);root=27+k;g=a[:]+[0]*(k+1)
                for v,s in enumerate(rows,27):
                    g[root]|=1<<v;g[v]=s|(1<<root)
                    for h in range(27):g[h]|=int(bool(s>>h&1))<<v
                assert check(g,((1<<(root+1))-1)^(1<<z),3,9);yes[z]=rows
            assert seen==set(range(27));return i,k,yes
        with ThreadPoolExecutor(8) as pool:
            for i,k,yes in pool.map(scan,product(sorted(ids),(6,7))):results[k][i]=yes
    assert set(results[6][42702])=={3,10,20,23} and all(results[7][i].keys()<=results[6][i].keys() for i in ids);counts={k:sum(map(len,ds.values())) for k,ds in results.items()};sources={k:sum(map(bool,ds.values())) for k,ds in results.items()};out=dict(record_deletions=27*len(ids),positive_deletions=counts,positive_records=sources,witnesses=results);print(out['record_deletions'],counts,sources);(D.parent/'ramsey_deleted27_seven_control.json').write_text(json.dumps(out,indent=2)+'\n')
if __name__=='__main__':audit()
