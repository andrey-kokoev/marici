"""Compare exact partner scores against exact order-28 reachability."""
from pathlib import Path
from subprocess import run
from tempfile import TemporaryDirectory
from os import name
from ramsey_39_pattern_three_choices import Random,options,add
rng=Random(39);pairs=[];ind=[0];rows=[]
for n in range(22):
    p=rng.choice(options(n,pairs,ind));rows.append(p);pairs,ind=add(n,p,pairs,ind)
with TemporaryDirectory() as tmp:
    exe=Path(tmp)/('rank.exe' if name=='nt' else 'rank');run(['rustc','-O',str(Path(__file__).with_name('ramsey_39_pattern_order22.rs')),'-o',str(exe)],check=True)
    s=run([str(exe),'--scores'],input=' '.join(map(str,rows)),text=True,capture_output=True,check=True).stdout
records=[tuple(map(int,line.split())) for line in s.splitlines()];best=max(r[1] for r in records);print('leaders',[r for r in records if r[1]==best]);w=[s for _,s,v in records if v];f=[s for _,s,v in records if not v];print('ranges',min(w),max(w),min(f),max(f),'AUC',sum((a>b)+0.5*(a==b) for a in w for b in f)/(len(w)*len(f)))
old=rng.choice(options(22,pairs,ind));print('original',next(r for r in records if r[0]==old));print('best failed',max(f),'winners above',sum(x>max(f) for x in w))
