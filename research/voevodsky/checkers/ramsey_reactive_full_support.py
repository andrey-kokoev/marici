"""Hypothesis: a supported attempt needs all distinct requesters at one responder."""
from collections import Counter
from math import log2
from pathlib import Path
import json
from ramsey_reactive_joint_support import inspect


def read(a,b,c):
    # Positive resolved links use a common gate in both views. Neutral responders
    # cannot be centers; their requester roles still belong to the opposite star.
    return not (b==127 or c==127),not bool(a&b&c&126)


def run():
    bins=Counter();states=Counter();least=22
    for a in range(128):
        for b in range(128):
            for c in range(128):
                r,s=read(a,b,c);k=inspect(a,b,c)[0];bins[k,r or s]+=1;states[r,s]+=1
                if not (r or s):least=min(least,a.bit_count()+b.bit_count()+c.bit_count())
    # Cross centered at (R2,B2), without and with its intersection.
    before=(2,125,2);after=(2,127,2);assert inspect(*before)[0]==inspect(*after)[0] and read(*before)==(True,True) and read(*after)==(False,False) and least==9
    keys={k for k,z in bins};amb=sum(bool(bins[k,True] and bins[k,False]) for k in keys);n=2**21
    def loss(counts):return sum(w*log2(sum(counts)/w) for w in counts if w)
    conditional=sum(loss((bins[k,False],bins[k,True])) for k in keys)/n
    out=dict(scope='all-requester support hypothesis, uniform shared gate, one neutral responder on each side',conditions={str(k):v for k,v in states.items()},least_links_for_both_positive=least,footprints=len(keys),ambiguous=amb,or_false_count=states[False,False],prior_OR_loss=loss((states[False,False],n-states[False,False]))/n,OR_loss_given_names=conditional);print(out);(Path(__file__).resolve().parents[1]/'results/ramsey_reactive_full_support.json').write_text(json.dumps(out,indent=2)+'\n')

if __name__=='__main__':run()
