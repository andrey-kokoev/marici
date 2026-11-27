"""Terminal footprint coding benchmark; no evaluation schedule or fitted source distribution."""
from collections import Counter
from fractions import Fraction
from math import comb,log2
import json
from pathlib import Path

# Count labeled bipartite subrelations with no isolated endpoints by inclusion-exclusion.
def onto(a,b):
    return sum((-1)**(i+j)*comb(a,i)*comb(b,j)*2**((a-i)*(b-j)) for i in range(a+1) for j in range(b+1))

def entropy(weights):
    return sum(-float(w)*log2(float(w)) for w in weights if w)

def run():
    # Independent check: add a whole row of a terminal relation in the counting DP.
    # This order enumerates graphs, not executions of the modeled carrier.
    hist={(0,0):1}
    for i in range(3):
        nxt=Counter()
        for (a,b),k in hist.items():
            for row in range(128):nxt[a|((1<<i) if row else 0),b|row]+=k
        hist=nxt
    assert all(k==onto(a.bit_count(),b.bit_count()) for (a,b),k in hist.items());total=sum(hist.values());assert total==2**21 and len(hist)==890
    p=[Fraction(k,total) for k in hist.values()];H=entropy(p);hb=lambda p:entropy([p,1-p]);marg=3*hb(Fraction(1,128))+7*hb(Fraction(1,8));out=dict(one_direction=dict(legal_footprints=len(hist),capacity_bits=log2(len(hist)),uniform_relation_joint_loss_bits=H,independent_marginal_loss_bits=marg,fair_endpoint_loss_bits=10),two_independent_directions=dict(capacity_bits=2*log2(len(hist)),joint_loss_bits=2*H,marginal_loss_bits=2*marg),same_support_both_directions=dict(joint_loss_bits=H,capacity_bits=log2(len(hist))),target='which named endpoints have at least one positive terminal directed comparison; not the entire realization or its OR');print(out);(Path(__file__).resolve().parents[1]/'results/ramsey_relational_footprint_bits.json').write_text(json.dumps(out,indent=2)+'\n')
if __name__=='__main__':run()
