"""Exact conditional prediction benchmark on a static 3-by-7 relational carrier.
A marked row/column is neutral as a RESPONDER only; it still asks in the mirror.
A shared relational gate (model assumption) is a function of the full realization.
The masks below enumerate possible terminal observations, not update steps.
"""
from collections import Counter
from math import log2
from pathlib import Path
import json


def entropy(counts):
    n=sum(counts.values());return log2(n)-sum(c*log2(c) for c in counts.values())/n


def tally():
    # Fix role 0 on each side as neutral. All choices of one each are equivalent
    # by separate row/column relabelings in the benchmark measure.
    joint=Counter()
    for a in range(128):
        for b in range(128):
            for c in range(128):
                # Red response ignores a (neutral target); mirror ignores bit 0.
                x=(int(bool(b))<<8)|(int(bool(c))<<9)|(b|c)
                y=(int(bool(a&126))<<7)|(int(bool(b&126))<<8)|(int(bool(c&126))<<9)|((a|b|c)&126)
                joint[x,y]+=1
    assert sum(joint.values())==2**21
    return joint


def prediction(joint,readout):
    source=Counter();target=Counter();pairs=Counter()
    for (x,y),n in joint.items():
        z=readout(x);source[z]+=n;target[y]+=n;pairs[z,y]+=n
    return entropy(pairs)-entropy(source),entropy(target)


def run():
    j=tally();out={}
    for name,dist in [('red_to_blue',j),('blue_to_red',{(y,x):n for (x,y),n in j.items()})]:
        count=lambda x:((x>>7).bit_count(),(x&127).bit_count())
        by_overlap=lambda x:((x>>7)&6,(x&126))
        loss={}
        for key,read in [('marks_only',lambda _:0),('endpoint_counts',count),('overlap_labels',by_overlap),('all_labels',lambda x:x)]:
            loss[key],base=prediction(dist,read)
        gain=base-loss['all_labels'];assert gain>0 and loss['all_labels']<=loss['endpoint_counts']<=base+1e-12
        out[name]=dict(loss=loss,gain=gain,independent_gates_control_gain=0)
    assert abs(out['red_to_blue']['gain']-out['blue_to_red']['gain'])<1e-10
    p=Path(__file__).resolve().parents[1]/'results/ramsey_reactive_masked_mirror.json';p.write_text(json.dumps(dict(realizations=2**21,observed_footprint_pairs=len(j),scope='uniform shared gate, one neutral target per side; independent mirror gate control factorizes at fixed marks',scores=out),indent=2)+'\n');print(out)

if __name__=='__main__':run()
