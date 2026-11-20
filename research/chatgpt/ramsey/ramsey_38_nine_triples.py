"""Test all order-27 hosts for a fixed-point-free simultaneous rotation of nine triples."""
from ramsey_border_order import unpack
from pathlib import Path
from subprocess import run
from tempfile import TemporaryDirectory
from urllib.request import urlopen
import gzip,os,sys

def main():
    raw=Path(sys.argv[1]).read_bytes() if len(sys.argv)>1 else gzip.decompress(urlopen('https://users.cecs.anu.edu.au/~bdm/data/r38_27.g6.gz',timeout=30).read());assert len(raw.splitlines())==477142
    with TemporaryDirectory() as tmp:
        exe=Path(tmp)/('filter.exe' if os.name=='nt' else 'filter');run(['rustc','-O',str(Path(__file__).with_name('ramsey_38_triple_filter.rs')),'-o',str(exe)],check=True);res=run([str(exe)],input=raw,capture_output=True,check=True);print(res.stderr.decode().strip())
    lines=res.stdout.splitlines();print('pass neighbor-degree test',len(lines));count=0
    for line in lines:
        idx,s=line.split();g=unpack(s)
        p=next((a for a in g.get_automorphisms_vf2() if all(a[i]!=i and a[a[a[i]]]==i for i in range(27))),None)
        if p is None:continue
        if not count:
            T=[(i,p[i],p[p[i]]) for i in range(27) if i==min(i,p[i],p[p[i]])];print('record',idx,'graph6',s,'orbits',T)
            for j in range(9):print(j+1,[''.join(str(int(g.are_adjacent(T[i][0],v))) for v in T[j]) for i in range(j)])
            assert g.clique_number()==2 and g.independence_number()==7
        count+=1
    print('valid hosts with nine triples',count)
if __name__=='__main__':main()
