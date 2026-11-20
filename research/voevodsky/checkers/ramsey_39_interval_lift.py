"""Reverse construction. Input: the 13-circle with plus distances 1,5, an interval embedding with any constant invertible stride on that core, and host order 35. Enumerate residual host distances; compare the generated passing models to the old host only afterwards."""
from itertools import combinations
from pathlib import Path
import json
D=Path(__file__).resolve().parents[1]/'results'
def run():
 n=35;out=[];passing=[]
 for a in range(1,7): # core circular index of the next interval position, up to sign
    forced={d for d in range(1,13) if a*d%13 in (1,5,8,12)};tri_free=legal=0
    for m in range(32):
        ds=forced|{13+i for i in range(5) if m>>i&1};S=ds|{n-d for d in ds};
        if any((b-c)%n in S for b,c in combinations(S,2)):continue
        tri_free+=1
        def ind(av,k):
            if k==0:return True
            while av.bit_count()>=k:
                b=av&-av;av^=b;i=b.bit_length()-1
                if ind(av&~N[i],k-1):return True
            return False
        N=[sum(1<<((i+d)%n) for d in S) for i in range(n)];
        if ind((1<<n)-1,9):continue
        legal+=1;passing.append(sorted(ds))
    out.append(dict(stride=a,forced=sorted(forced),triangle_free=tri_free,legal=legal))
 base=set(json.loads((D/'ramsey_39_glue_vs_circle.json').read_text())['circle_distances']);d=4;S=base|{35-i for i in base};basecore={v for v in range(n) if all((v-i*d)%35 not in S|{0} for i in range(4))};assert basecore=={i*d%35 for i in range(13,26)};assert sorted(i for i in range(1,18) if i*d%35 in S) in passing
 res=dict(trials=6*32,by_stride=out,passing=passing,interval_positions=list(range(13,26)),wrap_shift=(-35)%13);print(res);(D/'ramsey_39_interval_lift.json').write_text(json.dumps(res,indent=2)+'\n')
if __name__=='__main__':run()
