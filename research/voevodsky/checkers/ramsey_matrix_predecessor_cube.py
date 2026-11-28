"""Unrestricted column renaming makes the three directed pairs three unordered pairs for existence."""
from itertools import combinations,product,islice
import ast,gzip,json,subprocess,tempfile
from pathlib import Path
from ramsey_retention_slice import CAT,D,decode

def audit():
    x=json.loads((D.parent/'ramsey_matrix_successor_block.json').read_text());assert x['S']==[[int(all(a=='*' or a==b for a,b in zip(c,r))) for c in x['core_labels']] for r in x['port_roles']];cat=CAT/'r38_27.g6.gz'
    with tempfile.TemporaryDirectory() as td:
        exe=Path(td)/'cube.exe';subprocess.run(['rustc','-O',str(Path(__file__).with_suffix('.rs')),'-o',str(exe)],check=True);p=subprocess.run([str(exe)],input=gzip.open(cat,'rb').read(),capture_output=True,check=True);hist,ex=map(ast.literal_eval,p.stdout.decode().splitlines())
    idx,v,_,_=ex
    with gzip.open(cat,'rt') as f:a=decode(next(islice(f,idx-1,None)).strip())
    ns=[u for u in range(27) if a[v]>>u&1];supports={tuple(j for j in ns if a[u]>>j&1):u for u in range(27) if u!=v and u not in ns};best=0
    def partitions(seq):
        if not seq:yield [];return
        for y in seq[1:]:
            for t in partitions([z for z in seq[1:] if z!=y]):yield [(seq[0],y)]+t
    for six in combinations(ns,6):
        for pairs in partitions(six):
            bind={''.join(map(str,bits)):supports.get(tuple(sorted(p[b] for p,b in zip(pairs,bits)))) for bits in product(range(2),repeat=3)};n=sum(j is not None for j in bind.values())
            if n>best:best=n;example=dict(record=idx,root=v,pairs=pairs,exterior_vertices=bind)
    assert best==max(i for i,n in enumerate(hist) if n);out=dict(abstract_and_sheet_S_equal=True,root_count=sum(hist),hist_best_represented_roles=hist,example=example);print(out);(D.parent/'ramsey_matrix_predecessor_cube.json').write_text(json.dumps(out,indent=2)+'\n')
if __name__=='__main__':audit()
