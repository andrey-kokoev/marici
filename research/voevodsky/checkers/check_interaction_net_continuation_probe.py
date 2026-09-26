"""Minimal principal-port interaction-net prototype for continuation sufficiency.

TOKEN(bit) -- PROBE is an active pair; rewriting exposes bit at a free
output port. Disjoint active pairs commute. This is a local-rule experiment,
not a model of Nima's overlap or an actual research-event transition.
"""
from dataclasses import dataclass
from pathlib import Path
import json

@dataclass(frozen=True)
class Pair:
    token_bit: int
    probe: str
    output: str

def rewrite(pair):
    assert pair.token_bit in (0,1) and pair.probe=='read'
    return (pair.output,pair.token_bit)

def run(pairs,order):
    outputs={}
    for i in order:
        port,value=rewrite(pairs[i])
        assert port not in outputs
        outputs[port]=value
    return outputs

left=(Pair(0,'read','u'),Pair(1,'read','v'))
assert run(left,(0,1))==run(left,(1,0))=={'u':0,'v':1}
# A count-only compressed state conflates these one-pair nets, yet one
# permitted future local interaction distinguishes them.
a=(Pair(0,'read','u'),);b=(Pair(1,'read','u'),)
assert len(a)==len(b)==1 and run(a,(0,))!=run(b,(0,))
report={'passed':True,'rule':'principal TOKEN(bit)-PROBE(read) pair -> output(bit)','disjoint_diamond':'two disjoint pairs commute at named output ports','count_only_state':'insufficient: equal agent counts, different probe outputs','candidate_state':'retain boundary bit and port incidence','unproved':'uniform bounded-width representation, overlapping-redex confluence, Nima E/E_B correspondence, real source authority'}
out=Path(__file__).resolve().parents[1]/'results/interaction-net-continuation-probe.json'
out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
