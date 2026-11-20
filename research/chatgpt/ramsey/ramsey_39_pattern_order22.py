"""Replay the prefix, run the exhaustive Rust search and check its example independently."""
from pathlib import Path
from subprocess import run
from tempfile import TemporaryDirectory
from os import name
from ramsey_39_pattern_three_choices import Random,options,add

def audit(target=28):
    assert target in (28,29)
    rng=Random(39);pairs=[];ind=[0];rows=[]
    for n in range(22):
        p=rng.choice(options(n,pairs,ind));rows.append(p);pairs,ind=add(n,p,pairs,ind)
    with TemporaryDirectory() as tmp:
        exe=Path(tmp)/('audit.exe' if name=='nt' else 'audit')
        run(['rustc','-O',str(Path(__file__).with_suffix('.rs')),'-o',str(exe)],check=True)
        result=run([str(exe)]+(['--29'] if target==29 else []),input=' '.join(map(str,rows)),text=True,capture_output=True,check=True)
    count,*example=map(int,result.stdout.split());print('first borders reaching',target,':',count,'of',len(options(22,pairs,ind)))
    for n,p in enumerate(example,22):
        assert p in options(n,pairs,ind);pairs,ind=add(n,p,pairs,ind);print(n+1,[i+1 for i in range(n) if p>>i&1])
    assert not count or len(example)==target-22
if __name__=='__main__':
    import sys
    audit(int(sys.argv[1]) if len(sys.argv)>1 else 28)
