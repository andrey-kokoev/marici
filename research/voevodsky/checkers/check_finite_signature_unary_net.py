"""Finite-signature unary counter skeleton with measured space and work."""
from itertools import product
from pathlib import Path
import json

# Agent types ACC, BIT0, BIT1, UNIT, NIL, QUERY are finite. In this
# port-chain skeleton ACC--BIT0 reconnects ACC; ACC--BIT1 inserts one
# UNIT on the accumulator's unary auxiliary wire and reconnects ACC.
# This is not a full linear interaction-net encoding of insertion.
def consume(word):
    units=0;steps=0;peak=0
    for bit in word:
        assert bit in (0,1)
        units+=bit;steps+=1
        peak=max(peak,units)
    return units,steps,peak

def threshold(units,k):
    assert k>=0
    traversals=min(units,k)
    return units>=k,traversals

checks=0
for n in range(13):
    for word in product((0,1),repeat=n):
        count,steps,peak=consume(word)
        assert count==sum(word) and steps==n and peak==count
        for k in range(n+2):
            result,work=threshold(count,k)
            assert result==(sum(word)>=k) and work<=min(n,k)
            checks+=1
report={'passed':True,'finite_agent_names':['ACC','BIT0','BIT1','UNIT','NIL','QUERY'],'tested_threshold_cases':checks,'counter_units':'exact number of ones; worst-case n','consume_steps':'n active-pair skeleton steps','query_work':'min(count,k) unary traversals','qualification':'Insertion/read wiring and garbage management not yet specified as linear principal-port interaction-net rules; complexity is for abstract skeleton only.'}
out=Path(__file__).resolve().parents[1]/'results/finite-signature-unary-net.json'
out.write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
