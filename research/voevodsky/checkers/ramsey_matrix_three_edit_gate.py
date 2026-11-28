"""Three-removal gate: enumerate possible face sextets and their exact loss budgets."""
from ramsey_retention_slice import CAT,D,decode,has
from itertools import combinations
from collections import Counter
import json,gzip


def audit():
    S=json.loads((D.parent/'ramsey_matrix_successor_block.json').read_text())['S'];goal=sorted(8-sum(c) for c in zip(*S));stats=Counter();ex={};weights=bytes([(i-63).bit_count() if 63<=i<=126 else 0 for i in range(256)])
    for idx,line in enumerate(gzip.open(CAT/'r38_27.g6.gz','rb'),1):
        s=line.rstrip();ec=sum(s[1:].translate(weights));
        if ec not in (85,86):continue
        adj=decode(s.decode())
        for z,mask in enumerate(adj):
            if ec-mask.bit_count()!=79:continue
            stats['deletions']+=1;vs=[i for i in range(27) if i!=z];d={i:(adj[i]&~(1<<z)).bit_count() for i in vs};pool=sorted(vs,key=d.get);es=[(i,j) for i,j in combinations(vs,2) if adj[i]>>j&1];assert len(es)==79
            if any(d[i]<4 for i in vs) or sum(v==7 for v in d.values())<8:continue
            def sextets(start,left,budget,pre):
                if left==0:yield frozenset(pre);return
                for j in range(start,len(pool)-left+1):
                    i=pool[j];cost=d[i]-4
                    if left*cost>budget:break
                    yield from sextets(j+1,left-1,budget-cost,pre+[i])
            for F in sextets(0,6,6,[]):
                if any(d[i]<6 for i in vs if i not in F):continue
                loss=sum(d[i]-4 for i in F);internal=[e for e in es if set(e)<=F];assert loss>=5
                # At most one of six decrements can be outside F. Thus 2 or 3 removed edges must lie inside F.
                n=loss-3;cross=[e for e in es if len(F.intersection(e))==1] if n<3 else []
                for ins in combinations(internal,n):
                    for rem in combinations(cross,3-n):
                        edits=ins+rem;ends=Counter(i for e in edits for i in e)
                        if any(d[i]-ends[i]!=4 for i in F) or sorted(d[i]-ends[i] for i in vs)!=goal:continue
                        stats['degree_pass']+=1;sample=dict(parent=idx,deleted=z,edits=edits,faces=sorted(F));ex.setdefault('degree',sample);remaining=set(internal)-set(ins)
                        match=all(sum(i in e for e in remaining)<=1 for i in F)
                        if match:stats['face_matching_pass']+=1;ex.setdefault('matching',sample)
                        a=adj[:]
                        for i,j in edits:a[i]^=1<<j;a[j]^=1<<i
                        if has([~v for v in a],((1<<27)-1)^(1<<z),8):
                            stats['blue_eight']+=1
                            if 'first_blue_eight' not in ex:ex['first_blue_eight']=next(q for q in combinations(vs,8) if all(not (a[i]>>j&1) for i,j in combinations(q,2)))
                            continue
                        stats['no_core_blue_eight']+=1;ex.setdefault('blue',sample)
    print(stats,ex);(D.parent/'ramsey_matrix_three_edit_gate.json').write_text(json.dumps(dict(counts=stats,examples=ex),indent=2)+'\n')
if __name__=='__main__':audit()
