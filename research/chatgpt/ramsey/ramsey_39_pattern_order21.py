"""Replay 21-prefix; compile search; check each witness border independently."""
from pathlib import Path
from subprocess import run
from tempfile import TemporaryDirectory
from os import name
from ramsey_39_pattern_three_choices import Random,options,add

def audit(target=29):
    rng=Random(39);pairs=[];ind=[0];rows=[]
    for n in range(21):
        p=rng.choice(options(n,pairs,ind));rows.append(p);pairs,ind=add(n,p,pairs,ind)
    with TemporaryDirectory() as tmp:
        exe=Path(tmp)/('audit.exe' if name=='nt' else 'audit')
        run(['rustc','-O',str(Path(__file__).with_suffix('.rs')),'-o',str(exe)],check=True)
        result=run([str(exe),str(target)],input=' '.join(map(str,rows)),text=True,capture_output=True,check=True)
    count,*path=map(int,result.stdout.split());assert count==len(options(21,pairs,ind));print(count,'borders;',len(path),'new addresses')
    for n,p in enumerate(path,21):
        assert p in options(n,pairs,ind);pairs,ind=add(n,p,pairs,ind);print(n+1,[i+1 for i in range(n) if p>>i&1])
    assert len(path) in (0,target-21)
if __name__=='__main__':
    import sys
    audit(int(sys.argv[1]) if len(sys.argv)>1 else 29)
