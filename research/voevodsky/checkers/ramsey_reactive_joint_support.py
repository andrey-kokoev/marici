"""Compare two terminal readouts on the same static shared-relation ensemble."""
from collections import Counter
from math import log2
from pathlib import Path
import json


def inspect(a,b,c):
    x=(int(bool(b))<<8)|(int(bool(c))<<9)|(b|c)
    y=(int(bool(a&126))<<7)|(int(bool(b&126))<<8)|(int(bool(c&126))<<9)|((a|b|c)&126)
    # Row 1 ignores incoming requests; column 1 ignores mirror requests.
    # A supported positive means two DISTINCT incident requesters at one responder.
    nr=max(b.bit_count(),c.bit_count())<2
    nb=not (126 & ((a&b)|(a&c)|(b&c)))
    return (x,y),nr,nb


def run():
    bins=Counter();joint=Counter()
    for a in range(128):
        for b in range(128):
            for c in range(128):
                k,r,s=inspect(a,b,c);bins[k,int(r or s)]+=1;joint[int(r),int(s)]+=1
    keys={k for k,z in bins};mixed=[k for k in keys if bins[k,0] and bins[k,1]];N=2**21
    loss=sum(n*log2((bins[k,0]+bins[k,1])/n) for (k,z),n in bins.items())/N
    A=inspect(0,2,4);B=inspect(0,6,4);assert A[0]==B[0] and A[1:]==(True,True) and B[1:]==(False,False)
    out=dict(realizations=N,footprint_pairs=len(keys),ambiguous_pairs=len(mixed),realizations_in_ambiguous_pairs=sum(bins[k,0]+bins[k,1] for k in mixed),best_joint_OR_loss_given_both_footprints=loss,example_counts_at_same_footprints=[bins[A[0],i] for i in (0,1)],condition_counts={str(k):v for k,v in joint.items()},scope='Joint support alternative, not an operator-defined condition. Uniform labeled shared relation.');print(out);(Path(__file__).resolve().parents[1]/'results/ramsey_reactive_joint_support.json').write_text(json.dumps(out,indent=2)+'\n')

if __name__=='__main__':run()
