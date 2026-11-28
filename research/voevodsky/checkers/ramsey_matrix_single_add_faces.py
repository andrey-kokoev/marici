"""Census of individually coverable face sites under ONE COMMON permanently added edge."""
import gzip,json,subprocess,tempfile
from pathlib import Path
from ramsey_retention_slice import CAT,D,decode,has
from itertools import combinations

def audit():
    w=bytes([(i-63).bit_count() if 63<=i<=126 else 0 for i in range(256)]);data=[]
    with gzip.open(CAT/'r38_27.g6.gz','rb') as f:
        for i,l in enumerate(f,1):
            s=l.rstrip()
            if 85<=sum(s[1:].translate(w))<=87:data.append(f'{i} {s.decode()}')
    a=decode(next(row.split()[1] for row in data if row.startswith('110 ')));a[4]|=1<<10;a[10]|=1<<4;p=((1<<27)-1)^(1<<7);forced=set()
    for i in [5,6,8,18,24,26]:
        ns=[j for j in range(27) if a[i]&p&(1<<j)];ks=[k for k in combinations(ns,4) if not has([~v for v in a],p&~(1<<i)&~sum(1<<j for j in k),7)];assert len(ks)==1;forced.update(tuple(sorted((i,j))) for j in set(ns)-set(ks[0]))
    assert len(forced)==6
    with tempfile.TemporaryDirectory() as td:
        exe=Path(td)/'faces.exe';subprocess.run(['rustc','-O',str(Path(__file__).with_suffix('.rs')),'-o',str(exe)],check=True);p=subprocess.run([str(exe)],input='\n'.join(data),text=True,capture_output=True,check=True)
    ds,*h=[list(map(int,row.split())) for row in p.stdout.splitlines()];assert ds[0]==20030 and sum(c for _,_,c in h)==245*ds[0];out=dict(deletions=ds[0],deletions_with_passing_addition=ds[1],edge_trials=245*ds[0],passing_additions=sum(c for a,b,c in h if b>=6),raised_through_six=sum(c for a,b,c in h if a<6<=b),hist_columns=['before','after','count'],hist=h,example=p.stderr.strip(),example_forced_removals=sorted(forced));print({k:v for k,v in out.items() if k!='hist'});(D.parent/'ramsey_matrix_single_add_faces.json').write_text(json.dumps(out,indent=2)+'\n')
if __name__=='__main__':audit()
