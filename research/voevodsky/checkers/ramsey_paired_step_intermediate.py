"""Largest one-sided (4,5) or (5,4) intermediate in a saved (5,5) endpoint containing a designated seed. Mark each exterior subset containing the exterior portion of a monochromatic four-clique."""
from itertools import combinations
import json
from pathlib import Path
D=Path(__file__).resolve().parents[1]/'results'
def run(a,seed):
    n=len(a);ext={j:i for i,j in enumerate(v for v in range(n) if seed>>v&1==0)};full=(1<<len(ext))-1;out=[]
    for red in (True,False):
        bad=bytearray(full+1)
        for q in combinations(range(n),4):
            if all(bool(a[i]>>j&1)==red for i,j in combinations(q,2)):bad[sum(1<<ext[i] for i in q if i in ext)]=1
        assert not bad[0]
        for j in range(len(ext)):
            b=1<<j
            for start in range(b,full+1,2*b):
                for p in range(start,start+b):bad[p]|=bad[p^b]
        best=max((p for p in range(full+1) if not bad[p]),key=int.bit_count);out.append(dict(red=red,size=seed.bit_count()+best.bit_count(),mask=seed|sum(1<<i for i,j in ext.items() if best>>j&1)))
    return out
if __name__=='__main__':
    import sys
    from ramsey_retention_slice import check
    a=json.loads((D/'ramsey_paired_step_sat_35_g4_1.json').read_text())['red_masks'];assert check(a,(1<<35)-1,5,5);out=[]
    # Masks printed by running the induced-seed scan with --all on this graph.
    for seed in [131071,12882846480,17177813264]:
        assert seed.bit_count()==17 and check(a,seed,4,4);out.append(dict(seed=seed,best=run(a,seed)))
    print(out);(D/'ramsey_paired_step_sat35_intermediate.json').write_text(json.dumps(out,indent=1)+'\n')
