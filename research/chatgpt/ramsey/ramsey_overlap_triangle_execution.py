"""Close head and tail rim arcs using supplied native arrows. Distinguish fixed binding and orientation from reorienting arcs and choosing a common sewing base."""
from ramsey_oriented_overlap_reader import orient,cycle,m,P,X,r,D,json
from itertools import permutations
from pathlib import Path
import sys
sys.path.insert(0,str(D.parents[1]/'nima/checkers'))
from check_seed_typed_execution import execute,validate,registry,normalize,sew_at

def run():
    ds=cycle(m)[::2];out=[]
    for perm in permutations('ABCD'):
        label=lambda i:perm[i-1];
        if {label(1),label(4)}!={'A','B'}:continue
        rows=[]
        for d in (ds,[r[i] for i in ds]):
            w=[(label(a),label(b)) for a,b in (s['arrow'] for s in orient(d,X))];tail,head=w[-1];cycles=[];direct=[]
            for apex in (tail,head):
                a,= [a for a,b in w[:4] if b==apex];b,=[b for a,b in w[:4] if a==apex];tri=[a+apex,apex+b,b+a];ok=all(e in registry for e in tri);direct.append(ok);tri=tri if ok else [e[::-1] for e in tri[::-1]];assert all(e in registry for e in tri);cycles.append(tri)
            assert direct[0]==direct[1];receipts=[]
            for base in map(label,(1,4)):
                parts=[]
                for tri in cycles:
                    k,=[j for j,e in enumerate(tri) if e[0]==base];parts+=tri[k:]+tri[:k]
                path=validate(execute(parts));assert len(path)==6 and set(parts)==set(registry) and normalize(tuple(parts)) in sew_at(base);receipts.append(dict(base=base,word=parts,mark_bit=int(base==label(1))))
            rows.append(dict(raw_admitted=direct[0],apex_order=[tail,head],receipts=receipts))
        assert rows[0]['raw_admitted']!=rows[1]['raw_admitted'];out.append(dict(binding=''.join(perm),rows=rows))
    return out
if __name__=='__main__':
    out=run();print(out);(D/'ramsey_overlap_triangle_execution.json').write_text(json.dumps(out)+'\n')
