"""Run the (3,6) falsification test in increasing order. Needs igraph and rustc."""
from ramsey_border_order import unpack
from pathlib import Path
from tempfile import TemporaryDirectory
from subprocess import run
from urllib.request import urlopen
from functools import cache
import gzip,os

def data(n):
    compressed=11<=n<=16
    d=urlopen(f'https://users.cecs.anu.edu.au/~bdm/data/r36_{n}.g6'+('.gz' if compressed else ''),timeout=25).read()
    return gzip.decompress(d) if compressed else d

def main():
    hosts=list(map(unpack,data(17).splitlines()))
    @cache
    def allowed(g):return tuple(i+1 for i,h in enumerate(hosts) if h.subisomorphic_lad(unpack(g),induced=True))
    with TemporaryDirectory() as tmp:
        exe=Path(tmp)/('deck.exe' if os.name=='nt' else 'deck');run(['rustc','-O',str(Path(__file__).with_name('ramsey_36_deck_collision.rs')),'-o',str(exe)],check=True)
        for n in range(1,18):
            d=data(n);pairs=run([str(exe)],input=d,capture_output=True,check=True).stdout.splitlines();print(n,len(d.splitlines()),len(pairs),flush=True)
            for row in pairs:
                a,b=row.split()
                if bool(allowed(a))!=bool(allowed(b)):
                    def signature(g):
                        sets=[0]
                        for i,ns in enumerate(unpack(g).get_adjlist()):
                            adj=sum(1<<j for j in ns);sets += [s|1<<i for s in sets if not s&adj]
                        def poly(v):return tuple(sum(not(s&v) and s.bit_count()==k for s in sets) for k in range(6))
                        return poly(0),sorted(poly(1<<i) for i in range(n))
                    assert signature(a)==signature(b)
                    print('common polynomial coefficients:',signature(a)[0]);
                    for g in (a,b):print(g,allowed(g),unpack(g).get_edgelist())
                    return
if __name__=='__main__':main()
