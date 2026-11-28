"""Compare six joint supports on the same deletions with the frozen four-port prefixes."""
from ramsey_retention_slice import CAT,D,decode,check
import json,ast,gzip,subprocess,tempfile
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

def audit():
    p=json.loads((D.parent/'ramsey_patch_edge27.json').read_text());ids={r['row'] for r in p};graphs={i:s.decode().strip() for i,s in enumerate(gzip.open(CAT/'r38_27.g6.gz','rb')) if i in ids|{42702}};cases=[];control=[]
    with tempfile.TemporaryDirectory() as td:
        exe=Path(td)/'six.exe';subprocess.run(['rustc','-O',str(Path(__file__).with_suffix('.rs')),'-o',str(exe)],check=True)
        def run(item):
            i,s=item;res=subprocess.run([str(exe)],input=f'{i} {s}',text=True,capture_output=True,check=True);ls=res.stdout.splitlines();assert len(ls)==27;return ls
        with ThreadPoolExecutor(8) as pool:
            for ls in pool.map(run,graphs.items()):
                for l in ls:
                    i,z,ss=l.split(' ',2);rs=ast.literal_eval(ss);i,z=int(i),int(z)
                    if not rs:continue
                    a=decode(graphs[i]);assert len(rs)==6;g=a[:]+[0]*7
                    for j,s in enumerate(rs,27):
                        assert not s>>z&1;g[j]=s|(1<<33);g[-1]|=1<<j
                        for u in range(27):g[u]|=int(bool(s>>u&1))<<j
                    assert check(g,((1<<34)-1)^(1<<z),3,9);(control if i==42702 else cases).append(dict(record=i,deleted=z,rows=rs))
    assert 42702 not in ids and {3,10,20,23}<={r['deleted'] for r in control}
    out=dict(control42702=control,records=len(ids),deletions=27*len(ids),positive=len(cases),positive_records=len({r['record'] for r in cases}),witnesses=cases);print({k:v for k,v in out.items() if k not in ('witnesses','control42702')},cases[:1]);(D.parent/'ramsey_deleted27_six_joint.json').write_text(json.dumps(out,indent=2)+'\n')
if __name__=='__main__':audit()
