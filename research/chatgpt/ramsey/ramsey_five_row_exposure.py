"""Source-only filter for dangerous fives: maximal, or singly extendible by a vertex with >=2 spare port slots. Separately test maximal fives alone and rows equal to a vertex neighbourhood (not logically exhaustive). Count distinct bad assignments and record *all* their witnesses."""
from ramsey_capacity_transfer_78 import check,inds,bits,decode,D,json,Counter

def audit(H):
    fives=[s for s in inds(H) if s.bit_count()==5];F=(1<<22)-1;groups={};degrees=list(map(int.bit_count,H))
    for s in fives:
        blocked=s
        for v in bits(s):blocked|=H[v]
        ext=list(bits(F^blocked));g='maximal' if not ext else 'one_spare' if len(ext)==1 and degrees[ext[0]]<=5 else 'safe';groups[s]=g
    out=Counter();bad=[]
    def obs(S,tag):
        if tag=='valid':out['valid']+=1;return
        W=[s for s in fives if sum(not(t&s) for t in S)>=3];assert W and all(groups[s]!='safe' for s in W);bad.append(dict(witnesses=W,kinds=[groups[s] for s in W],neighbourhoods=[s for s in W if s in H]));out['bad']+=1;out['maximal_catches']+=any(groups[s]=='maximal' for s in W);out['one_spare_catches']+=any(groups[s]=='one_spare' for s in W);out['neighbourhood_catches']+=any(s in H for s in W)
    check(H,obs);return dict(pools=Counter(groups.values()),assignments=out,bad=bad)
if __name__=='__main__':
    rows=[audit(decode(l)) for l in (D/'pauli-realization-catalogues/r37_22.g6').read_bytes().splitlines()];print(sum((r['pools'] for r in rows),Counter()),sum((r['assignments'] for r in rows),Counter()));print([(i+1,r['bad'][0]) for i,r in enumerate(rows) if r['bad']]);(D/'ramsey_five_row_exposure.json').write_text(json.dumps(rows)+'\n')
