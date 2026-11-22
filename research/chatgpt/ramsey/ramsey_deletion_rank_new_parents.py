"""Transfer frozen original-seven hit score to 34-cores of DIFFERENT densities. Delete 0 from a constructed cyclic 35, then add the lexicographically first jointly triangle-safe k-edge augmentation for each k=1..4, without reading completion outcomes. Evaluate every legal deletion, including undo moves labelled separately."""
from itertools import combinations
from collections import Counter
from ramsey_ports_saturated_core import graph,induce
from ramsey_fork_deletion_rank import evaluate,D,json,verify

def run():
    G=graph((1,7,11,16));H=induce(G,list(range(1,35)));free=[(a,b) for a,b in combinations(range(34),2) if not ((H[a]>>b)&1 or H[a]&H[b])];out=[]
    for k in range(1,len(free)+1):
        for adds in combinations(free,k):
            B=H[:]
            for a,b in adds:B[a]|=1<<b;B[b]|=1<<a
            if any(B[a]&B[b] for a,b in adds):continue
            verify(B,9);rows=evaluate(B)
            for r in rows:r['undo']=tuple(r['edge']) in adds
            out.append(dict(added=adds,rows=rows));print(k,Counter((r['prediction'],r['valid'],r['undo']) for r in rows),flush=True);break
        (D/'ramsey_deletion_rank_new_parents.json').write_text(json.dumps(out)+'\n')
    return out
if __name__=='__main__':run()
