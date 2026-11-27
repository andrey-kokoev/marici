"""A separating context, conditional on a colored responder accepting a child vertex as its payload."""
from itertools import product
from pathlib import Path
import json

# A named ref returns a continuation, never an isolated Boolean result.
def ref(fn):return lambda:fn

def witness(full):return (1,1) in full['incidence']

def neutral_reply(full):return False

def context(mode):
    neutral=ref(neutral_reply);all_a=ref(witness if mode=='relation' else neutral_reply)
    # Child reduction for the frozen positive-binding control: no A-minus,
    # at least one positive B. Thus child OR agrees independent of all A+.
    def child_readout(net):
        a=neutral()(net);b=net['blue_witness']()(net)
        return not a or not b
    child=ref(child_readout)
    # The exterior R responder returns the child's exact reference, not a copy
    # or a forced observation. The B responder supplies its own payload ref.
    def red_request(responder):return all_a if responder=='R' else neutral
    def blue_request(responder,net):return net['blue_witness'] if responder=='B' else neutral
    def observe(net):
        r=red_request(net['RorN']);b=blue_request(net['BorN'],net)
        assert net['RorN']!='R' or r is all_a
        a=r()(net);z=b()(net);return not a or not z
    return child,ref(observe)

def run():
    results=[]
    for active,r,b in product((0,1),('R','N'),('B','N')):
        es=frozenset(((1,1),(2,2)) if active else ((1,2),(2,1)))
        net=dict(incidence=es,RorN=r,BorN=b,blue_witness=ref(lambda full:1 in full['positive_B']),positive_B=frozenset({1}));obs=[]
        for mode in ('local','relation'):
            c,outer=context(mode);obs.append((c()(net),outer()(net)))
        assert obs[0][0]==obs[1][0] and (obs[0][1]!=obs[1][1])==bool(active and r=='R' and b=='B');results.append(dict(edges=sorted(es),responders=(r,b),local=obs[0],relational=obs[1]))
    out=dict(scope='Finite candidate contexts; positive transfer and exterior forwarding are hypotheses, not implications of N declining negation.',observations='(child OR, exterior OR) at resolution',cases=results);(Path(__file__).resolve().parents[1]/'results/ramsey_tet_positive_exterior.json').write_text(json.dumps(out,indent=2)+'\n');print(len(results),'contexts checked')
if __name__=='__main__':run()
