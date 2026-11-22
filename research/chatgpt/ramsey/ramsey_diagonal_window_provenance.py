"""Read every native event of the apex passage against the actual three-duad overlap window. Distinguish visiting a block once per event from expanding both members of one duad. No use of cube colors."""
from ramsey_oriented_overlap_reader import cycle,m,r,orient,X,P,D,json
from ramsey_handoff_distance_audit import run as tours
from itertools import permutations,product

def run():
    ds=cycle(m)[::2];out=[]
    for p in permutations('ABCD'):
        if set(p[::3])!={'A','B'}:continue
        pair=[]
        for d in (ds,[r[i] for i in ds]):
            a,b=orient(d,X)[-1]['arrow'];tail,head=p[a-1],p[b-1];win=d[-1:]+d[:2];blocks=[{frozenset(p[v-1] for v in X[k]) for k in P[j]} for j in win];lifts=[]
            for t in tours():
                w=t['word'];i,=[i for i,e in enumerate(w) if e[0]==tail];w=w[i:]+w[:i];j,=[j for j,e in enumerate(w) if e[1]==head];arc=w[:j+1];slots=[[k for k,s in enumerate(blocks) if frozenset(e) in s] for e in arc]
                for seq in product(*slots):
                    if tuple(sorted(seq))==seq:lifts.append(dict(path=arc,slots=seq,seam=t['seam']))
            assert len(lifts)==1;pair.append(lifts[0])
        assert {v['slots'] for v in pair}=={(0,2),(1,1)};out.append(dict(binding=''.join(p),rows=pair))
    return out
if __name__=='__main__':
    out=run();print(out);(D/'ramsey_diagonal_window_provenance.json').write_text(json.dumps(out)+'\n')
