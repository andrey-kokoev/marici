"""Keep the first 24 of the verified order-29 path; test order 29 then 30."""
from pathlib import Path
from subprocess import run
from tempfile import TemporaryDirectory
from os import name
from ramsey_39_pattern_three_choices import Random,options,add

def audit(prefix=24):
    assert 21<=prefix<=24
    rng=Random(39);pairs=[];ind=[0];rows=[]
    for n in range(prefix):
        opts=options(n,pairs,ind)
        p=rng.choice(opts) if n<21 else sum(1<<(v-1) for v in ((1,4,6,8,13,19),(1,7,8,11,13,18),(7,9,10,16,18,20,22))[n-21]);assert p in opts
        rows.append(p);pairs,ind=add(n,p,pairs,ind)
    with TemporaryDirectory() as tmp:
        exe=Path(tmp)/('audit.exe' if name=='nt' else 'audit')
        run(['rustc','-O',str(Path(__file__).with_name('ramsey_39_pattern_order21.rs')),'-o',str(exe)],check=True)
        for target in (29,30):
            res=run([str(exe),str(target)],input=' '.join(map(str,rows)),text=True,capture_output=True,check=True)
            count,*path=map(int,res.stdout.split());assert count==len(options(prefix,pairs,ind));print('borders',count,'target',target,'witness',path);assert len(path) in (0,target-prefix)
            if target==29:assert path
            ps,ii=pairs,ind
            for n,p in enumerate(path,prefix):assert p in options(n,ps,ii);ps,ii=add(n,p,ps,ii)
if __name__=='__main__':
    import sys
    audit(int(sys.argv[1]) if len(sys.argv)>1 else 24)
