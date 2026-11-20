"""Exact breadth-first layers up to supplied radius, modulo matrix relabeling."""
import sys,gzip,os
from tempfile import TemporaryDirectory
from urllib.request import urlopen
from pathlib import Path
from subprocess import run
from ramsey_border_order import unpack

def canon(g):
    h=g.permute_vertices(g.canonical_permutation());return tuple(sorted(tuple(sorted(e)) for e in h.get_edgelist()))
def encode(edges):
    bits=[0]*59
    for i,j in edges:
        z=j*(j-1)//2+i;bits[z//6]|=1<<(5-z%6)
    return bytes([90]+[63+x for x in bits])

def bfs(record,depth):
    raw=gzip.decompress(urlopen('https://users.cecs.anu.edu.au/~bdm/data/r38_27.g6.gz',timeout=30).read()).splitlines();start=encode(canon(unpack(raw[record-1])));del raw
    front=[start];seen=set(front);print(0,1,1,flush=True)
    with TemporaryDirectory() as tmp:
        exe=Path(tmp)/('neighbors.exe' if os.name=='nt' else 'neighbors');run(['rustc','-O',str(Path(__file__).with_name('ramsey_38_replacement_neighbors.rs')),'-o',str(exe)],check=True)
        for d in range(1,depth+1):
            todo=[]
            for lo in range(0,len(front),512):
                batch=front[lo:lo+512];ans=run([str(exe)],input=b'\n'.join(batch)+b'\n',capture_output=True,check=True).stdout.splitlines();assert len(ans)==len(batch)
                for parent,moves in zip(batch,ans):
                    g=unpack(parent)
                    for move in moves.split():
                        v,p=map(int,move.split(b':'));h=g.copy();h.delete_edges(h.incident(v));h.add_edges([(i,v) for i in range(27) if p>>i&1]);key=encode(canon(h))
                        if key not in seen:seen.add(key);todo.append(key)
            front=todo;print(d,len(front),len(seen),flush=True)
            if not front:break
if __name__=='__main__':bfs(int(sys.argv[1]),int(sys.argv[2]))
