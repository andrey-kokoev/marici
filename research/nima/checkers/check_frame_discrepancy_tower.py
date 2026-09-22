"""Exact 100-frame tests for a stage-compatible discrepancy construction."""
from pathlib import Path
from fractions import Fraction as Q
from math import comb
import json


def add(a,b):return tuple(x+y for x,y in zip(a,b))
def sub(a,b):return tuple(x-y for x,y in zip(a,b))
def scale_frame(f,z):return tuple(Q(f+1)*v for v in z)
def align(f,z):return tuple(v/Q(f+1) for v in z)
def transition(g,f,z):return scale_frame(g,align(f,z))
def discrepancy(states):return tuple(sub(align(f,y),states[0]) for f,y in enumerate(states) if f)


def main():
    F=100;stages=routes=0
    for m in range(1,7):
        z=tuple(Q(i+1,i+2) for i in range(m))
        states=tuple(scale_frame(f,z) for f in range(F))
        assert all(not any(d) for d in discrepancy(states))
        bias=tuple(Q(1,7) for _ in z)
        biased=tuple(scale_frame(f,add(z,bias)) for f in range(F))
        assert biased!=states and all(not any(d) for d in discrepancy(biased))
        noisy=list(states)
        noisy[73]=add(noisy[73],tuple(Q(1,100) for _ in z))
        defects=discrepancy(noisy)
        assert any(defects[72])
        assert all(not any(d) for i,d in enumerate(defects) if i!=72)
        wanted=tuple(tuple(Q(f+i+1,1000) for i in range(m)) for f in range(1,F))
        lift=(tuple(Q(0) for _ in z),)+tuple(scale_frame(f,wanted[f-1]) for f in range(1,F))
        assert discrepancy(lift)==wanted
        if m>1:
            restricted=tuple(y[:-1] for y in noisy)
            assert discrepancy(restricted)==tuple(d[:-1] for d in defects)
        for f,g,h in ((0,1,99),(99,73,0),(2,7,42)):
            assert transition(h,g,transition(g,f,states[f]))==transition(h,f,states[f])
            routes+=1
        # Finite noise inequality for this exact diagonal-frame fixture.
        assert max(abs(v) for v in defects[72])==Q(1,100*(73+1))
        stages+=1
    edges=comb(F,2);tree=F-1;loops=edges-tree
    assert (edges,tree,loops)==(4950,99,4851)
    result={'passed':True,'frames':F,'tower_stages':stages,
        'transition_route_checks':routes,'tree_state_comparisons':tree,
        'complete_graph_edges':edges,'fundamental_transition_loops':loops,
        'checks':['synchronization','shared_bias_is_invisible','single_frame_disagreement',
                  'split_surjectivity','restriction_commutes_with_discrepancy'],
        'scope':'Exact abstract frame fixtures. Concrete corrected-frame admission, source realization and analytical noise constants remain separate inputs.'}
    out=Path(__file__).resolve().parents[1]/'results/frame-discrepancy-tower.json'
    out.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))


if __name__=='__main__':main()
