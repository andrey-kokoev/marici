"""Can the seven witnessed exterior rows already serve as seven blue ports? Enumerate all representatives."""
from itertools import combinations,product
from collections import Counter,defaultdict
from ramsey_retention_slice import CAT,D,decode
from pathlib import Path
import json,gzip,tempfile,subprocess


def pairings(xs):
    if not xs:yield ();return
    for y in xs[1:]:
        for p in pairings([z for z in xs[1:] if z!=y]):yield ((xs[0],y),)+p

def roots_and_lines():
    with gzip.open(CAT/'r38_27.g6.gz','rb') as f:data=f.read()
    with tempfile.TemporaryDirectory() as td:
        exe=Path(td)/'roots.exe';subprocess.run(['rustc','-O',str(Path(__file__).with_name('ramsey_matrix_predecessor_cube.rs')),'-o',str(exe)],check=True);p=subprocess.run([str(exe),'--seven'],input=data,capture_output=True,check=True);roots=[tuple(map(int,l.split())) for l in p.stderr.decode().splitlines()];assert len(roots)==161
    return roots,data.splitlines()

def audit():
    roots,lines=roots_and_lines();counts=Counter();best=Counter();frames=0;examples={}
    for idx,v in roots:
        a=decode(lines[idx-1].decode());ns=[i for i in range(27) if a[v]>>i&1];outside=defaultdict(list)
        for i in range(27):
            if i!=v and i not in ns:outside[frozenset(x for x in ns if a[i]>>x&1)].append(i)
        for six in combinations(ns,6):
            spare,=set(ns)-set(six)
            for pairs in pairings(list(six)):
                slots=[outside[frozenset(q)] for q in product(*pairs)];present=[i for i,ls in enumerate(slots) if ls];
                if len(present)!=7:continue
                frames+=1;cost=4
                for verts in product(*(slots[i] for i in present)):
                    red=[(i,j) for i,j in combinations(range(7),2) if a[verts[i]]>>verts[j]&1];assert red and all(present[i]^present[j]==7 for i,j in red);assert all(not(a[v]>>i&1 or a[spare]>>i&1) for i in verts);cost=min(cost,len(red));counts[len(red)]+=1;examples.setdefault(len(red),dict(record=idx,root=v,unused=spare,pairs=pairs,missing=next(i for i in range(8) if i not in present),representatives=dict(zip(present,verts)),red_pairs=[(verts[i],verts[j]) for i,j in red]))
                best[cost]+=1
    out=dict(roots=len(roots),frames=frames,representative_choices_by_internal_red=counts,frames_by_minimum_red=best,examples=examples);print(out);(D.parent/'ramsey_seven_role_coexist.json').write_text(json.dumps(out,indent=2)+'\n')
if __name__=='__main__':audit()
